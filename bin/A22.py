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
    def __init__(self,dict):
        #(but also check to see if the entire dictionary was given by accident)
        try:
            self.CID = dict["CID"]
        except:
            self.dict = dict
        else:
            self.dict = dict["values"]
        # We need the unit conversion json. First we find where it is located
        path_to_json = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..',
                                    'lib',
                                    'units.json'
                                    )
        # And then we open it an input it as a python dictionary
        with open(path_to_json) as f:
            data = json.load(f)
        # With our conversion ratios defined, we can run through the input dictionary
        # and convert all of the input values into the required SI units for future
        # functions.
        self.unitConvert()
    def unitConvert(self):
        # We start by creating a list of all of the 'allowed' terms
        SIUnits = ["m","m^2","Pa","kg/m^3","Pa*s","m^2/s","K","kg/s","m^3/s","m/s","radians"]
        for k,v in self.dict["component"].items():
            if SIUnits.count(self.dict["component"][k]["unit"]) == 1:
                continue
            else:
                self.dict["component"][k]["value"] *= 
