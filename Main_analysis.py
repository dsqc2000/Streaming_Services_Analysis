import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import plotly.offline as pyo
# Set notebook mode to work in offline
import plotly.express as px
# import cufflinks as cf
# cf.go_offline()
# import plotly.graph_objects as go
# fig = go.Figure()

# from wordcloud import WordCloud



df = pd.read_csv(r"D:\Onedrive\Bureau\P.F\P.Ps\FULL_STACK_DATA_SCIENTIST_(BootCamp)\Visualization\Netflix\moviestreams.csv")
#print(df)
#print(df.shape)
#print(cols)

df.drop(['Unnamed: 0', 'ID'], axis=1, inplace=True)
cols = df.columns.tolist()
#print(cols)

#print(df.isna().sum())
#print(df["Age"])
age_map = {"18+": 18, "7+": 7, "13+": 13, "All": 0, "16+": 16}
df["AgeCopy"] = df["Age"].map(age_map)
#print(df["AgeCopy"])

df['New_Rotten_Tomatoes'] = df['Rotten Tomatoes'].str.replace("%", "")
for i in df['New_Rotten_Tomatoes']:
  if i == str:
    i.astype(int)
#print(df['New_Rotten_Tomatoes'])


#---------visualisation----------------------------------------------------------------

#print(df['Age'].value_counts())

# counting and assigning the 10 top values to a variable
languages = df.Language.value_counts().head(10)

plt.figure(figsize=(12, 8))
plt.title('Top 10 languages in Streaming Services')
sns.barplot(x=languages.index, y=languages.values)
#plt.show()
#-----------------------------------pie_chart----------------------------
from IPython.display import HTML
import plotly.express as px
fig = px.pie(df,
             values=languages.values,
             names=languages.index,
             title='Top 10 languages in Streaming Services',
             height=600)
HTML(fig.to_html())
#fig.show()


#-----------------------number of movies in specific age group-----------------------
from IPython.display import HTML
import plotly.express as px
fig = px.bar(df,
             x=df['Age'].value_counts().index,
             y=df['Age'].value_counts(),
             title="Number of Movies in specific age group in All services",
             text=df['Age'].value_counts(),
             height=600)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()


#-----------------------number of movies in specific age group_NETFLIX-----------------------

netflix_df=df[df['Netflix']==1]
fig = px.bar(netflix_df,
             x=netflix_df['Age'].value_counts().index,
             y=netflix_df['Age'].value_counts(),
             title="Number of Movies in specific age group in Netflix",
             text=netflix_df['Age'].value_counts(),
             height=600)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()

#-----------------------number of movies in specific age group_AMAZON_PRIME-----------------------

prime_df=df[df['Prime Video']==1]
fig = px.bar(netflix_df,
             x=prime_df['Age'].value_counts().index,
             y=prime_df['Age'].value_counts(),
             title="Number of Movies in specific age group in Amazon Prime Video",
             text=prime_df['Age'].value_counts(),
             height=600)
fig.update_traces(marker_color='lightsalmon',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()


#-----------------------number of movies in specific age group_DISNEY+-----------------------

Disney_df=df[df['Disney+']==1]
fig = px.bar(netflix_df,
             x=Disney_df['Age'].value_counts().index,
             y=Disney_df['Age'].value_counts(),
             title="Number of Movies in specific age group in Disney+ Video",
             text=Disney_df['Age'].value_counts(),
             height=600)
fig.update_traces(marker_color='red',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()

#-----------------------number of movies in specific age group_HULU-----------------------

Hulu_df=df[df['Hulu']==1]
fig = px.bar(netflix_df,
             x=Hulu_df['Age'].value_counts().index,
             y=Hulu_df['Age'].value_counts(),
             title="Number of Movies in specific age group in Hulu Video",
             text=Hulu_df['Age'].value_counts(),
             height=600)
fig.update_traces(marker_color='black',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()



#---------------------Rotten Tomatoes Score----------------------------
fig = px.bar(df,
             x=df['Rotten Tomatoes'].value_counts().index,
             y=df['Rotten Tomatoes'].value_counts(),
             title="Overall Rotten Tomato Ratings",
             text=df['Rotten Tomatoes'].value_counts(),
             height=600)
fig.update_traces(marker_color='blue',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()

##-------------------Rotten Tomato Ratings For Each Services------------------------------------------------
rt_scores = pd.DataFrame({'Streaming Service': ["Prime Video", "Hulu","Disney+","NetFlix"],
                                    'Rotten Tomato Score' : [netflix_df['Rotten Tomatoes'].value_counts()[0],
                                                             prime_df['Rotten Tomatoes'].value_counts()[0],
                                                             Disney_df['Rotten Tomatoes'].value_counts()[0],
                                                              Hulu_df['Rotten Tomatoes'].value_counts()[0]]})
sorted_rt_score=rt_scores.sort_values(ascending=False, by="Rotten Tomato Score")
#print(sorted_rt_score)
#PLOT IT######################################
fig = px.bar(sorted_rt_score,
             x=sorted_rt_score['Streaming Service'],
             y=sorted_rt_score['Rotten Tomato Score'],
             title="Rotten Tomato Ratings For Each Services",
             text=sorted_rt_score['Rotten Tomato Score'],
             height=600)
fig.update_traces(marker_color='purple',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()


#-----------------------------IMDB Ratings---------------------------------------
fig = px.bar(df,
             y=df['IMDb'].value_counts(),
             x=df['IMDb'].value_counts().index,
             title="Overall IMDb Ratings For All Services",
             text=df['IMDb'].value_counts(),
             height=600)
fig.update_traces(marker_color='purple',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()

####------------------------Count Of Runtimes Of Movies-----------------------------------------------
RuntimeCount=pd.DataFrame(dict(df['Runtime'].value_counts().sort_values(ascending=False)[:10]).items(),
             columns=['Runtime', 'Count'])
#print(RuntimeCount.head())
fig = px.bar(df,
             x=RuntimeCount['Runtime'],
             y=RuntimeCount['Count'],
             title="Count Of Runtimes Of Movies",
             text=RuntimeCount['Runtime'],
             height=600)
fig.update_traces(marker_color='purple',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()

#------------------------------Directors And Their Count Of Movies They Have Directed------------------------
df['Directors']=df['Directors'].astype(str) #run below code b4 this
new_data = df[df['Directors'] !=np.nan]
# new_data=df['Directors']
directors_count = dict()
direc_in_data = list(new_data['Directors'])
for xdir in direc_in_data:
    curr_dirs = xdir.split(",")
    for xd in curr_dirs:
        if xd in directors_count.keys():
            directors_count[xd] = directors_count.get(xd) + 1
            # print(directors_count[xd])
            # print('========================')
        else:
            directors_count[xd] = 1
            # print(directors_count[xd])
DirCount = pd.DataFrame(directors_count.items(), columns=['Director', 'Count'])
DirCount=DirCount.sort_values(ascending=False, by='Count').head(20)
#print(DirCount)
DirCount = DirCount.drop(56, axis=0)
#print(DirCount)

fig = px.bar(DirCount,
             x=DirCount['Director'],
             y=DirCount['Count'],
             title="Directors And The Count Of Movies They Have Directed",
             text=DirCount['Count'],
             height=600)
fig.update_traces(marker_color='purple',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()
#print(df[df['Directors']=='Jay Chapman'][['Directors','Title','Genres']])

###------------------------------------------------Exploring Genres-----------------------------------------
genres_= dict(df['Genres'].value_counts())
count_genres = dict()
for g,count in genres_.items():
    g = g.split(",")
    for i in g:
        if i in count_genres.keys():
            count_genres[i] = count_genres.get(i)+1
        else:
            count_genres[i] = 1
count_genres_df = pd.DataFrame(count_genres.items(), columns=['Genre', 'Count'])
#print(count_genres_df)
fig = px.bar(count_genres_df,
             x=count_genres_df['Genre'],
             y=count_genres_df['Count'],
             title="Genre And their Counts",
             text=count_genres_df['Count'],
             height=600)
fig.update_traces(marker_color='lightsalmon',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()

###--------------------------------------------What Are The Top Movies On Each Platform?----------NETFLIX---------------
data_netflix_top = netflix_df[netflix_df['IMDb']>8.5]
data_netflix_top = data_netflix_top[['Title', 'IMDb']].sort_values(ascending=False, by='IMDb')
#print(data_netflix_top)
fig = px.bar(data_netflix_top,
             x=data_netflix_top['Title'],
             y=data_netflix_top['IMDb'],
             title="Top Movies On Netflix",
             text=data_netflix_top['IMDb'],
             height=800)
fig.update_traces(marker_color='brown',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#fig.show()

#----------------------On Amazon Prime
amz_top = prime_df[prime_df['IMDb']>8.5]
amz_top = amz_top[['Title', 'IMDb']].sort_values(ascending=False, by='IMDb')
#print(amz_top)
fig = px.bar(amz_top,
             x=amz_top['Title'],
             y=amz_top['IMDb'],
             title="Top Movies On Amazon Prime",
             text=amz_top['IMDb'],
             height=800)
fig.update_traces(marker_color='brown',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())
#----------------------On Disney+
disney_top = Disney_df[Disney_df['IMDb']>8.5]
disney_top = disney_top[['Title', 'IMDb']].sort_values(ascending=False, by='IMDb')
#print(disney_top)
fig = px.bar(disney_top,
             x=disney_top['Title'],
             y=disney_top['IMDb'],
             title="Top Movies On Disney+",
             text=disney_top['IMDb'],
             height=800)
fig.update_traces(marker_color='lightblue',texttemplate='%{text:.2s}', textposition='outside') #for the text to be outside.
HTML(fig.to_html())

