#Using the alternative method from Issue #7
#
#This function will input the name of the component type and output a full
# dictionary that can then be filled with values for the actual computation
# of the pressure drop. The input can be in lower case, upper case, or a mixture
# and the program should be able to find it. Alternative names are not programmed
# in yet, so be careful with how you type things.
#
#Values that are not required for a component are set to False
# This allows the loop to only require numbers that DON'T have
# False as their value.

#These dictionaries should be able to looped through by doing recursion.
# see recursionExample.py in /bin/ for an example of this.

class A21:
    #First we create the initialization which will take in the 'NAME' input
    def __init__(self,name):
        self.name = name
        #With that defined, we define our component types
        self.componentTypes()
        #And now we run the A21 function
        self.paramList = self.A21func()
    #######################
    # FUNCTION DEFINITION #
    #######################
    def A21func(self):
        self.upperName = str(self.name).upper()
        try:
            parameters = self.cTypes[self.upperName]
        except KeyError:
            raise KeyError("You have not input a valid component type. "+
                           "Look at the documentation to see what names"+
                           " have been assigned to which components.")
        else:
            return(parameters)
    #################
    #COMPONENT TYPES#
    #################
    def componentTypes(self):
        self.cTypes = {
            #LINE DEFINITION
            'LINE': {
              'CID' : 'LNE',
              'geometry' : {
                'length' : 'deltaX',
                'height' : 'deltaZ',
                'insideArea' : 'insideArea',
                'massFlow' : 'mDot',
                'hydraulicDiameter' : 'Dh',
                'bendRadius' : False,
                'bendAngle' : False
              },
              'valve' : {
                'valveCoefficient' : False,
                'specificGravity' : False,
                'valveAuthority' : False
              },
              'misc' : {
                'upstreamArea' : False,
                'downstreamArea' : False,
                'contractionAngledOrCurved' : False,
                'contractionParameters' : {
                    'angle' : False,
                    'downstreamDiameter' : False,
                    'downstreamRadiusOfCurvature' : False
                }
              },
              'fluidProperties' : {
                'density' : 'rho',
                'viscosity' : 'mu',
                'temperature' : 'T'
              },
              'calculated' : {
                'reynolds' : 'rey',
                'frictionFactor' : 'f',
                'ktLosses' : False,
                'pressureDrop' : 'deltaP'
              }
            },
            #BEND DEFINITION
            'BEND': {
              'CID' : 'BND',
              'geometry' : {
                'length' : 'deltaX',
                'height' : 'deltaZ',
                'insideArea' : 'insideArea',
                'massFlow' : 'mDot',
                'hydraulicDiameter' : 'Dh',
                'bendRadius' : 'radius',
                'bendAngle' : 'angle'
              },
              'valve' : {
                'valveCoefficient' : False,
                'specificGravity' : False,
                'valveAuthority' : False
              },
              'misc' : {
                'upstreamArea' : False,
                'downstreamArea' : False,
                'contractionAngledOrCurved' : False,
                'contractionParameters' : {
                    'angle' : False,
                    'downstreamDiameter' : False,
                    'downstreamRadiusOfCurvature' : False
                }
              },
              'fluidProperties' : {
                'density' : 'rho',
                'viscosity' : 'mu',
                'temperature' : 'T'
              },
              'calculated' : {
                'reynolds' : 'rey',
                'frictionFactor' : 'f',
                'ktLosses' : 'kt',
                'pressureDrop' : 'deltaP'
              }
            },
            #VALVE DEFINITION
            'VALVE': {
              'CID' : 'VLV',
              'geometry' : {
                'length' : False,
                'height' : False,
                'insideArea' : False,
                'massFlow' : False,
                'hydraulicDiameter' : False,
                'bendRadius' : False,
                'bendAngle' : False
              },
              'valve' : {
                'valveCoefficient' : 'cValve',
                'specificGravity' : 'rhoSpec',
                'valveAuthority' : 'N'
              },
              'misc' : {
                'upstreamArea' : False,
                'downstreamArea' : False,
                'contractionAngledOrCurved' : False,
                'contractionParameters' : {
                    'angle' : False,
                    'downstreamDiameter' : False,
                    'downstreamRadiusOfCurvature' : False
                }
              },
              'fluidProperties' : {
                'density' : False,
                'viscosity' : False,
                'temperature' : False
              },
              'calculated' : {
                'reynolds' : False,
                'frictionFactor' : False,
                'ktLosses' : False,
                'pressureDrop' : 'deltaP'
              }
            },
            #TUBE SPLIT DEFINITION
            'TUBESPLIT' : {
              'CID' : 'SPL',
              'geometry' : {
                'length' : False,
                'height' : 'deltaZ',
                'insideArea' : 'insideArea',
                'massFlow' : 'mDot',
                'hydraulicDiameter' : 'Dh',
                'bendRadius' : False,
                'bendAngle' : False
              },
              'valve' : {
                'valveCoefficient' : False,
                'specificGravity' : False,
                'valveAuthority' : False
              },
              'misc' : {
                'upstreamArea' : False,
                'downstreamArea' : False,
                'contractionAngledOrCurved' : False,
                'contractionParameters' : {
                    'angle' : False,
                    'downstreamDiameter' : False,
                    'downstreamRadiusOfCurvature' : False
                }
              },
              'fluidProperties' : {
                'density' : 'rho',
                'viscosity' : 'mu',
                'temperature' : 'T'
              },
              'calculated' : {
                'reynolds' : 'rey',
                'frictionFactor' : 'f',
                'ktLosses' : 'kt',
                'pressureDrop' : 'deltaP'
              }
            },
            #TUBE JOIN DEFINITION
            'TUBEJOIN' : {
              'CID' : 'JON',
              'geometry' : {
                'length' : False,
                'height' : 'deltaZ',
                'insideArea' : 'insideArea',
                'massFlow' : 'mDot',
                'hydraulicDiameter' : 'Dh',
                'bendRadius' : False,
                'bendAngle' : False
              },
              'valve' : {
                'valveCoefficient' : False,
                'specificGravity' : False,
                'valveAuthority' : False
              },
              'misc' : {
                'upstreamArea' : False,
                'downstreamArea' : False,
                'contractionAngledOrCurved' : False,
                'contractionParameters' : {
                    'angle' : False,
                    'downstreamDiameter' : False,
                    'downstreamRadiusOfCurvature' : False
                }
              },
              'fluidProperties' : {
                'density' : 'rho',
                'viscosity' : 'mu',
                'temperature' : 'T'
              },
              'calculated' : {
                'reynolds' : 'rey',
                'frictionFactor' : 'f',
                'ktLosses' : 'kt',
                'pressureDrop' : 'deltaP'
              }
            },
            #SUDDEN EXPANSION DEFINITION
            'SUDDENEXPANSION' : {
              'CID' : 'EXP',
              'geometry' : {
                'length' : False,
                'height' : False,
                'insideArea' : False,
                'massFlow' : False,
                'hydraulicDiameter' : False,
                'bendRadius' : False,
                'bendAngle' : False
              },
              'valve' : {
                'valveCoefficient' : False,
                'specificGravity' : False,
                'valveAuthority' : False
              },
              'misc' : {
                'upstreamArea' : 'upsteamArea',
                'downstreamArea' : 'downstreamArea',
                'contractionAngledOrCurved' : False,
                'contractionParameters' : {
                    'angle' : False,
                    'downstreamDiameter' : False,
                    'downstreamRadiusOfCurvature' : False
                }
              },
              'fluidProperties' : {
                'density' : 'rho',
                'viscosity' : 'mu',
                'temperature' : 'T'
              },
              'calculated' : {
                'reynolds' : 'rey',
                'frictionFactor' : 'f',
                'ktLosses' : 'kt',
                'pressureDrop' : 'deltaP'
              }
            },
            #SUDDEN CONTRACTION DEFINITION
            'SUDDENCONTRACTION' : {
              'CID' : 'CON',
              'geometry' : False,
              'valve' : {
                'valveCoefficient' : False,
                'specificGravity' : False,
                'valveAuthority' : False
              },
              'misc' : {
                'upstreamArea' : 'upsteamArea',
                'downstreamArea' : 'downstreamArea',
                'contractionAngledOrCurved' : 'a or c',
                'contractionParameters' : {
                    'angle' : 'contractAngle',
                    'downstreamDiameter' : 'contractDiam',
                    'downstreamRadiusOfCurvature' : 'contractCurvRad'
                }
              },
              'fluidProperties' : {
                'density' : 'rho',
                'viscosity' : 'mu',
                'temperature' : 'T'
              },
              'calculated' : {
                'reynolds' : False,
                'frictionFactor' : False,
                'ktLosses' : False,
                'pressureDrop' : 'deltaP'
              }
            },
            ####################################################################
            #The next three will be odd for calculating pressure drop for them.#
            # They will (probably) not use the typical values herein.          #
            ####################################################################
            #ORIFICE
            'ORIFICE' : {
              'CID' : 'ORF',
              'geometry' : {
                'length' : False,
                'height' : False,
                'insideArea' : False,
                'massFlow' : False,
                'hydraulicDiameter' : False,
                'bendRadius' : False,
                'bendAngle' : False
              },
              'valve' : {
                'valveCoefficient' : False,
                'specificGravity' : False,
                'valveAuthority' : False
              },
              'misc' : {
                'upstreamArea' : False,
                'downstreamArea' : False,
                'contractionAngledOrCurved' : False,
                'contractionParameters' : {
                    'angle' : False,
                    'downstreamDiameter' : False,
                    'downstreamRadiusOfCurvature' : False
                }
              },
              'fluidProperties' : {
                'density' : False,
                'viscosity' : False,
                'temperature' : False
              },
              'calculated' : {
                'reynolds' : False,
                'frictionFactor' : False,
                'ktLosses' : False,
                'pressureDrop' : 'deltaP'
              }
            },
            #INJECTOR
            'INJECTOR' : {
              'CID' : 'INJ',
              'geometry' : {
                'length' : False,
                'height' : False,
                'insideArea' : False,
                'massFlow' : False,
                'hydraulicDiameter' : False,
                'bendRadius' : False,
                'bendAngle' : False
              },
              'valve' : {
                'valveCoefficient' : False,
                'specificGravity' : False,
                'valveAuthority' : False
              },
              'misc' : {
                'upstreamArea' : False,
                'downstreamArea' : False,
                'contractionAngledOrCurved' : False,
                'contractionParameters' : {
                    'angle' : False,
                    'downstreamDiameter' : False,
                    'downstreamRadiusOfCurvature' : False
                }
              },
              'fluidProperties' : {
                'density' : False,
                'viscosity' : False,
                'temperature' : False
              },
              'calculated' : {
                'reynolds' : False,
                'frictionFactor' : False,
                'ktLosses' : False,
                'pressureDrop' : 'deltaP'
              }
            },
            #CATALYST BED
            'CATALYSTBED' : {
              'CID' : 'CAT',
              'geometry' : {
                'length' : False,
                'height' : False,
                'insideArea' : False,
                'massFlow' : False,
                'hydraulicDiameter' : False,
                'bendRadius' : False,
                'bendAngle' : False
              },
              'valve' : {
                'valveCoefficient' : False,
                'specificGravity' : False,
                'valveAuthority' : False
              },
              'misc' : {
                'upstreamArea' : False,
                'downstreamArea' : False,
                'contractionAngledOrCurved' : False,
                'contractionParameters' : {
                    'angle' : False,
                    'downstreamDiameter' : False,
                    'downstreamRadiusOfCurvature' : False
                }
              },
              'fluidProperties' : {
                'density' : False,
                'viscosity' : False,
                'temperature' : False
              },
              'calculated' : {
                'reynolds' : False,
                'frictionFactor' : False,
                'ktLosses' : False,
                'pressureDrop' : 'deltaP'
              }
            },
        }

#Example of this in use. Uncomment to see what happens and try some names out yourself
#print(A21('line').paramList)
