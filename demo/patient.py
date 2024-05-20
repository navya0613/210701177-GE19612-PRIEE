from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from sqlalchemy import create_engine
import urllib.parse
from header import header

# Define layout
layout = header(), dbc.Container([  
    html.H1('Patient Information Form', style={'color': '#004d40', 'text-align': 'center', 'margin-bottom': '30px'}),
    dbc.Form(
        id='patient-form',
        children=[
            dbc.Row([
                dbc.Col(dbc.Label('Name:', html_for='name', width=2, style={'font-weight': 'bold', 'color': '#004d40'})),
                dbc.Col(dcc.Input(type='text', id='name', placeholder='Enter your name', className='form-control'), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Age:', html_for='age', width=2, style={'font-weight': 'bold', 'color': '#004d40'})),
                dbc.Col(dcc.Input(type='number', id='age', placeholder='Enter your age', className='form-control'), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Gender:', html_for='gender', width=2, style={'font-weight': 'bold', 'color': '#004d40'})),
                dbc.Col(dcc.Dropdown(
                    id='gender',
                    options=[
                        {'label': 'Male', 'value': 'Male'},
                        {'label': 'Female', 'value': 'Female'},
                        {'label': 'Other', 'value': 'Other'}
                    ],
                    placeholder='Select gender',
                    className='form-control'
                ), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Hypertension:', html_for='hypertension', width=2, style={'font-weight': 'bold', 'color': '#004d40'})),
                dbc.Col(dcc.Dropdown(
                    id='hypertension',
                    options=[
                        {'label': 'Yes', 'value': 'Yes'},
                        {'label': 'No', 'value': 'No'}
                    ],
                    placeholder='Select hypertension status',
                    className='form-control'
                ), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Diabetes:', html_for='diabetes', width=2, style={'font-weight': 'bold', 'color': '#004d40'})),
                dbc.Col(dcc.Dropdown(
                    id='diabetes',
                    options=[
                        {'label': 'Yes', 'value': 'Yes'},
                        {'label': 'No', 'value': 'No'}
                    ],
                    placeholder='Select diabetes status',
                    className='form-control'
                ), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('History of Heart Disease:', html_for='heart_disease', width=2, style={'font-weight': 'bold', 'color': '#004d40'})),
                dbc.Col(dcc.Dropdown(
                    id='heart_disease',
                    options=[
                        {'label': 'Yes', 'value': 'Yes'},
                        {'label': 'No', 'value': 'No'}
                    ],
                    placeholder='Select heart disease status',
                    className='form-control'
                ), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Triage:', html_for='triage', width=2, style={'font-weight': 'bold', 'color': '#004d40'})),
                dbc.Col(dcc.Dropdown(
                    id='triage',
                    options=[
                        {'label': 'Red', 'value': 'Red'},
                        {'label': 'Yellow', 'value': 'Yellow'},
                        {'label': 'Green', 'value': 'Green'}
                    ],
                    placeholder='Select triage level',
                    className='form-control'
                ), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Location:', html_for='location', width=2, style={'font-weight': 'bold', 'color': '#004d40'})),
                dbc.Col(dcc.Input(type='text', id='location', placeholder='Enter location', className='form-control'), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Accident:', html_for='accident', width=2, style={'font-weight': 'bold', 'color': '#004d40'})),
                dbc.Col(dcc.Dropdown(
                    id='accident',
                    options=[
                        {'label': 'Yes', 'value': 'Yes'},
                        {'label': 'No', 'value': 'No'}
                    ],
                    placeholder='Select accident status',
                    className='form-control'
                ), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Cause of Accident:', html_for='cause', width=2, style={'font-weight': 'bold', 'color': '#004d40'})),
                dbc.Col(dcc.Dropdown(
                    id='cause',
                    options=[
                        {'label': 'Fall', 'value': 'Fall'},
                        {'label': 'Fire', 'value': 'Fire'},
                        {'label': 'Drowning', 'value': 'Drowning'},
                        {'label': 'Earthquakes', 'value': 'Earthquakes'},
                        {'label': 'Chemicals/Poisoning', 'value': 'Chemicals'},
                        {'label': 'Vehicle Crash', 'value': 'Vehicle Crash'},
                        {'label': '-', 'value': '-'}
                    ],
                    placeholder='Select cause of accident',
                    className='form-control'
                ), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Department:', html_for='dept', width=2, style={'font-weight': 'bold', 'color': '#004d40'})),
                dbc.Col(dcc.Dropdown(
                    id='dept',
                    options=[
                        {'label': 'Ophthalmology', 'value': 'Ophthalmology'},
                        {'label': 'Cardiology', 'value': 'Cardiology'},
                        {'label': 'Emergency Medicine', 'value': 'Emergency Medicine'},
                        {'label': 'Orthopedics', 'value': 'Orthopedics'},
                        {'label': 'Pulmonology', 'value': 'Pulmonology'},
                        {'label': 'Endocrinology', 'value': 'Endocrinology'},
                        {'label': 'General Surgery', 'value': 'General Surgery'},
                        {'label': 'Obstetrics and Gynaecology', 'value': 'Obstetrics and Gynaecology'},
                        {'label': 'Pediatrics', 'value': 'Pediatrics'}
                    ],
                    placeholder='Select the Department',
                    className='form-control'
                ), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Button('Submit', id='submit-button', className='mt-3', style={'width': '100%','background-color':'#008080'}), width={'size': 6, 'offset': 3}),
            ], className='mb-3'),
            html.Div(id='output-message', style={'margin-top': '20px', 'font-weight': 'bold', 'text-align': 'center', 'color': '#004d40'})
        ]
    )
], className='mt-5', style={'max-width': '800px', 'background-color': '#e0f7fa', 'padding': '20px', 'border-radius': '15px', 'box-shadow': '0 4px 8px 0 rgba(0,0,0,0.2)'})

password_encoded = urllib.parse.quote_plus("oviya@1604")
engine = create_engine(f'mysql+mysqlconnector://root:{password_encoded}@localhost:3306/healthcare')
conn = engine.connect()

# Function to insert patient information
def insert_patient_info(name, age, gender, hypertension, diabetes, heart_disease, triage, location, accident, cause, dept):
    query = f"""
    INSERT INTO patient_data (Name, Age, Gender, Hypertension, Diabetes, `History of Heart Disease`, Triage, Location, Accident, `Cause of Accident`, Department)
    VALUES ('{name}', {age}, '{gender}', '{hypertension}', '{diabetes}', '{heart_disease}', '{triage}', '{location}', '{accident}', '{cause}', '{dept}')
    """
    conn.execute(query)
    
def register_callbacks(app):
    @app.callback(
        Output('output-message', 'children'),
        Input('submit-button', 'n_clicks'),
        [State('name', 'value'), State('age', 'value'), State('gender', 'value'),
        State('hypertension', 'value'), State('diabetes', 'value'), State('heart_disease', 'value'),
        State('triage', 'value'), State('location', 'value'), State('accident', 'value'),
        State('cause', 'value'), State('dept', 'value')]
    )
    def handle_patient_form(n_clicks, name, age, gender, hypertension, diabetes, heart_disease, triage, location, accident, cause, dept):
        if n_clicks and name and age and gender and hypertension and diabetes and heart_disease and triage and location and accident and cause and dept:
            insert_patient_info(name, age, gender, hypertension, diabetes, heart_disease, triage, location, accident, cause, dept)
            return 'Patient information submitted successfully!'
        


