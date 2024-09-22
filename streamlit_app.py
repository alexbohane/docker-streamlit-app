import pandas as pd
import streamlit as st

### --- DATA IMPORT --- #####

df_train = pd.read_parquet("data/train.parquet")
df_test = pd.read_parquet("data/test.parquet")
df_all = pd.concat([df_train, df_test])

### ------------------ ####


st.set_page_config(layout="wide")

st.title('Bike Counters in Paris - Alex Bohane')


st.header('Introduction')
st.write('The motivation behind this project was to predict the number of bikes passing by "bike counters" in Paris for a given hour.\
         These bike counters are spread over Paris and data is provided to us every hour or so over a specific time period. \
         We will make use of a given opensource dataset and utilise external data sources such as weather data in Paris for the required time period.\
         Using this data we wanted to accurately predict the bike count for each counter in Paris.\
         I was assessed using an unseen dataset of features. The evaluation metric will be the RMSE (Root Mean Square Error).')
st.write("\n")
st.write('In this streamlit application, only the initial data exploration is shown, to give an introduction to the project.')

st.header("Exploratory Data Analysis (EDA)")



st.write("\n\n")

st.write("Firstly, we explored the data, what features do we have at our disposal? What is the quantity of data we have and what \
         are the dtypes? Also we will look at initial EDA graphics to help us visualise the data.")

info_df = pd.DataFrame({
    'Column': df_all.columns,
    'Value Count': df_all.count(),
    'Unique': df_all.nunique(),
    'Dtype': df_all.dtypes,
}).reset_index(drop=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Data summary table")
    st.dataframe(info_df)

with col2:
    st.subheader("Average bike traffic per month in Paris")
    st.image('graphs/month_count.png')

st.write('We are dealing with log bike counts in this project. We can also see some interesting observations from the monthly graph data.\
         This graph clearly shows dips in bike counts in the winter period, but also in August. This is likely because people go on holiday \
         in August. The other dips could be attributed to COVID related factors but this is hard to assess as we only have data for a COVID year (and not a regular non-COVID year)')

st.write("\n")

st.write('From the data summary table, we can see that we have 30 unique bike counter site names, and we have coordinate (latitude/longitude) data. \
         Using this information an interactive map was built using Folium to show bike counter frequency in Paris by site location.')

#### --- FOLIUM MAP --- #####
def load_map():

    with open('graphs/saved_map.html', 'r', encoding='utf-8') as f:
        html_string = f.read()

    # Use components to display the map
    st.components.v1.html(html_string, height=500, scrolling=True)

    # Display the colorbar image
    st.image('graphs/colorbar.png')

st.subheader('Bike Counter Frequency in Paris by Location')

load_map()
#### ---------------- ###

st.write('Lastly, let us look at a more granular level bike usage during the week.')

st.subheader('Weekly Traffic of Bike Journeys in Paris')
st.image('graphs/week_count.png')

st.write('There seems to be a clear cyclical daily trend for our bike count data. \
         Above we can see that there are generally two peaks during the day, one in the morning around 7/8 AM and one other larger peak around 4/5 PM. \
         This is logical as it indicates people commuting to and from work. On weekends there is more of a Gaussian distribution and traffic is lower than on week days. ')

### MODEL + RESULTS ####

st.header("Model and Results")

st.write('Feature engineering was then performed. For the modelling process, an XGBoost model was used. The final RMSE for the project was....')

if st.button('Click to find out the root mean squared error (RMSE)'):
    st.write('An RMSE of 0.63!')

