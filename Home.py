import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime
from PIL import Image


# Sidebar navigation
# pages = ["Dashboard", "Reports", "Supplier Insights", "Fruit Shelf Life"]
# page = st.sidebar.selectbox("Select a page", pages)



# Random Data Generators
def generate_fruit_data():
    fruit_types = ["🍎 Apple", "🍌 Banana", "🍊 Orange", "🥭 Mango", "🍑 Peach"]
    quality = ["Fresh", "Ripe", "Spoiled"]
    data = {
        "Fruit": [random.choice(fruit_types) for _ in range(100)],
        "Quality": [random.choice(quality) for _ in range(100)],
        "Tested At": [datetime.datetime.now() - datetime.timedelta(minutes=random.randint(0, 1000)) for _ in range(100)]
    }
    return pd.DataFrame(data)

def generate_supplier_data():
    suppliers = ["FarmFresh Co.", "Nature's Best", "Tropical Imports", "Green Valley"]
    fruit_types = ["🍎 Apple", "🍌 Banana", "🍊 Orange", "🥭 Mango", "🍑 Peach"]
    data = {
        "Supplier": [random.choice(suppliers) for _ in range(50)],
        "Fruit": [random.choice(fruit_types) for _ in range(50)],
        "Quality Score": [random.randint(60, 100) for _ in range(50)],
        "Shipment Date": [datetime.date.today() - datetime.timedelta(days=random.randint(0, 15)) for _ in range(50)]
    }
    return pd.DataFrame(data)

def generate_ripeness_prediction():
    fruit_types = ["🍎 Apple", "🍌 Banana", "🍊 Orange", "🥭 Mango", "🍑 Peach"]
    days_to_spoil = [random.randint(1, 7) for _ in fruit_types]
    return pd.DataFrame({
        "Fruit": fruit_types,
        "Days to Ripen": [random.randint(0, 3) for _ in fruit_types],
        "Days to Spoil": days_to_spoil
    })

st.set_page_config(
    page_title="🍉 Welcome to Fruit Quality Assistant",
    layout="centered"
)




st.title("🍇 Fruit Quality Control Assistant")
st.markdown("#### 🍏 Making fruit management smarter, fresher, and juicier!")

# import model 
from ultralytics import YOLO
model = YOLO('./best.pt')

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)

    results = model(image)
    results[0].show()  # or save/show annotated image
    st.image(results[0].plot(), caption="Prediction", use_container_width=True)

st.markdown("""
Welcome to our intelligent fruit quality control dashboard — an all-in-one tool designed to assist **supermarkets**, **suppliers**, and even **individual users**!

---

### 🍽️ What You Can Explore:

- **📊 Dashboard:**  
  Real-time visual overview of tested fruits and their quality (Fresh, Ripe, Spoiled).

- **📄 Reports:**  
  Auto-generated detailed reports for quality analysis and decision making.

- **🚛 Supplier Insights:**  
  Understand which suppliers are delivering the freshest fruits.

- **⏳ Fruit Shelf Life:**  
  Estimate when your fruit will ripen or spoil using fun visuals.

---

### 🤖 Future LLM Features (Showcase)

We're integrating smart language capabilities! Here's a **preview chatbot** that helps answer fruit-related questions:

""")


# Inject custom CSS for animation and style
st.markdown("""
<style>
.goal-card {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    color: white;
    animation: fadeIn 1s ease-in-out;
}

.goal-card img {
    width: 80px;
    margin-right: 20px;
}

.goal-2 { background-color: #DDA63A; }       /* Zero Hunger */
.goal-9 { background-color: #F36D25; }       /* Industry */
.goal-12 { background-color: #BF8B2E; }      /* Consumption */

@keyframes fadeIn {
    0% { opacity: 0; transform: translateY(10px); }
    100% { opacity: 1; transform: translateY(0); }
}

h2.section-title {
    margin-top: 0;
    margin-bottom: 30px;
    font-size: 28px;
    color: #263B76;
}
</style>
""", unsafe_allow_html=True)

# Section title
st.markdown('<h2 class="section-title">🌱 Sustainability Goals We Support</h2>', unsafe_allow_html=True)

# Cards
def goal_card(goal_class, img_path, title, desc):
    st.markdown(f"""
    <div class="goal-card {goal_class}">
        <img src="{img_path}">
        <div>
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

goal_card(
    "goal-2",
    "./Images/TheGlobalGoals_Icons_Color_Goal_2.png",
    "Goal 2: Zero Hunger",
    "Our system helps reduce food waste and improves fruit distribution efficiency. Detecting spoilage early means more produce reaches markets."
)

goal_card(
    "goal-9",
    "./Images/TheGlobalGoals_Icons_Color_Goal_9.png",
    "Goal 9: Industry, Innovation, and Infrastructure",
    "We use AI and robotics to bring cutting-edge agricultural solutions — transforming outdated sorting into smart, automated processes."
)

goal_card(
    "goal-12",
    "Images/TheGlobalGoals_Icons_Color_Goal_12.png",
    "Goal 12: Responsible Consumption and Production",
    "Minimizing post-harvest loss through smart detection ensures sustainable production and less waste across the supply chain."
)
# Simple LLM-style mock chatbot widget
user_question = st.text_input("Ask me anything about your fruit 🍌", placeholder="e.g., When will my banana go bad?")
if user_question:
    fake_answers = [
        "Based on average shelf life, your banana might spoil in 2–3 days.",
        "If your fruit has brown spots and smells fermented, it’s probably past its prime.",
        "You can store it in the fridge to extend freshness!",
        "Try turning your overripe fruit into a smoothie or jam. 🍓",
        "That mango sounds ready to eat — enjoy it before tomorrow!"
    ]
    st.info(f"🤖 Assistant: {random.choice(fake_answers)}")

st.markdown("---")
st.success("Use the sidebar to explore the features ➡️")
