######################
# Import libraries
######################

import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import streamlit as st

######################
# Page Title
######################

st.write("""
## EDA on 100 years of Olympics Data 
***
In this App, I explore a data set on Kaggle containing over 100 years of olympic records 
and how different athletes performed based on their sport, age, demographic, country etc.
***
""")

st.write("""
#### A quick look at the raw data we are working with
""")

### load data
athletes = pd.read_csv("athlete_events.csv")
athletes2 = athletes.drop(["ID"], axis = 1)

## Display DF on the app
st.dataframe(athletes2)

st.write("""
#### Next, we find out the medal tally of each Country across all the years
""")

### First we filter out the rows where a medal was not won
all_medals = athletes2[athletes2.Medal.notnull()]
medals = all_medals[all_medals.Season == "Summer"]

### Next, we will visualise this DF by top 10 countries
most_medals = medals.Team.value_counts().reset_index(name='medal_count').head(5)
st.dataframe(most_medals)

fig , ax = plt.subplots() 
sns.catplot(x="index", y="medal_count", data=most_medals, height = 6)
st.pyplot(fig)

st.write("""
As we see, USA is the best performing country over the years for Summer Olympics with most medals. Now, we proceed
to explore how they have fared over the years
""")

team_usa = medals[medals.NOC == "USA"]
st.dataframe(team_usa.head())

total_diff_medals = team_usa.groupby(['Year' , 'Medal'].sort_values.)

