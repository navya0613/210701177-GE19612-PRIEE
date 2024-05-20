import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc


link_style = {
    'padding': '15px 20px',     # Padding inside the link
    'margin': '10px',           # Margin around the link
    'background-color': '#9ACCCD',  # Light teal background color
    'color': '#1E3C72',         # Dark blue text color
    'border-radius': '10px',    # Rounded corners
    'text-decoration': 'none',  # Remove underline
    'display': 'inline-block',  # Display as block element
    'font-weight': 'bold',      # Bold text
    'cursor': 'pointer',        # Show pointer cursor on hover
    'font-size': '20px',        # Larger font size
    'text-align': 'center',     # Center-align text
    'width': '200px',           # Fixed width for the buttons
}


layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.H1("Main Page", style={'text-align': 'center'}),  # Center-align the heading
        html.Div([
            html.A('Input Patient Data', href='/patient', style=link_style),
            html.Br(),
            html.A('Patient Analysis', href='/analysis', style=link_style),
            html.Br(),
            html.A('Supplies', href='/supplies', style=link_style),
            html.Br(),
            html.A('Input Resources', href='/resources', style=link_style),
            html.Br(),
            # html.A('Go to Page E', href='/pageE', style=link_style),
        ], style={'text-align': 'center', 'margin-top': '50px'}),  # Center-align and add top margin
        html.Div(id='options')  # Placeholder for page content
    ], style={
        'display': 'flex', 
        'flex-direction': 'column', 
        'align-items': 'center', 
        'height': '100vh',
        'width': '100vw',              # Take up 100% of the viewport width
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
