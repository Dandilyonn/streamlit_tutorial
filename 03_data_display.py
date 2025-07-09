"""
Lesson 3: Data Display
=====================

In this lesson, you'll learn how to display data effectively in Streamlit:
- Tables and DataFrames
- Charts and graphs
- Data visualization
- Working with real data

This is where Streamlit really shines for data science!
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Data Display Tutorial",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Display Tutorial")
st.markdown("### Showing Data Beautifully in Streamlit")

# Introduction
st.write("""
Streamlit makes it incredibly easy to display data in various formats.
From simple tables to interactive charts, you can create professional-looking
data visualizations with just a few lines of code!
""")

# 1. CREATING SAMPLE DATA
st.header("📈 Creating Sample Data")

# Create sample data
np.random.seed(42)  # For reproducible results

# Sales data
dates = pd.date_range('2023-01-01', periods=100, freq='D')
sales_data = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.randint(100, 1000, 100),
    'Profit': np.random.randint(10, 200, 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Product': np.random.choice(['A', 'B', 'C', 'D'], 100)
})

# Student grades data
student_data = pd.DataFrame({
    'Student': [f'Student_{i}' for i in range(1, 21)],
    'Math': np.random.randint(60, 100, 20),
    'Science': np.random.randint(60, 100, 20),
    'English': np.random.randint(60, 100, 20),
    'History': np.random.randint(60, 100, 20)
})

st.write("We'll use this sample data throughout the lesson:")

# 2. DISPLAYING TABLES
st.header("📋 Tables and DataFrames")

# Basic table display
st.subheader("Basic Table Display")
st.write("**Sales Data (first 10 rows):**")
st.dataframe(sales_data.head(10))

# Interactive table with options
st.subheader("Interactive DataFrames")
st.write("**Student Grades (interactive):**")
st.dataframe(
    student_data,
    use_container_width=True,
    hide_index=True
)

# Table with formatting
st.subheader("Formatted Tables")
# Calculate average grades
student_data['Average'] = student_data[['Math', 'Science', 'English', 'History']].mean(axis=1)
student_data['Average'] = student_data['Average'].round(2)

# Display with highlighting
st.dataframe(
    student_data.style.highlight_max(axis=0, color='lightgreen')
                     .highlight_min(axis=0, color='lightcoral'),
    use_container_width=True
)

# 3. SIMPLE CHARTS WITH STREAMLIT
st.header("📊 Streamlit's Built-in Charts")

# Line chart
st.subheader("Line Chart")
chart_data = pd.DataFrame({
    'Date': sales_data['Date'][:30],
    'Sales': sales_data['Sales'][:30]
})
st.line_chart(chart_data.set_index('Date'))

# Bar chart
st.subheader("Bar Chart")
st.bar_chart(student_data.set_index('Student')[['Math', 'Science', 'English', 'History']])

# Area chart
st.subheader("Area Chart")
st.area_chart(sales_data.set_index('Date')[['Sales', 'Profit']])

# 4. PLOTLY CHARTS (INTERACTIVE)
st.header("🎯 Interactive Charts with Plotly")

# Line plot
st.subheader("Interactive Line Plot")
fig_line = px.line(sales_data, x='Date', y='Sales', 
                   title='Sales Over Time',
                   color='Region')
fig_line.update_layout(height=400)
st.plotly_chart(fig_line, use_container_width=True)

# Scatter plot
st.subheader("Scatter Plot")
fig_scatter = px.scatter(student_data, x='Math', y='Science',
                        title='Math vs Science Scores',
                        hover_data=['Student'],
                        size='Average',
                        color='Average',
                        color_continuous_scale='viridis')
st.plotly_chart(fig_scatter, use_container_width=True)

# Bar plot
st.subheader("Bar Plot")
region_sales = sales_data.groupby('Region')['Sales'].sum().reset_index()
fig_bar = px.bar(region_sales, x='Region', y='Sales',
                 title='Total Sales by Region',
                 color='Sales',
                 color_continuous_scale='plasma')
st.plotly_chart(fig_bar, use_container_width=True)

# 5. MATPLOTLIB AND SEABORN
st.header("🎨 Matplotlib and Seaborn")

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Histogram
axes[0, 0].hist(student_data['Math'], bins=10, alpha=0.7, color='skyblue')
axes[0, 0].set_title('Math Scores Distribution')
axes[0, 0].set_xlabel('Score')
axes[0, 0].set_ylabel('Frequency')

# Box plot
student_data[['Math', 'Science', 'English', 'History']].boxplot(ax=axes[0, 1])
axes[0, 1].set_title('Subject Scores Box Plot')
axes[0, 1].set_ylabel('Score')

# Correlation heatmap
correlation_matrix = student_data[['Math', 'Science', 'English', 'History']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=axes[1, 0])
axes[1, 0].set_title('Correlation Matrix')

# Pie chart
region_counts = sales_data['Region'].value_counts()
axes[1, 1].pie(region_counts.values, labels=region_counts.index, autopct='%1.1f%%')
axes[1, 1].set_title('Sales by Region')

plt.tight_layout()
st.pyplot(fig)

# 6. INTERACTIVE DATA EXPLORATION
st.header("🔍 Interactive Data Exploration")

# Sidebar filters
st.sidebar.header("Filters")

# Region filter
selected_regions = st.sidebar.multiselect(
    "Select Regions:",
    options=sales_data['Region'].unique(),
    default=sales_data['Region'].unique()
)

# Date range filter
date_range = st.sidebar.date_input(
    "Select Date Range:",
    value=(sales_data['Date'].min(), sales_data['Date'].max()),
    min_value=sales_data['Date'].min(),
    max_value=sales_data['Date'].max()
)

# Filter data based on selections
filtered_data = sales_data[
    (sales_data['Region'].isin(selected_regions)) &
    (sales_data['Date'] >= pd.to_datetime(date_range[0])) &
    (sales_data['Date'] <= pd.to_datetime(date_range[1]))
]

# Display filtered data
st.subheader("Filtered Data")
st.write(f"Showing {len(filtered_data)} records")

# Summary statistics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Sales", f"${filtered_data['Sales'].sum():,}")
with col2:
    st.metric("Average Sales", f"${filtered_data['Sales'].mean():.0f}")
with col3:
    st.metric("Total Profit", f"${filtered_data['Profit'].sum():,}")
with col4:
    st.metric("Profit Margin", f"{(filtered_data['Profit'].sum() / filtered_data['Sales'].sum() * 100):.1f}%")

# Interactive chart of filtered data
fig_filtered = px.line(filtered_data, x='Date', y='Sales', 
                      color='Region', title='Filtered Sales Data')
st.plotly_chart(fig_filtered, use_container_width=True)

# 7. ADVANCED VISUALIZATIONS
st.header("🚀 Advanced Visualizations")

# 3D Scatter plot
st.subheader("3D Scatter Plot")
fig_3d = px.scatter_3d(student_data, x='Math', y='Science', z='English',
                       title='3D View of Student Performance',
                       color='History',
                       hover_data=['Student'])
st.plotly_chart(fig_3d, use_container_width=True)

# Sunburst chart
st.subheader("Sunburst Chart")
fig_sunburst = px.sunburst(sales_data, path=['Region', 'Product'], values='Sales',
                          title='Sales by Region and Product')
st.plotly_chart(fig_sunburst, use_container_width=True)

# 8. DATA DOWNLOAD
st.header("💾 Data Export")

# Allow users to download the data
st.subheader("Download Data")
csv = sales_data.to_csv(index=False)
st.download_button(
    label="Download Sales Data as CSV",
    data=csv,
    file_name="sales_data.csv",
    mime="text/csv"
)

# 9. PUTTING IT ALL TOGETHER
st.header("🎯 Interactive Dashboard")

# Create tabs for different views
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Trends", "🎯 Analysis"])

with tab1:
    st.subheader("Sales Overview")
    
    # Key metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Sales", f"${sales_data['Sales'].sum():,}")
    with col2:
        st.metric("Average Daily Sales", f"${sales_data['Sales'].mean():.0f}")
    with col3:
        st.metric("Best Day", f"${sales_data['Sales'].max():,}")
    
    # Sales by region
    fig_overview = px.pie(sales_data.groupby('Region')['Sales'].sum().reset_index(),
                         values='Sales', names='Region',
                         title='Sales Distribution by Region')
    st.plotly_chart(fig_overview, use_container_width=True)

with tab2:
    st.subheader("Sales Trends")
    
    # Moving average
    sales_data['Moving_Average'] = sales_data['Sales'].rolling(window=7).mean()
    
    fig_trends = go.Figure()
    fig_trends.add_trace(go.Scatter(x=sales_data['Date'], y=sales_data['Sales'],
                                   mode='lines', name='Daily Sales'))
    fig_trends.add_trace(go.Scatter(x=sales_data['Date'], y=sales_data['Moving_Average'],
                                   mode='lines', name='7-Day Moving Average'))
    fig_trends.update_layout(title='Sales Trends with Moving Average')
    st.plotly_chart(fig_trends, use_container_width=True)

with tab3:
    st.subheader("Performance Analysis")
    
    # Correlation analysis
    st.write("**Correlation between Sales and Profit:**")
    correlation = sales_data['Sales'].corr(sales_data['Profit'])
    st.write(f"Correlation coefficient: **{correlation:.3f}**")
    
    # Performance by product
    product_performance = sales_data.groupby('Product').agg({
        'Sales': 'sum',
        'Profit': 'sum'
    }).reset_index()
    product_performance['Profit_Margin'] = (product_performance['Profit'] / product_performance['Sales'] * 100)
    
    fig_analysis = px.bar(product_performance, x='Product', y='Profit_Margin',
                          title='Profit Margin by Product',
                          color='Profit_Margin',
                          color_continuous_scale='RdYlGn')
    st.plotly_chart(fig_analysis, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Next lesson:** Layout and Styling - Learn to organize your app beautifully!")

# Challenge
with st.expander("🎯 Challenge: Create Your Own Data Dashboard"):
    st.write("""
    **Your challenge:** Create a dashboard that displays data in multiple formats.
    
    Ideas:
    - Weather data dashboard
    - Personal finance tracker
    - Fitness progress tracker
    - Movie/TV show ratings
    
    Use at least 3 different chart types and add interactive filters!
    """) 