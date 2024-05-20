from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.H1("Login"),
    dbc.Form([
        dbc.Row([
            dbc.Col(dbc.Label("Username", html_for="username")),
            dbc.Col(dbc.Input(type="text", id="username", placeholder="Enter your username"))
        ], className="mb-3"),
        dbc.Row([
            dbc.Col(dbc.Label("Password", html_for="password")),
            dbc.Col(dbc.Input(type="password", id="password", placeholder="Enter your password"))
        ], className="mb-3"),
        dbc.Button("Login", id="login-button", color="primary", className="mt-3")
    ])
], className="mt-5")
