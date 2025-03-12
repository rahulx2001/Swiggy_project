import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import io

# Set page configuration
st.set_page_config(
    page_title="Swiggy Restaurant Analysis",
    page_icon="🍽️",
    layout="wide"
)

# Add a title and description
st.title("Swiggy Restaurant Data Analysis")
st.markdown(" Created with Streamlit by [Rahul](https://www.linkedin.com/in/rahulx2001/)")
st.markdown("This application analyzes restaurant data from Swiggy to uncover insights about ratings, prices, popular food types, and more.")

import pandas as pd
import requests
import streamlit as st

def load_data():
    try:
        # Google Drive direct download link
        url = "https://drive.google.com/file/d/1mTxUtsSXthyz47mm--zwoQh2Ng-G9mc-/view?usp=sharing"
        
        # Request file from Google Drive
        response = requests.get(url)
        if response.status_code != 200:
            st.error(f"Failed to download file. Status code: {response.status_code}")
            return None
        
        # Read CSV into DataFrame using io.StringIO
        csv_data = io.StringIO(response.text)
        df = pd.read_csv(csv_data)
        
        # Check if DataFrame is empty
        if df.empty:
            st.error("The CSV file is empty.")
            return None
        
        return df

    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None


# Load the data first
df = load_data()

# Check if data loaded successfully before proceeding
if df is None:
    st.error("Could not load the data. Please check the following:")
    st.markdown("""
    1. Make sure 'swiggy.csv' is in the current directory
    """)
    
    # Show file upload option as a fallback
    uploaded_file = st.file_uploader("Upload your Swiggy CSV file", type=['csv'])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("Data loaded successfully from uploaded file!")
        except Exception as e:
            st.error(f"Error reading uploaded file: {str(e)}")

# Create a sidebar for navigation
st.sidebar.title("Navigation")
pages = ["Overview", "Price Analysis", "City Analysis", "Food Type Analysis", "Correlation Analysis"]
choice = st.sidebar.radio("Go to", pages)

# Now we can use the data in different pages
if choice == "Overview":
    st.header("Dataset Overview")
    
    if df is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Dataset Summary")
            st.write(f"Total Records: {len(df)}")
            st.write(f"Number of Cities: {df['City'].nunique()}")
            st.write(f"Number of Areas: {df['Area'].nunique()}")
            st.write(f"Price Range: ₹{df['Price'].min()} - ₹{df['Price'].max()}")
            st.write(f"Average Rating: {df['Avg ratings'].mean():.2f}/5")
        
        with col2:
            st.subheader("Rating Distribution")
            fig = px.histogram(df, x="Avg ratings", nbins=20, 
                               title="Distribution of Restaurant Ratings",
                               color_discrete_sequence=["#FF4B4B"])
            st.plotly_chart(fig)
        
        st.subheader("Sample Data")
        st.dataframe(df.head(10))
        
        st.subheader("Data Statistics")
        st.dataframe(df.describe())
    else:
        st.error("No data available to display in the Overview section.")

elif choice == "Price Analysis":
    st.header("Price Analysis")
    
    if df is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            # Price distribution
            st.subheader("Price Distribution")
            fig = px.histogram(df, x="Price", nbins=30, 
                               title="Distribution of Restaurant Prices",
                               color_discrete_sequence=["#1E88E5"])
            st.plotly_chart(fig)
        
        with col2:
            # Price categories pie chart
            st.subheader("Price Categories")
            price_range_counts = df['Price'].value_counts().nlargest(10)
            fig = px.pie(
                price_range_counts, 
                names=price_range_counts.index, 
                values=price_range_counts.values,
                title="Top 10 Price Points"
            )
            st.plotly_chart(fig)
        
        # Correlation between price and rating
        st.subheader("Price vs. Rating Correlation")
        fig = px.scatter(df, x='Price', y='Avg ratings', 
                         title='Correlation between Restaurant Price and Average Rating',
                         color='City', size='Total ratings', 
                         hover_data=['Restaurant', 'Area', 'Food type'],
                         height=600)
        st.plotly_chart(fig)
        
       
elif choice == "City Analysis":
    st.header("City Analysis")
    
    if df is not None:
        # Top 10 cities
        st.subheader("Top 10 Cities Ordering Food from Swiggy")
        city_count = df["City"].value_counts()
        top_n_cities = city_count.nlargest(10)
        
        fig = px.pie(
            names=top_n_cities.index, 
            values=top_n_cities.values,
            title='Top 10 Cities Ordering Food from Swiggy',
            height=600
        )
        st.plotly_chart(fig)
        
        # City with highest average rating
        st.subheader("Average Ratings by City")
        city_ratings = df.groupby('City')['Avg ratings'].mean().reset_index().sort_values('Avg ratings', ascending=False)
        
        fig = px.bar(
            city_ratings.head(10), 
            x='City', 
            y='Avg ratings',
            title='Top 10 Cities by Average Restaurant Rating',
            color='Avg ratings',
            color_continuous_scale='RdYlGn'
        )
        st.plotly_chart(fig)
        
        
elif choice == "Food Type Analysis":
    st.header("Food Type Analysis")
    
    if df is not None:
        # Function to extract all food types
        def extract_food_types(df):
            all_food_types = []
            for food_list in df['Food type'].dropna():
                types = food_list.split(',')
                all_food_types.extend([t.strip() for t in types])
            return pd.Series(all_food_types).value_counts()
        
        food_types = extract_food_types(df)
        
        # Top food types overall
        st.subheader("Most Popular Food Types")
        fig = px.bar(
            food_types.head(15), 
            x=food_types.head(15).index, 
            y=food_types.head(15).values,
            title='Top 15 Food Types Across All Cities',
            color=food_types.head(15).values,
            color_continuous_scale='YlOrRd'
        )
        st.plotly_chart(fig)
        
        # Create heatmap for food types by city
        st.subheader("Food Type Distribution Across Cities")
        
        # Get the top 10 cities by restaurant count
        top_cities = df['City'].value_counts().nlargest(10).index.tolist()
        # Get the top 15 food types
        top_food_types = food_types.head(15).index.tolist()
        
        # Create matrix for heatmap
        heatmap_data = []
        for city in top_cities:
            city_df = df[df['City'] == city]
            city_food_types = extract_food_types(city_df)
            
            row = []
            for food in top_food_types:
                if food in city_food_types:
                    row.append(city_food_types[food])
                else:
                    row.append(0)
            heatmap_data.append(row)
        
        # Create pandas DataFrame for the heatmap
        heatmap_df = pd.DataFrame(heatmap_data, index=top_cities, columns=top_food_types)
        
        # Create heatmap figure
        fig = go.Figure(data=go.Heatmap(
            z=heatmap_df.values,
            x=heatmap_df.columns,
            y=heatmap_df.index,
            colorscale='Viridis',
            hoverongaps=False
        ))
        
        fig.update_layout(
            title='Food Type Distribution by City (Top 10 Cities)',
            xaxis_title='Food Type',
            yaxis_title='City',
            height=600
        )
        
        # Show the heatmap
        st.plotly_chart(fig)
        
        # Most popular food type in each city
        st.subheader("Most Popular Food Types by City")
        
        # Let user select a city
        selected_city = st.selectbox("Select a City", sorted(df['City'].unique()))
        
        # Filter data for the selected city
        city_data = df[df['City'] == selected_city]
        
        if len(city_data) > 0:
            # Extract food types for the selected city
            city_food_types = extract_food_types(city_data)
            
            # Plot the top food types for the selected city
            if len(city_food_types) > 0:
                fig = px.bar(
                    city_food_types.head(10), 
                    x=city_food_types.head(10).index, 
                    y=city_food_types.head(10).values,
                    title=f'Top 10 Food Types in {selected_city}',
                    color=city_food_types.head(10).values,
                    color_continuous_scale='Viridis'
                )
                st.plotly_chart(fig)
            else:
                st.warning(f"No food type data available for {selected_city}")
        else:
            st.warning(f"No data available for {selected_city}")
    else:
        st.error("No data available to display in the Food Type Analysis section.")
elif choice == "Correlation Analysis":
    st.header("Correlation Analysis")
    
    if df is not None:
        # Correlation heatmap
        st.subheader("Correlation Heatmap")
        
        numeric_df = df.select_dtypes(include=[np.number])
        correlation_matrix = numeric_df.corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=correlation_matrix.values,
            x=correlation_matrix.columns,
            y=correlation_matrix.columns,
            colorscale='Viridis',
            hoverongaps=False)
        )
        fig.update_layout(
            title='Correlation Heatmap of Factors Affecting Restaurant Data',
            height=600,
        )
        st.plotly_chart(fig)
        
        st.write("""
        ## Key Correlation Findings:
        
        - **Price and Ratings**: Shows the relationship between restaurant pricing and customer satisfaction
        - **Delivery Time and Ratings**: Indicates how delivery speed affects customer perception
        - **Total Ratings and Average Ratings**: Reveals whether popular restaurants maintain consistent quality
        """)
        
       

# Add a footer
st.markdown("---")
st.markdown("Swiggy Restaurant Analysis Dashboard | Created with Streamlit by [Rahul](https://www.linkedin.com/in/rahulx2001/)")
