# 📊 Life Expectancy Forecasting Project

## 🔍 Overview
This project explores, analyzes, and forecasts global **life expectancy** data by gender from **1960 to 2021**. It combines **exploratory data analysis**, **supervised machine learning** (Random Forest), and **statistical time series forecasting** (ARIMA) to uncover trends, gender gaps, and generate predictions for future years.

## 🚀 Project Objectives
- Analyze trends in male vs female life expectancy across countries and decades
- Identify top-performing and underperforming countries
- Predict future life expectancy using:
  - **Random Forest Regressor** (Supervised ML)
  - **ARIMA** (Univariate time series)

## 📌 Key Techniques Used

### ✅ Exploratory Data Analysis (EDA)
- Trend analysis over time
- Top 20 countries by gender
- Gender gap visualization
- Correlation heatmaps

### ✅ Supervised Machine Learning
- **Random Forest Regression**
- Target: Life Expectancy
- Features: Year, Country Code (encoded), Male/Female Life Expectancy
- Evaluation:
  - Female MAE: ~1.01, R²: 0.98
  - Male MAE: ~0.91, R²: 0.98
- Visualized predicted vs actual life expectancy

### ✅ Time Series Forecasting
- **ARIMA** modeling for country-specific prediction
- Forecasted 5–10 years of female and male life expectancy
- Country-wise line plots with future trend projections for top most and last gender gap countries

## 📈 Sample Output Visuals
- Top 20 countries by life expectancy (bar and line plots)
- Gender gap by country
- Random Forest: Predicted vs Actual plot
- ARIMA: Country-wise 10-year forecast

## 🗂️ Dataset
- Source: Cleaned from World Bank life expectancy datasets (separated by Male and Female)
- Shape: ~17,000 rows per gender, covering 200+ countries over 60+ years
- Format: Long-format with columns for Country, Country Code, Year, and Life Expectancy
*Links to dataset*: <br/>
Life expectancy at birth, male (years)- https://data.worldbank.org/indicator/SP.DYN.LE00.MA.IN?end=2022&start=2013 <br/>
Life expectancy at birth, female (years) - https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN <br/>
