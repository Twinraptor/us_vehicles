import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header('Market of used cars data')

df_data = pd.read_csv('vehicles_us.csv')
#st.write(df_data)
#cleaning up the data the same way as the jupyter file.
df_data['model_year'] = pd.to_numeric(df_data['model_year'], errors='coerce').astype('Int64')
df_data['cylinders'] = pd.to_numeric(df_data['cylinders'], errors='coerce').astype('Int64')

def condition_number(condition):
    condition_array = ['new','like new','excellent','good','fair','salvage']
    for index, val in enumerate(condition_array, start = 1):
        if condition == val:
            return(index)

df_data['condition_number'] = df_data['condition'].apply(condition_number)
df_data['is_4wd'] = df_data['is_4wd'].fillna(0)
df_data['is_4wd'] = pd.to_numeric(df_data['is_4wd'], errors='coerce').astype('Int64')


st.write('Graph of days listed by each other factor.')
def on_change_checkbox(current_key, group):
    print('current_key:', current_key, group)

    # uncheck all checkboxes except current
    for key in checkbox_keys[group]:
        if key != current_key:
            st.session_state[key] = False

checkbox_keys = {}



# This is the scatterplot for model year vs days listed
st.write("Scatterplot of days listed by model year")
fig1 = px.scatter(df_data, x='model_year', y='days_listed')
st.plotly_chart(fig1)


# This is the histogram for data based on condition.
st.write("Histogram of days listed by model year by sum or average.")
mean_switch = st.checkbox("Display mean histogram.")

if mean_switch:
    hist_type = "avg"
else:
    hist_type = "count"

fig2= px.histogram(df_data, x='condition_number', y='days_listed', histfunc=hist_type)
st.plotly_chart(fig2)