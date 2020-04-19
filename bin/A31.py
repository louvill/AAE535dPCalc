#Subfunction A31 is responsible for inputting the component parameters
# and then using the information about the component to determine
# the pressure drop across that component
# ----------------------------------------------------------
# Using data structure from issues #4 and #7. Recall that each
# cell is labeled "False" if there is no data stored and thus
# we can call "if dict['parameterName']" to see if anything is there.
# ----------------------------------------------------------


class A31:
    def __init__(self,dict): #dict is for dictionary
        self.dict = dict
        #Now we set several new local variables for ease of calling them later
        self.CID = self.dict['CID']
        self.calc = self.dict['calculated']
        self.geo = self.dict['geometry']
        self.fluid = self.dict['fluidProperties']
        self.g = 9.81 #SI units here - we may alter this at some point
        #
        #Set up the logic tree to see what we need to do
        #
        #This method of finding the pressure drop for each different type
        # of component is WAY underoptimized. Feel free to improve it! :)
        if self.CID == 'LNE':
            self.calc['pressureDrop'] = self.lineCalc()
        elif self.CID == 'BND':
            self.calc['pressureDrop'] = False
        elif self.CID == 'ORF':
            self.calc['pressureDrop'] = False
        elif self.CID == 'INJ':
            self.calc['pressureDrop'] = False
        elif self.CID == 'CAT':
            self.calc['pressureDrop'] = False
        elif self.CID == 'BND':
            self.calc['pressureDrop'] = False
        elif self.CID == 'SPL':
            self.calc['pressureDrop'] = False
        elif self.CID == 'JON':
            self.calc['pressureDrop'] = False
        elif self.CID == 'EXP':
            self.calc['pressureDrop'] = False
        elif self.CID == 'CON':
            self.calc['pressureDrop'] = False
        if self.calc['pressureDrop'] == False:
            raise NotImplementedError('Only calculations for a line have '+
                                      'been implemented at this stage in '+
                                      'development.')
        else:
            self.dict['calculated']['pressureDrop'] = self.calc['pressureDrop']
    def lineCalc(self):
        rho = self.fluid['density']
        g = self.g
        z = self.geo['height']
        # !!BUG!! #
        #dynamic pressure hasn't been included in A21 yet
        #q = self.calc['dynamicPressure']
        # ------  #
        # !!SHORT TERM FIX!! #
        mDot = self.geo['massFlow']
        AInner = self.geo['insideArea']
        v = mDot / (rho*AInner)
        q = 0.5 * rho * v**2
        # ------------------ #
        f = self.calc['frictionFactor']
        x = self.geo['length']
        Dh = self.geo['hydraulicDiameter']
        pDrop = rho*g*z + q * ((4*f*x)/Dh)
        return(pDrop)
    
