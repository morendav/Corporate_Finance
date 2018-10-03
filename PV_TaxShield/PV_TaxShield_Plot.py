#######################################
# Plot 3d plot for 2 dependent variables
#   Sensitivity analysis for 3 variable plot
#
# Options (parameters)
#       -x  x array bounds in space delimited format: min max
#       -y  y array bounds in space delimited format: min max
#       -z  z array bounds in space delimited format: min max
#       -f  string representing the function of x and y and z's depenedence on those variables
#
# Example:
#       python3 taxRate_Plot.py -x 0.06 0.07 -y 0.4 0.3 -z 0.06 0.07 -f "(x*y*150000)/z"
#       Calculate tax shield PV based on x (debt rate), y (tax rate) and z (discount rate for future debt holding) for a debt holding of 150M USD
#           Tax = 30-40%    dRate = 0.06-0.07   zDiscRate = 0.06-0.07
#
#######################################
###     CodeBlock: Modules &  Init Var
#######################################
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser

### Read passed arguements from the command line
# x, y and z are space delimited array bounds. z - handling tbd
parser = ArgumentParser(
    description='plot 3d function x array by y array against z axis based on function passed in f as string. f must by a pythonic expression containing the dependent variables',
    epilog="Example:\r./script.py -x 1 10 -y 1 10 -z 1 10 -f 'x*z*y'\r")
parser.add_argument("-x", "--x_Array", dest="xArray", help="x array bounds in space delimited format: min max", nargs="+", default=[1,1], metavar="min max", type=float)
parser.add_argument("-y", "--y_Array", dest="yArray", help="y array bounds in space delimited format: min max", nargs="+", default=[1,1], metavar="min max", type=float)
parser.add_argument("-z", "--z_Array", dest="zArray", help="z array bounds in space delimited format: min max", nargs="+", default=[1,1], metavar="min max", type=float)
parser.add_argument("-f", "--function", dest="funct", help="string function representing the dependency of z based on x and y", metavar="'f(x,y)''", type=str)
args = parser.parse_args()
x_bound=args.xArray
y_bound=args.yArray
z_bound=args.zArray
f=args.funct


#######################################
###     CodeBlock: 3d Variable definition
#######################################
# create arrays for coorindates in cartesian space
x_array = np.linspace(x_bound[0],x_bound[1],100)
y_array = np.linspace(y_bound[0],y_bound[1],100)
z_array = np.linspace(z_bound[0],z_bound[1],6)
# create independent variable mesh grid (ie 2d plane representing x plane and y plane, respective to axis
x, y = np.meshgrid( x_array, y_array )
f_xyz={}


#######################################
###     CodeBlock: 3d Visualization of z=f(x y)
#######################################
# create plot object
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# evaluate dependent variable function(xyz) against x and y and z arrays iteratively
it=len(z_array)-1
for z in z_array:
    f_xyz[it] =  eval(f)
    ax.plot_surface(x, y, f_xyz[it], rstride=10, cstride=10, cmap=cm.viridis)
    it=it-1
# ax.plot_surface(x, y, fxyz, rstride=10, cstride=10, cmap=cm.viridis)
# ax.contour3D(x, y, z, 50, cmap='binary')

plt.show()
