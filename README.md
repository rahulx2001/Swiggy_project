# Swiggy Restaurant Analysis

![Swiggy Analysis Banner](https://img.shields.io/badge/Swiggy-Restaurant%20Analysis-orange)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Data Analysis](https://img.shields.io/badge/Data-Analysis-green)

## Overview
This project analyzes restaurant data from Swiggy, one of India's leading food delivery platforms, to uncover insights about restaurant ratings, pricing patterns, popular food types across different cities, and other key metrics. The analysis includes data visualization and an interactive Streamlit dashboard for exploring the findings.

## Features
- Comprehensive EDA (Exploratory Data Analysis) of Swiggy restaurant data
- Interactive Streamlit dashboard with multiple analysis sections
- Visualizations of price distributions, city-wise analysis, food type popularity, and more
- Correlation analysis of factors affecting restaurant ratings

## Demo
![Dashboard Preview](https://via.placeholder.com/800x400?text=Swiggy+Dashboard+Preview)

## Dataset
The dataset contains information about 8,680 restaurants across multiple cities in India and includes the following features:
- Restaurant ID, name, and location details
- Pricing information
- Average ratings and total number of ratings
- Food types offered
- Delivery time
- Address information

## Project Structure
```
swiggy-analysis/
├── swiggy.csv              # Dataset file
├── Swiggy_EDA.md           # Exploratory Data Analysis notebook (Markdown)
├── app.py                  # Streamlit dashboard application
├── README.md               # Project documentation
└── outputs/                # Visualization outputs
    └── *.png               # Visualization images
```

## Exploratory Data Analysis
The EDA process examines:
- Distribution of restaurant ratings
- Correlation between restaurant pricing and ratings
- City-wise restaurant distribution
- Popular food types across different cities
- Factors affecting average ratings through correlation analysis

Key visualizations include:
- Price vs. Rating scatter plots
- City distribution pie charts
- Food type popularity charts
- Correlation heatmaps

## Interactive Dashboard
The Streamlit dashboard provides an interactive way to explore the data with five main sections:

1. **Overview**: Dataset summary and rating distribution
2. **Price Analysis**: Price distribution, categories, and correlation with ratings
3. **City Analysis**: Top cities and their average ratings
4. **Food Type Analysis**: Most popular food types overall and by city
5. **Correlation Analysis**: Heatmap of correlations between numeric variables

## Installation and Usage

### Prerequisites
- Python 3.8 or higher
- Required Python packages (install using `pip install -r requirements.txt`):
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - plotly
  - streamlit

### Setup Instructions
1. Clone this repository:
   ```
   git clone https://github.com/rahulx2001/Swiggy_project.git
   cd Swiggy_project
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit dashboard:
   ```
   streamlit run app.py
   ```

4. Open your web browser and navigate to the URL provided in the terminal (typically http://localhost:8501)

## Insights
Some key findings from the analysis:
- Restaurant pricing shows a [relationship/correlation] with customer ratings
- [City name] has the highest number of restaurants on the platform
- [Food type] is the most popular cuisine across all cities
- Delivery time and ratings show [positive/negative] correlation

## Future Improvements
- Sentiment analysis of customer reviews
- Time-series analysis of restaurant performance
- Predictive modeling for restaurant success factors
- Integration with geospatial analysis

## About the Author
Created by [Rahul](https://www.linkedin.com/in/rahulx2001/) - Connect with me on LinkedIn!

## License
This project is open source and available under the [MIT License](LICENSE).
