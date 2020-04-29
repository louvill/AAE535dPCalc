d = {
    "mass_flow" : {
        "kg/s"  : "1",
        "g/s"   : "0.001",
        "lbm/s" : "0.453592"
    },
    "volumetric_flow" : {
        "m^3/s"  : "1",
        "cm^3/s" : "1/100^3",
        "ft^3/s" : "((2.54*12)/100)^3",
        "GPM"    : "1/15850"
    }
}
save = {
    "massFlow" : {
        "value" : 10,
        "displayName" : "Mass Flow Rate",
        "unit" : "g/s"
        },
    "volumetric_flow" : {
        "value" : 4,
        "displayName" : "Volumetric Flow Rate",
        "unit" : "GPM"
        }
    }
def unitConvert(di):
    # We start by creating a list of all of the 'allowed' terms
    SIUnits = ["m","m^2","Pa","kg/m^3","Pa*s","m^2/s","K","kg/s","m^3/s","m/s","radians"]
    units = d
    for k in di:
        v = di[k]["unit"]
        #print(v)
        if SIUnits.count(v) != 1:
            print("not found")
            for k2 in units.keys():
                if v in units[k2]:
                    print('units',units[k2][v])
                    print(di[k]["value"])
                    di[k]["value"] *= eval(units[k2][v])
                    for v2 in units[k2]:
                        if units[k2][v2] == "1":
                            print(v2)
                            di[k]["unit"] = v2
    return(di)
print(unitConvert(save))

