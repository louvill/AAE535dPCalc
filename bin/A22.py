#Creating the A22 function:
# This will define the different functions we need to actually
# calculate parameters like friction factor and Reynolds number
# using the values input from user (via MAIN.py)
#Need the math package in this function
import math
#Need the contraction kt method for this as well
#import suddenContractionKtRegression as sckr
#
class A22:
    def __init__(self,dict): #dict stands for dictionary
        self.dict = dict
        self.calc = self.dict['calculated']
        self.geo = self.dict['geometry']
        self.misc = self.dict['misc']
        self.fluid = self.dict['fluidProperties']
        #The angles input may have been given in degrees and not radians.
        # let's fix that now. If the number is >3.14, there is a good bet
        # that the person put in degrees and not radians.
        if self.geo['bendAngle']:
            if self.geo['bendAngle'] >= math.pi:
                self.geo['bendAngle'] = self.geo['bendAngle'] * (math.pi/180)
                self.dict['geometry'] = self.geo
        if self.misc['contractionParameters']['angle']:
            if self.misc['contractionParameters']['angle'] >= math.pi:
                self.misc['contractionParameters']['angle'] = (
                    self.misc['contractionParameters']['angle'] * (math.pi/180)
                    )
                self.dict['misc'] = self.misc
        #Lets find the velocity of the fluid (in whatever location we're looking at)
        self.vel = self.velCalc()
        #Now onto the logic tree of different parameters to calculate
        self.logicTree()
    #We create a logic tree that can take in the dictionary
    # input and determine which parameter values need to be calculated.
    # Because the data structure is set up so values that are not needed
    # are labeled 'False', we can check to see if we need a value by simply
    # asking 'if Parameter' and if it isn't False then we proceed.
    def logicTree(self):
        if self.calc['dynamicPressure']:
            self.calc['dynamicPressure'] = self.qFunc()
        if self.calc['reynolds']:
            self.calc['reynolds'] = self.reyFunc()
            if self.calc['frictionFactor']:
                self.calc['frictionFactor'] = self.fricFunc()
        if self.calc['ktLosses']:
            self.calc['ktLosses'] = self.ktFunc()
        self.dict['calculated'] = self.calc
    def velCalc(self):
        if self.dict['CID'] == 'CON' or self.dict['CID'] == 'EXP':
            smallerArea = min( [
                self.misc['upstreamArea'],
                self.misc['downstreamArea']
                ]
                               )
            vel = (
                self.geo['massFlow']/
                (smallerArea * self.fluid['density'])
                )
        else:
            vel = ( float(self.geo['massFlow'])/
                    (float(self.geo['insideArea']) *
                     float(self.fluid['density'])
                    )
            )
        return(vel)
    def qFunc(self):
        q = 0.5 * self.fluid['density'] * self.vel**2
        return(q)
    def reyFunc(self):
        rey = ( (float(self.fluid['density']) *
                 float(self.vel) *
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
        if self.dict['CID'] == 'BND':
            kt = (
                (
                    self.calc['frictionFactor']*self.geo['bendAngle']*
                    (self.geo['bendRadius']/self.geo['hydraulicDiameter'])
                    ) +
                (
                    (0.10 + 2.4*self.calc['frictionFactor'])*
                    math.sin(self.geo['bendAngle']/2)
                    ) +
                (
                    (
                        6.6 * self.calc['frictionFactor'] * (
                            math.sqrt(math.sin(self.geo['bendAngle']/2))
                            + math.sin(self.geo['bendAngle']/2)
                            )
                        ) /
                    (
                        (
                            self.geo['bendRadius']/self.geo['hydraulicDiameter']
                            ) **
                        (
                            (4 * self.geo['bendAngle']) / 2
                            )
                        )
                    )
                )
        elif self.dict['CID'] == 'EXP':
            kt = (
                1 - (
                    self.misc['upstreamArea']/self.misc['downstreamArea']
                    )
                ) ** 2
        elif self.dict['CID'] == 'CON':
            if self.misc['contractionParameters']['contractionAngledOrCurved'] == 'angle':
                cL = self.misc['contractionParameters']['contractionLength']
                angle = self.misc['contractionParameters']['angle']
                if angle < math.pi/6:
                    kt = 0
                elif angle < math.pi/4:
                    kt = 0.05
                else:
                    R = cL
                    A1 = self.misc['upstreamArea']
                    A2 = self.misc['downstreamArea']
                    D2 = 2 * math.sqrt(A2 / math.pi)
                    AR = A2/A1
                    rD = R/D2
                    kt = sckr.contractKt(AR,rD).kt
            else:
                R = self.misc['contractionParameters']['downstreamRadiusOfCurvature']
                A1 = self.misc['upstreamArea']
                A2 = self.misc['downstreamArea']
                D2 = 2 * math.sqrt(A2 / math.pi)
                AR = A2/A1
                rD = R / D2
                kt = sckr.contractKt(AR,rD).kt
                
        else:
            raise NotImplementedError('Calculations for kt of non-angles have not been '+
                                  'implemented in this pre-alpha build.')
        return(kt)
