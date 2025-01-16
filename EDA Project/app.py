import streamlit as st
import pandas as pd
import processor
import helper
import matplotlib.pyplot as plt
import graph
import plotly.express as px

# modifyig the dataframe
df1 = pd.read_csv('athlete_events.csv')
df_region = pd.read_csv('noc_regions.csv')
df = processor.process_data(df1, df_region)
# st.write(df)

# sidebar editing
st.sidebar.title('Olympics Analysis')
user = st.sidebar.radio('Select Analysis:',
  ('Medal Tally', 'Overall Analysis' , 'Country-wise Analysis')
)
# side bar menu

if user == 'Medal Tally':
  year,country = helper.selection(df)
  y = st.sidebar.selectbox('Year', year)
  con = st.sidebar.selectbox('Country', country)

  medal_ref = helper.medal_ref(df , y , con)
  st.table(medal_ref)
  
elif user == 'Overall Analysis':
  City_no = len(df.City.unique().tolist())
  Sport_no = len(df.Sport.unique().tolist())
  event_no = len(df.Event.unique().tolist())
  region_no = len(df.region.unique().tolist())
  year_no = len(df.Year.unique().tolist())
  name_no =len(df.Name.unique().tolist())

  st.title('Overall Analysis')
  col1, col2 , col3  , col4 = st.columns([1, 1 , 1 ,1])
  with col1:
    st.header('Editions')
    st.subheader(year_no)
  with col2:
    st.header('Sports')
    st.subheader(Sport_no)
  with col3:
    st.header('Events')
    st.subheader(event_no)
  with col4:
    st.header('Athletes')
    st.subheader(name_no)
  col5 ,col6 , col7 , col8 = st.columns([1, 1,1,1])
  with col5:
    st.header('Nations')
    st.subheader(region_no)
  with col6:
    st.header('Hosts')
    st.subheader(City_no)
    
# PLotting the graphs

  #  country participated
  graph.country_plot(df)
  # Events Occured plot
  graph.event_plot(df)
  # athelete plot
  graph.athelet_plot(df)
  # male and female participation
  graph.pie_gender(df)
  # Heatmap
  graph.Heatmap_year(df)

# top players
  st.divider()
  st.title('Top Players')
  sport = df.Sport.unique().tolist()
  sport.insert(0 , 'Overall')
  sports = st.selectbox('Select Sport', sport)
  s_val = helper.succesful(df , sports)
  st.table(s_val)

elif user == 'Country-wise Analysis':
  st.title('Country-wise Analysis')
  year,country = helper.selection(df)
  con = st.sidebar.selectbox('Select Country', country)
  ye = st.sidebar.selectbox('Select Year', year)
  tally = helper.tally_country(df , con ,ye)
  st.table(tally)



  
 

  


  
  
  


  

