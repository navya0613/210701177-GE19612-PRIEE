import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# Define the admin username and password
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "123"

# Define the layout of the admin login page
layout = dbc.Container([
    html.Div([
        html.Div([
            html.Div([
                html.Img(src="/assets/doctor_consultation.jpg", alt="doctor", style={"height": "350px", "width": "300px", "display": "block", "margin": "0 auto", "padding": "0"})
            ], className="col-md-6 text-center"),  # First column for the image
            html.Div([
                html.H2("Admin Login", style={"text-align": "center"}),
                html.Div([
                    html.Label("Username"),
                    dbc.Input(type="text", id="username", placeholder="Enter your username", className="form-control", style={"width": "100%"}),
                ], className="form-group"),html.Br(),
                html.Div([
                    html.Label("Password"),
                    dbc.Input(type="password", id="password", placeholder="Enter your password", className="form-control", style={"width": "100%"}),
                ], className="form-group"),
                html.Br(),
                html.Div([
                    dbc.Button("Login", id="login-button", color="white", outline=True, className="btn btn-primary btn-block align-items-center justify-content-center text-center color-white",style={"width":"50%"}),  # Removed block=True
                ], style={"text-align": "center", "margin-top": "10px"}),  # Center the button only
                html.Div(id="login-status", style={"margin-top": "10px", "text-align": "center"}),
            ],id="login", className="col-md-6", style={"margin-top": "10px", "background-color": "#e0fbfc", "padding": "20px", "border-radius": "15px", "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)", "margin": "0px"}),  # Second column for the login form
             
        ], className="row align-items-center justify-content-center", style={"background-color": "white", "height": "500px", "margin": "0", "width": "70%", "border": "1px solid black", "border-radius": "25px"}),
    ], className="row align-items-center justify-content-center", style={"background-color": "#66cccc", "padding": "50px", "height": "100vh", "margin": "0"}),
], fluid=True, style={"background-color": "black", "padding": "0"})

def register_callbacks(app):
    @app.callback(
        Output('login-status', 'children'),
        [Input('login-button', 'n_clicks')],
        [State('username', 'value'),
         State('password', 'value')]
    )
    def admin_login(n_clicks, username, password):
        if n_clicks:
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                return dcc.Location(pathname='/option', id='login-redirect')  # Redirect to '/option' if login successful
            else:
                return html.Div("Invalid username or password", style={"color": "red"})  # Display error message



