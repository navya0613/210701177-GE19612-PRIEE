import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import urllib.parse
from sqlalchemy import create_engine, text
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import atexit
from header import header


# Database update function
def update_database(selected_resources):
    password_encoded = urllib.parse.quote_plus("oviya@1604")
    engine = create_engine(f'mysql+mysqlconnector://root:{password_encoded}@localhost:3306/healthcare')
    conn = engine.connect()
    
    for resource in selected_resources:
        query = text("SELECT in_use FROM resource WHERE name = :resource")
        result = conn.execute(query, {'resource': resource})
        current_in_use = result.fetchone()[0]
        
        new_in_use = current_in_use + 1
        query = text("UPDATE resource SET in_use = :new_in_use, last_updated = NOW() WHERE name = :resource")

        conn.execute(query, {'new_in_use': new_in_use, 'resource': resource})
    
    conn.close()

# Free resources function
def free_resources():
    password_encoded = urllib.parse.quote_plus("oviya@1604")
    engine = create_engine(f'mysql+mysqlconnector://root:{password_encoded}@localhost:3306/healthcare')
    conn = engine.connect()

    now = datetime.now()
    one_hour_ago = now - timedelta(hours=1)

    query = text("SELECT name, in_use FROM resource WHERE last_updated <= :one_hour_ago")
    result = conn.execute(query, {'one_hour_ago': one_hour_ago})

    for row in result:
        resource = row['name']
        current_in_use = row['in_use']
        if current_in_use > 0:
            new_in_use = current_in_use - 1

            update_query = text("UPDATE resource SET in_use = :new_in_use, last_updated = NOW() WHERE name = :resource")
            conn.execute(update_query, {'new_in_use': new_in_use, 'resource': resource})

    conn.close()

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(free_resources, 'interval', hours=1)
scheduler.start()

# Ensure the scheduler stops when the app exits
atexit.register(lambda: scheduler.shutdown())

# CSS styles for hospital theme
hospital_style = {
    'container': {
        'backgroundColor': '#e0f7fa',
        'padding': '10px',
        'borderRadius': '8px',
        'boxShadow': '0 4px 8px rgba(0,0,0,0.1)',
        'display':'flex',
        'justify-content':'center',
        'align-items':'center',
        'width':'500px',
        'margin-left':'400px' 
    },
    'header': {
        'textAlign': 'center',
        'color': '#343a40',
        'marginBottom': '30px',
    },
    'label': {
        'fontWeight': 'bold',
        'color': '#495057',
        'font-size':'30px',
        'text-align':'center',
        'align-items':'center',
        'margin-left':'60px'
    },
    'button': {
        'marginTop': '20px',
        'background-color':'#008080',
        'width':'250px'
    },
    'message': {
        'marginTop': '20px',
        'padding': '10px',
        'borderRadius': '5px',
        
        'color': '#155724',
        'textAlign': 'center',
    },
}

layout = header(), dbc.Container([
    html.H1("Resource Quantity Form", style=hospital_style['header']),
    
    dbc.Card([
        dbc.CardBody([
            html.Div([
                html.Label("Resources", style=hospital_style['label']),
                html.Br(),
                html.Br(),
                dcc.Checklist(
                    options=[
                        {'label': 'Beds', 'value': 'Beds'},
                        {'label': 'Nebulizers', 'value': 'Nebulizers'},
                        {'label': 'Oxygen Masks', 'value': 'Oxygen Masks'},
                        {'label': 'Catheters', 'value': 'Catheters'},
                        {'label': 'Ventilators', 'value': 'Ventilators'},
                        {'label': 'IV Fluids', 'value': 'IV Fluids'},
                        {'label': 'Endotracheal Tubes', 'value': 'Endotracheal Tubes'}
                    ],
                    id='resource-checklist',style={'font-size':'22px'},
                    inputClassName='mx-2'
                ),
                html.Br(),
                dbc.Button('Submit', id='submit-val', n_clicks=0, style=hospital_style['button']),
                html.Br(),
                html.Div(id='resource_ip', children='Select resources and press submit', style=hospital_style['message'])
            ])
        ])
    ], style=hospital_style['container'])
], className="mt-4")

def register_callbacks(app):
    @app.callback(
        Output('resource_ip', 'children'),
        Input('submit-val', 'n_clicks'),
        State('resource-checklist', 'value')
    )
    def update_output(n_clicks, selected_resources):
        if n_clicks > 0:
            if selected_resources:
                update_database(selected_resources)
                supplies = [f"{resource.replace('_', ' ').title()}" for resource in selected_resources]
                return ', '.join(supplies) + ' have been updated.'
            else:
                return 'No resources selected.'
       

