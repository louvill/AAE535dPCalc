### Line - LNE
 - Inside area

If circle, it can be OD and wall thickness<br>
If other shape, would be easiest to have internal area directly.

 - Mass flow rate
 - Hydraulic diameter
 - Length
 - Height(Altitude) change
#### Fluid Properties
 - Fluid density
 - Fluid viscosity
 - Fluid temperature if being used for density and viscosity

### Bend - BND
Same as LNE but including the following:
 - Bend radius
 - Bend angle
 - Whether it is flat or goes up/down (altitude change)

### Valve - VLV
 - Flow coefficient
 - Specific gravity/density
 - N value (depends on units)

### Tube Split - SPL *AND* Tube Join - JON
 - Inside area

If circle, it can be OD and wall thickness<br>
If other shape, would be easiest to have internal area directly

 - Length
 - Height (Altitude) change
 - Kt loss
 - Mass flow rate
 - Hydraulic diameter
#### Fluid Properties
 - Fluid density
 - Fluid viscosity
 - Fluid temperature if being used for density and viscosity

### Sudden Expansion - EXP
 - Upstream Area
 - Downstream area
#### Fluid Properties
 - Fluid density
 - Fluid viscosity
 - Fluid temperature if being used for density and viscosity

### Sudden Contraction - CON
 - Upstream Area
 - Downstream Area
 - Identifier for angled or curved. This will be either an "a" or a "c" as one of the array elements

If angle, we will need an angle of the contraction.<br>
If curved, we will need the downstream diameter and the radius of curvature<br>

#### Fluid Properties
 - Fluid density
 - Fluid viscosity
 - Fluid temperature if being used for density and viscosity
