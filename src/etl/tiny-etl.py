import pyodbc
import pandas as pd

# 1) Configuración de conexión
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=PracticaSQL;"
    "Trusted_Connection=yes;"
)

try:
    # 2) Conectar y leer datos
    conn = pyodbc.connect(conn_str)
    query = "SELECT IdPedido, Cliente, FechaPedido, MontoTotal FROM Pedidos;"
    df = pd.read_sql(query, conn)

    # 3) Validaciones
    results = []

    # Null check
    nulls = df.isna().sum()
    for col, count in nulls.items():
        if count > 0:
            results.append({"Validation": f"Nulls in {col}", "Count": count})

    # No numeric amount
    bad_amount = pd.to_numeric(df['MontoTotal'], errors='coerce').isna().sum()
    if bad_amount > 0:
        results.append({"Validation": "Invalid numeric in MontoTotal", "Count": bad_amount})

    #Invalid datetimes
    bad_dates = pd.to_datetime(df['FechaPedido'], errors='coerce').isna().sum()
    if bad_dates > 0:
        results.append({"Validation": "Invalid date in FechaPedido", "Count": bad_dates})

    # 4) Export results
    results_df = pd.DataFrame(results)
    results_df.to_excel("Data_Validation_Report.xlsx", index=False)

    print("Validation complete. Report saved to Data_Validation_Report.xlsx")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'conn' in locals():
        conn.close()
