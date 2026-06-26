CREATE TABLE cleaned_sales_dataset;
USE sales_project;
SHOW DATABASES;
USE sales_project;
show tables;
DROP TABLE IF EXISTS cleaned_sales_dataset;

CREATE TABLE cleaned_dataset (
    Order_ID VARCHAR(50),
    Order_Date VARCHAR(50),
    Customer_ID VARCHAR(50),
    Customer_Name VARCHAR(100),
    Age VARCHAR(20),
    Gender VARCHAR(20),
    City VARCHAR(100),
    Product VARCHAR(100),
    Category VARCHAR(100),
    Quantity VARCHAR(20),
    Unit_Price VARCHAR(50),
    Total_Sales VARCHAR(50),
    Age_Group VARCHAR(20),
    Month VARCHAR(20)
);
show tables;
USE sales_project;

SELECT COUNT(*)
FROM cleaned_dataset;
SELECT Product,
       SUM(Total_Sales) AS Revenue
FROM cleaned_dataset
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5;

SELECT Category,
       SUM(Total_Sales) AS Revenue
FROM cleaned_dataset
GROUP BY Category
ORDER BY Revenue DESC;

SELECT City,
       SUM(Total_Sales) AS Revenue
FROM cleaned_dataset
GROUP BY City
ORDER BY Revenue DESC;

SELECT Gender,
       SUM(Total_Sales) AS Revenue
FROM cleaned_dataset
GROUP BY Gender;

SELECT Age_Group,
       SUM(Total_Sales) AS Revenue
FROM cleaned_dataset
GROUP BY Age_Group
ORDER BY Revenue DESC;

SELECT ROUND(AVG(Total_Sales),2) AS Average_Order_Value
FROM cleaned_dataset;

SELECT Month,
       SUM(Total_Sales) AS Revenue
FROM cleaned_dataset
GROUP BY Month;
