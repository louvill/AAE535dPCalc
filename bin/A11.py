"""
This class acts as a read-file. No computations will actually be completed here.
Rather, this class will store all of the required parameters that each
component type needs in order for the pressure drop to be calculated. This will
only output the "values" dictionary and nothing else. All other parts of the dictionary
(e.g. the IIN, CID, parent, child) must be specified elsewhere.

It should be noted that although we have included several different component
types here, not all of them may necessarily be implemented.

As of writing this (April 28 2020) here is the progress.
Fully tested:
 - Line
 - Bend
Implemented, but not fully tested:
 - Sudden Expansion
 - Sudden Contraction
 - Angled Contraction

All other components are not implemented at this time.
"""


class A11:
    
    # First we initialize the class since we will be inputting the name of the component
    def __init__(self,name):
        self.name = name
        # stored below we have all of the values necessary for each componenet defined in a function.
        self.componentValues()
        # And now we assign the values based on the name input
        self.valDict = self.A11func()
        # With that value defined, anything calling this class now has access to all of the
        # required information that needs to be input by the user.

    # Function Definition
    def A11func(self):
        # To ensure non-case sensitivity, we first change the input string to upper case
        self.upperName = str(self.name).upper()
        # We then see if the name is in our database and if not then give an error message
        try:
            parameters = self.cTypes[self.upperName]
        except KeyError:
            raise KeyError("You have either not input a valid component type "+
                           "or you have input a component type not yet implemented. "+
                           "Look at the documentation to see what names "+
                           "have been assigned to which components.")
        else:
            return(parameters)

    # Component Types
    def componentValues():
        self.cTypes = {
            # Line Definition
            "LINE" : {
                "component" : {
                    "length" : {
                        "value" : null,
                        "displayName" : "Length measured from the center line",
                        "unit" : "length"
                        },
                    "height" : {
                        "value" : null,
                        "displayName" : "Height Change",
                        "unit" : "length"
                        },
                    "insideArea" : {
                        "value" : null,
                        "displayName" : "Inside Area of the Pipe",
                        "unit" : "area"
                        },
                    "massFlow" : {
                        "value" : null,
                        "displayName" : "Fluid Mass Flow",
                        "unit" : "mass_flow"
                        },
                    "hydraulicDiameter" : {
                        "value" : null,
                        "displayName" : "Hydraulic Diameter",
                        "unit" : "length"
                        }
                    },
                "fluid" : {
                    "density" : {
                        "value" : null,
                        "displayName" : "Fluid Density",
                        "unit" : "density"
                        },
                    "viscosity" : {
                        "value" : null,
                        "displayName" : "Fluid Viscosity",
                        "unit" : "viscosity_dynamic"
                        }
                    }
                },
            # Bend Definition
            "BEND" : {
                "component" : {
                    "length" : {
                            "value" : null,
                            "displayName" : "Length measured from the center line",
                            "unit" : "length"
                            },
                    "height" : {
                            "value" : null,
                            "displayName" : "Height Change",
                            "unit" : "length"
                            },
                    "insideArea" : {
                            "value" : null,
                            "displayName" : "Inside Area of the Pipe",
                            "unit" : "area"
                            },
                    "massFlow" : {
                            "value" : null,
                            "displayName" : "Fluid Mass Flow",
                            "unit" : "mass_flow"
                            },
                    "hydraulicDiameter" : {
                            "value" : null,
                            "displayName" : "Hydraulic Diameter",
                            "unit" : "length"
                            },
                    "bendRadius" : {
                            "value" : null,
                            "displayName" : "Radius of Curvature of the Bend",
                            "unit" : "distance"
                            },
                    "bendAngle" : {
                            "value" : null,
                            "displayName" : "Angle of the Bend",
                            "unit" : "angle"
                            },
                    },
                "fluid" : {
                    "density" : {
                            "value" : null,
                            "displayName" : "Fluid Density",
                            "unit" : "density"
                            },
                    "viscosity" : {
                            "value" : null,
                            "displayName" : "Fluid Viscosity",
                            "unit" : "viscosity_dynamic"
                            }
                    }
                },
            # Sudden Expansion Definition
            "EXPANSION" : {
                "component" : {
                    "massFlow" : {
                            "value" : null,
                            "displayName" : "Fluid Mass Flow",
                            "unit" : "mass_flow"
                            },
                    "hydraulicDiameter" : {
                            "value" : null,
                            "displayName" : "Hydraulic Diameter",
                            "unit" : "length"
                            },
                    "contractExpandUpstream" : {
                            "value" : null,
                            "displayName" : "Upstrem Area",
                            "unit" : "area"
                            },
                    "contractExpandDownstream" : {
                            "value" : null,
                            "displayName" : "Downstream Area",
                            "unit" : "area"
                            }
                    },
            "fluid" : {
                "density" : {
                        "value" : null,
                        "displayName" : "Fluid Density",
                        "unit" : "density"
                        },
                "viscosity" : {
                        "value" : null,
                        "displayName" : "Fluid Viscosity",
                        "unit" : "viscosity_dynamic"
                        }
                }
            },
            # Contraction Definition
            "CONTRACTION" : {
                "component" : {
                    "massFlow" : {
                            "value" : null,
                            "displayName" : "Fluid Mass Flow",
                            "unit" : "mass_flow"
                            },
                    "hydraulicDiameter" : {
                            "value" : null,
                            "displayName" : "Hydraulic Diameter",
                            "unit" : "length"
                            },
                    "contractExpandUpstream" : {
                            "value" : null,
                            "displayName" : "Upstrem Area",
                            "unit" : "area"
                            },
                    "contractExpandDownstream" : {
                            "value" : null,
                            "displayName" : "Downstream Area",
                            "unit" : "area"
                            },
                    "contractionAngledOrCurved" : {
                            "value" : null,
                            "displayName" : "Is the contraction angled or curved?",
                            "unit" : "string"
                            },
                    "angle" : {
                            "value" : null,
                            "displayName" : "Double angle of Contraction",
                            "unit" : "angle"
                            },
                    "contractionLength" : {
                            "value" : null,
                            "displayName" : "Centerline Length of Contraction",
                            "unit" : "length"
                            },
                    "downstreamRadiusOfCurvature" : {
                            "value" : null,
                            "displayName" : "Contraction Radius of Curvature",
                            "unit" : "length"
                            }
                    },
                "fluid" : {
                    "density" : {
                            "value" : null,
                            "displayName" : "Fluid Density",
                            "unit" : "density"
                            },
                    "viscosity" : {
                            "value" : null,
                            "displayName" : "Fluid Viscosity",
                            "unit" : "viscosity_dynamic"
                            }
                    }
                }
            }
