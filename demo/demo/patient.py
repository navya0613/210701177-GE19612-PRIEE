from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.H1('Patient Information Form', style={'color': 'A4EDDD'}),
    dbc.Form(
        id='patient-form',
        children=[
            dbc.Row([
                dbc.Col(dbc.Label('Name:', html_for='name', width=2)),
                dbc.Col(dcc.Input(type='text', id='name', placeholder='Enter your name', className='form-control'), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Age:', html_for='age', width=2)),
                dbc.Col(dcc.Input(type='number', id='age', placeholder='Enter your age', className='form-control'), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Gender:', html_for='gender', width=2)),
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
                dbc.Col(dbc.Label('Hypertension:', html_for='hypertension', width=2)),
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
                dbc.Col(dbc.Label('Diabetes:', html_for='diabetes', width=2)),
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
                dbc.Col(dbc.Label('History of Heart Disease:', html_for='heart_disease', width=2)),
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
                dbc.Col(dbc.Label('Triage:', html_for='triage', width=2)),
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
                dbc.Col(dbc.Label('Location:', html_for='location', width=2)),
                dbc.Col(dcc.Input(type='text', id='location', placeholder='Enter location', className='form-control'), width=10)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label('Accident:', html_for='accident', width=2)),
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
                dbc.Col(dbc.Label('Cause of Accident:', html_for='cause', width=2)),
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
                dbc.Col(dbc.Label('Department:', html_for='dept', width=2)),
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
            dbc.Button(
                'Submit',
                id='submit-button',
                color='success',
                className='mt-3'
            ),
            html.Div(id='output-message', style={'margin-top': '20px', 'font-weight': 'bold', 'margin': 'auto'})
        ]
    )
], className='mt-5')
