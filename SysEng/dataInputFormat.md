## Finalized Input Data format

The data for the pressure drop calculator will be input in the following manner:


### Python file format
```python
{
  'CID' : CID,
  'geometry' : {
    'length' : deltaX,
	'height' : deltaZ,
	'insideArea' : Ainside,
	'massFlow' : mDot,
	'hydraulicDiameter' : Dh,
	'bendRadius' : radius,
	'bendAngle' : angle
  },
  'valve' : {
    'valveCoefficient' : cValve,
	'specificGravity' : rhoSpec,
	'valveAuthority' : N,
  },
  'misc' : {
    'upstreamArea' : upsteamArea,
	'downstreamArea' : downstreamArea,
	'contractionAngledOrCurved' : 'a or c',
	'contractionParameters' : {
	  'angle' : contractAngle,
	  'downstreamDiameter' : contractDiam,
	  'downstreamRadiusOfCurvature' : contractCurvRad
    }
  },
  'fluidProperties' : {
    'density' = rho,
	'viscosity' = mu,
	'temperature' = T
  },
  'calculated' : {
    'reynolds' : rey,
	'frictionFactor' : f,
	'ktLosses' : kt,
	'pressureDrop' : deltaP
  }
}
```

### .json/JavaScript file format
```javascript
{
  "CID": CID,
  "geometry": [
    {
      "length" : deltaX,
      "height" : deltaZ,
	  "insideArea" : Ainside,
	  "massFlow" : mDot,
	  "hydraulicDiameter" : Dh,
      "bendRadius" : radius,
      "bendAngle" : angle
    }
  ],
  "valve" : {
    "valveCoefficient" : cValve,
	"specificGravity" : rhoSpec,
	"valveAuthority" : N,
  },
  "misc" : [
    {
      "contractExpandUpstream" : upsteamArea,
      "contractExpandDownstream" : downstreamArea,
      "contractionAngledOrCurved" : 'a or c',
      "contractionParameters" : [
        {
          "angle" : contractAngle,
          "downstreamDiameter" : contractDiam,
          "downstreamRadiusOfCurvature" : contractCurvRad
        }
      ]
    }
  ],
  "fluidProperties" : [
    {
      "density" : rho,
      "viscosity" : mu,
      "temperature" : T
    }
  ],
  "calculatedTerms" : [
    {
      "reynoldsNumber" : rey,
      "frictionFactor" : f,
      "ktLosses" : kt,
      "pressureDrop" : deltaP
    }
  ]
}
```

As these components are input, they should be assigned a unique index identification number (IIN) that tells the program which step this is. A parent/child value should also be appended somewhere (look at [issue #7](https://github.com/louvill/AAE535dPCalc/issues/7) for more info)

# .json output format
This last section details how the file type will look when it is output by MAIN.py and sent back to electron to be presented to the user. The 'components' dictionary will output the pressure drop along every single component including their Index Identification Number (IIN) and the Component ID (CID). After all of the components have been output, the final value will be the total pressure drop of the system.

```javascript
{
	"components" : [
	  {
	    "IIN" : IIN1,
		"CID" : CID1,
		"pressureDrop" : deltaP1
	  },
	  {
	    "IIN" : IIN2,
		"CID" : CID2,
		"pressureDrop" : deltaP2
	  }
	  // This will continue for all of the components of the system
	],
	"pressureDropSum" : sumDeltaP
}
```
