SELECT * FROM customers LIMIT 5;

SELECT COUNT(*) AS total_customers,
       SUM(CASE WHEN "Churn" = 'True' THEN 1 ELSE 0 END) AS churned_customers,
       ROUND(SUM(CASE WHEN "Churn" = 'True' THEN 1 ELSE 0 END) * 100 / COUNT(*), 2) AS churn_percentage       
FROM customers;

SELECT
    "Churn",
    AVG("Recency") AS avg_recency,
    AVG("Frequency") AS avg_frequency,
    AVG("Monetary Value") AS avg_monentary_value
FROM customers
GROUP BY "Churn";

SELECT 
    "Customer ID",
    "Recency",
    "Frequency",
    "Monetary Value"
FROM customers
WHERE "Churn" = 'True'
    AND "Frequency" < (SELECT AVG("Frequency") FROM customers)
    AND "Monetary Value" < (SELECT AVG("Monetary Value") FROM customers);

SELECT 
    "Recency",
    COUNT(*) AS customer_count,
    SUM(CASE WHEN "Churn" = 'True' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN "Churn" = 'True' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_percentage
FROM customers
GROUP BY "Recency"
ORDER BY "Recency";







