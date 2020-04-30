#Creating the A22 function:
# This will define the different functions we need to actually
# calculate parameters like friction factor and Reynolds number
# using the values input from user (via MAIN.py)
#Need the math package in this function
import math
#Need the contraction kt method for this as well
#import suddenContractionKtRegression as sckr


class A23:
    def __init__(self,d): #d stands for dictionary
        self.dict = d
        # For ease of use within this method, we define the full values dictionary
        # and the component and fluid parameters all as seperate variables
        self.vals = self.dict["values"]
        self.comp = self.vals["component"]
        self.fluid = self.vals["fluid"]
        # Next we define a new variable for our calculated values that will
        # be filled with terms from here and A31.
        self.calc = {}

        # UNIT CONVERSIONS : this might happen elsewhere later.
        # The angles input may have been given in degrees and not radians.
        # let's fix that now. If the number is >3.14, there is a good bet
        # that the person put in degrees and not radians.
        if 'bendAngle' in self.comp.keys():
            if self.comp['bendAngle']["value"] >= math.pi:
                self.comp['bendAngle']["value"] = self.comp['bendAngle']["value"] * (math.pi/180)
                self.dict["values"]["component"] = self.comp
        if "angle" in self.comp.keys():
            if self.comp['angle']["value"] >= math.pi:
                self.comp['angle']["value"] = self.comp['angle']["value"]*(math.pi/180)
                self.dict["values"]["component"] = self.comp
        #Now onto the logic tree of different parameters to calculate
        self.logicTree()
        #Once we have all of the local variables defined, redefine dict
        self.dict["values"]["calculated"] = self.calc
        
    # We create a logic tree that can take in the dictionary
    # input and determine which parameter values need to be calculated.
    def logicTree(self):
        # Fluid Velocity: We need mass flow, area, and density
        if ("massFlow" in self.comp.keys()
            and "insideArea" in self.comp.keys()
            and "density" in self.fluid.keys()
            ):
            self.calc["velocity"] = self.velCalc()
        # Dynamic Pressure: We need velocity (if we have velocity, we'll have density)
        if "velocity" in self.calc.keys():
            self.calc["dynamicPressure"] = self.qFunc()
        # Reynolds: We need velocity, hydraulic diameter, and viscosity
        if ("velocity" in self.calc.keys()
            and "hydraulicDiameter" in self.comp.keys()
            and "viscosity" in self.fluid.keys()):
            self.calc['reynolds'] = self.reyFunc()
            # And if we have Reynolds, let's get Friction Factor too
            self.calc['frictionFactor'] = self.fricFunc()
        # kt Losses has it's own logic tree
        self.calc['ktLosses'] = self.ktFunc()
    def velCalc(self):
        if self.dict['CID'] == 'CON' or self.dict['CID'] == 'EXP':
            smallerArea = min( [
                float(self.comp['upstreamArea']["value"]),
                float(self.comp['downstreamArea']["value"])
                ]
                               )
            vel = (
                float(self.comp['massFlow']["value"])/
                (smallerArea * float(self.fluid['density']["value"]))
                )
        else:
            vel = ( float(self.comp['massFlow']["value"])/
                    (float(self.comp['insideArea']["value"]) *
                     float(self.fluid['density']["value"])
                    )
            )
        return(vel)
    def qFunc(self):
        q = 0.5 * float(self.fluid['density']["value"]) * self.calc["velocity"]**2
        return(q)
    def reyFunc(self):
        rey = ( (float(self.fluid['density']["value"]) *
                 float(self.calc["velocity"]) *
                 float(self.comp['hydraulicDiameter']["value"])
                 )/
                float(self.fluid['viscosity']["value"])
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
                    self.calc['frictionFactor']*self.comp['bendAngle']["value"]*
                    (self.geo['bendRadius']["value"]/self.comp['hydraulicDiameter']["value"])
                    ) +
                (
                    (0.10 + 2.4*self.calc['frictionFactor'])*
                    math.sin(self.comp['bendAngle']["value"]/2)
                    ) +
                (
                    (
                        6.6 * self.calc['frictionFactor'] * (
                            math.sqrt(math.sin(self.comp['bendAngle']["value"]/2))
                            + math.sin(self.comp['bendAngle']["value"]/2)
                            )
                        ) /
                    (
                        (
                            self.comp['bendRadius']["value"]/self.comp['hydraulicDiameter']["value"]
                            ) **
                        (
                            (4 * self.comp['bendAngle']["value"]) / 2
                            )
                        )
                    )
                )
        elif self.dict['CID'] == 'EXP':
            kt = (
                1 - (
                    self.comp['upstreamArea']["value"]/self.comp['downstreamArea']["value"]
                    )
                ) ** 2
        # THIS WHOLE METHOD NEEDS TO BE REWRITTEN #
        elif self.dict['CID'] == 'CON':
            if self.comp['contractionAngledOrCurved'] == 'angle':
                cL = self.comp['contractionLength']["value"]
                angle = self.comp['angle']["value"]
                if angle < math.pi/6:
                    kt = 0
                elif angle < math.pi/4:
                    kt = 0.05
                else:
                    R = cL
                    A1 = self.misc['upstreamArea']["value"]
                    A2 = self.misc['downstreamArea']["value"]
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
        ############################################
        else:
            kt = 0
        return(kt)
