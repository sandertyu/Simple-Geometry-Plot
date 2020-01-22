import os
import bicycleparameters as bp

### Clunkily draws and saves default plots ###

bike = bp.Bicycle("Stratos", pathToData=os.getcwd()+"\\data", forceRawCalc=True)  # Alter Bicycle name
plot = bike.plot_bicycle_geometry()
plot.savefig(os.getcwd()+'\\assets\\defaults\\Stratos.png')  # Alter png name


'''

Error adding Gyro, Rigidcl, Stratos
- "TypeError: slice indices must be integers or None or have an __index__ method"

'''
