# PV_TaxShield_Plot.py

Script used to calculate the present value of debt for a financing decision undertaken by a firm. Used to visualize the sensitivity analysis performed for a PV calculation provided a range of at most 3 variables.

## Prerequisites

A number of python libraries are used in these scripts at different points. Please refer to the .py file for specific modules required by each script.
These are mostly from SciPy and commonly available in standard IDEs used in python development

In no specific order:
  + mplot3d
  + matplotlib
  + numpy
  + argparse


### Running the script

E.G.   PV(debt shield) = Tc Rd (debt) / Rdisc   where:
  - Rd      is the debt rate
  - Tc      is the tax rate
  - Rdisc   is the discount rate of the PV calculation

  > NOTE: the script requires at least 1 parameter, and at most 4 to be defined when running the script
  > NOTE: the -f parameter is required, and should be a string equivalent of a python function of x,y,z that can be evaluated e.g. x*y*z  MUST BE LOWERCASE

Example Run:
```
python3 PV_TaxShield_plot.py -x 0.06 0.07 -y 0.4 0.3 -z 0.6 0.8 -f "(x*y*150)/z"
```

In this example we are performing the sensitivity analysis for the PV for the ranges:
- Rd      6% - 7%
- Tc      30% - 40%
- Rdisc   6% - 8%



### Sample Output:
![alt text](https://raw.githubusercontent.com/morendav/Corporate_Finance/master/PV_TaxShield/samples/PV_CorpTaxShield.png)


## Version

### V 1.01
  + 3 intake variable parameters with defaults included
  + output graph with interaction enabled
  + single color scale for all plots on same graph
