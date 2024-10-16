import streamlit as st
import pandas as pd
import numpy as np
import math
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###

st.set_page_config(page_title='Single Beer Analysis')

###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# Load in data

# Desktop file locations
BEER_df = pd.read_csv(r'C:\Users\...\Streamlit Beer Page files\Beer_df')
BEER_TSNE_df = pd.read_csv(r'C:\Users\...\Streamlit Beer Page files\BEER_TSNE_df')


###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###
st.title('Good Beer')
st.write('Welcome to Good Beer. Here we explore a small subset of beer rankings to try and figure out what is a good beer. '
         'Take some time to look through the beer table and explore some beers, or brewers, you may have never herd of. '
         'This list contains information on over 5000 commercial beers from over 1000 different brewerys. ' 
         'When your ready, scroll down to see what attributes are impotent in making a good beer. '
         'Majority of data used in this app was pulled from the form a 2021 log from the website *BeerAdvocate*')

# Desktop file location
BEER_df = pd.read_csv(r'C:\Users\jrruh\OneDrive\Documents\Homework\Data Sciance\CSME 830\Project 1\Streamlit Beer Page files\Beer_df')

BEER_df = BEER_df.rename(columns={'Name': 'Name of Beer', 'Style_x':'Brewing Style', 'Style Color Mean': 'Style Color Mean (SRM)', 'Style Color Var':'Style Color Var (SRM)'})

BEER_df = BEER_df.iloc[:,[19, 0, 3, 1, 2, 30, 5, 4, 26, 27, 6, 7, 28, 29, 20, 21, 22, 23, 24, 25, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 31]]

st.dataframe(BEER_df, use_container_width=True)

###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# Single beer analysis
st.title('Single Beer Analysis')
user_input_1 = st.text_input('Enter The Name of a Beer From the Table:', 'Beer Name')

# Creation of a single beer analysis tool

# Box for user input 1
if user_input_1 in BEER_df['Name of Beer'].values:
    st.write(user_input_1, ': Found')

    beer_row = BEER_df[BEER_df['Name of Beer'] == user_input_1]

    if not beer_row.empty:
    # Print value list
        rank_value = BEER_df.loc[BEER_df['Name of Beer'] == user_input_1, 'Ave Rating'].values[0]
        ABV_value = BEER_df.loc[BEER_df['Name of Beer'] == user_input_1, 'ABV'].values[0]
        Min_IBU_value = BEER_df.loc[BEER_df['Name of Beer'] == user_input_1, 'Min IBU'].values[0]
        Max_IBU_value = BEER_df.loc[BEER_df['Name of Beer'] == user_input_1, 'Max IBU'].values[0]
        Style_Name = BEER_df.loc[BEER_df['Name of Beer'] == user_input_1, 'Brewing Style'].values[0]

        st.write(f'Style Name : {Style_Name}')
        st.write(f'Score : {rank_value}/5')
        st.write(f'ABV : {ABV_value}')
        st.write(f'Min_IBU : {Min_IBU_value}')
        st.write(f'Rank Max_IBU : {Max_IBU_value}')
    else:
        st.write(user_input_1, ' : No data available for this beer.')
    
    # Polar bar chart of Attributes (CHAT GPT 4 (10/13/2024) helped write the code for this)

    # Locate beer data associated with the beer name
    beer_name_row = BEER_df[BEER_df['Name of Beer'] == user_input_1].iloc[0]

    # Set up attributes and their values
    attributes = ['Alcohol', 'Astringency', 'Body', 'Bitter', 'Fruits', 'Hoppy', 'Malty', 'Salty', 'Sour', 'Spices']
    values = [beer_name_row[attr] for attr in attributes]

    # Normalize values by dividing by the maximum value in each attribute
    normalized_values = [value / BEER_df[attr].max() for attr, value in zip(attributes, values)]

    # Create a plot DataFrame with normalized values
    polar_plot_data = pd.DataFrame({
        'Attribute': attributes,
        'Value': normalized_values
    })

    # Add angles for each attribute
    num_attributes = len(attributes)
    polar_plot_data['Angle'] = polar_plot_data['Attribute'].apply(lambda x: (attributes.index(x) / num_attributes) * 2 * np.pi)

    # Create polar bar chart using Plotly Express
    fig = px.bar_polar(polar_plot_data,
                        r='Value',
                        theta='Attribute',
                        color='Attribute',
                        template='plotly',
                        title=f'Normalized Attributes of {user_input_1}',
                        color_discrete_sequence=px.colors.qualitative.Dark24,)
    
    # Update layout to change tick label color to black
    fig.update_layout(
        polar=dict(
            angularaxis=dict(tickfont=dict(color='white')),  # Change angular axis tick font color
            radialaxis=dict(showticklabels=False,
                range=[0, 1])  # Change radial axis tick font color
        ),
    )
    st.plotly_chart(fig)

    # Print value in description column
    beer_described = BEER_df.loc[BEER_df['Name of Beer'] == user_input_1, 'Description'].values[0]
    st.write(user_input_1, f': {beer_described}')
else:
    st.write(user_input_1, ' : Beer Not Found in Data')

###------------------------------------------###

# Box for user input 2

user_input_2 = st.text_input('Another Name of a Beer From the Table To Compare to the first Beer:', 'Beer Name')


if user_input_2 in BEER_df['Name of Beer'].values:
    st.write(user_input_2, ': Found')

    # Print value list

    beer_row = BEER_df[BEER_df['Name of Beer'] == user_input_2]

    if not beer_row.empty:

        rank_value = BEER_df.loc[BEER_df['Name of Beer'] == user_input_2, 'Ave Rating'].values[0]
        ABV_value = BEER_df.loc[BEER_df['Name of Beer'] == user_input_2, 'ABV'].values[0]
        Min_IBU_value = BEER_df.loc[BEER_df['Name of Beer'] == user_input_2, 'Min IBU'].values[0]
        Max_IBU_value = BEER_df.loc[BEER_df['Name of Beer'] == user_input_2, 'Max IBU'].values[0]
        Style_Name = BEER_df.loc[BEER_df['Name of Beer'] == user_input_2, 'Brewing Style'].values[0]

        st.write(f'Style Name : {Style_Name}')
        st.write(f'Score : {rank_value}/5')
        st.write(f'ABV : {ABV_value}')
        st.write(f'Min_IBU : {Min_IBU_value}')
        st.write(f'Rank Max_IBU : {Max_IBU_value}')
    
    else:
        st.write(user_input_2, ' : Beer Not Found in Data')
    # Polar bar chart of Attributes (CHAT GPT 4 (10/13/2024) helped write the code for this)

    # Locate beer data associated with the beer name
    beer_name_row = BEER_df[BEER_df['Name of Beer'] == user_input_2].iloc[0]

    # Set up attributes and their values
    attributes = ['Alcohol', 'Astringency', 'Body', 'Bitter', 'Fruits', 'Hoppy', 'Malty', 'Salty', 'Sour', 'Spices']
    values = [beer_name_row[attr] for attr in attributes]

    # Normalize values by dividing by the maximum value in each attribute
    normalized_values = [value / BEER_df[attr].max() for attr, value in zip(attributes, values)]

    # Create a plot DataFrame with normalized values
    polar_plot_data = pd.DataFrame({
        'Attribute': attributes,
        'Value': normalized_values
    })

    # Add angles for each attribute
    num_attributes = len(attributes)
    polar_plot_data['Angle'] = polar_plot_data['Attribute'].apply(lambda x: (attributes.index(x) / num_attributes) * 2 * np.pi)

    # Create polar bar chart using Plotly Express
    fig = px.bar_polar(polar_plot_data,
                        r='Value',
                        theta='Attribute',
                        color='Attribute',
                        template='plotly',
                        title=f'Normalized Attributes of {user_input_2}',
                        color_discrete_sequence=px.colors.qualitative.Dark24,)
    
    # Update layout to change tick label color to black
    fig.update_layout(
        polar=dict(
            angularaxis=dict(tickfont=dict(color='white')),  # Change angular axis tick font color
            radialaxis=dict(showticklabels=False,
                range=[0, 1])  # Change radial axis tick font color
        ),
    )
    st.plotly_chart(fig)

    # Print value in description column
    beer_described = BEER_df.loc[BEER_df['Name of Beer'] == user_input_2, 'Description'].values[0]
    st.write(user_input_2, f': {beer_described}')
else:
    st.write(user_input_2, ' : Beer Not Found in Data')

###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###
# Brewery Analysis

st.title('Brewery Analysis')
user_input = st.text_input('Enter The Full Name of a Brewery From the Table:', 'Brewery')

if user_input in BEER_df['Brewery'].values:
    st.write(user_input, ': Found')

    # Print value list
    n_beers = len(BEER_df.loc[BEER_df['Brewery'] == user_input])
    AVG_brewer_rank = BEER_df.loc[BEER_df['Brewery'] == user_input, 'Ave Rating'].mean()
    highest_rated_beer_row = BEER_df.loc[BEER_df['Brewery'] == user_input].loc[
        BEER_df['Ave Rating'] == BEER_df.loc[BEER_df['Brewery'] == user_input, 'Ave Rating'].max()]
    highest_rated_beer = highest_rated_beer_row['Name of Beer'].values[0]

    st.write(f'Number of beers from brewer in list : {n_beers}')
    st.write(f'Average rank of all beers from brewer in list : {AVG_brewer_rank: .2f}/5')
    st.write(f'Highest ranked beer from brewer in list : {highest_rated_beer}')

else:
    st.write(user_input, ' : Brewery Not Found in Data')

###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###

# Style specific variables for later analysis
BEER_Style = BEER_df[['Brewing Style', 'Ave Rating', 'ABV', 'Min IBU', 'Max IBU', 'Style Color Mean (SRM)', 'Astringency', 'Body', 'Alcohol', 'Bitter', 'Sweet', 'Sour', 'Salty', 'Fruits', 'Hoppy', 'Spices', 'Malty']]
BEER_Ave_Style = BEER_Style.groupby('Brewing Style').mean()
BEER_Standard_Style = (BEER_Ave_Style - BEER_Ave_Style.mean())/ BEER_Ave_Style.std()
BEER_Standard_Style = BEER_Standard_Style.sort_values(by='Ave Rating', ascending=False)
BEER_Standard_Style.reset_index(inplace=True)


###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###

st.title('Style Rank Analysis')
user_input = st.text_input('Enter The Full Name of a Brewing Style From the Table:', 'Brewing Style')
if user_input in BEER_df['Brewing Style'].values:
    st.write(user_input, ': Found')

    # Print value list
    AVG_brewer_rank = BEER_df.loc[BEER_df['Brewing Style'] == user_input, 'Ave Rating'].mean()

    # Print style ranking analysis
    st.write(f'Average rank of all beers in Style list : {AVG_brewer_rank: .2f}/5')

    Style_Rank_mean = BEER_Ave_Style['Ave Rating'].mean()
    Style_Rank_std = BEER_Ave_Style['Ave Rating'].std()
    deviation = (AVG_brewer_rank - Style_Rank_mean) / Style_Rank_std

    message = []
    if deviation > 1.28: # Top 10% in a normal distribution
        message.append(f"A style rating of {AVG_brewer_rank:.2f} is a FANTASTIC score compared to other styles. The Style rating is {deviation:.2f} standard deviations ABOVE the mean style score")
    elif deviation > 0.67: # Top 25% in a normal distribution
        message.append(f"A style rating of {AVG_brewer_rank:.2f} is a ABOVE AVERAGE score compared to other styles. The Style rating is {deviation:.2f} standard deviations ABOVE the mean style score")
    elif deviation < -0.67: # Bottom 25% in a normal distribution
        message.append(f"A style rating of {AVG_brewer_rank:.2f} is a BELOW AVERAGE score compared to other styles. The Style rating is {abs(deviation):.2f} standard deviations BELOW the mean style score")
    elif deviation < -1.28: # Bottom 10% in a normal distribution
        message.append(f"A style rating of {AVG_brewer_rank:.2f} is a TERRIBLE score compared to other styles. The Style rating is {abs(deviation):.2f} standard deviations BELOW the mean style score")
    else:
        message.append(f"A style rating of {AVG_brewer_rank:.2f} is an AVERAGE score compared to other styles. The Style rating is {abs(deviation):.2f} standard deviations from the mean style score")

    # Display the messages
    for message in message:
        st.write(message)

    Style_ABV_Mean = BEER_df.loc[BEER_df['Brewing Style'] == user_input, 'Style ABV Mean'].values[0]
    Var_ABV = BEER_df.loc[BEER_df['Brewing Style'] == user_input, 'Style ABV Var'].values[0]
    Style_IBU_Mean = BEER_df.loc[BEER_df['Brewing Style'] == user_input, 'Style IBU Mean'].values[0]
    Var_IBU = BEER_df.loc[BEER_df['Brewing Style'] == user_input, 'Style IBU Var'].values[0]
    Style_Color_Mean = BEER_df.loc[BEER_df['Brewing Style'] == user_input, 'Style Color Mean (SRM)'].values[0]
    Var_Color = BEER_df.loc[BEER_df['Brewing Style'] == user_input, 'Style Color Var (SRM)'].values[0]
    highest_rated_beer_row = BEER_df.loc[BEER_df['Brewing Style'] == user_input].loc[
        BEER_df['Ave Rating'] == BEER_df.loc[BEER_df['Brewing Style'] == user_input, 'Ave Rating'].max()]
    highest_rated_beer = highest_rated_beer_row['Name of Beer'].values[0]
    lowest_rated_beer_row = BEER_df.loc[BEER_df['Brewing Style'] == user_input].loc[
        BEER_df['Ave Rating'] == BEER_df.loc[BEER_df['Brewing Style'] == user_input, 'Ave Rating'].min()]
    lowest_rated_beer = lowest_rated_beer_row['Name of Beer'].values[0]

    st.write(f'Mean Style ABV: {Style_ABV_Mean :.2f}')
    st.write(f'Variance in Style ABV: {Var_ABV :.2f}')
    st.write(f'Mean Style IBU : {Style_IBU_Mean :.2f}')
    st.write(f'Variance in Style IBU : {Var_IBU :.2f}')
    st.write(f'Mean Style Color : {Style_Color_Mean :.2f}')
    st.write(f'Variance in Style Color : {Var_Color :.2f}')
    st.write(f'Name of Highest ranked beer in style : {highest_rated_beer}')
    st.write(f'Name of Lowest ranked beer in style : {lowest_rated_beer}')

    # polar map style attribute plot
    beer_style_rows = BEER_Ave_Style.loc[user_input]

    # Set up attributes and their values
    attributes = ['Alcohol', 'Astringency', 'Body', 'Bitter', 'Fruits', 'Hoppy', 'Malty', 'Salty', 'Sour', 'Spices']
    values = [beer_style_rows[attr] for attr in attributes]

    # Normalize values by dividing by the maximum value in each attribute
    normalized_values = [values / BEER_Ave_Style[attr].max() for attr, values in zip(attributes, values)]

    # Create a plot DataFrame with normalized values
    polar_plot_data = pd.DataFrame({
        'Attribute': attributes,
        'Value': normalized_values
    })

    # Add angles for each attribute
    num_attributes = len(attributes)
    polar_plot_data['Angle'] = polar_plot_data['Attribute'].apply(lambda x: (attributes.index(x) / num_attributes) * 2 * np.pi)

    # Create polar bar chart using Plotly Express
    fig = px.bar_polar(polar_plot_data,
                        r='Value',
                        theta='Attribute',
                        color='Attribute',
                        template='plotly',
                        title=f'Normalized Attributes of {user_input}',
                        color_discrete_sequence=px.colors.qualitative.Dark24,)
    
    # Update layout to change tick label color to black
    fig.update_layout(
        polar=dict(
            angularaxis=dict(tickfont=dict(color='white')),  # Change angular axis tick font color
            radialaxis=dict(showticklabels=False,
                range=[0, 1])  # Change radial axis tick font color
        ),
    )
    st.plotly_chart(fig)


else:
    st.write(user_input, ' : Brewing Style Not Found in Data')


###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###

# Place holder heatmap image
st.title('Beer Style Attribute Heatmap')
st.image(r"C:\Users\...\matplotlib Beer style atribute heatmap.png", caption="Beer style attributes are normal distributed and organized in descending order", use_column_width=True)

# Interactive heatmap through plotly
# BEER_Ave_Style_heatmap = BEER_df[['Brewing Style', 'Ave Rating', 'ABV', 'Min IBU', 'Max IBU', 'Style Color Mean (SRM)', 'Astringency', 'Body', 'Alcohol', 'Bitter', 'Sweet', 'Sour', 'Salty', 'Fruits', 'Hoppy', 'Spices', 'Malty']]
# BEER_Ave_Style_heatmap = BEER_Ave_Style_heatmap.groupby('Brewing Style').mean()
# BEER_Standard_Style_heatmap = (BEER_Ave_Style_heatmap - BEER_Ave_Style_heatmap.mean())/ BEER_Ave_Style_heatmap.std()
# BEER_Standard_Style_heatmap = BEER_Standard_Style_heatmap.sort_values(by='Ave Rating', ascending=False)
# BEER_Standard_Style_heatmap.reset_index(inplace=True)
# fig = px.imshow(BEER_Standard_Style_heatmap.set_index('Brewing Style'),
#                 color_continuous_scale='icefire',
#                 labels=dict(x= 'Attributes', y='Brewing Style', color='Standardized Value'),
#                 title="Beer Style Feature Heatmap",
#                 width=2000,
#                 height=3000,
#                 )
# st.plotly_chart(fig)

###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###
st.title('Attribute Analysis')

st.write('In this data set 3 attributes are quantitative values from ABV, IBU, and color value measurements. ' 
        'The other 11 attributes are from qualitative values from flavor analysis. '
        'Looking at the listed attributes provided in the data table, as well as rank, in a correlation matrix produces the heat map below.')
# Place holder heatmap image
st.image(r"C:\Users\...\matplotlib Beer atribute corr heatmap.png", caption= "", use_column_width=True)

st.markdown('''
        Notes on attribute correlations:
        Overall, according to the data, an increase in any flavor value gives an increase in rating.
        descending list of correlated attributes with average rating (most positively correlated at the top)
        1. ABV
        2. Fruit
        3. IBU
        4. Color
        5. Body/thickness
        6. Sweet
        7. Sour
        8. Apparent Bitterness
        9. Apparent Alcohol Taste
        10. Malty
        11. Spicy / warm
        12. Astringent
        13. Hoppy/Earthy
        14. Salty
        ''')
st.markdown('''
        Positive correlation groups in the data
         - Sour, Fruity, Astringency (Example style: sour beers) 
         - Malty, Body, Bitter, Sweet, Alcohol (Example style: Porters and Stouts)
         - Hoppy, Astringency, Bitter (Example style: IPAs)
         - Light beer, Sour, Fruity, Hoppy
         - Dark Beer, Body, Bitter, ABV, Malty
        ''')
st.markdown('''
        Negative correlation groups in the data
         - (Salty, Astringency), (ABV, IBU)
         - Malty, Sour
         ''')
st.write('So what do these correlating factors look like in a paired plot? Well... its not pretty to look at.')

# Place holder pair plot
st.image(r'C:\Users\...\Atribute Corr Pairplot.png', use_column_width=True)

st.write('The big idea from the pairplot is to show most of the bivariate analysis data is not liner when including all of the data, therefore correlations between attributes should be taken with a grain of salt.')

###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###

st.title('Style to Style Analysis')

st.write('''
         The data included in the table above is organized into just around 111 styles.
         A Beer style can be thought of as a recipe group.
         Think of a Beer Style like a cookie recipe, there are many different kinds of cookies like chocolate chip, penutbutter and oatmeal.
         with in each category of cookie there is even more variation as not all chocolate chip cookies taste the same.
         Beer styles are a little more complicated then cookie recipes but the cookie analogy should help anyone who is unfamiliar with making beer or beer culture understand what a style is.
         If we judge beer only on the attributes above then it seams unreasonable to think 111 styles of beer exist.
         Another way to think about the style number problem is poring one of each of the 111 styles out and being told to sort all of the beers into the correct style on looks and taste alone.
         Drinking 111 beers let alone all 5000+ beers and grouping them is a bad idea but we can attempt to cluster our beer styles to see if we end up with 111 groups.
         ''')

###------------------------------------------###

# PCA plot

BEER_PCA_df = BEER_df[['Brewing Style', 'ABV', 'Min IBU', 'Max IBU', 'Style Color Mean (SRM)', 'Astringency', 'Body', 'Alcohol', 'Bitter', 'Sweet', 'Sour', 'Salty', 'Fruits', 'Hoppy', 'Spices', 'Malty', 'Style_Group']]

X = BEER_PCA_df[['ABV', 'Min IBU', 'Max IBU', 'Style Color Mean (SRM)', 'Astringency', 'Body', 'Alcohol', 'Bitter', 'Sweet', 'Sour', 'Salty', 'Fruits', 'Hoppy', 'Spices', 'Malty']]

pca = PCA(n_components=2)
components = pca.fit_transform(X)

user_input_width = st.text_input('Scale the width of the plot to your screen:', 1000)
user_input_height = st.text_input('Scale the height of the plot to your screen:', 1000)
try:
    plot_width = int(user_input_width)
    plot_height = int(user_input_height)
except ValueError:
    st.error("Please enter valid integers for width and height.")
    plot_width = 1000  # default value
    plot_height = 1000  # default value
fig = px.scatter(components, 
x=0, 
y=1, 
color=BEER_PCA_df['Brewing Style'], 
hover_name = BEER_df['Name of Beer'], 
width=plot_width, 
height=plot_height)

st.title('PCA Plot Grouped by Beer Style')

st.write('''
         PCA, for those who are unfamiliar with it, is method of reducing high dimensional data into a lower dimension.
         In simpler terms PCA takes all attributes of the data and squishes them all on a number line or a single axis.
         This is a gross simplification of what PCA is actually doing but all you need to know is each axis represents all of the data attributes but each component weights the influence of each axis differently.
         The product of PCA is a plot where beer that is more similar is closer to each other on the plot.
         ''')

st.plotly_chart(fig)

st.write('''Above is a scatter plot of PCA components 0 and 1.
         The graph was made using plotly express which allows users to click on the legend to hide styles from the plot.
         Points that are closer to each other are more smiler in taste while points further away from each other are more dissected from each other.
         The take away message from this graph is very few beers styles are that unique from each other and hard to justify placing it in its own style category.
         We can attempt to combine styles into style groups but to do that we need to use another method of organizing the data.
         ''')

###------------------------------------------###

# TSNE plot

st.title('T-SNE Plot Grouped by Beer Style')

st.write('''
         T-SNE, like PCA, reduces our high dimensional data into a lower dimension.
         Unlike PCA which reduces the dimensionality of data using something called an eigenvector. T-SNE is an algorithm that clusters data points together using both a normal and T distribution of the data.
         T-SNE, as your about to see, will make much better use of space and start to form clusters of points on our two axis graph
         ''')

user_input_width = st.text_input('Scale the width of the plot to your screen:', 1000, key='plot_width')
user_input_height = st.text_input('Scale the height of the plot to your screen:', 1000, key='plot_height')

try:
    plot_width1 = int(user_input_width)
    plot_height1 = int(user_input_height)
except ValueError:
    st.error("Please enter valid integers for width and height.")
    plot_width1 = 1000  # default value
    plot_height1 = 1000  # default value

fig = px.scatter(BEER_TSNE_df, 
x = 'tsne-comp-one', 
y = 'tsne-comp-two', 
color=BEER_TSNE_df['Brewing Style'], 
hover_name = BEER_df['Name of Beer'], 
width = plot_width1, 
height = plot_height1,)

st.plotly_chart(fig)

st.write('''
         Now our Beer styles are more visual clustered. 
         Its still hard to look at but its a much better graph than the PCA graph.
         Like the PCA component graph you can hide styles from the graph by clicking on them from the legend.
         See if you can make out any style groups on the graph.
         ''')

###------------------------------------------###

st.write('''
         If you have not notice yet I have already created style groups using the T-SNE graph and included them in the table above.
         if we look at the T-SNE scatter plot again and organize them into the style groups provided, can you make out any groups of data?
         ''')

fig = px.scatter(BEER_TSNE_df, 
x = 'tsne-comp-one', 
y = 'tsne-comp-two', 
color=BEER_TSNE_df['Style_Group'], 
hover_name = BEER_df['Name of Beer'], 
width = plot_width1, 
height = plot_height1)
st.plotly_chart(fig)

st.write('''
         The clusters were made by using some of the existing style group information presents in the Brewing style description as well as using style color and ABV means to further organize styles into grater clusters.
         Overall I ended up making 12 style groups.
         Some style groups are more spread out than other styles and some beers in a style group may even belong inside another style group.
         Some of the more defined style groups I made are, IPAs, Porters and Stouts, Fruit and Sour Beer, Spiced and Smoked beer, Light Lagers, Golden Heavy Ale, and Dark Heavy Ale.
         Try looking at only the well defined styles I listed above and see if you can make out where each one sits on the graph.
         Now Look at the less defined styles on the graph (Amber and brown Ales, Pale Ale, Farm style Ale, and Dark Lagers).
         Notice how spread out each of the less defined styles are.
         The variety in the less defined style groups also suggests a variety in the styles with in those style groups, and therefor a variety in beer rankings within that style.
         ''')

###------------------------------------------###

st.write('''
        Lets take a look at our PCA plot again but this time organized into style groups
         ''')

fig = px.scatter(components, 
x=0, 
y=1, 
color=BEER_PCA_df['Style_Group'], 
hover_name = BEER_df['Name of Beer'], 
width=plot_width, 
height=plot_height)
st.plotly_chart(fig)

st.write('''
        Again we see a similar pattern of more and less defined style groups on our PCA scatter plot.
         ''')

###------------------------------------------###

st.title('Rank Clusters')

st.write('''
        Lets take another look at our T-SNE scatter plot.
        This time lets organize the plot according to rank.
         ''')

# chat GPT 4 (10/14/2024 made the bins for the graph)
rank_bins = np.linspace(1, 5, 10)
labels = [f"{rank_bins[i]:.2f} - {rank_bins[i+1]:.2f}" for i in range(len(rank_bins)-1)]
BEER_TSNE_df['Bins'] = pd.cut(BEER_df['Ave Rating'], bins = rank_bins, labels = labels, right = False)

fig = px.scatter(BEER_TSNE_df, 
x = 'tsne-comp-one', 
y = 'tsne-comp-two',
hover_name = BEER_df['Name of Beer'], 
color=BEER_TSNE_df['Bins'], 
width = plot_width1, 
height = plot_height1,)

st.plotly_chart(fig)

st.write('''
        looking at how beer is ranked we see beer with stronger attributes are located on the edge of the graph and are ranked higher than the weaker, lower ranked beers in the middle.
        Although we can make out ranked clusters on the graph the show increasing our beers attributes increase rank, what we see are some high ranked beers in low rank clusters and low raked clusters?
        As an exercise. Go back to the top of the page and compare the two beers Gatecrasher, and Zombie dust. The two beers are practically identical, so why are they ranked so differently?
         ''')
st.markdown('''
        Here is a list of reasons why similar beers have rank discrepancy.

        1. The beers being looked at are not similar. 
        Our similarity judgment is based on a simplification of multidimensional data. 
        Perhaps if another method of reducing the plots dimensions was used it could show the smiler beers to be further apart. 
        I think, with the data I have, its unlikely that beers clustered together are not similar to each other, so there must be another reason why we see rank discrepancy. 
        
        2. The data being used is incomplete
        What dose incomplete data mean? It means that there are other attributes not recorded in the data table used for analysis. 
        Take for example the fruity attribute, fruity in beer can mean a lot of things from hop oil flavors giving off grapefruit, citrus, mango flavors, to actual fruit flavors being used like charry, raspberry, apple, and peach. 
        perhaps braking down flavor attributes into more category will help explain why beers are ranked differently. 

        3. Beer bias
        As stated previously, the data collected comes from a public beer forum called *Beer Advocate*. 
        Users can set a rank and enter there thoughts about beer. 
        What if differently ranked beers are truly similar to each other but one beer has more post engagement than the other and causes the rank to appear different than what it actually could be?
''')
