# Python script for my first streamlit application
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import streamlit as st 
import matplotlib.ticker as ticker 
import plotly.tools as tls
import plotly.express as px

st.set_page_config(layout='wide')

# Custom CSS for background and text color
custom_css = """
<style>
    body {
        background-color: #f8f2e1;  /* Light gray background */
        color: #FF000;  /* Darker text color */
    }
    .stApp {
        background-color: #FFFFFF;
    }
    .css-1d391kg {  /* Sidebar class */
        background-color: #FF000;  /* Secondary background color for sidebar */ # doesnt work but idk why 
    }
    h1, h2, h3, h4, h5, h6 {
        color: #FF0000;  /* Custom header color */
    }
</style>
"""
from PIL import Image

# Open an image file
img_path = "/Volumes/SEAGATE BAC/DataScienceLearning/proj_NeighborhoodBirds/BCSLogo.png"
img_path2 = "/Volumes/SEAGATE BAC/DataScienceLearning/proj_NeighborhoodBirds/BCSbirds.png"
image = Image.open(img_path)
image2 = Image.open(img_path2)

# Display the image using Streamlit
st.image(image, width=500)

bcs_colors = {'dark green' : "#0A3C23",
  'cream' : "#FAF5F0",
  'yellow green' : "#E6FF55",
  'peach' : "#FFB98C",
  'bright green' : "#36BA3A"} 

def theme_bcs(fig): 
    fig.update_layout( 
    # Background: 
     plot_bgcolor=bcs_colors["cream"],
        paper_bgcolor=bcs_colors["cream"],
        
        # Grid Lines
        xaxis=dict(showgrid=True, gridcolor=bcs_colors["dark green"], gridwidth=0.5, zeroline=False),
        yaxis=dict(showgrid=True, gridcolor=bcs_colors["dark green"], gridwidth=0.5, zeroline=False),
        
        # Text
        font=dict(color=bcs_colors["dark green"]),
        title=dict(font=dict(size=28, color=bcs_colors["dark green"], family="bold")),
        xaxis_title=dict(font=dict(color=bcs_colors["dark green"])),
        yaxis_title=dict(font=dict(color=bcs_colors["dark green"])),
        
        # Legend
        legend=dict(
            bgcolor=bcs_colors["cream"],
            font=dict(color=bcs_colors["dark green"]),
        ),
        
        # Margins and Borders
        margin=dict(l=50, r=50, t=50, b=50),
    )
    
    # Customizing traces (e.g., lines, markers)
    fig.update_traces(
        # line=dict(color=bcs_colors["dark green"]),
        marker=dict(color=bcs_colors["dark green"]),
    )
    
    return fig

# Inject CSS into the app
st.markdown(custom_css, unsafe_allow_html=True)
# make small dataframes for each individual park 
Seward = inputfile[inputfile['Park'] == 'Seward Park'] # create a new df from og where park is equal to 'Seward Park'
GoldenGardens = inputfile[inputfile['Park'] == 'Golden Gardens Park']
Discovery = inputfile[inputfile['Park'] == 'Discovery Park']
Carkeek = inputfile[inputfile['Park'] == 'Carkeek Park']
Lincoln = inputfile[inputfile['Park'] == 'Lincoln Park']
Magnuson = inputfile[inputfile['Park'] == 'Magnuson Park']
Cheasty = inputfile[inputfile['Park'] == 'Cheasty Greenspace']
WashingtonParkArboretum = inputfile[inputfile['Park'] == 'Washington Park Arboretum']
Genesee = inputfile[inputfile['Park'] == 'Genesee Park']
Walsh = inputfile[inputfile['Park'] == 'Walsh Property']
Bliner = inputfile[inputfile['Park'] == 'Bliner Property']
ShadowLakeBog = inputfile[inputfile['Park'] == 'Shadow Lake Bog']
LakeForest = inputfile[inputfile['Park'] == 'Lake Forest Park']
SoosCreek = inputfile[inputfile['Park'] == 'Soos Creek']
ClarkLake = inputfile[inputfile['Park'] == 'Clark Lake Park']
JenkinsCreek = inputfile[inputfile['Park'] == "Jenkin's Creek Park"]

# Calculate richness from inputfile and map to the correct park
inputfile = pd.read_csv('NBPdata.csv')
inputfile['richness'] = inputfile['Park'].map({ # here we are creating a dictionary where based on inputfile['Park'] we map the richness calculation to the correct column
    'Seward Park' : len(Seward['Species'].unique()),
    'Golden Gardens Park' : len(GoldenGardens['Species'].unique()),
    'Discovery Park' : len(Discovery['Species'].unique()),
    'Carkeek Park' : len(Carkeek['Species'].unique()),
    'Lincoln Park' : len(Lincoln['Species'].unique()),
    'Magnuson Park' : len(Magnuson['Species'].unique()),
    'Cheasty Greenspace' : len(Cheasty['Species'].unique()),
    'Washington Park Arboretum' : len(WashingtonParkArboretum['Species'].unique()),
    'Genesee Park' : len(Genesee['Species'].unique()),
    'Walsh Property' : len(Walsh['Species'].unique()),
    'Bliner Property' : len(Bliner['Species'].unique()),
    'Shadow Lake Bog' : len(ShadowLakeBog['Species'].unique()),
    'Lake Forest Park' : len(LakeForest['Species'].unique()),
    'Soos Creek' : len(SoosCreek['Species'].unique()),
    'Clark Lake Park' : len(ClarkLake['Species'].unique()),
    "Jenkin's Creek Park" : len(JenkinsCreek['Species'].unique())
})

with st.container():
    col1, gap, col2= st.columns([1,0.1,1])
#Viz 0 
with col1: 
    st.markdown('<h1 style="color:black; font-size:40px;">Neighborhood Bird Project Dashboard</h1>', unsafe_allow_html=True) # change font of title? 
    # st.markdown('<h6 style="color:gray; font-size:20px;">Charts on the left show species richness are shown in this column</h6>', unsafe_allow_html=True) # change font of subtitle
    # st.write('Here is our Dataset:') # write these words in the UI
    # st.dataframe(inputfile.drop(['notes', 'surveyors'], axis = 1)) # show the dataframe in the UI 
    df = inputfile # create a DF 
    st.write('The figure below is a boxplot of total species richness') # write these words in the UI
#     # sns.barplot(x = 'Park', y = 'richness', data = df, width = 0.8, color = '#7dcea0') # create this barplot 
#     # plt.xticks(rotation = 90) # rotate the x labels # of degrees
#     # plt.ylabel('Species Richness')
#     # plt.title('Total Species Richness of Surveryed Parks 1996-2023')
#     # st.pyplot(plt) # show the plt in the UI 

    # putting in a script for the 'same' barchart but usign plotly so that we can hover and zoom and stuff
    parksrich = pd.DataFrame(df.groupby('Park').agg({'richness' : 'first'}).reset_index()) 
    # groups df by park and then pulls the first value for richness associated with that park and maps it to the correct cell
    #parksrich
    fig = px.bar(parksrich, x = 'Park', y= 'richness', color_discrete_sequence=['#7dcea0'])
    # BEGINNING OF FORMATTING FOR PLOTLY.EXPRESS
    fig.update_layout(
        title={
        'text': 'Total Species Richness of Surveryed Parks 1996-2023',
        'x': 0.5,  # Center the title
        'xanchor': 'center',  # Center align the title horizontally
        'yanchor': 'top',  # Anchor the title to the top
        'font': {
            'size' : 24,
            'color' : 'black'
        }
    },
        xaxis_title = 'Park',
        yaxis_title = 'Species Richness',
        width = 800,
        height = 800,
        shapes =[
        dict(
            type='rect',
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            xref='paper',
            yref='paper',
            line=dict(
                color='black',
                width=2
            ),
            fillcolor='rgba(0,0,0,0)'  # Transparent fill
        )
    ],
        margin = dict(l=40, r=40)
        )
    fig.update_xaxes(tickangle = -45,
                     title_font = dict(size = 18, color = 'black'),
                     tickfont = dict(size = 18, color = 'black'))
    fig.update_yaxes(range=[0, df['richness'].max()+20], 
                     title_font = dict(size = 18, color = 'black'),
                     tickfont = dict(size = 18, color = 'black')) # END FORMATING
    theme_bcs(fig)
    st.write(fig)
    
    
    st.markdown('<hr style= "border: 2px solid black;">', unsafe_allow_html= True)

    
#     # lets make another with select boxes so we can play with the data in the app based on the year  
    

# Viz 0.5
    # USE " COMMAND + [ " to untab a whole block of code
    years_sorted = sorted(df['Year'].unique()) # Creates a list of unique years in ascending order 
    selected_year = st.selectbox('Select a Year', years_sorted) # Create a select box to pick which column to use in the barplot
    min_value = st.slider('Select a minimum value for richness', min_value= 0, max_value= 250, value=0)
    filtered_df = df[(df['Year'] == selected_year) &  (df['richness'] >= min_value)] # filter the dataframe based on the selected year & minimum value
    # fig, ax = plt.subplots()
#     # sns.barplot(x = filtered_df['Park'], y = filtered_df['richness'], data=filtered_df, ax=ax, color = '#7dcea0')
#     # plt.xticks(rotation =90)
#     # plt.ylabel('Species Richness')
#     # plt.title(f'Species Richness by Park {selected_year}')
#     # st.pyplot(plt)
    
    filtered_df1 = pd.DataFrame(filtered_df.groupby('Park').agg({'richness' : 'first'}).reset_index()) 

    fig1 = px.bar(filtered_df1, x = 'Park', y= 'richness', color_discrete_sequence=['#7dcea0'])
    
    fig1.update_layout(
        title={
        'text': f"Species Richness by Park {selected_year}",
        'x': 0.5,  # Center the title
        'xanchor': 'center',  # Center align the title horizontally
        'yanchor': 'top',  # Anchor the title to the top
        'font': {
            'size' : 24,
            'color' : 'black'
        }
    },
        xaxis_title = 'Park',
        yaxis_title = 'Species Richness',
        width = 800,
        height = 800,
        shapes =[
        dict(
            type='rect',
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            xref='paper',
            yref='paper',
            line=dict(
                color='black',
                width=2
            ),
            fillcolor='rgba(0,0,0,0)'  # Transparent fill
        )
    ],
        margin = dict(l=40, r=40)
        )
    fig1.update_xaxes(tickangle = -45,
                     title_font = dict(size = 18, color = 'black'),
                     tickfont = dict(size = 18, color = 'black'))
    fig1.update_yaxes(range=[0, df['richness'].max()+20], 
                     title_font = dict(size = 18, color = 'black'),
                     tickfont = dict(size = 18, color = 'black')) 
    theme_bcs(fig1)
    st.write(fig1)
    st.markdown("<div style = 'height: 550px;'></div>", unsafe_allow_html=True)
    st.image(image2, width=700)
with gap: 
    st.markdown("<div style = 'height: 80px;'></div>", unsafe_allow_html=True)
with col2:     
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)  # Adjust height as needed here for lowering start of col2
    # st.markdown('<h6 style="color:gray; font-size:20px;">Figures visualizing species counts are shown in this column</h6>', unsafe_allow_html=True) # change font of subtitle    
    
    # # Viz #1 - count of all species at a PARK on a given day 

    inputfile['Survey Date'] = pd.to_datetime(inputfile['Survey Date']).dt.date
    inputfile['detections'] = inputfile[['Seen','Heard','Fly']].apply(lambda x : x.sum(), axis = 1)
    
    # in order to add another selection box we need to define the parks for the selection box to filter on 
    parks = sorted(inputfile['Park'].unique()) # create & sort list alphabeticlly of parks in inputfile 
    selectedpark = st.selectbox('Select Park', parks, key = 'park_select_1')

    filter1 = pd.DataFrame(inputfile[(inputfile['Park'] == selectedpark)]) # make new df "filter1" based on selected park
    
    # filter for dates at the "SELECTEDPARK" below 
    survey_dates = sorted(filter1['Survey Date'].unique()) # creates unique list of survey dates from filter1
    selected_date = st.selectbox('Select survey date: YYYY-MM-DD',survey_dates) # streamlit selection box of survey dates available 
    filter2 = pd.DataFrame(filter1[(filter1['Survey Date'] == selected_date)]) # filter filter 1 into another for the graph to use based on selected date
    specdet = pd.DataFrame(filter2.groupby('Species')['detections'].sum())

    # # fig = plt.figure()
    # # sns.barplot(data= specdet, x='Species', y = 'detections', color = '#7dcea0', width=0.8, errorbar = None) 
    # # plt.xticks(rotation =90) # rotates the x axis ticks (labels)
    # # plt.title(f"Count of Species at {selectedpark} on {selected_date}")    
    # # plt.xlabel('Species')
    # # plt.ylabel('Count')
    # # # plotly_fig = tls.mpl_to_plotly(fig)
    # # # st.plotly_chart(plotly_fig)
    # # st.pyplot(fig)
    # # st.write(f"No other species were recorded at {selectedpark} on {selected_date}")
    
    specdet.reset_index()
    # st.write(specdet)
    fig2 = px.bar(specdet,y = 'detections', color_discrete_sequence=['#7dcea0'])
    fig2.update_layout(
        title={
        'text': f"Count of Each Species at {selectedpark} on {selected_date}",
        'x': 0.5,  # Center the title
        'xanchor': 'center',  # Center align the title horizontally
        'yanchor': 'top',  # Anchor the title to the top
        'font': {
            'size' : 24,
            'color' : 'black'
        }
    },
        xaxis_title = 'Species',
        yaxis_title = 'Number of Detections',
        width = 800,
        height = 800,
        shapes =[
        dict(
            type='rect',
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            xref='paper',
            yref='paper',
            line=dict(
                color='black',
                width=2
            ),
            fillcolor='rgba(0,0,0,0)'  # Transparent fill
        )
    ],
        margin = dict(l=40, r=40)
        )
    fig2.update_xaxes(tickangle = -90,
                     title_font = dict(size = 18, color = 'black'),
                     tickfont = dict(size = 18, color = 'black'))
    fig2.update_yaxes(range=[0, specdet['detections'].max()+(specdet['detections'].max()*0.05)], 
                     title_font = dict(size = 18, color = 'black'),
                     tickfont = dict(size = 18, color = 'black'))
    theme_bcs(fig2)
    st.write(fig2)
    st.write(f"No other species were recorded at {selectedpark} on {selected_date}")
    st.markdown('<hr style= "border: 2px solid black;">', unsafe_allow_html= True)     
#     #Viz 2
    # species detection numbers for any given survey
    
    parks3 = sorted(inputfile['Park'].unique())
    park = st.selectbox('Select a park', parks3, key= 'park_select_3')
    dfparky = pd.DataFrame(inputfile[inputfile['Park'] == park]) 
    stationz = sorted(dfparky['Station'].unique())
    station = st.selectbox('Select a station',stationz)
    dfparkstation = pd.DataFrame(dfparky[dfparky['Station'] == station])
    datez = sorted(dfparkstation['Survey Date'].unique())
    # date = selected_date = st.date_input("Select a date") # cool - adds a calendar widget but won't work well here due to sporadic date options
    date = st.selectbox('Select survey date: YYYY-MM-DD',datez, key = "date1")
    dfparkstationdate = dfparkstation[dfparkstation['Survey Date'] == date]

    sums = pd.DataFrame(dfparkstationdate.groupby('Species')['detections'].sum())
    # sums

    # fig1 = plt.figure()
    # sns.barplot(data = sums, x = 'Species', y='detections', color = '#7dcea0', width=0.8)
    # plt.xticks(rotation = 90)
    # plt.xlabel('Species')
    # plt.ylabel('Count')
    # plt.title(f"Count of each species detected at {park} station {station} on {date}")
    # st.write(f"Total number of detections at {park} station {station} on {date}", sum(dfparkstationdate['detections']))
    # st.pyplot(fig1)
    figsurv = px.bar(sums, y = 'detections', color_discrete_sequence=['#7dcea0'])
    figsurv.update_layout(
        title={
        'text': f"Number of Detections by Species at {park}, station {station}, on {date}",
        'x': 0.5,  # Center the title
        'xanchor': 'center',  # Center align the title horizontally
        'yanchor': 'top',  # Anchor the title to the top
        'font': {
            'size' : 24,
            'color' : 'black'
        }
    },
        xaxis_title = 'Species',
        yaxis_title = 'Number of Detections',
        width = 800,
        height = 800,
        shapes =[
        dict(
            type='rect',
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            xref='paper',
            yref='paper',
            line=dict(
                color='black',
                width=2
            ),
            fillcolor='rgba(0,0,0,0)'  # Transparent fill
        )
    ],
        margin = dict(l=40, r=40)
        )
    figsurv.update_xaxes(tickangle = -45,
                        title_font = dict(size = 18, color = 'black'),
                        tickfont = dict(size = 18, color = 'black'))
    figsurv.update_yaxes(range=[0, sums['detections'].max()+sums['detections'].max()*0.05], 
                        title_font = dict(size = 18, color = 'black'),
                        tickfont = dict(size = 18, color = 'black'))
    theme_bcs(figsurv)
    st.write(figsurv)
    
    #Viz 2 - count of ONE species in a park through time (yearly)
    parks2 = sorted(inputfile['Park'].unique()) # create & sort list alphabeticlly of parks in inputfile 
    selectedpark2 = st.selectbox('Select Park', parks2, key = 'park_select_2')
    dfpark = inputfile[(inputfile['Park'] == selectedpark2)]
    
    # dfpark['datecount'] = dfpark.groupby(['Survey Date', 'Species'])['Species'].transform('size') 
    speciez = sorted(dfpark['Species'].unique())
    sp_choice = st.selectbox('Select species of interest', speciez)
    st.write('If your species is not in the dropdown list, it has not been detected at this park according to our dataset.')    
    dfpark_species = dfpark[dfpark['Species'] == sp_choice]
    
    ct_year = pd.DataFrame(dfpark_species.groupby('Year')['detections'].sum().reset_index())
    
    # fig = plt.figure()
    # sns.scatterplot(data = avg_ct_year, x = 'Year', y = 'detections', color = '#7dcea0')
    # sns.lineplot(data = avg_ct_year, x = 'Year', y = 'detections', color = '#e1f8f2')
    # plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    # plt.title(f'Avg annual count of {sp_choice} at {selectedpark2}')
    # st.write(fig)
    
    line = px.scatter(ct_year, x = 'Year', y = 'detections', color_discrete_sequence=['#7dcea0'], trendline= 'ols')
    line.update_layout(
        title={
        'text': f'Annual Number of Detections of {sp_choice} at {selectedpark2}',
        'x': 0.5,  # Center the title
        'xanchor': 'center',  # Center align the title horizontally
        'yanchor': 'top',  # Anchor the title to the top
        'font': {
            'size' : 24,
            'color' : 'black'
        }
    },
        xaxis_title = 'Year',
        yaxis_title = 'Mean Number of Detections',
        width = 1000,
        height = 500,
        shapes =[
        dict(
            type='rect',
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            xref='paper',
            yref='paper',
            line=dict(
                color='black',
                width=2
            ),
            fillcolor='rgba(0,0,0,0)'  # Transparent fill
        )
    ],
        margin = dict(l=40, r=40)
        )
    line.update_xaxes(tickangle = 0,
                     title_font = dict(size = 18, color = 'black'),
                     tickfont = dict(size = 18, color = 'black'),
                     nticks = 10)
    line.update_yaxes(title_font = dict(size = 18, color = 'black'),
                     tickfont = dict(size = 18, color = 'black'))
    theme_bcs(line)
    st.write(line)
    st.markdown('<hr style= "border: 2px solid black;">', unsafe_allow_html= True)
