#Creating the A22 function:
# This will define the different functions we need to actually
# calculate parameters like friction factor and Reynolds number
# using the values input from user (via MAIN.py)
#Need the math package in this function
import math
#
class A22:
    def __init__(self,dict): #dict stands for dictionary
        self.dict = dict
        self.calc = self.dict['calculated']
        self.geo = self.dict['geometry']
        self.fluid = self.dict['fluidProperties']
        self.logicTree()
    #We create a logic tree that can take in the dictionary
    # input and determine which parameter values need to be calculated.
    # Because the data structure is set up so values that are not needed
    # are labeled 'False', we can check to see if we need a value by simply
    # asking 'if Parameter' and if it isn't False then we proceed.
    def logicTree(self):
        if self.calc['reynolds']:
            self.calc['reynolds'] = self.reyFunc()
            if self.calc['frictionFactor']:
                self.calc['frictionFactor'] = self.fricFunc()
        if self.calc['ktLosses']:
            self.calc['ktLosses'] = self.ktFunc()
        self.dict['calculated'] = self.calc
    def reyFunc(self):
        vel = ( float(self.geo['massFlow'])/
                (float(self.geo['insideArea']) *
                 float(self.fluid['density'])
                )
        )
        rey = ( (float(self.fluid['density']) *
                 float(vel) *
                 float(self.geo['hydraulicDiameter'])
                 )/
                float(self.fluid['viscosity'])
            )
        return(rey)
    def fricFunc(self):
        def implicitF(self,f):
            output = (
                (1. / (f**(1./2.))) -
                (4.0 * math.log10(float(self.calc['reynolds']) * (f**(1./2.)))) +
                (0.4)
                )
            return(output)
        fGuess = 0.0000001
        switch = False
        step = 0.001
        i = 0
        while abs(implicitF(self,fGuess)) > 10**(-5):
            if implicitF(self,fGuess) > 0:
                if switch:
                    step *= -0.1
                    switch = not(switch)
            else:
                if not(switch):
                    step *= -0.1
                    switch = not(switch)
            fGuess += step
            i += 1
            if i > 10000:
                raise OverflowError('Friction Factor not converging.'+
                                ' Check your input values and try again')
                break
        return(fGuess)
    def ktFunc(self):
        raise NotImplementedError('Calculations for kt have not yet been implemented for '+
                                  'this pre-alpha build.')
        return('A kt Value')
