import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import urllib.parse
from sqlalchemy import create_engine

# Database update function
def update_database(selected_resources):
    password_encoded = urllib.parse.quote_plus("oviya@1604")
    engine = create_engine(f'mysql+mysqlconnector://root:{password_encoded}@localhost:3306/healthcare')
    conn = engine.connect()
    
    for resource in selected_resources:
        query = "SELECT in_use FROM resource WHERE name = %s"
        result = conn.execute(query, (resource,))
        current_in_use = result.fetchone()[0]
        
        new_in_use = current_in_use + 1
        
        query = "UPDATE resource SET in_use = %s WHERE name = %s"
        conn.execute(query, (new_in_use, resource))
    
    conn.close()

# Dash app setup
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = dbc.Container([
    html.H1("Resource Quantity Form"),
    html.Div([
        html.Label("Beds"),
        dcc.Input(id='beds', type='number', placeholder='Enter quantity'),
        dcc.Checklist(
            options=[{'label': 'Update Beds', 'value': 'beds'}],
            id='beds-checklist'
        ),
        html.Br(),
        html.Label("Nebulizers"),
        dcc.Input(id='nebulizers', type='number', placeholder='Enter quantity'),
        dcc.Checklist(
            options=[{'label': 'Update Nebulizers', 'value': 'nebulizers'}],
            id='nebulizers-checklist'
        ),
        html.Br(),
        html.Label("Oxygen Masks"),
        dcc.Input(id='oxygen-masks', type='number', placeholder='Enter quantity'),
        dcc.Checklist(
            options=[{'label': 'Update Oxygen Masks', 'value': 'oxygen_masks'}],
            id='oxygen-masks-checklist'
        ),
        html.Br(),
        html.Label("Catheters"),
        dcc.Input(id='catheters', type='number', placeholder='Enter quantity'),
        dcc.Checklist(
            options=[{'label': 'Update Catheters', 'value': 'catheters'}],
            id='catheters-checklist'
        ),
        html.Br(),
        html.Label("Ventilators"),
        dcc.Input(id='ventilators', type='number', placeholder='Enter quantity'),
        dcc.Checklist(
            options=[{'label': 'Update Ventilators', 'value': 'ventilators'}],
            id='ventilators-checklist'
        ),
        html.Br(),
        html.Label("IV Fluids"),
        dcc.Input(id='iv-fluids', type='number', placeholder='Enter quantity'),
        dcc.Checklist(
            options=[{'label': 'Update IV Fluids', 'value': 'iv_fluids'}],
            id='iv-fluids-checklist'
        ),
        html.Br(),
        html.Label("Endotracheal Tubes"),
        dcc.Input(id='endotracheal-tubes', type='number', placeholder='Enter quantity'),
        dcc.Checklist(
            options=[{'label': 'Update Endotracheal Tubes', 'value': 'endotracheal_tubes'}],
            id='endotracheal-tubes-checklist'
        ),
        html.Br(),
        html.Button('Submit', id='submit-val', n_clicks=0),
        html.Br(),
        html.Div(id='resource_ip', children='Enter values and press submit')
    ])
])

def register_callbacks(app):
    @app.callback(
        Output('resource_ip', 'children'),
        Input('submit-val', 'n_clicks'),
        State('beds', 'value'),
        State('nebulizers', 'value'),
        State('oxygen-masks', 'value'),
        State('catheters', 'value'),
        State('ventilators', 'value'),
        State('iv-fluids', 'value'),
        State('endotracheal-tubes', 'value'),
        State('beds-checklist', 'value'),
        State('nebulizers-checklist', 'value'),
        State('oxygen-masks-checklist', 'value'),
        State('catheters-checklist', 'value'),
        State('ventilators-checklist', 'value'),
        State('iv-fluids-checklist', 'value'),
        State('endotracheal-tubes-checklist', 'value')
    )
    def update_output(n_clicks, beds, nebulizers, oxygen_masks, catheters, ventilators, iv_fluids, endotracheal_tubes,
                      beds_checked, nebulizers_checked, oxygen_masks_checked, catheters_checked, ventilators_checked,
                      iv_fluids_checked, endotracheal_tubes_checked):
        if n_clicks > 0:
            supplies = []
            selected_resources = []
            if beds_checked and 'beds' in beds_checked:
                selected_resources.append('beds')
                supplies.append(f"Beds: {beds}")
            if nebulizers_checked and 'nebulizers' in nebulizers_checked:
                selected_resources.append('nebulizers')
                supplies.append(f"Nebulizers: {nebulizers}")
            if oxygen_masks_checked and 'oxygen_masks' in oxygen_masks_checked:
                selected_resources.append('oxygen_masks')
                supplies.append(f"Oxygen Masks: {oxygen_masks}")
            if catheters_checked and 'catheters' in catheters_checked:
                selected_resources.append('catheters')
                supplies.append(f"Catheters: {catheters}")
            if ventilators_checked and 'ventilators' in ventilators_checked:
                selected_resources.append('ventilators')
                supplies.append(f"Ventilators: {ventilators}")
            if iv_fluids_checked and 'iv_fluids' in iv_fluids_checked:
                selected_resources.append('iv_fluids')
                supplies.append(f"IV Fluids: {iv_fluids}")
            if endotracheal_tubes_checked and 'endotracheal_tubes' in endotracheal_tubes_checked:
                selected_resources.append('endotracheal_tubes')
                supplies.append(f"Endotracheal Tubes: {endotracheal_tubes}")
            
            if selected_resources:
                update_database(selected_resources)
            
            return ', '.join(supplies)
        else:
            return 'Enter values and press submit'



if __name__ == '__main__':
    app.run_server(debug=True)
