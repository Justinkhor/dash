from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import requests
import random
from PIL import Image
from io import BytesIO

# List of image names
images = ["fire", "insta", "tesla"]

# Configurations for the dcc Graph
config = {
    "modeBarButtonsToAdd": [
        "drawline",
        "drawopenpath",
        "drawclosedpath",
        "drawcircle",
        "drawrect",
        "eraseshape",
    ]
}

# Create Dash application
app = Dash(__name__)

# Add the layout for the application
app.layout = html.Div([
    html.H3("Obtain PNG Image via HTTP Request", style={'font-family':'Verdana'}),
    html.Button('Generate Image', id='generate', n_clicks=0), 
    dcc.Graph(id='output', config=config)   
])

@app.callback(
    Output('output', 'figure'),
    Input('generate', 'n_clicks')
)

def update_output(n_clicks):

    # Randomly choose one image
    img = random.choice(images)
    site = 'https://raw.githubusercontent.com/Justinkhor/dash/main/images/' + img + '.png'

    # Use HTTP requests to obtain PNG image
    req = requests.get(site)

    # Retrieve image file
    img = Image.open(BytesIO(req.content))

    fig = px.imshow(img)
    fig.update_layout(dragmode="drawrect")

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
