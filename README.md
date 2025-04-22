# 📊 Life Expectancy Forecasting Project

## 🔍 Overview
This project analyzes global life expectancy trends from 1960–2022, focusing on gender-based differences and country-level insights. It combines Python for data wrangling and machine learning, MySQL for structured data storage, and Power BI for interactive dashboarding.

## 📌 Key Techniques Used
###Exploratory Data Analysis (EDA)
- Trend analysis, gender gap visuals, top countries, and correlation heatmaps
###Supervised Machine Learning
- **Random Forest Regression**
-  (R² ≈ 0.98, MAE ~1.0) to predict life expectancy by gender and year
###Time Series Forecasting
- ARIMA models for 5–10 year forecasts by country, including top and bottom gender gap nations
## 📈 Output Visuals
- Predicted vs actual plots, country-wise life expectancy trends, gender gap charts, and global ranking bars

### 🗃️ MySQL (Database Storage)
- Created a relational database `life_expectancy_db` using SQLAlchemy
- Stored cleaned, merged, and modeled outputs as a table
- Configured user access and permissions for secure connectivity from BI tools

### 📊 Power BI (Visualization & Insights)
- Connected directly to MySQL for live data visualization
- Built a multi-page interactive dashboard with:
  - **Scatter plot** of male vs female life expectancy by country
  - **Stacked area chart** showing trends over time
  - **Bar chart** for Top 10 countries with highest gender gap
  - **Treemap and KPI card** to highlight average gender gap by year
- Enabled filters for Year and Country to explore data dynamically

## 🗂️ Dataset
- Source: Cleaned from World Bank life expectancy datasets (separated by Male and Female)
- Shape: ~17,000 rows per gender, covering 200+ countries over 60+ years
- Format: Long-format with columns for Country, Country Code, Year, and Life Expectancy

 
*Links to dataset*: <br/>

Life expectancy at birth, male (years)- https://data.worldbank.org/indicator/SP.DYN.LE00.MA.IN?end=2022&start=2013 <br/>

Life expectancy at birth, female (years) - https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN <br/>
