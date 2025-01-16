import streamlit as st
import numpy as np
import pandas as pd
import processor

def medal_tally(df):
    medal_tally = df
    # medal_tally.groupby('region').sum()[['Gold' , 'Silver' , 'Bronze']].sort_values('Gold' , ascending = False).reset_index()
    medal_tally = medal_tally.groupby(['region']).sum()[['Gold' , 'Silver' , 'Bronze']].sort_values('Gold' , ascending = False).reset_index()
    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']
    # print(medal_tally)
    return medal_tally


def selection(df):
    year = df.Year.unique().tolist()
    year.sort()    
    year.insert(0 , 'Overall')

    country = np.unique(df['region'].dropna().values).tolist()
    country.insert(0 , 'Overall')
    return year , country


def medal_ref(df , year , country):
    medal_df = df
    # st.title("Medal Tally of Olympics")
    if year == 'Overall' and country == 'Overall':
        st.subheader('Overall Olympics Medal Tally')
        temp_df = medal_df
    elif year != 'Overall' and country == 'Overall':
        st.subheader(f'{year} Olympics Medal Tally')
        temp_df = medal_df[medal_df['Year'] == int(year)]
    elif year == 'Overall' and country != 'Overall':
        st.subheader(f'{country} Olympics Medal Tally')
        temp_df = medal_df[medal_df['region'] == country]
    else:
        st.subheader(f'{country} in {year} Olympics Medal Tally')
        temp_df = medal_df[(medal_df['region'] == country) & (medal_df['Year'] == int(year))]
    x = temp_df.groupby(['region']).sum()[['Gold' , 'Silver' , 'Bronze']].sort_values('Gold' , ascending = False).reset_index()
    x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']
  
    return(x)


def participated_country(df):
    data = df.drop_duplicates(subset = ['Year' , 'region']).Year.value_counts().reset_index().sort_values('Year')
    data.rename(columns = {'count' : 'Country Participated'} , inplace = True)
    return data

def events_occur(df):
    data = df.drop_duplicates(subset = ['Year' , 'Event']).Year.value_counts().reset_index().sort_values('Year')
    data.rename(columns = {'count' : 'Event occured'} , inplace = True)
    return data

def athletes(df):
    data = df.drop_duplicates(subset = ['Year' , 'Name']).Year.value_counts().reset_index().sort_values('Year')
    data.rename(columns = {'count' : 'Atheletes Participated'} , inplace = True)
    return data

def succesful(df , sport):
    suc_df = df.dropna(subset = ['Medal'])
    if sport != 'Overall':
        suc_df = suc_df[suc_df['Sport'] == sport]
    return suc_df.Name.value_counts().reset_index().rename(columns = {'count' : 'Medal won'}).merge(df , how = 'left')[['Name' , 'Medal won' , 'Sport' , 'region']].drop_duplicates('Name').reset_index().drop('index' , axis = 1).head(15)
    
def tally_country(df, country , year):
    st.write(f"{country} Medal Tally")
    temp_df = df[df['region'] == country ].drop_duplicates(subset=['NOC', 'Games', 'Medal', 'Year' , 'Team', 'Sport', 'Event'])
    new_df = temp_df.groupby(['Year' , 'Medal']).sum()[['Gold' , 'Silver' , 'Bronze']].reset_index()
    new_df.drop('Medal' , axis = 1 , inplace= True)
    if year != 'Overall':
        new_df = new_df[new_df['Year'] == int(year)]
    merged_df = new_df.groupby("Year", as_index=False).sum()
    return(merged_df)

    

