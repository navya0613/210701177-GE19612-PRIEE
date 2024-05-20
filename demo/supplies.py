import dash
from dash import dcc
from dash import html
from sqlalchemy import create_engine
from header import header

# Define the database connection
password_encoded = "oviya%401604"  # Password URL encoded
engine = create_engine(f'mysql+mysqlconnector://root:{password_encoded}@localhost:3306/healthcare')

# Sample data (replace this with your actual data)
with engine.connect() as conn:
    query = "SELECT name, total, in_use FROM resource"  # Replace 'your_table' with the actual table name
    healthcare_items = conn.execute(query).fetchall()

# Define the layout of the dashboard
layout = header(), html.Div(style={'backgroundColor': '#ffffff', 'padding': '50px'}, children=[
    html.H1(
        children='Healthcare Inventory Status',
        style={'textAlign': 'center', 'color': '#014F53'}  # White text
    ),
    
    # Display healthcare items using flexbox layout
    html.Div(className='item-container', style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center'}, children=[
        # Loop through healthcare items
        *[html.Div(className='item', style={'width': '25%', 'margin': '10px', 'backgroundColor': '#AEE8EE', 'padding': '20px', 'borderRadius': '10px'}, children=[
            html.H2(item[0], style={'color': '#008080', 'textAlign': 'center'}),  # Dark teal heading
            html.P(f'TOTAL: {item[1]}', style={'fontSize': '18px', 'fontWeight': 'bold', 'textAlign': 'center'}),
            html.P(f'IN USE: {item[2]}', style={'fontSize': '18px', 'fontWeight': 'bold', 'textAlign': 'center'})
        ]) for item in healthcare_items]
 ] )
])

