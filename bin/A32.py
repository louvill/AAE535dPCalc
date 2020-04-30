"""
The A32 function will sum up the pressure drop for each component and
then create a new dictionary for the pressure drop sum and each pressure
drop of each component. 
"""



class A32:
    def __init__(self,pDropArray,fullComponentList):
        # Set local variables for ease of access
        self.pDrops = pDropArray
        self.cList = fullComponentList
        # The only reason for including a pDrops array. Making the sum WAY easier
        self.pDropSum = sum(self.pDrops)
        # Create a dictionary that we will fill with values
        self.output = {
            "components" : [],
            "pressureDropSum" : {
                "value" : self.pDropSum,
                "displayName" : "Total Pressure Drop",
                "unit" : "Pa"
                }
            }
        # And now we run through our components to build the dictionary
        self.A32Func()

    # This sub function loops through all of the components and builds the output file
    def A32Func(self):
        for i in range(len(self.pDrops)):
            # To start, we want to convert the current index into a string
            # that we can look up in the component list dictionary. To this
            # end, we make sure the index we're on is of the proper length
            # with the proper format
            self.indexWrite(i)
            # With the index defined, we can pull the required info as detailed
            # in /SysEng/jsonOutputFileFormat.md
            IIN = self.cList[i]["IIN"]
            CID = self.cList[i]["CID"]
            pDrop = self.cList[i]["values"]["calculated"]["pressureDrop"]
            self.output["components"].append({
                "IIN" : IIN,
                "CID" : CID,
                "pressureDrop" : {
                    "value" : pDrop["value"],
                    "displayName" : "Pressure Drop Across Component "+str(IIN),
                    "unit" : pDrop["unit"]
                    }
                })
        return(None)
                                    
    # Get the IIN of the component
    def indexWrite(self,i):
        if len(str(i+1)) == 1:
            self.index = "00"+str(i+1)
        elif len(str(i)) == 2:
            self.index = "0"+str(i+1)
        elif len(str(i)) == 3:
            self.index = str(i+1)
        else:
            raise OverflowError("There are more than 999 components in"
                                + " your fluid system. You will need to"
                                + " enhace this software or use a different"
                                + " program in order to have that many"
                                + " components in your system")
        return(None)
    
    
