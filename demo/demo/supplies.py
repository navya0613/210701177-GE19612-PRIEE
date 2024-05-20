import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.H1("Resource Quantity Form"),
    html.Div([
        html.Label("Beds"),
        dcc.Input(id='beds', type='number', placeholder='Enter quantity'),
        html.Br(),
        html.Label("Nebulizers"),
        dcc.Input(id='nebulizers', type='number', placeholder='Enter quantity'),
        html.Br(),
        html.Label("Oxygen Masks"),
        dcc.Input(id='oxygen-masks', type='number', placeholder='Enter quantity'),
        html.Br(),
        html.Label("Catheters"),
        dcc.Input(id='catheters', type='number', placeholder='Enter quantity'),
        html.Br(),
        html.Label("Ventilators"),
        dcc.Input(id='ventilators', type='number', placeholder='Enter quantity'),
        html.Br(),
        html.Label("IV Fluids"),
        dcc.Input(id='iv-fluids', type='number', placeholder='Enter quantity'),
        html.Br(),
        html.Label("Endotracheal Tubes"),
        dcc.Input(id='endotracheal-tubes', type='number', placeholder='Enter quantity'),
        html.Br(),
        html.Button('Submit', id='submit-val', n_clicks=0),
        html.Br(),
        html.Div(id='supplies', children='Enter values and press submit')
    ])
])
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
        if n_clicks > 0:
            return f"Beds: {beds}, Nebulizers: {nebulizers}, Oxygen Masks: {oxygen_masks}, Catheters: {catheters}, Ventilators: {ventilators}, IV Fluids: {iv_fluids}, Endotracheal Tubes: {endotracheal_tubes}"
        else:
            return 'Enter values and press submit'

