#Using the alternative method from Issue #7
#def A21Func():
#Values that are not required for a component are set to False
# This allows the loop to only require numbers that DON'T have
# False as their value.

#These dictionaries should be able to looped through by doing recursion.
# see recursionExample.py in /bin/ for an example of this.

cTypes = {
    #LINE DEFINITION
    'line': {
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
    'bend': {
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
    'valve': {
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
    'tubeSplit' : {
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
    'tubeJoin' : {
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
    'suddenExpansion' : {
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
    'suddenContraction' : {
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
    'orifice' : {
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
    'injector' : {
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
    'catalystBed' : {
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
