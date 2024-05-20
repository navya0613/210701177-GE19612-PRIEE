import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from sqlalchemy import create_engine
import urllib.parse

age_grp = {
    '1-17': (1, 17),
    '18-25': (18, 25),
    '26-35': (26, 35),
    '36-50': (36, 50),
    '51-70': (51, 70),
    '71-100': (71, 100),
}

def assign_age_group(age):
    for grp, (start, end) in age_grp.items():
        if start <= age <= end:
            return grp
    return 'Unknown'

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = dbc.Container([
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Univariate', 'value': 'option1'},
            {'label': 'Bivariate', 'value': 'option2'},
            {'label': 'Multivariate', 'value': 'option3'}
        ],
        value='option1',
        style={"width": "50%"}
    ),
    html.Div(id='output-container')
], className="my-4")

def query_data():
    # Create a connection to your MySQL database
    password_encoded = urllib.parse.quote_plus("oviya@1604")
    engine = create_engine(f'mysql+mysqlconnector://root:{password_encoded}@localhost:3306/healthcare')
    
    # Query data from the database
    query = "SELECT * FROM patient_data"
    df = pd.read_sql(query, engine)
    
    # Close the database connection
    engine.dispose()
    return df


    
def register_callbacks(app):
    @app.callback(
        Output('output-container', 'children'),
        [Input('dropdown', 'value')]
    )
    def update_output(selected_option):
        if selected_option == 'option1':
            df = query_data()
            triage_colors = {'Yellow': 'Yellow', 'Green': 'Green', 'Red': 'Red'}
            accident_counts = df.groupby(['Gender', 'Accident']).size().reset_index(name='count')
            df['Age_Group'] = df['Age'].apply(assign_age_group)
            return html.Div([
                    dbc.Row([
                    dbc.Col(dcc.Graph(
                    id='histogram',
                    figure=px.histogram(df, x='Age_Group', title='Age Distribution', color_discrete_sequence=px.colors.qualitative.Safe)
                ), width=6),
                    dbc.Col(dcc.Graph(
                        id='triage-vs-dept',
                        figure=px.histogram(df, x=df['Triage'], title="Triage",  color='Triage', 
                            color_discrete_map=triage_colors
                                )
                    ), width=6),
                ]),
                dbc.Row([
                    dbc.Col(dcc.Graph(
                        id='location',
                        figure=px.histogram(df, x=df['Location'], title="Location",
                                            color_discrete_sequence=px.colors.qualitative.Set3)
                    ), width=6),
                    dbc.Col(dcc.Graph(
                        id='dept',
                        figure=px.pie(df, names=df['Department'], title="Department",
                                    color_discrete_sequence=px.colors.qualitative.Plotly)
                    ), width=6)
                ]),
                dbc.Row([
                    dbc.Col(dcc.Graph(
                        id='accident',
                        figure=px.histogram(df, x=df['Accident'], title="Accident",
                                            color_discrete_sequence=px.colors.qualitative.Bold)
                    ), width=4),
                    dbc.Col(dcc.Graph(
                        id='diabetes',
                        figure=px.histogram(df, x=df['Diabetes'], title="Diabetes",
                                            color_discrete_sequence=px.colors.qualitative.Safe)
                    ), width=4),
                    dbc.Col(dcc.Graph(
                        id='hyper',
                        figure=px.histogram(df, x=df['Hypertension'], title="Hypertension",
                                            color_discrete_sequence=px.colors.qualitative.Set3)
                    ), width=4)
                ]),
                dbc.Row([
                    dbc.Col(dcc.Graph(
                        id='heart',
                        figure=px.histogram(df, x=df['History of Heart Disease'], title="Heart Disease",
                                            color_discrete_sequence=px.colors.qualitative.Pastel2)
                    ), width=4),
                    dbc.Col(dcc.Graph(
                        id="gender",
                        figure=px.histogram(df, x=df['Gender'], title="Gender",
                                            color_discrete_sequence=px.colors.qualitative.Prism)
                    ), width=4),
                    dbc.Col(dcc.Graph(
                        id="cause-of-accident",
                        figure=px.histogram(df, x=df['Cause of Accident'], title="Cause of Accident",
                                            color_discrete_sequence=px.colors.qualitative.G10)
                    ), width=4)
                ]),
                        dbc.Row([
                                dbc.Col(dcc.Graph(
                        id='age',
                        figure=px.pie(df, names=df['Age_Group'], title="Age",
                                    color_discrete_sequence=px.colors.qualitative.Pastel)
                    ), width=6),
                dbc.Col(dcc.Graph(
                    id='pie-chart',
                    figure=px.pie(df, names='Gender', title='Gender Distribution')
                ), width=6)
            ])
            ])
        
        elif selected_option == 'option2':
            df = query_data()
            df_filtered = df[df['Cause of Accident'] != '-']
            accident_counts = df.groupby(['Gender', 'Accident']).size().reset_index(name='count')
            triage_colors = {'Yellow': 'Yellow', 'Green': 'Green', 'Red': 'Red'}
            df['Age_Group'] = df['Age'].apply(assign_age_group)
            return html.Div([
                dbc.Row([
                    dbc.Col(dcc.Graph(
                        id='triage-vs-dept',
                        figure=px.box(df, x=df['Triage'], y=df['Department'], title="Triage vs Departments",  color='Triage', 
                            color_discrete_map=triage_colors
                                )
                    ), width=6),
                    dbc.Col(dcc.Graph(
                        id='count-of-accidents',
                        figure=px.bar(accident_counts, x='Gender', y='count', color='Accident',
                                    title='Count of Accidents by Gender', barmode='stack')
                    ), width=6)
                ]),
                dbc.Row([
                    dbc.Col(dcc.Graph(
                        id='cause-department',
                        figure=px.bar(df_filtered, x='Department', color='Cause of Accident', title='Cause of Accident vs Department')
                    ), width=6),
                    dbc.Col(dcc.Graph(
                        id='age-group-department',
                        figure=px.bar(df, x='Department', color='Age_Group', title='Age Group vs Department')
                    ), width=6)
                ])
            ])
        elif selected_option == 'option3':
            df = query_data()
            df_filtered = df[df['Cause of Accident'] != '-']
            count_filtered = len(df_filtered)
            return html.Div([
            dbc.Row([
                dbc.Col(dcc.Graph(
                    id='scatter-1',
                    figure=px.scatter(df, x='Age', y='Department', color='Gender', title='Age vs Department by Gender')
                ), width=12),
                dbc.Col(dcc.Graph(
                    id='scatter-2',
                    figure=px.scatter(df_filtered, x='Age', y='Department', color='Cause of Accident',
                                    title=f'Age vs Department by Cause of Accident (Count: {count_filtered})')
                ), width=12)
            ])

        ])
