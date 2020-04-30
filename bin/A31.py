"""
Subfunction A31 is responsible for inputting the component parameters
and then using the information about the component to determine
the pressure drop across that component
----------------------------------------------------------
Using data structure from /SysEng/jsonParameterFileFormat/ recall that each
cell is only present if there is data stored and thus
we can call "if "parameterName" in dict.keys()" to see if it is there.
"""

#Need math function
import math


class A31:
    def __init__(self,dict): #dict is for dictionary
        self.dict = dict
        #Now we set several new local variables for ease of calling them later
        self.CID = self.dict["CID"]
        self.val = self.dict["values"]
        self.calc = self.val["calculated"]
        self.comp = self.val["component"]
        self.fluid = self.val["fluid"]
        # Create a new key for the pressure drop
        self.calc["pressureDrop"] = {}
        #We also need to define 'g' for this method (in SI)
        self.g = 9.81 
        #
        #Set up the logic tree to see what we need to do
        #
        #This method of finding the pressure drop for each different type
        # of component is WAY underoptimized. Feel free to improve it! :)
        if self.CID == 'LNE':
            self.calc['pressureDrop']["value"] = self.lineCalc()
        elif self.CID == 'BND':
            self.calc['pressureDrop']["value"] = self.bendCalc()
        elif self.CID == 'VLV':
            self.calc['pressureDrop']["value"] = False
        elif self.CID == 'ORF':
            self.calc['pressureDrop']["value"] = False
        elif self.CID == 'INJ':
            self.calc['pressureDrop']["value"] = False
        elif self.CID == 'CAT':
            self.calc['pressureDrop']["value"] = False
        elif self.CID == 'BND':
            self.calc['pressureDrop']["value"] = False
        elif self.CID == 'SPL':
            self.calc['pressureDrop']["value"] = False
        elif self.CID == 'JON':
            self.calc['pressureDrop']["value"] = False
        elif self.CID == 'EXP':
            self.calc['pressureDrop']["value"] = self.expansionCalc()
        elif self.CID == 'CON':
            self.calc['pressureDrop']["value"] = self.contractionCalc()
        if self.calc['pressureDrop']["value"] == False:
            raise NotImplementedError('Calcuations for a '+
                                      str(self.dict['CID'])+' have not yet '+
                                        'been implemented in this' +
                                        'pre-alpha state.')
        else:
            self.calc["pressureDrop"]["unit"] = "Pa"
            self.dict["values"]["calculated"]["pressureDrop"] = self.calc["pressureDrop"]

    def expansionCalc(self):
        q = self.calc['dynamicPressure']
        kt = self.calc['ktLosses']
        pDrop = kt * q
        return(pDrop)

    def contractionCalc(self):
        f = self.calc['frictionFactor']
        kt = self.calc['ktLosses']
        A1 = self.comp['upstreamArea']["value"]
        A2 = self.comp['downstreamArea']["value"]
        q = self.calc['dynamicPressure']
        D1 = 2 * math.sqrt(A1/math.pi)
        D2 = 2 * math.sqrt(A2/math.pi)
        cL = self.comp['contractionLength']
        if self.comp['contractionAngledOrCurved']["value"] == 'angle':
            angle = self.comp['angle']["value"]
            if angle < math.pi/4:
                pDrop = (
                    kt + 4*f * (
                        cL / (
                            (D1 + D2) / 2
                            )
                        )
                    ) * q
            else:
                pDrop = kt * q
        else:
            pDrop = kt * q
        return(pDrop)            

    def lineCalc(self):
        # Create some local variables for ease of use
        rho = self.fluid["density"]["value"]
        q = self.calc["dynamicPressure"]
        g = self.g
        z = self.comp["height"]["value"]
        f = self.calc["frictionFactor"]
        x = self.comp["length"]["value"]
        Dh = self.comp["hydraulicDiameter"]["value"]
        pDrop = rho*g*z + q * ((4*f*x)/Dh)
        return(pDrop)

    def bendCalc(self):
        rho = self.fluid['density']["value"]
        g = self.g
        z = self.comp['height']["value"]
        f = self.calc['frictionFactor']
        x = self.comp['length']["value"]
        Dh = self.comp['hydraulicDiameter']["value"]
        kt = self.calc['ktLosses']
        pDrop = rho*g*z + q * (
            ((4*f*x)/Dh) + kt
            )
        return(pDrop)
    
