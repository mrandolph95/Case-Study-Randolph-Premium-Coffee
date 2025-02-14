# Customer Churn Prediction

### Overview

This project aims to predict customer churn for a business by analyzing historical data using a Random Forest classifier. The dataset includes information about customer orders, and the model predicts whether a customer is likely to churn based on metrics such as recency, frequency, and monetary value. The project demonstrates data engineering, SQL integration, and machine learning workflows.

### Tools Used

  - Pandas for data manipulation and analysis.
  - SQLAlchemy for connecting to a PostgreSQL database.
  - scikit-learn for building and evaluating the machine learning model.
  - PostgreSQL for storing and managing the data.

### Dataset

The data used for this project comes from an Excel file containing two sheets:

  1. orders: Contains information on customer orders.
  2. customers: Contains information on customers, including customer ID and name.

### Workflow

  1. Data Preprocessing:
     
    - The data from the Excel file is loaded and merged on Customer ID and Order ID to combine customer details with their order history.
    - Recency (days since last purchase), frequency (number of orders), and monetary value (total spent by the customer) are calculated        for each customer.

  2. Customer Segmentation:

    - A churn label is added based on the recency metric (customers who haven't purchased in over 180 days are considered likely to churn).

  3. SQL Integration:

    - The processed data is inserted into a PostgreSQL database using SQLAlchemy to facilitate storage and querying.

  4. Machine Learning Model:

    - A Random Forest classifier is trained using the recency, frequency, and monetary value features to predict customer churn.
    - Model performance is evaluated using classification metrics like accuracy, precision, recall, and F1-score.

### Running the Code

  1. Dependencies:

    - pandas
    - sqlalchemy
    - scikit-learn
    - psycopg2
    - PostgreSQL
    

  2. Database Setup:

    - Ensure PostgreSQL is installed and running.
    - Create a database named customer_churn and provide the connection details in the script.
    
  3. Execution:

    - Run the script to process the data, store it in PostgreSQL, and train the Random Forest model.

### Results

The model was trained on the recency, frequency, and monetary value features, achieving a classification report with 100% accuracy. However, the model may need further evaluation due to potential issues with data imbalance and overfitting.

### Next Steps

For deployment, the model can be containerized using Docker and deployed on AWS to provide real-time predictions.


