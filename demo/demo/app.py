import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from database import insert_patient_info
import analysis
import option
import supplies
import resources
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
    else:
        return '404'

# Include URL component
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback for login form submission
@app.callback(
    Output('url', 'pathname'),
    Input('login-button', 'n_clicks'),
    [State('username', 'value'), State('password', 'value')]
)
def handle_login(n_clicks, username, password):
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "123"
    if n_clicks and username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return '/option'
    return '/'

# Callback for patient form submission
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
    return 'Enter all patient information and press submit'

analysis.register_callbacks(app)
option.register_callbacks(app)
supplies.register_callbacks(app)
resources.register_callbacks(app)


if __name__ == '__main__':
    app.run_server(debug=True)
