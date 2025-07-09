"""
Lesson 2: Basic Widgets
======================

In this lesson, you'll learn about Streamlit widgets - the interactive elements
that make your apps dynamic and user-friendly.

Widgets covered:
- Buttons
- Text inputs
- Number inputs
- Sliders
- Select boxes
- Checkboxes
- Radio buttons
"""

import streamlit as st
import random

# Page configuration
st.set_page_config(
    page_title="Streamlit Widgets Tutorial",
    page_icon="🎛️",
    layout="wide"
)

st.title("🎛️ Streamlit Widgets Tutorial")
st.markdown("### Making Your Apps Interactive")

# Introduction
st.write("""
Widgets are interactive elements that allow users to input data and control your app.
They're what make Streamlit apps truly interactive!
""")

# 1. BUTTONS
st.header("🔘 Buttons")
st.write("Buttons are the simplest widget. They return `True` when clicked, `False` otherwise.")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Click Me!"):
        st.success("Button was clicked! 🎉")
    else:
        st.info("Button hasn't been clicked yet.")

with col2:
    if st.button("🎲 Roll Dice"):
        result = random.randint(1, 6)
        st.write(f"You rolled a **{result}**!")

with col3:
    if st.button("🎈 Celebrate"):
        st.balloons()
        st.write("Party time! 🎊")

# 2. TEXT INPUTS
st.header("📝 Text Inputs")

# Simple text input
user_name = st.text_input("Enter your name:", placeholder="Type your name here...")
if user_name:
    st.write(f"Hello, **{user_name}**! 👋")

# Text area for longer text
user_bio = st.text_area("Tell us about yourself:", 
                       placeholder="Write a short bio...",
                       height=100)
if user_bio:
    st.write("**Your bio:**", user_bio)

# Password input
password = st.text_input("Enter password:", type="password")
if password:
    st.write("Password entered (hidden for security)")

# 3. NUMBER INPUTS
st.header("🔢 Number Inputs")

col1, col2 = st.columns(2)

with col1:
    # Integer input
    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=18)
    st.write(f"You are **{age}** years old.")

with col2:
    # Float input
    height = st.number_input("Enter your height (meters):", 
                           min_value=0.5, 
                           max_value=2.5, 
                           value=1.7, 
                           step=0.01)
    st.write(f"Your height is **{height}** meters.")

# 4. SLIDERS
st.header("🎚️ Sliders")

col1, col2 = st.columns(2)

with col1:
    # Integer slider
    temperature = st.slider("Temperature (°C):", min_value=-20, max_value=50, value=20)
    st.write(f"Temperature: **{temperature}°C**")
    
    # Color temperature indicator
    if temperature < 0:
        st.info("❄️ It's cold!")
    elif temperature > 30:
        st.warning("🔥 It's hot!")
    else:
        st.success("😊 Nice temperature!")

with col2:
    # Float slider
    volume = st.slider("Volume:", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    st.write(f"Volume: **{volume}**")
    
    # Visual volume indicator
    volume_bar = "🔊" * int(volume * 10)
    st.write(volume_bar)

# 5. SELECT BOXES
st.header("📋 Select Boxes")

# Simple selectbox
favorite_color = st.selectbox(
    "What's your favorite color?",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
)
st.write(f"Your favorite color is **{favorite_color}**!")

# Selectbox with index
favorite_fruit = st.selectbox(
    "Choose your favorite fruit:",
    ["Apple", "Banana", "Cherry", "Dragon Fruit", "Elderberry"],
    index=1  # Default selection
)
st.write(f"You chose **{favorite_fruit}**!")

# 6. CHECKBOXES
st.header("☑️ Checkboxes")

st.write("Select your interests:")

reading = st.checkbox("📚 Reading")
gaming = st.checkbox("🎮 Gaming")
sports = st.checkbox("⚽ Sports")
music = st.checkbox("🎵 Music")
coding = st.checkbox("💻 Coding")

# Show selected interests
interests = []
if reading: interests.append("Reading")
if gaming: interests.append("Gaming")
if sports: interests.append("Sports")
if music: interests.append("Music")
if coding: interests.append("Coding")

if interests:
    st.write("**Your interests:**", ", ".join(interests))
else:
    st.write("No interests selected yet.")

# 7. RADIO BUTTONS
st.header("🔘 Radio Buttons")

# Simple radio buttons
meal_choice = st.radio(
    "What would you like for lunch?",
    ["Pizza", "Burger", "Salad", "Sushi"]
)
st.write(f"You chose **{meal_choice}** for lunch!")

# Radio buttons with custom options
experience_level = st.radio(
    "What's your programming experience?",
    options=["Beginner", "Intermediate", "Advanced"],
    index=0,
    help="Select the option that best describes your experience level"
)
st.write(f"Experience level: **{experience_level}**")

# 8. PUTTING IT ALL TOGETHER
st.header("🎯 Interactive Calculator")

st.write("Let's create a simple calculator using widgets!")

col1, col2, col3 = st.columns(3)

with col1:
    num1 = st.number_input("First number:", value=0)

with col2:
    operation = st.selectbox("Operation:", ["+", "-", "*", "/"])

with col3:
    num2 = st.number_input("Second number:", value=0)

# Calculate result
if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")
            result = None
    
    if result is not None:
        st.success(f"**Result:** {num1} {operation} {num2} = {result}")

# 9. SESSION STATE (Bonus)
st.header("💾 Session State")

# Initialize session state
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0

st.write("Session state allows you to remember values between interactions.")

if st.button("Count Clicks"):
    st.session_state.click_count += 1

st.write(f"Button clicked **{st.session_state.click_count}** times!")

if st.button("Reset Counter"):
    st.session_state.click_count = 0

# Footer
st.markdown("---")
st.markdown("**Next lesson:** Data Display - Learn to show tables, charts, and visualizations!")

# Challenge
with st.expander("🎯 Challenge: Create Your Own Widget App"):
    st.write("""
    **Your challenge:** Create a simple app that uses at least 3 different widgets.
    
    Ideas:
    - A personality quiz
    - A simple game
    - A survey form
    - A unit converter
    
    Try combining different widgets to create something fun!
    """) 