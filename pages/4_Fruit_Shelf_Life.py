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

st.title("⏳ Fruit Ripeness & Spoilage Estimator")
df = generate_ripeness_prediction()
st.write("### 🍐 Estimated Days to Ripen & Spoil")
st.dataframe(df)

    # Melt the data for Altair stacked bar chart
melt_df = df.melt(id_vars=["Fruit"], value_vars=["Days to Ripen", "Days to Spoil"],
                      var_name="Stage", value_name="Days")

shelf_chart = alt.Chart(melt_df).mark_bar().encode(
        x=alt.X("Fruit:N", title="Fruit"),
        y=alt.Y("Days:Q", title="Days"),
        color=alt.Color("Stage:N", scale=alt.Scale(range=["orange", "red"])),
        tooltip=["Fruit", "Stage", "Days"]
    ).properties(
        title="🌡️ Shelf Life Timeline",
        width=700
    )
st.altair_chart(shelf_chart, use_container_width=True)