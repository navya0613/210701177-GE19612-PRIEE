import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

link_style = {
    'padding': '30px',            # Padding inside the link
    'background-color': '#66b2b2',  # Light blue background color
    'color': '#000000',           # Dark blue text color
    'border-radius': '25px',      # Rounded corners
    'text-decoration': 'none',    # Remove underline
    'cursor': 'pointer',          # Show pointer cursor on hover
    'font-size': '30px',          # Larger font size
    'text-align': 'center',       # Center-align text
    'width': '500px',             # Fixed width for the buttons
    'display': 'block',           # Display as block element
    'margin': '50px',             # Margin around each link for spacing
}

# Define the layout
layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.H1("FOR YOUR EMERGENCY ROOMS", style={'text-align': 'center', 'color': '#000000', 'margin-bottom': '50px'}),  # Center-align the heading
        html.Div([
            html.Div([
                html.A('PATIENT DATA', href='/patient', style=link_style),
                html.A('PATIENT ANALYSIS', href='/analysis', style=link_style),
            ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'center'}),
            html.Div([
                html.A('INVENTORY STATUS', href='/supplies', style=link_style),
                html.A('RESOURCE INPUT', href='/resources', style=link_style),
            ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'center'}),
        ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
    ], style={
        'height': '100vh',
        'width': '100vw',              # Take up 100% of the viewport width
        'background-color': '#F0F8FF',  # Light blue background color
        'display': 'flex',
        'flex-direction': 'column',
        'justify-content': 'center',
        'align-items': 'center',
    })
])

def register_callbacks(app):
# Callback to render different page content based on URL
    @app.callback(
        Output('options', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/patient':
            # Import layout from pageA.py
            from patient import layout as patient_layout
            return patient_layout
        elif pathname == '/analysis':
            # Import layout from pageB.py
            from analysis import layout as analysis_layout
            return analysis_layout
        elif pathname == '/supplies':
            # Import layout from pageC.py
             from supplies import layout as supplies_layout
             return supplies_layout
        elif pathname == '/resources':
             # Import layout from pageD.py
             from resources import layout as resources_layout
             return resources_layout
        # elif pathname == '/pageE':
        #     # Import layout from pageE.py
        #     from pages.pageE import layout as layout_pageE
        #     return layout_pageE
