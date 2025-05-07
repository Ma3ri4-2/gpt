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

st.title("🚚 Supplier Quality Insights")
df = generate_supplier_data()

avg_score = df.groupby("Supplier")["Quality Score"].mean().reset_index()

supplier_chart = alt.Chart(avg_score).mark_bar().encode(
        x=alt.X("Supplier", sort=None),
        y="Quality Score",
        color=alt.Color("Supplier", scale=alt.Scale(scheme="set2")),
        tooltip=["Supplier", "Quality Score"]
    ).properties(
        title="📦 Average Quality Score by Supplier",
        width=600
    )
st.altair_chart(supplier_chart, use_container_width=True)

st.write("### 🚛 Shipment Records")
st.dataframe(df)

st.write("### 🚚 Last Shipment Health Score")
latest_score = random.randint(60, 100)
if latest_score >= 85:
    color = "green"
    status = "Excellent Condition"
elif latest_score >= 70:
    color = "orange"
    status = "Okay Condition"
else:
    color = "red"
    status = "Poor Condition"

st.markdown(f"""
        <div style='padding: 1rem; border-radius: 10px; background-color: {color}; color: white;'>
            <h4>🚚 Last Shipment Score: {latest_score}/100 – {status}</h4>
        </div>
    """, unsafe_allow_html=True)