#.\myenv\Scripts\Activate.ps1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read the Excel file
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

# Show first 5 rows
print(df.head())

# Show dataset information
print(df.info())

# Show missing values
print("missing values",df.isnull().sum())

#checking for the duplicates
print("Duplicate rows",df.duplicated().sum())

#checking duplicate ordered id's
print("duplicated ordered id's",df["Order_ID"].duplicated().sum())

#fill missing values
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["City"]=df["City"].fillna(df["City"].mode()[0])

print("after",df.isnull().sum())

#date is in str formate change to proper one 
df["Order_Date"]=pd.to_datetime(df["Order_Date"])
print(df.dtypes)

#creating age column
def  age_group(age):
    if age<25:
        return "Young"
    elif age<45:
        return "Adult" 
    else:
        return "Senior"

df["Age_Group"]=df["Age"].apply(age_group)

#creating month column
df["Month"] = df["Order_Date"].dt.month_name()

#saving the cleaned dataset
df.to_excel("cleaned_sales_dataset.xlsx", index=False)

print("Dataset saved successfully!")


print("Dataset Shape:", df.shape)
print("Missing Values:")
print(df.isnull().sum())

#category analysis 
plt.figure(figsize=(8,5))
category_sales = df.groupby('Category')['Total_Sales'].sum()
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total_Sales")
plt.savefig("images/category_analysis.png")
plt.close()
#plt.show()

#city analysis
plt.figure(figsize=(8,5))
city=df.groupby('City')['Total_Sales'].sum()
city.plot(kind="bar")
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total_Sales")
plt.savefig("images/city_analysis.png")
plt.close()
#plt.show()

#Gender analysis
plt.figure(figsize=(8,5))
gender=df.groupby('Gender')['Total_Sales'].sum()
gender.plot(kind="bar")
plt.title("Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total_Sales")
plt.savefig("images/gender analysis.png")
plt.close()
#plt.show()

#Age_group analysis
age_order=['Young','Adult','Senior']
plt.figure(figsize=(8,5))
age=df.groupby('Age_Group')['Total_Sales'].sum()
age=age.reindex(age_order)

age.plot(kind="bar")
plt.title("Sales by Age_Group")
plt.xlabel("Age_Group")
plt.ylabel("Total_Sales")
plt.savefig("images/age_analysis.png")
plt.close()
#plt.show()

#Month analysis

month_order = [
    'January','February','March','April','May','June',
    'July','August','September','October','November','December'
]

plt.figure(figsize=(8,5))
month = df.groupby('Month')['Total_Sales'].sum()
month = month.reindex(month_order)

month.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.savefig("images/month_analysis.png")
plt.close()
#plt.show()

#Product analysis
plt.figure(figsize=(8,5))
top_product=df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(10)
top_product.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total_Sales")
plt.savefig("images/product_analysis.png")
plt.close()
#plt.show()

#histogram analysis
plt.figure(figsize=(8,5))
plt.hist(df['Total_Sales'])
plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")
plt.savefig("images/histogram_analysis.png")
plt.close()
#plt.show()


#correlation analysis

plt.figure(figsize=(8,5))

corr = df[['Age','Quantity','Unit_Price','Total_Sales']].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title("Correlation Heatmap")

plt.savefig("images/correlation_heatmap.png")
plt.close()


#scatter plot creation
plt.figure(figsize=(8,5))

plt.scatter(df['Quantity'], df['Total_Sales'])

plt.title("Quantity vs Total Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")

plt.savefig("images/scatter_quantity_sales.png")
plt.close()

#pairplot
sns.pairplot(
    df[['Age','Quantity','Unit_Price','Total_Sales']]
)

plt.savefig("images/pairplot.png")
plt.close()


#for database creation save the file into csv

import pandas as pd

df = pd.read_excel("cleaned_sales_dataset.xlsx")

df.to_csv(
    r"C:\Users\bindh\OneDrive\python learn\analaticstask1\cleaned_sales_dataset.csv",
    index=False
)
df = pd.read_csv("cleaned_sales_dataset.csv")

print(df.shape)
print(df.head())

