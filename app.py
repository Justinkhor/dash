from dash import Dash, html, dcc
import requests
import plotly.express as px
from PIL import Image
from io import BytesIO

# Use HTTP requests to obtain PNG image (Change this line to other images)
x = requests.get('https://raw.githubusercontent.com/Justinkhor/dash/main/images/fire.png')

# Retrieve image file
img = Image.open(BytesIO(x.content))

# Create the figure
fig = px.imshow(img)
fig.update_layout(dragmode="drawrect")

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
app.layout = html.Div(
    [html.H3("Obtain PNG Image via HTTP Request", style={'font-family':'Verdana'}), dcc.Graph(figure=fig, config=config),]
)

if __name__ == '__main__':
    app.run_server(debug=True)
