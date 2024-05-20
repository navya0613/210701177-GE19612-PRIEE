import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Define the header function
def header():
    button_style = {
        'color': '#ffffff',
        'backgroundColor': '#212529',
        'fontWeight': 'bold',
        'fontSize': '16px',
        'padding': '10px 20px',
        'marginRight': '10px',
        'border': 'none',
        'borderRadius': '5px',
        'textDecoration': 'none',
    }
    html.H1()
    buttons = [

        html.A("Patient", href="/patient", style=button_style),
        html.A("Analysis", href="/analysis", style=button_style),
        html.A("Resources", href="/resources", style=button_style),
        html.A("Supplies", href="/supplies", style=button_style),
        html.A("Inventory", href="/inventory", style=button_style),
    ]

    return html.Div(
        children=buttons,
        style={
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
            'padding': '20px',
            'backgroundColor': '#ffffff',  # Deep blue color for header
        }
        
    )

# Define the layout
layout = dbc.Container([
    header(),
    html.Div([
        html.Meta(charSet='UTF-8'),
        html.Meta(name='viewport', content='width=device-width, initial-scale=1'),
    ]),
], style={
    'paddingTop': '20px',  # Add some top padding to the container
    'paddingBottom': '20px',  # Add some bottom padding to the container
})

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Set the app layout
app.layout = layout

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
