import dash
import dash_core_components as dcc
import dash_html_components as html

import os
import bicycleparameters as bp

def draw_plot():
    os.chdir("C:\\Users\\xyzasdf\\Desktop\\bike-lab\\BicycleParameters-master\\data")
   
    bike = bp.Bicycle("Benchmark")
    plot = bike.plot_bicycle_geometry()

    os.chdir('C:\\Users\\xyzasdf\\Desktop\\bike-lab\\test-code\\geo-plot-app\\assets')
    plot.savefig('plot.png')

draw_plot

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Benchmark Bicycle Geometry Plot'), html.Img(src='/assets/plot.png')
])

if __name__ == '__main__':
    app.run_server(debug=True)
