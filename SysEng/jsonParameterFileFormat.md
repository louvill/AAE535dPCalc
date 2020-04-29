## File structure for components.
The file components will have the following data structure. This data structure is a general format. Any parameter that is not required for a given calculation (such as valve coefficient not be necessary for a line calculation) will not be included in as part of the .json definitions. This is the exhaustive list of EVERYTHING that might go into an input or output file and no .json or python dictionary should include all of these things.

Notation:
 - IIN : Index Identification Number
 - CID : Component Identification Number
 - parent : The component IIN that is directly upstream of this component
 - child : The component IIN that is directly downstream of this component
 - values : All of the values that are needed for pressure drop calculation, including the pressure drop itself.
 
 As these components are input, they will be assigned a unique index identification number (IIN) that tells the program where in relation to the other parts a component is located. A parent/child value is also included for future work with joins and splits. (look at [issue #7](https://github.com/louvill/AAE535dPCalc/issues/7) for more info)

```python
{
  "SHORT NAME" : {
    "IIN" : "IIN",
    "CID" : "CID",
	"displayName" : "LONGER NAME",
	"parent" : "something",
	"child" : "something",
	"values" : {
	  "component" : {
	    "length" : {
		  "value" : null,
		  "displayName" : "Length measured from the center line",
		  "unit" : "distance"
		},
	    "height" : {
		  "value" : null,
		  "displayName" : "Height Change",
		  "unit" : "distance"
		},
	    "insideArea" : {
		  "value" : null,
		  "displayName" : "Inside Area of the Pipe",
		  "unit" : "area"
		},
	    "massFlow" : {
		  "value" : null,
		  "displayName" : "Fluid Mass Flow",
		  "unit" : "massFlow"
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
        "valveCoefficient" : {
		  "value" : null,
		  "displayName" : "Valve Coefficient (Cv)",
		  "unit" : null
		},
	    "specificGravity" : {
		  "value" : null,
		  "displayName" : "Specific Gravity of the Fluid",
		  "unit" : null
		},
	    "valveAuthority" : {
		  "value" : null,
		  "displayName" : "Valve Authority (N)",
		  "unit" : null
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
		  "unit" : "mass/volume"
		},
        "viscosity" : {
		  "value" : null,
		  "displayName" : "Fluid Viscosity",
		  "unit" : "pressure*time"
		}
	  },
	  "calc" : {
	    "dynamicPressure" : {
		  "value" : null,
		  "displayName" : "Dynamic Pressure",
		  "unit" : "pressure"
		},
        "reynoldsNumber" : {
		  "value" : null,
		  "displayName" : "Reynolds Number",
		  "unit" : null
		},
        "frictionFactor" : {
		  "value" : 0,
		  "displayName" : "Friction Factor",
		  "unit" : null
		},
        "ktLosses" : {
		  "value" : null,
		  "displayName" : "kt Losses",
		  "unit" : null
		},
        "pressureDrop" : {
		  "value" : null,
		  "displayName" : "Component Pressure Drop",
		  "unit" : "pressure"
		}
	  }
	}
  }
}
```
