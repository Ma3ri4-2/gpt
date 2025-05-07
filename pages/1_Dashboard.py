import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime
import altair as alt


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
st.title("🍓 Fruit Quality Control Dashboard")
df = generate_fruit_data()

col1, col2, col3 = st.columns(3)
col1.metric("🍏 Total Fruits Tested", len(df))
col2.metric("✅ Fresh Fruits", (df["Quality"] == "Fresh").sum())
col3.metric("❌ Spoiled Fruits", (df["Quality"] == "Spoiled").sum())

chart_df = df["Quality"].value_counts().reset_index()
chart_df.columns = ["Quality", "Count"]

bar_chart = alt.Chart(chart_df).mark_bar(color="#FF6F61").encode(
    x=alt.X("Quality", sort=None),
    y="Count",
    color=alt.Color("Quality", scale=alt.Scale(scheme="category20")),
    tooltip=["Quality", "Count"]
    ).properties(
    title="Fruit Quality Distribution",
    width=600
    )
st.altair_chart(bar_chart, use_container_width=True)