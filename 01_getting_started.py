"""
Lesson 1: Getting Started with Streamlit
========================================

Welcome to your first Streamlit app! In this lesson, you'll learn:
- How to create a simple Streamlit app
- Basic Streamlit commands
- How to run your app

Let's start with the fundamentals!
"""

import streamlit as st
import datetime

# Set page configuration
st.set_page_config(
    page_title="My First Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Main title
st.title("🚀 Welcome to Streamlit!")
st.markdown("### Your First Interactive Web App")

# Introduction
st.write("""
This is your first Streamlit app! Streamlit makes it super easy to turn Python scripts 
into interactive web applications. Let's explore some basic features.
""")

# Sidebar
st.sidebar.header("Navigation")
st.sidebar.write("Use this sidebar to navigate through different sections!")

# Basic text and markdown
st.header("📝 Text and Markdown")
st.write("This is regular text using `st.write()`")

st.markdown("""
### This is a markdown header
You can use **bold text**, *italic text*, and even `code snippets`.

- Bullet points work too!
- And numbered lists:
  1. First item
  2. Second item
  3. Third item
""")

# Displaying data
st.header("📊 Displaying Data")

# Simple variables
name = "Python Student"
age = 18
favorite_language = "Python"

st.write(f"**Name:** {name}")
st.write(f"**Age:** {age}")
st.write(f"**Favorite Language:** {favorite_language}")

# Lists and dictionaries
st.subheader("Lists and Dictionaries")
my_list = ["Apple", "Banana", "Cherry"]
my_dict = {"Name": "Alice", "Age": 20, "City": "Pythonville"}

st.write("**My List:**", my_list)
st.write("**My Dictionary:**", my_dict)

# Current time
st.header("⏰ Real-time Updates")
current_time = datetime.datetime.now()
st.write(f"**Current time:** {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Success, info, warning, and error messages
st.header("💬 Different Types of Messages")
st.success("This is a success message! 🎉")
st.info("This is an info message! ℹ️")
st.warning("This is a warning message! ⚠️")
st.error("This is an error message! ❌")

# Code display
st.header("💻 Code Display")
st.code("""
# This is how you display code
import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first app!")
""", language="python")

# Expander for additional information
with st.expander("🤔 How to run this app"):
    st.write("""
    1. Save this file as `01_getting_started.py`
    2. Open your terminal/command prompt
    3. Navigate to this directory
    4. Run: `streamlit run 01_getting_started.py`
    5. Your browser will open automatically!
    """)

# Footer
st.markdown("---")
st.markdown("**Next lesson:** Basic Widgets - Learn about buttons, sliders, and more!")

# Fun interactive element
if st.button("🎉 Click me for a surprise!"):
    st.balloons()
    st.write("🎊 Congratulations! You just used your first Streamlit widget!") 