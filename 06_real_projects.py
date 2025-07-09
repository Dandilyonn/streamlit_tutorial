"""
Lesson 6: Real Projects
=======================

In this lesson, you'll build complete, real-world applications using everything
you've learned about Streamlit. These projects will help you understand how to
combine all the concepts into practical applications.

Projects included:
1. Personal Finance Tracker
2. Weather Dashboard
3. Image Processing App
4. Survey Data Analyzer
5. Recipe Manager

Choose a project and build it step by step!
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import requests
import json
import io
from datetime import datetime, timedelta
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Real Projects Tutorial",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Real Projects Tutorial")
st.markdown("### Build Complete Applications")

# Introduction
st.write("""
Welcome to the final lesson! Here you'll find complete, real-world projects that
combine all the Streamlit concepts you've learned. Each project is designed to be
practical and useful, while demonstrating different aspects of Streamlit development.

Choose a project that interests you and follow along!
""")

# Project selection
st.header("📋 Choose Your Project")

project_choice = st.selectbox(
    "Select a project to build:",
    [
        "💰 Personal Finance Tracker",
        "🌤️ Weather Dashboard", 
        "🖼️ Image Processing App",
        "📊 Survey Data Analyzer",
        "👨‍🍳 Recipe Manager"
    ]
)

# Initialize session state for projects
if 'finance_data' not in st.session_state:
    st.session_state.finance_data = []
if 'recipes' not in st.session_state:
    st.session_state.recipes = []

# PROJECT 1: PERSONAL FINANCE TRACKER
if project_choice == "💰 Personal Finance Tracker":
    st.header("💰 Personal Finance Tracker")
    
    st.write("""
    Build a comprehensive personal finance tracker that helps you monitor your income,
    expenses, and savings. This project demonstrates data management, visualization,
    and interactive features.
    """)
    
    # Sidebar for adding transactions
    st.sidebar.header("➕ Add Transaction")
    
    with st.sidebar.form("transaction_form"):
        transaction_type = st.selectbox("Type:", ["Income", "Expense"])
        amount = st.number_input("Amount ($):", min_value=0.01, value=10.00, step=0.01)
        category = st.selectbox("Category:", 
            ["Salary", "Freelance", "Investment"] if transaction_type == "Income" else
            ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Other"]
        )
        description = st.text_input("Description:")
        date = st.date_input("Date:", value=datetime.now())
        
        submitted = st.form_submit_button("Add Transaction")
        
        if submitted:
            transaction = {
                'date': date,
                'type': transaction_type,
                'amount': amount,
                'category': category,
                'description': description,
                'timestamp': datetime.now()
            }
            st.session_state.finance_data.append(transaction)
            st.sidebar.success("Transaction added!")
    
    # Main dashboard
    if st.session_state.finance_data:
        # Convert to DataFrame
        df = pd.DataFrame(st.session_state.finance_data)
        df['date'] = pd.to_datetime(df['date'])
        
        # Calculate metrics
        total_income = df[df['type'] == 'Income']['amount'].sum()
        total_expenses = df[df['type'] == 'Expense']['amount'].sum()
        net_income = total_income - total_expenses
        
        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Income", f"${total_income:,.2f}")
        with col2:
            st.metric("Total Expenses", f"${total_expenses:,.2f}")
        with col3:
            st.metric("Net Income", f"${net_income:,.2f}")
        with col4:
            st.metric("Transactions", len(df))
        
        # Charts
        tab1, tab2, tab3 = st.tabs(["📈 Overview", "💰 Income vs Expenses", "📊 Categories"])
        
        with tab1:
            # Monthly overview
            df['month'] = df['date'].dt.to_period('M')
            monthly_data = df.groupby(['month', 'type'])['amount'].sum().reset_index()
            
            fig_overview = px.line(monthly_data, x='month', y='amount', color='type',
                                 title='Monthly Income vs Expenses')
            st.plotly_chart(fig_overview, use_container_width=True)
        
        with tab2:
            # Income vs Expenses pie chart
            income_expense_data = pd.DataFrame({
                'Type': ['Income', 'Expenses'],
                'Amount': [total_income, total_expenses]
            })
            
            fig_pie = px.pie(income_expense_data, values='Amount', names='Type',
                           title='Income vs Expenses Distribution')
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with tab3:
            # Category breakdown
            category_data = df.groupby(['type', 'category'])['amount'].sum().reset_index()
            
            fig_category = px.bar(category_data, x='category', y='amount', color='type',
                                title='Spending by Category')
            st.plotly_chart(fig_category, use_container_width=True)
        
        # Recent transactions
        st.subheader("Recent Transactions")
        recent_df = df.sort_values('timestamp', ascending=False).head(10)
        st.dataframe(recent_df[['date', 'type', 'amount', 'category', 'description']], 
                    use_container_width=True)
        
        # Export data
        if st.button("Export Data"):
            csv_data = df.to_csv(index=False)
            st.download_button(
                label="Download Finance Data",
                data=csv_data,
                file_name="finance_data.csv",
                mime="text/csv"
            )
    
    else:
        st.info("Add your first transaction using the sidebar to get started!")

# PROJECT 2: WEATHER DASHBOARD
elif project_choice == "🌤️ Weather Dashboard":
    st.header("🌤️ Weather Dashboard")
    
    st.write("""
    Create a weather dashboard that fetches real-time weather data and displays it
    in an interactive format. This project demonstrates API integration, data
    visualization, and real-time updates.
    """)
    
    # City input
    city = st.text_input("Enter city name:", value="London")
    
    if st.button("Get Weather") or city:
        try:
            # Simulate weather API call (in real app, you'd use a weather API)
            # For demo purposes, we'll generate random weather data
            
            # Generate weather data
            weather_data = {
                'temperature': np.random.randint(10, 30),
                'humidity': np.random.randint(30, 90),
                'wind_speed': np.random.randint(0, 25),
                'pressure': np.random.randint(1000, 1020),
                'description': np.random.choice(['Sunny', 'Cloudy', 'Rainy', 'Partly Cloudy']),
                'feels_like': np.random.randint(8, 32)
            }
            
            # Current weather display
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Temperature", f"{weather_data['temperature']}°C")
            with col2:
                st.metric("Feels Like", f"{weather_data['feels_like']}°C")
            with col3:
                st.metric("Humidity", f"{weather_data['humidity']}%")
            with col4:
                st.metric("Wind Speed", f"{weather_data['wind_speed']} km/h")
            
            # Weather description
            st.subheader(f"Weather in {city}")
            st.write(f"**Current conditions:** {weather_data['description']}")
            st.write(f"**Pressure:** {weather_data['pressure']} hPa")
            
            # Generate 7-day forecast
            forecast_data = []
            for i in range(7):
                date = datetime.now() + timedelta(days=i)
                forecast_data.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'day': date.strftime('%A'),
                    'temp_high': np.random.randint(15, 35),
                    'temp_low': np.random.randint(5, 20),
                    'condition': np.random.choice(['Sunny', 'Cloudy', 'Rainy', 'Partly Cloudy']),
                    'humidity': np.random.randint(30, 90)
                })
            
            forecast_df = pd.DataFrame(forecast_data)
            
            # Forecast charts
            tab1, tab2 = st.tabs(["📅 7-Day Forecast", "📊 Weather Trends"])
            
            with tab1:
                # Temperature forecast
                fig_forecast = go.Figure()
                fig_forecast.add_trace(go.Scatter(
                    x=forecast_df['day'], 
                    y=forecast_df['temp_high'],
                    mode='lines+markers',
                    name='High Temperature',
                    line=dict(color='red')
                ))
                fig_forecast.add_trace(go.Scatter(
                    x=forecast_df['day'], 
                    y=forecast_df['temp_low'],
                    mode='lines+markers',
                    name='Low Temperature',
                    line=dict(color='blue')
                ))
                fig_forecast.update_layout(
                    title='7-Day Temperature Forecast',
                    xaxis_title='Day',
                    yaxis_title='Temperature (°C)'
                )
                st.plotly_chart(fig_forecast, use_container_width=True)
                
                # Forecast table
                st.subheader("Detailed Forecast")
                st.dataframe(forecast_df, use_container_width=True)
            
            with tab2:
                # Weather trends
                col1, col2 = st.columns(2)
                
                with col1:
                    # Humidity trend
                    fig_humidity = px.bar(forecast_df, x='day', y='humidity',
                                        title='Humidity Forecast')
                    st.plotly_chart(fig_humidity, use_container_width=True)
                
                with col2:
                    # Condition distribution
                    condition_counts = forecast_df['condition'].value_counts()
                    fig_conditions = px.pie(values=condition_counts.values, 
                                          names=condition_counts.index,
                                          title='Weather Conditions')
                    st.plotly_chart(fig_conditions, use_container_width=True)
        
        except Exception as e:
            st.error(f"Error fetching weather data: {e}")

# PROJECT 3: IMAGE PROCESSING APP
elif project_choice == "🖼️ Image Processing App":
    st.header("🖼️ Image Processing App")
    
    st.write("""
    Build an image processing application that allows users to upload images and
    apply various filters and transformations. This project demonstrates file
    handling, image processing, and interactive controls.
    """)
    
    # File upload
    uploaded_image = st.file_uploader("Upload an image:", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_image is not None:
        # Load image
        image = Image.open(uploaded_image)
        
        # Processing options
        st.sidebar.header("🛠️ Processing Options")
        
        # Basic transformations
        st.sidebar.subheader("Transformations")
        resize = st.sidebar.checkbox("Resize Image")
        if resize:
            new_width = st.sidebar.slider("Width:", 100, 1000, image.width)
            new_height = st.sidebar.slider("Height:", 100, 1000, image.height)
        
        rotation = st.sidebar.slider("Rotation (degrees):", 0, 360, 0)
        
        # Filters
        st.sidebar.subheader("Filters")
        brightness = st.sidebar.slider("Brightness:", 0.1, 2.0, 1.0)
        contrast = st.sidebar.slider("Contrast:", 0.1, 2.0, 1.0)
        
        # Apply processing
        processed_image = image.copy()
        
        if resize:
            processed_image = processed_image.resize((new_width, new_height))
        
        if rotation != 0:
            processed_image = processed_image.rotate(rotation)
        
        # Apply brightness and contrast (simplified)
        if brightness != 1.0 or contrast != 1.0:
            # Convert to numpy array for processing
            img_array = np.array(processed_image)
            img_array = img_array * brightness
            img_array = np.clip(img_array, 0, 255).astype(np.uint8)
            processed_image = Image.fromarray(img_array)
        
        # Display images
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original Image")
            st.image(image, caption="Original", use_column_width=True)
            
            # Image info
            st.write("**Image Information:**")
            st.write(f"Size: {image.size}")
            st.write(f"Mode: {image.mode}")
            st.write(f"Format: {image.format}")
        
        with col2:
            st.subheader("Processed Image")
            st.image(processed_image, caption="Processed", use_column_width=True)
            
            # Download processed image
            buffer = io.BytesIO()
            processed_image.save(buffer, format='PNG')
            img_data = buffer.getvalue()
            
            st.download_button(
                label="Download Processed Image",
                data=img_data,
                file_name="processed_image.png",
                mime="image/png"
            )
        
        # Additional features
        st.subheader("Additional Features")
        
        # Image analysis
        tab1, tab2 = st.tabs(["📊 Image Analysis", "🎨 Color Palette"])
        
        with tab1:
            # Basic image statistics
            img_array = np.array(image)
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Width", image.width)
            with col2:
                st.metric("Height", image.height)
            with col3:
                st.metric("Total Pixels", image.width * image.height)
            with col4:
                st.metric("File Size", f"{len(uploaded_image.getvalue()) / 1024:.1f} KB")
        
        with tab2:
            # Extract dominant colors
            img_array = np.array(image)
            pixels = img_array.reshape(-1, img_array.shape[-1])
            
            # Simple color analysis
            unique_colors = np.unique(pixels, axis=0)
            if len(unique_colors) > 10:
                # Sample colors for display
                sample_colors = unique_colors[::len(unique_colors)//10][:10]
            else:
                sample_colors = unique_colors
            
            st.write("**Dominant Colors:**")
            for i, color in enumerate(sample_colors):
                # Create a color swatch
                color_hex = '#{:02x}{:02x}{:02x}'.format(*color[:3])
                st.color_picker(f"Color {i+1}", color_hex, disabled=True)

# PROJECT 4: SURVEY DATA ANALYZER
elif project_choice == "📊 Survey Data Analyzer":
    st.header("📊 Survey Data Analyzer")
    
    st.write("""
    Create a survey data analyzer that can process and visualize survey responses.
    This project demonstrates data analysis, statistical visualization, and
    interactive filtering.
    """)
    
    # Sample survey data
    @st.cache_data
    def generate_survey_data():
        """Generate sample survey data"""
        np.random.seed(42)
        
        # Generate sample responses
        n_responses = 200
        
        data = {
            'age': np.random.randint(18, 65, n_responses),
            'gender': np.random.choice(['Male', 'Female', 'Other'], n_responses),
            'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_responses),
            'satisfaction': np.random.randint(1, 6, n_responses),
            'recommend': np.random.choice(['Yes', 'No', 'Maybe'], n_responses),
            'feedback': [
                f"Response {i}: " + np.random.choice([
                    "Great experience!", "Could be better.", "Excellent service!",
                    "Needs improvement.", "Very satisfied.", "Disappointed."
                ]) for i in range(n_responses)
            ]
        }
        
        return pd.DataFrame(data)
    
    survey_data = generate_survey_data()
    
    # File upload option
    st.subheader("📁 Upload Your Survey Data")
    uploaded_survey = st.file_uploader("Upload CSV file:", type=['csv'])
    
    if uploaded_survey is not None:
        try:
            survey_data = pd.read_csv(uploaded_survey)
            st.success("Survey data uploaded successfully!")
        except Exception as e:
            st.error(f"Error reading file: {e}")
            st.info("Using sample data instead.")
    
    # Data overview
    st.subheader("📋 Data Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Responses", len(survey_data))
    with col2:
        st.metric("Average Age", f"{survey_data['age'].mean():.1f}")
    with col3:
        st.metric("Average Satisfaction", f"{survey_data['satisfaction'].mean():.1f}/5")
    with col4:
        recommend_rate = (survey_data['recommend'] == 'Yes').mean() * 100
        st.metric("Recommendation Rate", f"{recommend_rate:.1f}%")
    
    # Filters
    st.subheader("🔍 Filters")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age_range = st.slider("Age Range:", 
                             int(survey_data['age'].min()), 
                             int(survey_data['age'].max()),
                             (int(survey_data['age'].min()), int(survey_data['age'].max())))
    
    with col2:
        selected_genders = st.multiselect("Gender:", 
                                        survey_data['gender'].unique(),
                                        default=survey_data['gender'].unique())
    
    with col3:
        selected_education = st.multiselect("Education:", 
                                          survey_data['education'].unique(),
                                          default=survey_data['education'].unique())
    
    # Apply filters
    filtered_data = survey_data[
        (survey_data['age'].between(age_range[0], age_range[1])) &
        (survey_data['gender'].isin(selected_genders)) &
        (survey_data['education'].isin(selected_education))
    ]
    
    st.write(f"**Showing {len(filtered_data)} responses**")
    
    # Analysis tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Demographics", "😊 Satisfaction", "📈 Trends", "💬 Feedback"])
    
    with tab1:
        # Demographics analysis
        col1, col2 = st.columns(2)
        
        with col1:
            # Age distribution
            fig_age = px.histogram(filtered_data, x='age', nbins=20,
                                 title='Age Distribution')
            st.plotly_chart(fig_age, use_container_width=True)
        
        with col2:
            # Gender distribution
            gender_counts = filtered_data['gender'].value_counts()
            fig_gender = px.pie(values=gender_counts.values, 
                              names=gender_counts.index,
                              title='Gender Distribution')
            st.plotly_chart(fig_gender, use_container_width=True)
        
        # Education by gender
        education_gender = pd.crosstab(filtered_data['education'], filtered_data['gender'])
        fig_education = px.bar(education_gender, title='Education by Gender')
        st.plotly_chart(fig_education, use_container_width=True)
    
    with tab2:
        # Satisfaction analysis
        col1, col2 = st.columns(2)
        
        with col1:
            # Satisfaction distribution
            satisfaction_counts = filtered_data['satisfaction'].value_counts().sort_index()
            fig_satisfaction = px.bar(x=satisfaction_counts.index, 
                                    y=satisfaction_counts.values,
                                    title='Satisfaction Distribution')
            st.plotly_chart(fig_satisfaction, use_container_width=True)
        
        with col2:
            # Satisfaction by demographic
            satisfaction_by_gender = filtered_data.groupby('gender')['satisfaction'].mean()
            fig_satisfaction_gender = px.bar(x=satisfaction_by_gender.index,
                                           y=satisfaction_by_gender.values,
                                           title='Average Satisfaction by Gender')
            st.plotly_chart(fig_satisfaction_gender, use_container_width=True)
        
        # Satisfaction heatmap
        satisfaction_heatmap = pd.crosstab(filtered_data['education'], 
                                         filtered_data['gender'], 
                                         values=filtered_data['satisfaction'], 
                                         aggfunc='mean')
        fig_heatmap = px.imshow(satisfaction_heatmap, 
                               title='Satisfaction Heatmap by Education and Gender')
        st.plotly_chart(fig_heatmap, use_container_width=True)
    
    with tab3:
        # Trend analysis
        # Create time-based analysis (simulated)
        filtered_data['response_date'] = pd.date_range(
            start='2023-01-01', 
            periods=len(filtered_data), 
            freq='D'
        )
        
        # Satisfaction over time
        fig_trend = px.line(filtered_data.groupby('response_date')['satisfaction'].mean().reset_index(),
                           x='response_date', y='satisfaction',
                           title='Satisfaction Trend Over Time')
        st.plotly_chart(fig_trend, use_container_width=True)
    
    with tab4:
        # Feedback analysis
        st.subheader("💬 Recent Feedback")
        
        # Show recent feedback
        recent_feedback = filtered_data['feedback'].tail(10)
        for i, feedback in enumerate(recent_feedback, 1):
            st.write(f"**Response {i}:** {feedback}")
        
        # Word cloud (simplified)
        st.subheader("📝 Feedback Summary")
        all_feedback = ' '.join(filtered_data['feedback'])
        st.write(f"**Total feedback length:** {len(all_feedback)} characters")
        st.write(f"**Average feedback length:** {len(all_feedback) / len(filtered_data):.1f} characters")
    
    # Export results
    if st.button("Export Analysis"):
        # Create summary report
        report_data = {
            'Metric': ['Total Responses', 'Average Age', 'Average Satisfaction', 'Recommendation Rate'],
            'Value': [
                len(filtered_data),
                f"{filtered_data['age'].mean():.1f}",
                f"{filtered_data['satisfaction'].mean():.1f}/5",
                f"{(filtered_data['recommend'] == 'Yes').mean() * 100:.1f}%"
            ]
        }
        
        report_df = pd.DataFrame(report_data)
        csv_data = report_df.to_csv(index=False)
        
        st.download_button(
            label="Download Analysis Report",
            data=csv_data,
            file_name="survey_analysis.csv",
            mime="text/csv"
        )

# PROJECT 5: RECIPE MANAGER
elif project_choice == "👨‍🍳 Recipe Manager":
    st.header("👨‍🍳 Recipe Manager")
    
    st.write("""
    Build a recipe manager that allows users to store, search, and organize recipes.
    This project demonstrates data management, search functionality, and user
    interface design.
    """)
    
    # Initialize recipes if empty
    if not st.session_state.recipes:
        st.session_state.recipes = [
            {
                'name': 'Spaghetti Carbonara',
                'ingredients': ['pasta', 'eggs', 'bacon', 'parmesan', 'black pepper'],
                'instructions': 'Cook pasta, mix eggs with cheese, combine with hot pasta and bacon.',
                'cooking_time': 20,
                'difficulty': 'Medium',
                'cuisine': 'Italian',
                'tags': ['pasta', 'quick', 'dinner']
            },
            {
                'name': 'Chicken Stir Fry',
                'ingredients': ['chicken', 'vegetables', 'soy sauce', 'ginger', 'garlic'],
                'instructions': 'Stir fry chicken, add vegetables, season with soy sauce and spices.',
                'cooking_time': 25,
                'difficulty': 'Easy',
                'cuisine': 'Asian',
                'tags': ['chicken', 'healthy', 'quick']
            }
        ]
    
    # Sidebar for adding recipes
    st.sidebar.header("➕ Add New Recipe")
    
    with st.sidebar.form("recipe_form"):
        recipe_name = st.text_input("Recipe Name:")
        ingredients = st.text_area("Ingredients (one per line):")
        instructions = st.text_area("Instructions:")
        cooking_time = st.number_input("Cooking Time (minutes):", min_value=1, value=30)
        difficulty = st.selectbox("Difficulty:", ["Easy", "Medium", "Hard"])
        cuisine = st.selectbox("Cuisine:", ["Italian", "Asian", "Mexican", "American", "Other"])
        tags = st.text_input("Tags (comma-separated):")
        
        submitted = st.form_submit_button("Add Recipe")
        
        if submitted and recipe_name:
            new_recipe = {
                'name': recipe_name,
                'ingredients': [ing.strip() for ing in ingredients.split('\n') if ing.strip()],
                'instructions': instructions,
                'cooking_time': cooking_time,
                'difficulty': difficulty,
                'cuisine': cuisine,
                'tags': [tag.strip() for tag in tags.split(',') if tag.strip()]
            }
            st.session_state.recipes.append(new_recipe)
            st.sidebar.success("Recipe added!")
    
    # Search and filter
    st.subheader("🔍 Search Recipes")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_term = st.text_input("Search by name or ingredients:")
    
    with col2:
        selected_cuisine = st.selectbox("Filter by cuisine:", 
                                      ["All"] + list(set(r['cuisine'] for r in st.session_state.recipes)))
    
    with col3:
        selected_difficulty = st.selectbox("Filter by difficulty:", 
                                         ["All", "Easy", "Medium", "Hard"])
    
    # Filter recipes
    filtered_recipes = st.session_state.recipes
    
    if search_term:
        filtered_recipes = [
            r for r in filtered_recipes 
            if search_term.lower() in r['name'].lower() or 
               any(search_term.lower() in ing.lower() for ing in r['ingredients'])
        ]
    
    if selected_cuisine != "All":
        filtered_recipes = [r for r in filtered_recipes if r['cuisine'] == selected_cuisine]
    
    if selected_difficulty != "All":
        filtered_recipes = [r for r in filtered_recipes if r['difficulty'] == selected_difficulty]
    
    # Display recipes
    st.subheader(f"📖 Recipes ({len(filtered_recipes)} found)")
    
    if filtered_recipes:
        # Recipe cards
        for i, recipe in enumerate(filtered_recipes):
            with st.expander(f"🍽️ {recipe['name']}"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.write(f"**Cuisine:** {recipe['cuisine']}")
                    st.write(f"**Difficulty:** {recipe['difficulty']}")
                    st.write(f"**Cooking Time:** {recipe['cooking_time']} minutes")
                    
                    st.write("**Ingredients:**")
                    for ingredient in recipe['ingredients']:
                        st.write(f"• {ingredient}")
                    
                    st.write("**Instructions:**")
                    st.write(recipe['instructions'])
                
                with col2:
                    st.write("**Tags:**")
                    for tag in recipe['tags']:
                        st.write(f"🏷️ {tag}")
                    
                    # Recipe actions
                    if st.button(f"Delete Recipe", key=f"delete_{i}"):
                        st.session_state.recipes.remove(recipe)
                        st.rerun()
    else:
        st.info("No recipes found matching your criteria.")
    
    # Recipe statistics
    if st.session_state.recipes:
        st.subheader("📊 Recipe Statistics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Recipes", len(st.session_state.recipes))
        
        with col2:
            avg_time = sum(r['cooking_time'] for r in st.session_state.recipes) / len(st.session_state.recipes)
            st.metric("Average Cooking Time", f"{avg_time:.1f} min")
        
        with col3:
            cuisines = set(r['cuisine'] for r in st.session_state.recipes)
            st.metric("Cuisine Types", len(cuisines))
        
        with col4:
            difficulties = [r['difficulty'] for r in st.session_state.recipes]
            most_common = max(set(difficulties), key=difficulties.count)
            st.metric("Most Common Difficulty", most_common)
        
        # Charts
        tab1, tab2 = st.tabs(["📈 Recipe Analysis", "🏷️ Tag Cloud"])
        
        with tab1:
            # Cuisine distribution
            cuisine_counts = pd.Series([r['cuisine'] for r in st.session_state.recipes]).value_counts()
            fig_cuisine = px.pie(values=cuisine_counts.values, 
                               names=cuisine_counts.index,
                               title='Recipes by Cuisine')
            st.plotly_chart(fig_cuisine, use_container_width=True)
            
            # Cooking time distribution
            cooking_times = [r['cooking_time'] for r in st.session_state.recipes]
            fig_time = px.histogram(x=cooking_times, nbins=10,
                                  title='Cooking Time Distribution')
            st.plotly_chart(fig_time, use_container_width=True)
        
        with tab2:
            # Tag analysis
            all_tags = []
            for recipe in st.session_state.recipes:
                all_tags.extend(recipe['tags'])
            
            if all_tags:
                tag_counts = pd.Series(all_tags).value_counts()
                fig_tags = px.bar(x=tag_counts.index, y=tag_counts.values,
                                title='Most Popular Tags')
                st.plotly_chart(fig_tags, use_container_width=True)
    
    # Export recipes
    if st.button("Export Recipes"):
        recipes_df = pd.DataFrame(st.session_state.recipes)
        csv_data = recipes_df.to_csv(index=False)
        
        st.download_button(
            label="Download Recipe Book",
            data=csv_data,
            file_name="recipe_book.csv",
            mime="text/csv"
        )

# Footer
st.markdown("---")
st.markdown("🎉 **Congratulations! You've completed the Streamlit tutorial!**")

# Final challenge
with st.expander("🎯 Final Challenge: Build Your Own App"):
    st.write("""
    **Your final challenge:** Create your own complete Streamlit application!
    
    **Requirements:**
    - Use at least 5 different Streamlit widgets
    - Include data visualization
    - Implement file upload/download
    - Use session state for data persistence
    - Create a professional layout with styling
    - Add interactive features
    
    **Ideas for your app:**
    - Personal task manager
    - Study planner
    - Fitness tracker
    - Book review system
    - Travel itinerary planner
    - Personal blog
    - Quiz application
    - Portfolio website
    
    **Tips:**
    - Start simple and add features gradually
    - Test your app thoroughly
    - Make it user-friendly
    - Add helpful documentation
    - Consider real-world use cases
    
    Good luck with your project! 🚀
    """)

# Additional resources
st.sidebar.markdown("---")
st.sidebar.header("📚 Additional Resources")
st.sidebar.markdown("""
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Community](https://discuss.streamlit.io/)
- [GitHub Examples](https://github.com/streamlit/streamlit-example)
""") 