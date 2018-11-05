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
import matplotlib

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





def cmap_map(function, cmap):
    """ Applies function (which should operate on vectors of shape 3: [r, g, b]), on colormap cmap.
    This routine will break any discontinuous points in a colormap.
    """
    cdict = cmap._segmentdata
    step_dict = {}
    # First get the list of points where the segments start or end
    for key in ('red', 'green', 'blue'):
        step_dict[key] = list(map(lambda x: x[0], cdict[key]))
    step_list = sum(step_dict.values(), [])
    step_list = np.array(list(set(step_list)))
    # Then compute the LUT, and apply the function to the LUT
    reduced_cmap = lambda step : np.array(cmap(step)[0:3])
    old_LUT = np.array(list(map(reduced_cmap, step_list)))
    new_LUT = np.array(list(map(function, old_LUT)))
    # Now try to make a minimal segment definition of the new LUT
    cdict = {}
    for i, key in enumerate(['red','green','blue']):
        this_cdict = {}
        for j, step in enumerate(step_list):
            if step in step_dict[key]:
                this_cdict[step] = new_LUT[j, i]
            elif new_LUT[j,i] != old_LUT[j, i]:
                this_cdict[step] = new_LUT[j, i]
        colorvector = list(map(lambda x: x + (x[1], ), this_cdict.items()))
        colorvector.sort()
        cdict[key] = colorvector

    return matplotlib.colors.LinearSegmentedColormap('colormap',cdict,1024)
### Change the colormap per iteration


#######################################
###     CodeBlock: 3d Variable definition
#######################################
# create arrays for coorindates in cartesian space
x_array = np.linspace(x_bound[0],x_bound[1],100)
y_array = np.linspace(y_bound[0],y_bound[1],100)
z_array = np.linspace(z_bound[0],z_bound[1],12)
z_array.sort() # sort the z array to make hte normalization make sense
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
for ind,z in zip(range(0,len(z_array)), z_array):
    f_xyz[ind] =  eval(f)
    colorMap = cmap_map(lambda x: (x/2 + (0.5-0.1*ind)), matplotlib.cm.jet)
    ax.plot_surface(x, y, f_xyz[ind], rstride=10, cstride=10, cmap=colorMap)

print(z_array)
plt.show()
