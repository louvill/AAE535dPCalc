## Finalized Input Data format

The data for the pressure drop calculator will be input in the following stucture:

### Python file format
```python
[
  CID, 
  ['deltaX', 'deltaZ','radius','angle'],
  ['insideArea','massFlow','D_h'],
  ['valveCoefficient','specificGravity','N'],
  ['upstreamArea','downstreamArea','contractionType (a or c)',['contractionParameters']]
  ['rho', 'mu', 'T'],
  ['rey', 'f','kt', 'deltaP']
]
```

### .json/JavaScript file format
```javascript
{
  "componentID": CID,
  "distanceValues": [
    {
      "lengthChange" : deltaX,
      "altitudeChange" : deltaZ,
      "bendRadius" : radius,
      "bendAngle" : angle
    }
  ],
  "miscInfo" : [
    {
      "valveCoefficient" : valveCoefficient,
      "contractExpandUpstream" : upsteamArea,
      "contractExpandDownstream" : downstreamArea,
      "contractionAngledOrCurved" : expandType,
      "contractionParameters" : [
        {
          "angle" : contractAngle,
          "downstreamDiameter" : contractDiameter,
          "downstreamRadiusOfCurvature" : contractRadius
        }
      ]
    }
  ],
  "fluidProperties" : [
    {
      "fluidDensity" : rho,
      "fluidViscosity" : mu,
      "fluidTemperature" : T
    }
  ],
  "calculatedTerms" : [
    {
      "reynoldsNumber" : rey,
      "frictionFactor" : f,
      "ktLosses" : kt,
      "pressureLoss" : deltaP
    }
  ]
}
```

As these components are input, they should be assigned a unique index identification number (IIN) that tells the program which step this is. A parent/child value should also be appended somewhere (look at [issue #7](https://github.com/louvill/AAE535dPCalc/issues/7) for more info)