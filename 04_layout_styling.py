"""
Lesson 4: Layout and Styling
============================

In this lesson, you'll learn how to organize and style your Streamlit apps:
- Columns and containers
- Sidebars and tabs
- Custom CSS styling
- Responsive layouts
- Professional app design

Make your apps look professional and user-friendly!
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Layout & Styling Tutorial",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    
    .highlight-box {
        background-color: #e8f4fd;
        border: 1px solid #1f77b4;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .success-box {
        background-color: #d4edda;
        border: 1px solid #28a745;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffc107;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main title with custom styling
st.markdown('<h1 class="main-header">🎨 Layout & Styling Tutorial</h1>', unsafe_allow_html=True)
st.markdown("### Organizing Your Apps Beautifully")

# Introduction
st.markdown("""
<div class="highlight-box">
    <strong>What you'll learn:</strong><br>
    • How to organize content with columns and containers<br>
    • Using sidebars for navigation and controls<br>
    • Creating tabs for different sections<br>
    • Custom CSS styling for professional looks<br>
    • Responsive layouts that work on all devices
</div>
""", unsafe_allow_html=True)

# 1. BASIC LAYOUT - COLUMNS
st.header("📐 Basic Layout with Columns")

st.write("Columns help you organize content side by side. Let's see different ways to use them:")

# Equal width columns
st.subheader("Equal Width Columns")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("Column 1")
    st.write("This is the first column with equal width.")
    st.button("Button 1")

with col2:
    st.success("Column 2")
    st.write("This is the second column with equal width.")
    st.button("Button 2")

with col3:
    st.warning("Column 3")
    st.write("This is the third column with equal width.")
    st.button("Button 3")

# Custom width columns
st.subheader("Custom Width Columns")
col1, col2 = st.columns([2, 1])  # 2:1 ratio

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>Wide Column (2/3 width)</h3>
        <p>This column takes up 2/3 of the available space. Perfect for main content, charts, or detailed information.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>Narrow Column (1/3 width)</h3>
        <p>This column takes up 1/3 of the space. Great for side information, controls, or summaries.</p>
    </div>
    """, unsafe_allow_html=True)

# 2. CONTAINERS
st.header("📦 Containers")

st.write("Containers help you group related content together:")

# Using containers
with st.container():
    st.subheader("Grouped Content")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Temperature Data:**")
        temp_data = pd.DataFrame({
            'Time': pd.date_range('2023-01-01', periods=24, freq='H'),
            'Temperature': np.random.randint(15, 30, 24)
        })
        st.line_chart(temp_data.set_index('Time'))
    
    with col2:
        st.write("**Humidity Data:**")
        humidity_data = pd.DataFrame({
            'Time': pd.date_range('2023-01-01', periods=24, freq='H'),
            'Humidity': np.random.randint(40, 80, 24)
        })
        st.line_chart(humidity_data.set_index('Time'))

# 3. SIDEBAR
st.header("📋 Sidebar Navigation")

# Sidebar content
st.sidebar.title("🎛️ App Controls")
st.sidebar.markdown("---")

# Sidebar widgets
st.sidebar.subheader("Settings")
theme = st.sidebar.selectbox("Choose Theme:", ["Light", "Dark", "Auto"])
language = st.sidebar.selectbox("Language:", ["English", "Spanish", "French"])

st.sidebar.markdown("---")
st.sidebar.subheader("Filters")
date_range = st.sidebar.date_input(
    "Select Date Range:",
    value=(datetime.now() - timedelta(days=30), datetime.now())
)

st.sidebar.markdown("---")
st.sidebar.subheader("Quick Actions")
if st.sidebar.button("🔄 Refresh Data"):
    st.sidebar.success("Data refreshed!")

if st.sidebar.button("📊 Export Report"):
    st.sidebar.info("Report exported!")

# Display sidebar selections
st.subheader("Current Settings")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Theme", theme)
with col2:
    st.metric("Language", language)
with col3:
    st.metric("Date Range", f"{len(date_range)} days")

# 4. TABS
st.header("📑 Tabs for Organization")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📈 Analytics", "⚙️ Settings", "📝 Documentation"])

with tab1:
    st.subheader("Main Dashboard")
    
    # Dashboard metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Users", "1,234", "+12%")
    with col2:
        st.metric("Revenue", "$45,678", "+8%")
    with col3:
        st.metric("Orders", "567", "+15%")
    with col4:
        st.metric("Satisfaction", "4.8/5", "+0.2")
    
    # Dashboard chart
    chart_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [100, 120, 140, 160, 180, 200],
        'Profit': [20, 24, 28, 32, 36, 40]
    })
    
    fig = px.line(chart_data, x='Month', y=['Sales', 'Profit'],
                  title='Monthly Performance')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Analytics")
    
    # Analytics content
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**User Demographics**")
        demographics = pd.DataFrame({
            'Age Group': ['18-25', '26-35', '36-45', '46-55', '55+'],
            'Percentage': [25, 35, 20, 15, 5]
        })
        fig_demo = px.pie(demographics, values='Percentage', names='Age Group',
                         title='Age Distribution')
        st.plotly_chart(fig_demo, use_container_width=True)
    
    with col2:
        st.write("**Geographic Distribution**")
        geo_data = pd.DataFrame({
            'Region': ['North', 'South', 'East', 'West'],
            'Users': [300, 250, 400, 284]
        })
        fig_geo = px.bar(geo_data, x='Region', y='Users',
                        title='Users by Region')
        st.plotly_chart(fig_geo, use_container_width=True)

with tab3:
    st.subheader("Settings")
    
    st.markdown("""
    <div class="highlight-box">
        <h4>App Configuration</h4>
        <p>Configure your app settings here. Changes will be applied immediately.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Settings form
    with st.form("settings_form"):
        st.write("**General Settings**")
        app_name = st.text_input("App Name", value="My Streamlit App")
        description = st.text_area("Description", value="A beautiful Streamlit application")
        
        st.write("**Display Settings**")
        show_sidebar = st.checkbox("Show Sidebar", value=True)
        show_footer = st.checkbox("Show Footer", value=True)
        
        st.write("**Data Settings**")
        refresh_interval = st.slider("Auto-refresh interval (minutes)", 1, 60, 5)
        
        submitted = st.form_submit_button("Save Settings")
        if submitted:
            st.success("Settings saved successfully!")

with tab4:
    st.subheader("Documentation")
    
    st.markdown("""
    <div class="success-box">
        <h4>📚 How to Use This App</h4>
        <p>This tutorial demonstrates various layout and styling techniques in Streamlit.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("**Key Features:**")
    st.write("• **Columns**: Organize content side by side")
    st.write("• **Containers**: Group related content together")
    st.write("• **Sidebar**: Navigation and controls")
    st.write("• **Tabs**: Organize different sections")
    st.write("• **Custom CSS**: Professional styling")

# 5. EXPANDERS
st.header("📂 Expanders")

# Using expanders
with st.expander("🔍 Click to see advanced options", expanded=False):
    st.write("This is hidden content that can be expanded.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("Advanced Setting 1", value=10)
    with col2:
        st.number_input("Advanced Setting 2", value=20)

with st.expander("📊 Detailed Statistics"):
    st.write("Here are some detailed statistics:")
    
    # Generate some sample statistics
    stats_data = pd.DataFrame({
        'Metric': ['Mean', 'Median', 'Std Dev', 'Min', 'Max'],
        'Value': [45.2, 42.1, 12.3, 15.0, 89.7]
    })
    st.dataframe(stats_data, use_container_width=True)

# 6. RESPONSIVE LAYOUT
st.header("📱 Responsive Layout")

st.markdown("""
<div class="warning-box">
    <strong>💡 Tip:</strong> Streamlit automatically makes your layouts responsive. 
    Content will adjust based on screen size!
</div>
""", unsafe_allow_html=True)

# Responsive columns example
st.subheader("Responsive Column Example")

# This will automatically adjust based on screen size
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Metric 1", "100")
with col2:
    st.metric("Metric 2", "200")
with col3:
    st.metric("Metric 3", "300")
with col4:
    st.metric("Metric 4", "400")

# 7. PUTTING IT ALL TOGETHER
st.header("🎯 Complete Layout Example")

# Create a professional dashboard layout
st.markdown('<h2 class="main-header">📊 Professional Dashboard</h2>', unsafe_allow_html=True)

# Top metrics row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>Total Revenue</h3>
        <h2>$125,430</h2>
        <p style="color: green;">↗ +12.5%</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>Active Users</h3>
        <h2>2,847</h2>
        <p style="color: green;">↗ +8.2%</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>Conversion Rate</h3>
        <h2>3.2%</h2>
        <p style="color: red;">↘ -0.5%</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>Avg. Order Value</h3>
        <h2>$89.45</h2>
        <p style="color: green;">↗ +5.1%</p>
    </div>
    """, unsafe_allow_html=True)

# Main content area with tabs
tab1, tab2, tab3 = st.tabs(["📈 Performance", "👥 Users", "💰 Revenue"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Performance chart
        performance_data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=30, freq='D'),
            'Sales': np.random.randint(1000, 5000, 30),
            'Orders': np.random.randint(50, 200, 30)
        })
        
        fig_perf = px.line(performance_data, x='Date', y=['Sales', 'Orders'],
                          title='Daily Performance')
        st.plotly_chart(fig_perf, use_container_width=True)
    
    with col2:
        # Performance metrics
        st.subheader("Quick Stats")
        st.metric("Today's Sales", "$4,230")
        st.metric("Today's Orders", "47")
        st.metric("Avg. Order Value", "$90.00")
        
        st.markdown("---")
        st.subheader("Top Products")
        products = ["Product A", "Product B", "Product C", "Product D"]
        sales = [1200, 980, 850, 720]
        
        for product, sale in zip(products, sales):
            st.write(f"**{product}:** ${sale:,}")

with tab2:
    st.subheader("User Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # User demographics
        user_data = pd.DataFrame({
            'Age Group': ['18-25', '26-35', '36-45', '46-55', '55+'],
            'Users': [450, 680, 520, 380, 200]
        })
        
        fig_users = px.pie(user_data, values='Users', names='Age Group',
                          title='User Age Distribution')
        st.plotly_chart(fig_users, use_container_width=True)
    
    with col2:
        # User activity
        activity_data = pd.DataFrame({
            'Hour': range(24),
            'Active Users': np.random.randint(50, 300, 24)
        })
        
        fig_activity = px.bar(activity_data, x='Hour', y='Active Users',
                             title='Hourly User Activity')
        st.plotly_chart(fig_activity, use_container_width=True)

with tab3:
    st.subheader("Revenue Analysis")
    
    # Revenue breakdown
    revenue_data = pd.DataFrame({
        'Category': ['Electronics', 'Clothing', 'Books', 'Home', 'Sports'],
        'Revenue': [45000, 32000, 18000, 22000, 8400]
    })
    
    fig_revenue = px.bar(revenue_data, x='Category', y='Revenue',
                        title='Revenue by Category',
                        color='Revenue',
                        color_continuous_scale='viridis')
    st.plotly_chart(fig_revenue, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Next lesson:** Interactive Features - File uploads, session state, and more!")

# Challenge
with st.expander("🎯 Challenge: Create a Professional Dashboard"):
    st.write("""
    **Your challenge:** Create a professional dashboard using all the layout techniques you've learned.
    
    Requirements:
    - Use columns for layout
    - Include a sidebar with controls
    - Use tabs for different sections
    - Add custom styling with CSS
    - Make it responsive
    
    Ideas:
    - E-commerce dashboard
    - Social media analytics
    - Weather dashboard
    - Personal finance tracker
    
    Make it look professional and user-friendly!
    """) 