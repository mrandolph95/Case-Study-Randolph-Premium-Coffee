import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load Excel data
file = 'RandolphPremiumCoffeeSales_test.xlsx'

try:
    data = pd.ExcelFile(file)   
    orders = data.parse('orders')
    customers = data.parse('customers')
except FileNotFoundError:
    print('File Not Found')
    exit()
except Exception as e:
    print(f"Error reading Excel file: {e}")

# Merging Customer ID and Order ID columns
orders['Order Date'] = pd.to_datetime(orders['Order Date'])
customer_orders = orders.merge(customers[['Customer ID', 'Customer Name']],
                                on='Customer ID', how='left')

# Calculate recency
last_purchase_date = customer_orders.groupby('Customer ID')['Order Date'].max()
last_date = pd.Timestamp('2022-08-19')
recency = (last_date - last_purchase_date).dt.days
recency = recency.reset_index()
recency.columns = ['Customer ID', 'Recency']

# Calculate frequency
frequency = customer_orders.groupby('Customer ID')['Order Date'].count().reset_index()
frequency.columns = ['Customer ID', 'Frequency']

# Calculate monetary value
customer_orders['Sales'] = pd.to_numeric(customer_orders['Sales'], errors='coerce')
monetary_value = customer_orders.groupby('Customer ID')['Sales'].sum().reset_index()
monetary_value.columns = ['Customer ID', 'Monetary Value']

# Add churn lable
churn_threshold = 180
recency['Churn'] = recency['Recency'] > churn_threshold

# Merge all data frames for RFM metrics
rfm = recency.merge(frequency, on='Customer ID').merge(monetary_value, on='Customer ID')

print(rfm.head())


# POSTGRE SQL
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'mysecretpassword'
DATABASE = 'customer_churn'
PORT = 5432

# Connection string
connection = f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# SQLAlchemy engine
engine = create_engine(connection)

# Put data in PostgreSQL
try:
    table = 'churns'
    rfm.to_sql(table, engine, if_exists='replace', index=False)
    print(f"Data inserted into table {table} in the {DATABASE} database.")
except Exception as e:
    print(f"Operation failed: {e}")

print(rfm.head())

# Prepare data for Random Trees model
X = rfm[['Recency', 'Frequency', 'Monetary Value']]
y = rfm['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Predict
y_pred = rf_model.predict(X_test)

print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Accuracy Score:")
print(accuracy_score(y_test, y_pred))
