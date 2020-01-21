import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import os
import bicycleparameters as bp

###!!!Must ensure that current working directory is set to directory immediatly containing '\data\'!!!###
###---------------------------------------------------------------------------------------------------###

### Initializes Benchmark and draws the geometry plot ###
def draw_plot():
    bike = bp.Bicycle("Benchmark", pathToData=os.getcwd()+"\\data")
    plot = bike.plot_bicycle_geometry()
    plot.savefig('\\assets\\plot.png')
draw_plot()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Benchmark Bicycle Geometry Plot'),
    html.Button("Calculate Geometry Plot",  
                id="plot-button",
                type="button",
                n_clicks=0),
    html.Img(src='/assets/plot.png',  # Why does this work without a file in this location? (It works inconsistently??)
             alt='A plot revealing the general geometry, centers of mass and moments of inertia of the given bicycle system.',
             id="geometry-plot",
             width="640",
             height="480")
])
'''
@app.callback(Output('output-state', 'children'),
              [Input('plot-button', 'n_clicks')],
def update_output(n_clicks):
    return draw_plot()
        format(n_clicks, input1, input2)
'''
if __name__ == '__main__':
    app.run_server(debug=True)
