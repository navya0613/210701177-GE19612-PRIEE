import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import analysis
import option
import login
import resources
import patient
import inventory
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
server = app.server

app.layout = html.Div(id='page-content', children=[])

# Define the callback to update the page content
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        from login import layout as login_layout
        return login_layout
    elif pathname == '/option':
        from option import layout as option_layout
        return option_layout
    elif pathname == '/patient':
        from patient import layout as patient_layout
        return patient_layout
    elif pathname == '/analysis':
        from analysis import layout as analysis_layout
        return analysis_layout
    elif pathname == '/supplies':
        from supplies import layout as supplies_layout
        return supplies_layout
    elif pathname == '/resources':
        from resources import layout as resources_layout
        return resources_layout
    elif pathname == '/inventory':
        from inventory import layout as inventory_layout
        return inventory_layout
    else:
        return '404'

# Include URL component
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


login.register_callbacks(app)
patient.register_callbacks(app)
analysis.register_callbacks(app)
option.register_callbacks(app)
resources.register_callbacks(app)
inventory.register_callbacks(app)


if __name__ == '__main__':
    app.run_server(debug=True)
