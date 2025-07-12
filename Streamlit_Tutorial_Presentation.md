# Streamlit Tutorial Presentation
## Interactive Web Apps with Python

---

# 🚀 Streamlit Tutorial
### Building Interactive Web Applications with Python

**Presented by:** Archana Chaudhary  
**Date:** July 13th 2025
**For:** SEEDS Python Students


##  What is Streamlit?
### The Python Web App Framework

- **Streamlit** is a Python library for creating web applications
- **Perfect for students** - no HTML/CSS/JavaScript required
- **Data science focused** - built for ML and data visualization
- **Simple syntax** - write Python, get web apps instantly

**Why Streamlit?**
- ✅ Easy to learn
- ✅ Fast development
- ✅ Great for data visualization
- ✅ Perfect for projects and portfolios

---

## What You'll Learn Today
### Complete Learning Path

1. **Getting Started** - Your first Streamlit app
2. **Basic Widgets** - Interactive elements
3. **Data Display** - Tables, charts, visualizations
4. **Layout & Styling** - Professional app design
5. **Interactive Features** - Advanced functionality
6. **Real Projects** - Complete applications

**By the end:** You'll build your own interactive web applications!

---

## Installation & Setup
### Getting Ready to Code

**Prerequisites:**
- Python 3.7 or higher
- Basic Python knowledge
- Curiosity and enthusiasm!

**Installation:**
```bash
pip install streamlit
```

**Running your first app:**
```bash
streamlit run your_app.py
```

---

##  Lesson 1 - Getting Started
### Your First Streamlit App

**Key Concepts:**
- Basic Streamlit commands
- Page configuration
- Text and markdown display
- Data presentation
- Real-time updates

**Demo:** Let's see a live example!

---

## Basic Streamlit Commands
### Essential Functions

```python
import streamlit as st

# Page setup
st.set_page_config(page_title="My App", page_icon="🚀")

# Content display
st.title("My App Title")
st.header("Section Header")
st.subheader("Subsection")
st.write("Regular text")
st.markdown("**Bold text** and *italic*")

# Messages
st.success("Success message!")
st.info("Info message!")
st.warning("Warning message!")
st.error("Error message!")
```

---

##  Lesson 2 - Basic Widgets
### Making Apps Interactive

**Widgets Covered:**
- 🔘 Buttons
- 📝 Text inputs
- 🔢 Number inputs
- 🎚️ Sliders
- 📋 Select boxes
- ☑️ Checkboxes
- 🔘 Radio buttons

**Why Widgets Matter:**
- User interaction
- Data collection
- App control
- Dynamic content

---

##  Widget Examples
### Interactive Elements in Action

**Button:**
```python
if st.button("Click Me!"):
    st.write("Button clicked!")
```

**Text Input:**
```python
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
```

**Slider:**
```python
age = st.slider("Your age:", 0, 100, 25)
st.write(f"You are {age} years old.")
```

---

##  Lesson 3 - Data Display
### Visualizing Information

**Data Display Tools:**
- 📊 Tables and DataFrames
- 📈 Charts and graphs
- 🎨 Interactive plots
- 📋 Data filtering

**Libraries Used:**
- pandas (DataFrames)
- plotly (Interactive charts)
- matplotlib (Static plots)
- altair (Declarative charts)

---

## Data Visualization Examples
### Charts and Graphs

**Line Chart:**
```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({'x': [1,2,3,4], 'y': [1,4,2,3]})
fig = px.line(df, x='x', y='y')
st.plotly_chart(fig)
```

**Bar Chart:**
```python
st.bar_chart(data)
```

**DataFrame:**
```python
st.dataframe(df)
```

---

## Lesson 4 - Layout & Styling
### Professional App Design

**Layout Tools:**
- 📐 Columns and containers
- 📱 Sidebars and navigation
- 🎨 Custom CSS styling
- 📏 Responsive design

**Design Principles:**
- Clean and organized
- User-friendly navigation
- Consistent styling
- Mobile-responsive

---

## Layout Examples
### Organizing Your App

**Columns:**
```python
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Left column")
with col2:
    st.write("Middle column")
with col3:
    st.write("Right column")
```

**Sidebar:**
```python
st.sidebar.header("Navigation")
st.sidebar.selectbox("Choose page:", ["Home", "About", "Contact"])
```

---

##  Lesson 5 - Interactive Features
### Advanced Functionality

**Advanced Features:**
- 📁 File uploads and downloads
- 💾 Session state management
- 📝 Forms with validation
- ⚡ Caching for performance
- 🔄 Real-time updates

**Real-world Applications:**
- Data analysis tools
- Machine learning interfaces
- Dashboard applications
- Interactive reports

---

## File Upload Examples
### Handling Different File Types

**CSV File Upload with Validation:**
```python
import pandas as pd
import streamlit as st

uploaded_file = st.file_uploader(
    "Choose a CSV file", 
    type=['csv'],
    help="Upload a CSV file to analyze"
)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ File uploaded successfully! Shape: {df.shape}")
        st.dataframe(df.head())
        
        # Show file info
        st.write(f"**File name:** {uploaded_file.name}")
        st.write(f"**File size:** {uploaded_file.size} bytes")
        
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
```

**Multiple File Upload:**
```python
uploaded_files = st.file_uploader(
    "Upload multiple files",
    type=['csv', 'xlsx', 'json'],
    accept_multiple_files=True
)

if uploaded_files:
    st.write(f"📁 {len(uploaded_files)} files uploaded:")
    for file in uploaded_files:
        st.write(f"- {file.name} ({file.size} bytes)")
```

**Image Upload with Preview:**
```python
from PIL import Image

uploaded_image = st.file_uploader(
    "Upload an image",
    type=['png', 'jpg', 'jpeg'],
    help="Upload an image to process"
)

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption=uploaded_image.name, use_column_width=True)
    
    # Show image details
    st.write(f"**Image size:** {image.size}")
    st.write(f"**Image mode:** {image.mode}")
```


---

## Session State & Caching
### Managing App State

**Session State:**
```python
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Count: {st.session_state.counter}")
```

**Caching:**
```python
@st.cache_data
def expensive_function(data):
    # Expensive computation
    return result
```

##  Best Practices
### Tips for Success

**Code Organization:**
- Start simple, add features gradually
- Use clear variable names
- Add helpful comments
- Test thoroughly

**User Experience:**
- Intuitive navigation
- Clear instructions
- Responsive design
- Error handling

**Performance:**
- Use caching for expensive operations
- Optimize data processing
- Limit data size
- Test with real data

---

##  Common Pitfalls
### What to Avoid

❌ **Overcomplicating** - Start simple  
❌ **Ignoring Errors** - Always handle gracefully  
❌ **Poor Layout** - Plan before coding  
❌ **No Testing** - Test with real users  
❌ **Forgetting Mobile** - Consider mobile users  

✅ **Start Simple** - Build incrementally  
✅ **Handle Errors** - Graceful error messages  
✅ **Plan Layout** - Sketch your app first  
✅ **Test Thoroughly** - Multiple scenarios  
✅ **Mobile-First** - Responsive design  

---

##  Deployment & Sharing
### Taking Your Apps Live

**Streamlit Cloud:**
- Free hosting for Streamlit apps
- Easy deployment from GitHub
- Automatic updates
- Public sharing

**Other Options:**
- Heroku
- AWS
- Google Cloud
- Local hosting

**Sharing Your Work:**
- GitHub repositories
- Streamlit Gallery
- Portfolio websites
- Social media

---

##  Resources & Support
### Where to Get Help

**Official Resources:**
- 📚 [docs.streamlit.io](https://docs.streamlit.io/)
- 🖼️ [streamlit.io/gallery](https://streamlit.io/gallery)
- 💬 [discuss.streamlit.io](https://discuss.streamlit.io/)
- 📦 [github.com/streamlit/streamlit-example](https://github.com/streamlit/streamlit-example)

**Learning Path:**
- Complete all tutorial lessons
- Build personal projects
- Share your work
- Help others learn


**Happy Coding! 🚀**

--
--

*This presentation accompanies the comprehensive Streamlit tutorial. Use these slides to guide your learning and share knowledge with others.* 