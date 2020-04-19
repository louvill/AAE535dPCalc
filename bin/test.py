import math
class friction():
    def __init__(self,dict):
        self.dict = dict
        self.f = self.fricFunc()
    def fricFunc(self):
        def implicitF(self,f):
            output = (
                    (1. / (f**(1./2.))) -
                    (4.0 * math.log10(float(self.dict['reynolds']) * (f**(1./2.)))) +
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
            if i > 100:
                raise OverflowError('Friction Factor not converging.'+
                                    ' Check your input values and try again')
                break
        return(fGuess)
test = { 'reynolds' : 12000}
print(friction(test).f)
