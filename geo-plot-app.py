import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import os
import bicycleparameters as bp

###!!!Must ensure that current working directory is set to directory immediatly containing '\data\'!!!###
###---------------------------------------------------------------------------------------------------###

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Bicycle Geometry Plot'),
    dcc.Dropdown(id="bike-dropdown",
                 options=[{'label': 'Benchmark', 'value': 'Benchmark'},
                          {'label': 'Browser', 'value': 'Browser'},
                          {'label': 'Browserins', 'value': 'Browserins'},
                          {'label': 'Crescendo', 'value': 'Crescendo'},
                          {'label': 'Fisher', 'value': 'Fisher'},
                          {'label': 'Pista', 'value': 'Pista'},
                          {'label': 'Rigid', 'value': 'Rigid'},
                          {'label': 'Silver', 'value': 'Silver'},
                          {'label': 'Tms', 'value': 'Tms'},
                          {'label': 'Yellow', 'value': 'Yellow'},
                          {'label': 'Yellowrev', 'value': 'Yellowrev'}],
                 value='Benchmark') , 
    html.Img(src='',  
             alt='A plot revealing the general geometry, centers of mass and moments of inertia of the given bicycle system.',
             id="geometry-plot",
             width="640",
             height="480"),
])

    # Updates image path with dropdown value
@app.callback(Output('geometry-plot', 'src'), [Input('bike-dropdown', 'value')])
def reveal_plot(value):
    image = str(value)+'.png'
    path = '/assets/defaults/'+image
    return path

if __name__ == '__main__':
    app.run_server(debug=True)

#(For safe keeping)
''' 
html.Button("Calculate Geometry Plot",  
                id="calculate-button",
                type="button",
                n_clicks=0),
'''

'''
### Initializes Benchmark and draws the geometry plot ###
def new_plot():
    bike = bp.Bicycle("Benchmark", pathToData=os.getcwd()+"\\data")
    plot = bike.plot_bicycle_geometry()
    plot.savefig(os.getcwd()+'\\assets\\plot.png')
'''

'''
    # Change to add to list of plots, but not actually show it
@app.callback(Output('geometry-plot', 'src'), [Input('calculate-button', 'n_clicks')])
def calculate_geo_plot(n_clicks):
    return draw_plot()
'''