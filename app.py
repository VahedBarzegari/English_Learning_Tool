import ast
import asyncio
from datetime import datetime
import os
from gtts import gTTS
import folium.map
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import branca.colormap as cm
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
from folium import Choropleth
from pathlib import Path
from branca.colormap import linear
import folium
from shapely.geometry import Point, Polygon
import altair as alt
import calendar
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from shiny import reactive
from shiny.express import render,input, ui
from shinywidgets import render_plotly, render_altair, render_widget
import geopandas as gpd
import pandas as pd
import folium
from shapely.geometry import Point
import h3
import h3
from shapely.geometry import Polygon
from shiny.express import ui, render

from worddatabase import word_database
ui.tags.style(
    """





        body {

            background-color: white;
            padding: 10px !important;
            Margin: 10px !important;
        
        
        }
        .card1 {
            background-color: white;
            padding: 0px !important;
            border-radius: 0px !important;
            margin: 0px !important;
            box-shadow: none !important;
            border: 1px solid black; /* or border-color if you already have a border defined */
        }
        .card2 {
            background-color: orange !important;
            padding: 0px !important;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(250, 0, 0, 0.3) !important;
            margin: 10px !important;
            border-color: black;
        }
        .card {
            background-color: white;
            padding: 0px !important;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 250, 0, 0.3);
            margin: 10px !important;
            border-color: black;
        }
        .modebar{
            display: none;
        
        }
        .battery-input-row {
            margin-top: -20px !important; /* Pull rows closer together */
            margin-bottom: -25px !important;
            padding-top: 0px !important; 
            padding-bottom: 0px !important;
        }
        .battery-input-row label {
            font-size: 10px !important; /* Adjust the font size as needed */
            padding: 0px !important;
            margin: 0px !important;
            justify-content: center !important;
            align-items: center !important; 
        }

        .small-number-input input {
            padding: 0px !important;  /* Adjust padding for a compact look */
           
        }
        .info-gen-css-word {
            border-top-left-radius: 0px !important;
            border-top-right-radius: 0px !important;
            font-size: 16px !important; /* Adjust the size as needed */
            color: white !important;
            display: flex !important; /* Enables centering */
            align-items: center !important; /* Centers vertically */
            justify-content: center !important; /* Centers horizontally */
            text-align: center !important; /* Ensures text alignment */
            font-weight: bold !important; /* Makes the text bold */
            background-color: green !important;
        }
        .info-gen-css-pronunciation {
            border-top-left-radius: 0px !important;
            border-top-right-radius: 0px !important;
            font-size: 16px !important; /* Adjust the size as needed */
            color: white !important;
            display: flex !important; /* Enables centering */
            align-items: center !important; /* Centers vertically */
            justify-content: center !important; /* Centers horizontally */
            text-align: center !important; /* Ensures text alignment */
            font-weight: bold !important; /* Makes the text bold */
            background-color: brown !important;
        }
        .info-gen-css-definition {
            border-top-left-radius: 0px !important;
            border-top-right-radius: 0px !important;
            font-size: 16px !important; /* Adjust the size as needed */
            color: white !important;
            display: flex !important; /* Enables centering */
            align-items: center !important; /* Centers vertically */
            justify-content: center !important; /* Centers horizontally */
            text-align: center !important; /* Ensures text alignment */
            font-weight: bold !important; /* Makes the text bold */
            background-color: blue !important;
        }
        .info-gen-css-example {
            border-top-left-radius: 0px !important;
            border-top-right-radius: 0px !important;
            font-size: 16px !important; /* Adjust the size as needed */
            color: white !important;
            display: flex !important; /* Enables centering */
            align-items: center !important; /* Centers vertically */
            justify-content: center !important; /* Centers horizontally */
            text-align: center !important; /* Ensures text alignment */
            font-weight: bold !important; /* Makes the text bold */
            background-color: purple !important;
        }
        .sidebar {
            background-color: lightblue !important;
     
            
        }
        .custom-nav-wrapper {
            background-color: #001861;  
            padding: 10px;
            border-radius: 8px;
            margin: 0px;
        }
        .nav-pills .nav-link {
            background-color: #f8f9fa;   /* Light gray background */
            color: #000;                 /* Black text */
            border: 1px solid #ccc;      /* Light border */
            margin-bottom: 10px;
            margin-right: 10px !important;
            font-weight: bold;
        }

        .nav-pills .nav-link.active {
            background-color: #007bff;   /* Bootstrap primary blue for active */
            color: white;
        }

        .nav-pills .nav-link:hover {
            background-color: yellow;   /* Slightly darker on hover */
            color: #000;
        }
        .vb-title {
            font-size: 13px;
            font-weight: bold;
            margin-bottom: 4px;
            color: black;
        }

        .vb-value {
            font-size: 16px;
            font-weight: 600;
        }
        .vb-small {
            
            min-height: 63px !important;
            height: 63px !important;
        }
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100px;
            padding: 10px;
            margin: 0px !important;
        }
        .logo-container {
            margin: 0px !important;
            height: 100%;
            padding: 10px;
        
        }
        .logo-container img {
            height: 100px;
            margin: 0px !important;
           
        }
        #side-label {
            color: darkblue !important;
            font-size: 13px !important;

        }
        .center-container {
            display: flex;
            justify-content: center;
            margin: -20px !important;
        }
        .btnnext {
            font-size: 15px !important;
            padding: 8px 16px;
            background-color: #0c7063;
            color: white;
            border: none;
            border-radius: 5px;
            width: 180px !important;
        }
        .btnprev {
            font-size: 15px !important;
            padding: 8px 16px;
            background-color: #00c2b8;
            color: white;
            border: none;
            border-radius: 5px;
            width: 180px !important;
        }
        .btnsave {
            font-size: 15px !important;
            padding: 8px 16px;
            background-color: #0d0d0d;
            color: white;
            border: none;
            border-radius: 5px;
            width: 180px !important;
        }
        .btnnext:hover {
            background-color: #e3e314; /* darker teal on hover */
        }
        .btnprev:hover {
            background-color: #e3e314; /* darker teal on hover */
        }
    """
)



ui.page_opts(window_title="English Toolkit", fillable=True)


current_index = reactive.Value(-1)
last_next = reactive.Value(0)
last_prev = reactive.Value(0)


df1 = word_database[word_database["Point"] == 1]

df2 = word_database[word_database["Point"] == 0]



with ui.card(full_screen=True, height="400px", class_="card2"):
    with ui.layout_sidebar():
        with ui.sidebar(bg="#f8f8f8"):
            ui.input_selectize(
                "learningmethod",
                ui.tags.label("Practice Option", id="side-label"),
                ['New Words', 'Review', 'All Words'],
                multiple=False,
                selected="All Words"
            )

            ui.input_selectize(
                "category",
                ui.tags.label("Category", id="side-label"),
                ['All', 'General', 'Business', 'Education', 'Emotion', 'Political', 'Social', 'Economic', 'Health'],
                multiple=False,
                selected="All"
            )

            ui.input_selectize(
                "level",
                ui.tags.label("Level", id="side-label"),
                ['All', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2'],
                multiple=False,
                selected="All"
            )
            ui.input_selectize(
                "noofwords",
                ui.tags.label("Number of Words", id="side-label"),
                choices={"5": 5, "10": 10, "15": 15, "20": 20, "25": 25, "All": "All"},
                multiple=False,
                selected="All"
            )
            
            # ⬇️ New section: Browse CSV file
            ui.div(
                ui.input_file(
                    "csv_file",
                    "Upload your CSV File",
                    accept=[".csv"]
                ),
                style="""
                    font-size: 12px;
                    margin-top: 8px;
                    color: darkblue;
                    margin-bottom: 12px;
                """
            )


        # Three separate cards for Word, Definition, Example
        with ui.layout_columns(col_widths={"sm": (6,6,6,6)}):

            with ui.card(height="100px"):
                ui.card_header("Word", class_="info-gen-css-word")

                @render.ui
                @reactive.event(input.Next, input.Previous, input.Save)
                def show_word():



                    # 
                    if input.Next() > last_next.get():
                        current_index.set(current_index.get() + 1)
                        last_next.set(input.Next())
                    elif input.Previous() > last_prev.get():
                        current_index.set(current_index.get() - 1)
                        last_prev.set(input.Previous())


                    if input.learningmethod() == "New Words":
                        if input.category() == 'All':
                            df21 = df2.copy()
                        else:
                            df21 = df2[df2['Category']==input.category()]

                        if input.level()== 'All':
                            df211=df21.copy()

                        else:
                            df211 = df21[df21['Level']==input.level()]

 
                        # Get the list of indexes
                        index_list = df211.index.tolist()
                    elif input.learningmethod() == "Review":

                        if input.category() == 'All':
                            df11 = df1.copy()
                        else:
                            df11 = df1[df1['Category']==input.category()]

                        if input.level()== 'All':
                            df111=df11.copy()

                        else:
                            df111 = df11[df11['Level']==input.level()]


                        index_list = df111.index.tolist()

                    else:

                        if input.category() == 'All':
                            df31 = word_database.copy()
                        else:
                            df31 = word_database[word_database['Category']==input.category()]


                        if input.level()== 'All':
                            df311=df31.copy()

                        else:
                            df311 = df31[df31['Level']==input.level()]


                        index_list = df311.index.tolist()

                    if input.noofwords() == "All":
                        noofwords=2000
                    else:
                        noofwords=input.noofwords()

                    # Wrap around
                    if current_index.get() >= min(int(noofwords), len(index_list)):
                        current_index.set(0)
                    elif current_index.get() < 0:
                        current_index.set(min(int(noofwords), len(index_list))- 1)

                    idx1 = current_index.get()
                    idx = index_list[idx1]
                    word = word_database.loc[idx, "Word"]
                    word_level = word_database.loc[idx, "Level"]

                    wordpluslevel = f"Level: {word_level}"


                    # 
                    checkbox_id = f"learned_{idx}"
                    checked = word_database.loc[idx, "Point"] == 1
                    checked_attr = "checked" if checked else ""

                    

                    if input.Save() > 0:
                        print(input.Save())
                        word_database.to_csv("Words.csv", index=False)

                    return ui.HTML(f"""
                        <div style='text-align:center; padding: 6px; font-weight:bold; font-size:28px;'>{word}</div>
                        <div style='text-align:center; padding: 6px; font-size:14px; color: brown'>{wordpluslevel}</div>
                        <div style='text-align:center; padding: 6px;'>
                            <input type="checkbox" id="{checkbox_id}" {checked_attr}
                                onchange="Shiny.setInputValue('chk_event', {{id:{idx}, value:this.checked}}, {{priority: 'event'}})">
                            <label for="{checkbox_id}">Mark as Learned</label>
                        </div>
                    """)

                # 
                @reactive.effect
                @reactive.event(input.chk_event)
                def update_point():
                    idx = input.chk_event()["id"]
                    val = input.chk_event()["value"]
                    word_database.loc[idx, "Point"] = 1 if val else 0
                   
            with ui.card(height="100px"):
                ui.card_header("Pronunciation", class_="info-gen-css-pronunciation")

                @render.ui
                @reactive.event(input.Next, input.Previous)
                def show_pronunciation():



                    if input.learningmethod() == "New Words":
                        if input.category() == 'All':
                            df21 = df2.copy()
                        else:
                            df21 = df2[df2['Category']==input.category()]

                        if input.level()== 'All':
                            df211=df21.copy()

                        else:
                            df211 = df21[df21['Level']==input.level()]

 
                        # Get the list of indexes
                        index_list = df211.index.tolist()
                    elif input.learningmethod() == "Review":

                        if input.category() == 'All':
                            df11 = df1.copy()
                        else:
                            df11 = df1[df1['Category']==input.category()]

                        if input.level()== 'All':
                            df111=df11.copy()

                        else:
                            df111 = df11[df11['Level']==input.level()]


                        index_list = df111.index.tolist()

                    else:

                        if input.category() == 'All':
                            df31 = word_database.copy()
                        else:
                            df31 = word_database[word_database['Category']==input.category()]


                        if input.level()== 'All':
                            df311=df31.copy()

                        else:
                            df311 = df31[df31['Level']==input.level()]


                        index_list = df311.index.tolist()


                    idx1 = current_index.get()
                    idx = index_list[idx1]

                    word = word_database.loc[idx, "Word"]
                    audio_file = f"Pronunciation/{word}.mp3"


                    folder = "www/Pronunciation"
                    os.makedirs(folder, exist_ok=True)  # Ensure folder exists
                    
                    audio_file = os.path.join(folder, f"{word}.mp3")

                    # Check if audio exists, otherwise create it
                    if not os.path.exists(audio_file):
                        tts = gTTS(text=word, lang="en")
                        tts.save(audio_file)

                    audio_file = f"Pronunciation/{word}.mp3"


                    # HTML audio player with autoplay
                    return ui.HTML(f"""
                        <div style='text-align:center;  padding: 100px;'>
                            <audio controls autoplay>
                                <source src='{audio_file}' type='audio/mpeg'>
                                Your browser does not support the audio element.
                            </audio>
                        </div>
                    """)
                

            with ui.card(height="100px"):
                ui.card_header("Definition", class_="info-gen-css-definition")

                @render.ui
                @reactive.event(input.Next, input.Previous)
                def show_Definition():


                    if input.learningmethod() == "New Words":
                        if input.category() == 'All':
                            df21 = df2.copy()
                        else:
                            df21 = df2[df2['Category']==input.category()]

                        if input.level()== 'All':
                            df211=df21.copy()

                        else:
                            df211 = df21[df21['Level']==input.level()]

 
                        # Get the list of indexes
                        index_list = df211.index.tolist()
                    elif input.learningmethod() == "Review":

                        if input.category() == 'All':
                            df11 = df1.copy()
                        else:
                            df11 = df1[df1['Category']==input.category()]

                        if input.level()== 'All':
                            df111=df11.copy()

                        else:
                            df111 = df11[df11['Level']==input.level()]


                        index_list = df111.index.tolist()

                    else:

                        if input.category() == 'All':
                            df31 = word_database.copy()
                        else:
                            df31 = word_database[word_database['Category']==input.category()]


                        if input.level()== 'All':
                            df311=df31.copy()

                        else:
                            df311 = df31[df31['Level']==input.level()]


                        index_list = df311.index.tolist()



                    idx1 = current_index.get()
                    idx = index_list[idx1]

                    Definition = word_database.loc[idx, "Definition"]
                    return ui.HTML(f"<div style='text-align:left; font-weight:bold; font-size:20px;'>{Definition}</div>")
                

            with ui.card(height="100px"):
                ui.card_header("Example", class_="info-gen-css-example")


                @render.ui
                @reactive.event(input.Next, input.Previous)
                def show_Example():


                    if input.learningmethod() == "New Words":
                        if input.category() == 'All':
                            df21 = df2.copy()
                        else:
                            df21 = df2[df2['Category']==input.category()]

                        if input.level()== 'All':
                            df211=df21.copy()

                        else:
                            df211 = df21[df21['Level']==input.level()]

 
                        # Get the list of indexes
                        index_list = df211.index.tolist()
                    elif input.learningmethod() == "Review":

                        if input.category() == 'All':
                            df11 = df1.copy()
                        else:
                            df11 = df1[df1['Category']==input.category()]

                        if input.level()== 'All':
                            df111=df11.copy()

                        else:
                            df111 = df11[df11['Level']==input.level()]


                        index_list = df111.index.tolist()

                    else:

                        if input.category() == 'All':
                            df31 = word_database.copy()
                        else:
                            df31 = word_database[word_database['Category']==input.category()]


                        if input.level()== 'All':
                            df311=df31.copy()

                        else:
                            df311 = df31[df31['Level']==input.level()]


                        index_list = df311.index.tolist()


                    idx1 = current_index.get()
                    idx = index_list[idx1]

                    Example = word_database.loc[idx, "Example"]
                    
                    return ui.HTML(f"<div style='text-align:left; font-weight:bold; font-size:20px;'>{Example}</div>")


            # with ui.card(height="300px"):
            #     @render.data_frame
            #     def show_file_info():
            #         file = input.csv_file()
            #         if file is None:
            #             return pd.DataFrame({"Message": ["No file uploaded yet."]})
            #         # read CSV into DataFrame
            #         df = pd.read_csv(file[0]["datapath"])
            #         return render.DataGrid(df)

        ui.div(
            ui.input_action_button("Previous", "Previous", class_="btnprev"),
            ui.input_action_button("Next", "Next", class_="btnnext"),
            ui.input_action_button("Save", "Save", class_="btnsave"),
            class_="d-flex justify-content-center gap-5",
            style="margin: auto;"
        )


