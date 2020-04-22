#For a sudden contraction, we have a sequence of different regressions that
# we need to use to determine the kt loss. As such we need a few things to
# do this:

class contractKt:
    def __init__(self,areaRatio,rOverD):
        self.AR = areaRatio
        self.rD = rOverD
        self.kt = self.contractionRegression()
    #Cubic regression implicit method
    def cubReg(points):
        n = len(points)
        X = [item[0] for item in points]
        Y = [item[1] for item in points]
        Sx = sum(X)
        Sy = sum(Y)
        S2x = sum([item**2 for item in X])
        S3x = sum([item**3 for item in X])
        S4x = sum([item**4 for item in X])
        S5x = sum([item**5 for item in X])
        S6x = sum([item**6 for item in X])
        Sxy = sum([X[i] * Y[i] for i in range(n)])
        S2xy = sum([X[i]**2 * Y[i] for i in range(n)])
        S3xy = sum([X[i]**3 * Y[i] for i in range(n)])
        A = [[S6x,S5x,S4x,S3x],[S5x,S4x,S3x,S2x],[S4x,S3x,S2x,Sx],[S3x,S2x,Sx,n]]
        b = [[S3xy],[S2xy],[Sxy],[Sy]]
        coef = np.linalg.solve(A, b)
        return(coef)
    #Regressions for contraction
    def contractionRegression(self):
        x = self.AR
        rD = self.rD
        #The following regressions were pulled from
        # “SAE Aerospace Applied Thermodynamics Manual,” Developed by SAE Committee
        # AC-9, Aircraft Environmental Systems, Society of Automotive Engineers, Inc., New
        # York, 1969.
        rDVals = [0,0.01,0.02,0.03,0.04,0.06,0.08,0.12]
        correlations = [
            -0.1863*x**4 + 0.7805*x**3 - 1.1731*x**2 + 0.0951*x + 0.4874,
            -0.2712*x**4 + 0.8021*x**3 - 1.0011*x**2 + 0.0872*x + 0.382,
            -0.1396*x**4 + 0.4837*x**3 - 0.7008*x**2 + 0.0441*x + 0.31,
            -0.1953*x**4 + 0.5822*x**3 - 0.7017*x**2 + 0.0684*x + 0.246,
            -0.0814*x**4 + 0.3217*x**3 - 0.4701*x**2 + 0.0291*x + 0.2011,
            -0.0803*x**4 + 0.2268*x**3 - 0.2941*x**2 + 0.026*x + 0.1207,
            0.024*x**4 - 0.033*x**3 - 0.0561*x**2 - 0.0051*x + 0.0688,
            -0.0048*x**4 + 0.0069*x**3 - 0.0351*x**2 + 0.0195*x + 0.0122]
        #if we happen to have gotten a regression r/D, don't do the cubic regression
        if rD in rDVals:
            kt = correlations[rDVals.index(rD)]
        #Otherwise, set up a cubic regresssion and find kt loss
        else:
            points = [[rDVals[i],correlations[i]] for i in range(len(rDVals))]
            # we create a cubic regression of the values going up a given A2/A1 values
            reg = cubReg(points)
            kt = reg[0][0]*rD**3 + reg[1][0]*rD**2 + reg[2][0]*rD + reg[3][0]
        return(kt)
