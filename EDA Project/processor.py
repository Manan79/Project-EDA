import streamlit as st
import pandas as pd
# import app



def process_data(df, df_region):

    df = df[df.Season == 'Summer']
    df = df.merge(df_region , on = 'NOC' , how = 'left')
    df = df.drop_duplicates()

    medal = pd.get_dummies(df['Medal'] , dtype = 'int')
    df =  pd.concat([df , medal] , axis = 1 )
    df = df.drop_duplicates(subset=['NOC', 'Games', 'Year', 'Medal', 'Team', 'Sport', 'Event'])
    return (df)

