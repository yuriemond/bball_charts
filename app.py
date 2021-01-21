from nba_api.stats.endpoints import shotchartdetail
import json 
import requests
import pandas as pd 
import datetime
import plotly.express as px 
import plotly.graph_objs as go
import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode, iplot


import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

