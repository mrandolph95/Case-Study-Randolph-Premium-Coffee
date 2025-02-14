# Randolph’s Premium Coffee 
***You’ll enjoy our delicious, nutritious, and fictitious roasted coffee beans sourced from Ethiopia.***



### Inspiration:

I wanted to practice some Excel skills, so I found a creator on YouTube who provided a step-by-step training video on an Excel portfolio project idea. After I completed the project, I wanted to challenge myself more and came up with the idea to write a script that did exactly what I just did: find the video on YouTube, download the file, and fill out the data in the report with Excel formulas. This project helped me understand Docker and gave me hands-on experience in deploying models in AWS.

### Scenario:

Randolph’s Coffee Sales Analyst pulls their sales data from a 3rd party source every day at 1:00 p.m., then prepares the report and pivot tables by filling in the missing values and calculating the sales of each order. The analyst wants the report to be automated from start to finish so they have time to complete more tasks.

### Solution: 

I built and automated web scraper to pull the data using selenium to pull the data from the resource (YouTube: Mo Chen), and an automated report builder to prepare the Microsoft Excel report. These models help operational efficiency so an employee may handle other tasks while the report is being prepared. 

Currently, the report generation currently takes an average of 18.5 minutes to run due to the data processing inefficiencies caused by xlwings. I plan to optimize pandas to prepare the data to reduce run time. Additionally, I plan to pull the data from Mo Chen's YouTube video using their API.


## Table of Contents:
  - Project 1: Daily Web Scraper
    - Python script
    - README
    - Docker file
  - Project 2: Automated Report Generator
    - Python script
    - README
    - Modified Excel workbook
  - Project 3: Customer Churn
    - Python cript
    - README
    - SQL script
    - SQL results as CSV file
  - Power BI Dashboard (visualizations of sales data)


### Future scopes:
- Automated Report Generator
    - Modify Python script to use pandas to clean and prepare data instead of xlwings
- Daily Web Scraper
    - Modify script to pull data using API

