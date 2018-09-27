# Corporate Finance Python Library

Scripted solutions used in my MBA for corporate finance, and securities related courses.


## Description

Personal playground to attempt our homework problems in python as opposed to Excel. These are not assignement answers nor do I advocate using them for solving homework problems. They are purely educational and entertainment of my own devices.


## Prerequisites

A number of python libraries are used in these scripts at different points. Please refer to the .py file for specific modules required by each script.
These are mostly from SciPy and commonly available in standard IDEs used in python development

In no specific order:
  + mplot3d
  + matplotlib
  + numpy
  + argparse


## Corporate Finance Suite

This section will detail each of the scripts and their common corporate finance applications & potentially other translational uses.


### PV_TaxShield_Plot.py

Script used to calculate the present value of debt for a financing decision undertaken by a firm. Used to visualize the sensitivity analysis performed for a PV calculation provided a range of at most 3 variables.

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

Output:
![alt text](https://raw.githubusercontent.com/morendav/Corporate_Finance/master/samples/PV_CorpTaxShield.png)


### More to come...
