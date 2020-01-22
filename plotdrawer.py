import os
import bicycleparameters as bp

### Clunkily draws and saves default plots ###

def draw_plot(bike_data):
    bike = bp.Bicycle(bike_data, pathToData=os.getcwd()+"\\data")  # Alter Bicycle name
    plot = bike.plot_bicycle_geometry()
    plot.savefig(os.getcwd()+'\\assets\\user-bikes\\'+bike_data+'.png')  # Alter png name


'''

Error adding Gyro, Rigidcl, Stratos
- "TypeError: slice indices must be integers or None or have an __index__ method"

'''
