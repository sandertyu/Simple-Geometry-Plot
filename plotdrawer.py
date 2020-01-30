import os
import bicycleparameters as bp

### Clunkily draws and saves default plots ###

def draw_plot():
    bike = bp.Bicycle('Benchmark', pathToData=os.getcwd()+"\\data")  # Alter Bicycle name
    bike.add_rider('Jason', reCalc=True)
    plot = bike.plot_bicycle_geometry()
    plot.savefig(os.getcwd()+'\\assets\\user-bikes\\Jason-with-rider.png')  # Alter png name


'''

Error adding Gyro, Rigidcl, Stratos
- "TypeError: slice indices must be integers or None or have an __index__ method"

'''
