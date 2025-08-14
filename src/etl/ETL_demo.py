"""
ETL lite version: DB -> CSV/Excel with basic validation and error handling
"""

import os
import sys
import logging
import urllib.parse
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from src.core.config import env

# ---- Logger ----
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("etl-lite")

# ---- Config (puede leer de .env o valores por defecto)
db_driver = env("DB_DRIVER")
db_server = env("DB_SERVER", r"localhost\SQLEXPRESS")
db_database = env("DB_DATABASE", "PracticaSQL")
encrypt = env("DB_ENCRYPT", "no")
trust_cert = env("DB_TRUST_CERT", "yes")
trusted = str(env("DB_TRUSTED_CONNECTION", "true")).lower() in ("1", "true", "yes")

def make_engine():
    """Crea el engine de conexión a SQL Server."""
    parts = [
        f"DRIVER={{{db_driver}}}",
        f"SERVER={db_server}",
        f"DATABASE={db_database}",
        f"Encrypt={encrypt}",
        f"TrustServerCertificate={trust_cert}",
        "Trusted_Connection=yes" if trusted else ""
    ]
    odbc_str = ";".join(p for p in parts if p)
    odbc_enc = urllib.parse.quote_plus(odbc_str)
    return create_engine(f"mssql+pyodbc:///?odbc_connect={odbc_enc}")

def validate_basic(df: pd.DataFrame) -> list[str]:
    """Validación simple de columnas requeridas y datos vacíos."""
    issues = []
    required = {"Nombre"}
    if df.empty:
        issues.append("No data found")
    missing = required - set(df.columns)
    if missing:
        issues.append(f"Missing columns: {sorted(missing)}")
    return issues

def run(outdir="outputs", write_excel=True):
    """Ejecuta el ETL: lee DB, valida y exporta CSV/Excel."""
    try:
        log.info("Connecting to DB...")
        eng = make_engine()
        df = pd.read_sql(text("SELECT Nombre FROM Empleados WHERE Departamento = 'Ventas' ;"), eng)
        log.info("Rows fetched: %s", len(df))

        log.info("Validating...")
        issues = validate_basic(df)
        if issues:
            for e in issues:
                log.error("Validation: %s", e)
            sys.exit(1)

        os.makedirs(outdir, exist_ok=True)
        csv_path = os.path.join(outdir, "Empleados.csv")
        df.to_csv(csv_path, index=False, encoding="utf-8")
        log.info("Wrote CSV -> %s", csv_path)

        if write_excel:
            try:
                import openpyxl
                xlsx_path = os.path.join(outdir, "Empleados.xlsx")
                with pd.ExcelWriter(xlsx_path, engine="openpyxl") as w:
                    df.to_excel(w, sheet_name="Empleados", index=False)
                log.info("Wrote Excel -> %s", xlsx_path)
            except ModuleNotFoundError:
                log.warning("openpyxl not installed; skipped Excel export")

        log.info("ETL Done.")
    except (SQLAlchemyError, OSError) as ex:
        log.exception("ETL failed: %s", ex)
        sys.exit(1)

if __name__ == "__main__":
    run()
