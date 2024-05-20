import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from header import header
from sqlalchemy import create_engine, text
import urllib.parse

# Define the layout
layout = html.Div([
    header(),
    dbc.Container([
        html.H1("Resource Quantity Form", style={'color': '#004d40', 'text-align': 'center', 'margin-bottom': '30px'}),
        dbc.Form([
            dbc.Row([
                dbc.Col(dbc.Label("Beds", style={'font-weight': 'bold', 'color': '#004d40'}), width=4),
                dbc.Col(dcc.Input(id='beds', type='number', placeholder='Enter quantity', className='form-control'), width=8)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label("Nebulizers", style={'font-weight': 'bold', 'color': '#004d40'}), width=4),
                dbc.Col(dcc.Input(id='nebulizers', type='number', placeholder='Enter quantity', className='form-control'), width=8)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label("Oxygen Masks", style={'font-weight': 'bold', 'color': '#004d40'}), width=4),
                dbc.Col(dcc.Input(id='oxygen-masks', type='number', placeholder='Enter quantity', className='form-control'), width=8)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label("Catheters", style={'font-weight': 'bold', 'color': '#004d40'}), width=4),
                dbc.Col(dcc.Input(id='catheters', type='number', placeholder='Enter quantity', className='form-control'), width=8)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label("Ventilators", style={'font-weight': 'bold', 'color': '#004d40'}), width=4),
                dbc.Col(dcc.Input(id='ventilators', type='number', placeholder='Enter quantity', className='form-control'), width=8)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label("IV Fluids", style={'font-weight': 'bold', 'color': '#004d40'}), width=4),
                dbc.Col(dcc.Input(id='iv-fluids', type='number', placeholder='Enter quantity', className='form-control'), width=8)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Label("Endotracheal Tubes", style={'font-weight': 'bold', 'color': '#004d40'}), width=4),
                dbc.Col(dcc.Input(id='endotracheal-tubes', type='number', placeholder='Enter quantity', className='form-control'), width=8)
            ], className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Button('Submit', id='submit-val', className='mt-3', style={'width': '100%','background-color':'#008080'}), width={'size': 6, 'offset': 3})
            ], className='mb-3'),
            html.Div(id='supplies', style={'margin-top': '20px', 'font-weight': 'bold', 'text-align': 'center', 'color': '#004d40'})
        ])
    ], className='mt-5', style={'max-width': '600px', 'background-color': '#e0f7fa', 'padding': '20px', 'border-radius': '15px', 'box-shadow': '0 4px 8px 0 rgba(0,0,0,0.2)'})
])

# Database connection
password_encoded = urllib.parse.quote_plus("oviya@1604")
engine = create_engine(f'mysql+mysqlconnector://root:{password_encoded}@localhost:3306/healthcare')
resource_mapping = {
    'beds': 'Beds',
    'nebulizers': 'Nebulizers',
    'oxygen-masks': 'Oxygen Masks',
    'catheters': 'Catheters',
    'ventilators': 'Ventilators',
    'iv-fluids': 'IV Fluids',
    'endotracheal-tubes': 'Endotracheal Tubes'
}

def update_database(form_values):
    with engine.connect() as conn:
        # Prepare the update statement
        update_stmt = text("""
            UPDATE resource
            SET total = total + :quantity
            WHERE name = :resource_name
        """)
        
        # Execute the update statement for each form value
        for form_id, quantity in form_values.items():
            resource_name = resource_mapping.get(form_id)
            if resource_name:
                conn.execute(update_stmt, quantity=quantity, resource_name=resource_name)

def register_callbacks(app):
    @app.callback(
        Output('supplies', 'children'),
        [Input('submit-val', 'n_clicks')],
        [
            State('beds', 'value'),
            State('nebulizers', 'value'),
            State('oxygen-masks', 'value'),
            State('catheters', 'value'),
            State('ventilators', 'value'),
            State('iv-fluids', 'value'),
            State('endotracheal-tubes', 'value')
        ]
    )
    def update_output(n_clicks, beds, nebulizers, oxygen_masks, catheters, ventilators, iv_fluids, endotracheal_tubes):
        if n_clicks:
            form_values = {
                'beds': beds if beds else 0,
                'nebulizers': nebulizers if nebulizers else 0,
                'oxygen-masks': oxygen_masks if oxygen_masks else 0,
                'catheters': catheters if catheters else 0,
                'ventilators': ventilators if ventilators else 0,
                'iv-fluids': iv_fluids if iv_fluids else 0,
                'endotracheal-tubes': endotracheal_tubes if endotracheal_tubes else 0
            }
            
            update_database(form_values)
            
            return "Database updated successfully!"
       

