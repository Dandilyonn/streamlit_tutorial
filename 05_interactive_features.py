"""
Lesson 5: Interactive Features
=============================

In this lesson, you'll learn about advanced interactive features in Streamlit:
- File uploads and downloads
- Session state management
- Forms and validation
- Progress bars and spinners
- Caching for performance
- Real-time updates

Take your apps to the next level!
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
import json
import io
from PIL import Image
import requests

# Page configuration
st.set_page_config(
    page_title="Interactive Features Tutorial",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Interactive Features Tutorial")
st.markdown("### Advanced Streamlit Functionality")

# Introduction
st.write("""
In this lesson, you'll learn how to create truly interactive applications with features
like file handling, state management, and real-time updates. These are the features that
make Streamlit apps powerful and user-friendly!
""")

# 1. SESSION STATE
st.header("💾 Session State Management")

st.write("""
Session state allows you to store and persist data throughout a user's session.
This is essential for creating interactive applications that remember user choices.
""")

# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

if 'app_state' not in st.session_state:
    st.session_state.app_state = 'initial'

# Session state examples
st.subheader("Counter Example")
col1, col2, col3 = st.columns(3)

with col1:
    st.write(f"**Current count:** {st.session_state.counter}")
    
with col2:
    if st.button("Increment"):
        st.session_state.counter += 1
        st.rerun()
        
with col3:
    if st.button("Reset"):
        st.session_state.counter = 0
        st.rerun()

# User data storage
st.subheader("User Data Storage")
user_name = st.text_input("Enter your name:", key="name_input")
user_age = st.number_input("Enter your age:", min_value=0, max_value=120, key="age_input")

if st.button("Save User Data"):
    st.session_state.user_data = {
        'name': user_name,
        'age': user_age,
        'timestamp': time.time()
    }
    st.success("User data saved!")

if st.session_state.user_data:
    st.write("**Saved user data:**")
    st.json(st.session_state.user_data)

# 2. FILE UPLOADS
st.header("📁 File Uploads")

st.write("Streamlit makes it easy to handle file uploads. Let's explore different file types:")

# File uploader
uploaded_file = st.file_uploader(
    "Choose a file to upload:",
    type=['csv', 'txt', 'json', 'png', 'jpg', 'jpeg'],
    help="Upload CSV, text, JSON, or image files"
)

if uploaded_file is not None:
    st.success(f"File uploaded: {uploaded_file.name}")
    
    # Handle different file types
    file_extension = uploaded_file.name.split('.')[-1].lower()
    
    if file_extension == 'csv':
        # Handle CSV files
        try:
            df = pd.read_csv(uploaded_file)
            st.write("**CSV Data Preview:**")
            st.dataframe(df.head(), use_container_width=True)
            
            # Show basic statistics
            st.write("**Data Statistics:**")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Rows:** {len(df)}")
                st.write(f"**Columns:** {len(df.columns)}")
            with col2:
                st.write(f"**Memory usage:** {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
                
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
    
    elif file_extension in ['txt', 'json']:
        # Handle text and JSON files
        content = uploaded_file.read()
        
        if file_extension == 'json':
            try:
                json_data = json.loads(content)
                st.write("**JSON Data:**")
                st.json(json_data)
            except json.JSONDecodeError:
                st.error("Invalid JSON file")
        else:
            st.write("**Text Content:**")
            st.text_area("File content:", content.decode('utf-8'), height=200)
    
    elif file_extension in ['png', 'jpg', 'jpeg']:
        # Handle image files
        image = Image.open(uploaded_file)
        st.write("**Uploaded Image:**")
        st.image(image, caption=uploaded_file.name, use_column_width=True)
        
        # Show image information
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"**Size:** {image.size}")
        with col2:
            st.write(f"**Mode:** {image.mode}")
        with col3:
            st.write(f"**Format:** {image.format}")

# 3. FILE DOWNLOADS
st.header("💾 File Downloads")

st.write("Allow users to download data and files from your app:")

# Generate sample data for download
@st.cache_data
def generate_sample_data():
    """Generate sample data for download examples"""
    data = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
        'Salary': [50000, 60000, 55000, 65000, 58000]
    })
    return data

sample_data = generate_sample_data()

# Download options
st.subheader("Download Options")

col1, col2, col3 = st.columns(3)

with col1:
    # CSV download
    csv_data = sample_data.to_csv(index=False)
    st.download_button(
        label="📊 Download as CSV",
        data=csv_data,
        file_name="sample_data.csv",
        mime="text/csv"
    )

with col2:
    # JSON download
    json_data = sample_data.to_json(orient='records', indent=2)
    st.download_button(
        label="📄 Download as JSON",
        data=json_data,
        file_name="sample_data.json",
        mime="application/json"
    )

with col3:
    # Excel download (using pandas)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        sample_data.to_excel(writer, sheet_name='Data', index=False)
    excel_data = buffer.getvalue()
    st.download_button(
        label="📈 Download as Excel",
        data=excel_data,
        file_name="sample_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# 4. FORMS
st.header("📝 Forms and Validation")

st.write("Forms allow you to collect multiple inputs and validate them together:")

# Simple form
with st.form("user_registration"):
    st.subheader("User Registration Form")
    
    # Form fields
    first_name = st.text_input("First Name", required=True)
    last_name = st.text_input("Last Name", required=True)
    email = st.text_input("Email", type="email", required=True)
    password = st.text_input("Password", type="password", required=True)
    confirm_password = st.text_input("Confirm Password", type="password", required=True)
    
    # Dropdown and selectbox
    country = st.selectbox("Country", ["USA", "Canada", "UK", "Australia", "Other"])
    interests = st.multiselect("Interests", ["Technology", "Sports", "Music", "Travel", "Cooking"])
    
    # Checkbox for terms
    agree_terms = st.checkbox("I agree to the terms and conditions", required=True)
    
    # Submit button
    submitted = st.form_submit_button("Register")
    
    if submitted:
        # Validation
        if password != confirm_password:
            st.error("Passwords do not match!")
        elif len(password) < 6:
            st.error("Password must be at least 6 characters long!")
        elif not agree_terms:
            st.error("You must agree to the terms and conditions!")
        else:
            st.success("Registration successful!")
            
            # Store in session state
            st.session_state.user_data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'country': country,
                'interests': interests
            }

# 5. PROGRESS BARS AND SPINNERS
st.header("⏳ Progress Indicators")

st.write("Show progress and loading states to improve user experience:")

# Progress bar
st.subheader("Progress Bar")
progress_value = st.slider("Progress", 0, 100, 50)
progress_bar = st.progress(progress_value)
st.write(f"Progress: {progress_value}%")

# Animated progress
if st.button("Start Progress Animation"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(101):
        time.sleep(0.05)
        progress_bar.progress(i)
        status_text.text(f"Processing... {i}%")
    
    status_text.text("Complete!")
    st.success("Task completed successfully!")

# Spinner
st.subheader("Spinner")
if st.button("Show Spinner"):
    with st.spinner("Processing your request..."):
        time.sleep(3)
    st.success("Done!")

# 6. CACHING
st.header("🚀 Performance with Caching")

st.write("""
Caching helps improve performance by storing the results of expensive computations.
This is especially useful for data processing and API calls.
""")

# Simple caching example
@st.cache_data
def expensive_calculation(n):
    """Simulate an expensive calculation"""
    time.sleep(2)  # Simulate processing time
    return sum(i**2 for i in range(n))

# Caching demonstration
st.subheader("Caching Demonstration")
number = st.number_input("Enter a number for calculation:", min_value=1, max_value=1000, value=100)

if st.button("Calculate (with caching)"):
    start_time = time.time()
    result = expensive_calculation(number)
    end_time = time.time()
    
    st.write(f"**Result:** {result}")
    st.write(f"**Time taken:** {end_time - start_time:.2f} seconds")
    st.info("Try running this again - it will be much faster due to caching!")

# 7. REAL-TIME UPDATES
st.header("🔄 Real-Time Updates")

st.write("Create dynamic content that updates in real-time:")

# Auto-refresh example
st.subheader("Auto-refreshing Content")

# Add a checkbox to control auto-refresh
auto_refresh = st.checkbox("Enable auto-refresh")

if auto_refresh:
    # This will refresh every 5 seconds
    time.sleep(5)
    st.rerun()

# Real-time clock
st.subheader("Real-time Clock")
current_time = time.strftime("%H:%M:%S")
st.write(f"**Current time:** {current_time}")

if st.button("Update Time"):
    st.rerun()

# 8. INTERACTIVE DATA PROCESSING
st.header("🔧 Interactive Data Processing")

st.write("Let's create an interactive data processing tool:")

# File upload for processing
uploaded_data = st.file_uploader("Upload CSV for processing:", type=['csv'])

if uploaded_data is not None:
    df = pd.read_csv(uploaded_data)
    
    st.write("**Original Data:**")
    st.dataframe(df.head(), use_container_width=True)
    
    # Processing options
    st.subheader("Data Processing Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Column selection
        selected_columns = st.multiselect("Select columns to display:", df.columns.tolist())
        
        # Filtering
        if len(df.columns) > 0:
            filter_column = st.selectbox("Filter by column:", df.columns.tolist())
            if df[filter_column].dtype in ['object', 'string']:
                unique_values = df[filter_column].unique()
                filter_value = st.selectbox("Filter value:", unique_values)
                filtered_df = df[df[filter_column] == filter_value]
            else:
                min_val = float(df[filter_column].min())
                max_val = float(df[filter_column].max())
                filter_range = st.slider("Filter range:", min_val, max_val, (min_val, max_val))
                filtered_df = df[(df[filter_column] >= filter_range[0]) & 
                               (df[filter_column] <= filter_range[1])]
    
    with col2:
        # Sorting
        sort_column = st.selectbox("Sort by:", df.columns.tolist())
        sort_ascending = st.checkbox("Sort ascending", value=True)
        
        # Aggregation
        agg_column = st.selectbox("Aggregate by:", df.columns.tolist())
        agg_function = st.selectbox("Aggregation function:", ["mean", "sum", "count", "min", "max"])
    
    # Apply processing
    if st.button("Apply Processing"):
        # Apply column selection
        if selected_columns:
            processed_df = filtered_df[selected_columns]
        else:
            processed_df = filtered_df
        
        # Apply sorting
        processed_df = processed_df.sort_values(by=sort_column, ascending=sort_ascending)
        
        st.write("**Processed Data:**")
        st.dataframe(processed_df, use_container_width=True)
        
        # Show aggregation
        if agg_column and agg_function:
            agg_result = processed_df[agg_column].agg(agg_function)
            st.write(f"**{agg_function.title()} of {agg_column}:** {agg_result}")
        
        # Download processed data
        processed_csv = processed_df.to_csv(index=False)
        st.download_button(
            label="Download Processed Data",
            data=processed_csv,
            file_name="processed_data.csv",
            mime="text/csv"
        )

# 9. PUTTING IT ALL TOGETHER
st.header("🎯 Complete Interactive App")

st.write("Let's create a complete interactive application that combines all these features:")

# Create tabs for different sections
tab1, tab2, tab3 = st.tabs(["📊 Data Analysis", "🎨 Image Processor", "📈 Real-time Dashboard"])

with tab1:
    st.subheader("Interactive Data Analysis")
    
    # File upload
    analysis_file = st.file_uploader("Upload data for analysis:", type=['csv'], key="analysis")
    
    if analysis_file is not None:
        analysis_df = pd.read_csv(analysis_file)
        
        # Analysis options
        col1, col2 = st.columns(2)
        
        with col1:
            chart_type = st.selectbox("Chart type:", ["Line", "Bar", "Scatter", "Histogram"])
            x_column = st.selectbox("X-axis:", analysis_df.columns.tolist())
            y_column = st.selectbox("Y-axis:", analysis_df.columns.tolist())
        
        with col2:
            color_column = st.selectbox("Color by (optional):", ["None"] + analysis_df.columns.tolist())
            if color_column == "None":
                color_column = None
        
        # Create chart
        if st.button("Generate Chart"):
            if chart_type == "Line":
                fig = px.line(analysis_df, x=x_column, y=y_column, color=color_column)
            elif chart_type == "Bar":
                fig = px.bar(analysis_df, x=x_column, y=y_column, color=color_column)
            elif chart_type == "Scatter":
                fig = px.scatter(analysis_df, x=x_column, y=y_column, color=color_column)
            elif chart_type == "Histogram":
                fig = px.histogram(analysis_df, x=x_column, color=color_column)
            
            st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Image Processing Tool")
    
    # Image upload
    image_file = st.file_uploader("Upload an image:", type=['png', 'jpg', 'jpeg'], key="image")
    
    if image_file is not None:
        image = Image.open(image_file)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Original Image:**")
            st.image(image, caption="Original", use_column_width=True)
        
        with col2:
            # Processing options
            st.write("**Processing Options:**")
            
            # Resize
            resize = st.checkbox("Resize image")
            if resize:
                new_width = st.slider("New width:", 100, 1000, image.width)
                new_height = st.slider("New height:", 100, 1000, image.height)
                processed_image = image.resize((new_width, new_height))
            else:
                processed_image = image
            
            # Rotate
            rotation = st.slider("Rotation (degrees):", 0, 360, 0)
            if rotation != 0:
                processed_image = processed_image.rotate(rotation)
            
            # Apply processing
            if st.button("Apply Processing"):
                st.write("**Processed Image:**")
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

with tab3:
    st.subheader("Real-time Dashboard")
    
    # Simulate real-time data
    if 'dashboard_data' not in st.session_state:
        st.session_state.dashboard_data = []
    
    # Add new data point
    if st.button("Add Data Point"):
        new_point = {
            'timestamp': time.time(),
            'value': np.random.randint(50, 150),
            'category': np.random.choice(['A', 'B', 'C'])
        }
        st.session_state.dashboard_data.append(new_point)
        
        # Keep only last 20 points
        if len(st.session_state.dashboard_data) > 20:
            st.session_state.dashboard_data = st.session_state.dashboard_data[-20:]
    
    if st.session_state.dashboard_data:
        # Convert to DataFrame
        dashboard_df = pd.DataFrame(st.session_state.dashboard_data)
        dashboard_df['timestamp'] = pd.to_datetime(dashboard_df['timestamp'], unit='s')
        
        # Display metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Points", len(dashboard_df))
        with col2:
            st.metric("Average Value", f"{dashboard_df['value'].mean():.1f}")
        with col3:
            st.metric("Latest Value", dashboard_df['value'].iloc[-1])
        
        # Chart
        fig = px.line(dashboard_df, x='timestamp', y='value', color='category',
                     title='Real-time Data')
        st.plotly_chart(fig, use_container_width=True)
        
        # Data table
        st.write("**Recent Data:**")
        st.dataframe(dashboard_df.tail(10), use_container_width=True)
    else:
        st.info("Click 'Add Data Point' to start collecting data!")

# Footer
st.markdown("---")
st.markdown("**Next lesson:** Real Projects - Build complete applications!")

# Challenge
with st.expander("🎯 Challenge: Build an Interactive App"):
    st.write("""
    **Your challenge:** Create a complete interactive application using all the features you've learned.
    
    Requirements:
    - File upload and processing
    - Session state management
    - Forms with validation
    - Real-time updates
    - Data visualization
    - File downloads
    
    Ideas:
    - Personal finance tracker
    - Image gallery with filters
    - Survey data analyzer
    - Weather data dashboard
    - Recipe manager
    
    Make it comprehensive and user-friendly!
    """) 