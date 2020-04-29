## Output from Python file format

Since the function A32 will output a .json file to give all of the pressure drop values back to Electron, this document shows the outline of what the file structure looks like.

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

We may decide to include the other calculated values as output. If such values were desired, one can include them by splicing
```javascript
		  "calculatedValues" : {
		    "dynamicPressure" : "q",
			"reynoldsNumber" : "rey",
			"frictionFactor" : "f",
		  }
```
within each of the component dictionaries and thus have them to call upon in the main Electron UI.