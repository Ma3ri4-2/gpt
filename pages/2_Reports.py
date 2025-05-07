import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime

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

st.title("📄 Auto-generated Quality Reports")
df = generate_fruit_data()
st.write("### 📊 Report Summary by Fruit and Quality Level")
st.write(df.groupby("Fruit")["Quality"].value_counts().unstack().fillna(0))

st.write("### 🧾 Sample Record Table")
st.dataframe(df.head(20))

if st.button("🧠 Generate Summary using LLM"):
    total = len(df)
    fresh = (df["Quality"] == "Fresh").sum()
    fresh_percent = round((fresh / total) * 100)
    best_fruit = df[df["Quality"] == "Fresh"]["Fruit"].value_counts().idxmax()
    worst_fruit = df[df["Quality"] == "Spoiled"]["Fruit"].value_counts().idxmax()
    supplier = random.choice(["FarmFresh Co.", "Nature's Best", "Tropical Imports", "Green Valley"])

    summary = f"Out of {total} fruits tested today, {fresh_percent}% were fresh. {best_fruit}s performed the best, while {worst_fruit}s showed signs of early spoilage. Supplier ‘{supplier}’ delivered the highest quality produce this week."
    st.success(summary)