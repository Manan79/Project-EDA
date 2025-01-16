import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import helper

def Heatmap_year(df):
    st.divider()
    st.subheader('Heatmap of Events by Sport and Year')

    # table = df.drop_duplicates(subset = ['Year' , 'Event' , 'Sport'])
    # fig , ax = plt.subplots(figsize = (20,16))
    # pivot_table = table.pivot_table(
    #     index='Sport',
    #     columns='Year',
    #     values='Event',
    #     aggfunc='count',
    #     fill_value=0,
    # )

    
    # ax = sns.heatmap(pivot_table.astype('int') , annot=True)
    # plt.title("Heatmap of Events by Sport and Year")
    # plt.xlabel("Year")
    # plt.ylabel("Sport")
    # st.pyplot(fig)

    # direct image loading to save time 
    st.image("overall_heatmap.png", caption="Heatmap", use_column_width=True)

def pie_gender(df):
    st.divider()
    gender = df.Sex.value_counts().reset_index()
    gender.rename(columns = {'count' : 'Values'} , inplace = True)
    gender.Sex.replace({'M' : 'Males' , 'F': 'Females'} , inplace = True)
    
    fig = px.pie(gender , names="Sex", values="Values", title="Gender Distribution")
    st.plotly_chart(fig)

def athelet_plot(df):
    st.divider()

    st.subheader('Participation')
    a_data = helper.athletes(df)
    fig = px.line(a_data, x='Year' , y = 'Atheletes Participated')
    fig.update_layout(

        yaxis_title="Atheletes Participated",
        xaxis_title="Year"
    )
    st.plotly_chart(fig)

def event_plot(df):
    st.divider()
    st.subheader('Events Occured')
    e_data = helper.events_occur(df)
    # plt.figure(figsize=(18, 12))
    fig = px.line(e_data, x='Year' , y = 'Event occured')
    fig.update_layout(

        yaxis_title="Events Occured",
        xaxis_title="Year"
    )
    st.plotly_chart(fig)

def country_plot(df):
    st.divider()
    st.subheader('Countries Participation')
    n_data = helper.participated_country(df)
    fig = px.line(n_data, x='Year' , y = 'Country Participated')
    fig.update_layout(

        yaxis_title="Countries Participated",
        xaxis_title="Year"
    )
    st.plotly_chart(fig)