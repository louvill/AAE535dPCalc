"""
The A22 file acts as a unit conversion tool for the Pressure Drop Calculator.
Since the units are defined by the user in the Electron front end, this method
will input parameters in all sorts of units and output parameters in the
required SI units for calculation.

One required library for this method is units.json (since that dictionary holds
all of the required conversion factors).

To convert from the non-SI unit to SI, multiply by the element of that dictionary
key. To convert from SI to non-SI, divide by the element.
"""

import math
import json
import os


class A22:
    
    # Initialization will take in the dictionary of values
    def __init__(self,d):
        # Define a local variable
        self.dict = d
        # Define the component values
        self.val = self.dict["values"]
        # We need the unit conversion json. First we find where it is located
        path_to_json = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..',
                                    'lib',
                                    'units.json'
                                    )
        # And then we open it an input it as a python dictionary
        with open(path_to_json) as f:
            self.units = json.load(f)

        #### EVALUATION OF EACH CELL ####
        # we need to eval each cell since they are input as strings
        self.evaluation()
        # Redefine dictionary
        self.dict["values"] = self.val
        
        
        # With our conversion ratios defined and the values now actual values,
        # we can run through the input dictionary and convert all of the input
        # values into the required SI units for future functions.
        self.unitConvert()

    # EVALUATION FUNCTION
    def evaluation(self):
        for k1 in self.val.keys():
            for k2 in self.val[k1].keys():
                # We evaluate the string located in the "value" key of each
                # parameter.
                self.val[k1][k2]["value"] = eval(self.val[k1][k2]["value"])

    # UNIT CONVERSION FUNCTION
    def unitConvert(self):
        # We start by creating a list of all of the 'allowed' terms
        SIUnits = ["m","m^2","Pa","kg/m^3","Pa*s","m^2/s","K","kg/s",
                   "m^3/s","m/s","radians"]
        # Because of the way this was tested, and due to time restrictions
        # we need to 'define' local variables to the tested version works
        di = self.val
        units = self.units
        for k1 in di:
            for k2 in di[k1]:
                #print(k2)
                u = di[k1][k2]["unit"]
                #print('u',u)
                if SIUnits.count(u) != 1:
                    #print("This is not an SI unit")
                    for k3 in units.keys():
                        #print("type of unit:",k3)
                        if u in units[k3]:
                            if k3 == "temperature":
                                #print('unit conversion factor',units[k3][u])
                                #print(di[k1][k2]["value"])
                                #print("temp Array",units[k3][u])
                                di[k1][k2]["value"] *= eval(units[k3][u][0])
                                di[k1][k2]["value"] += eval(units[k3][u][1])
                                for v2 in units[k3]:
                                    if units[k3][v2] == "1":
                                        print(v2)
                                        di[k1][k2]["unit"] = v2
                            else:
                                #print('unit conversion factor',units[k3][u])
                                #print(di[k1][k2]["value"])
                                di[k1][k2]["value"] *= eval(units[k3][u])
                                for v2 in units[k3]:
                                    if units[k3][v2] == "1":
                                        #print(v2)
                                        di[k1][k2]["unit"] = v2
        return(di)
