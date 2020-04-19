#import sys
#sys.path.insert(0, '/bins/A21func/')
import math
import bin
name = 'line'
#print(bin.A21(name).paramList)
def iterdict(d):
    for k,v in d.items():
        if k == 'CID':
            continue
        elif k == 'calculated':
            continue
        elif isinstance(v, dict):
            iterdict(v)
        else:
            if v:
                d[k] = float(input('Give a value for '+str(k)+': '))
    return(d)
newDict = iterdict(bin.A21(name).paramList)
newDict = bin.A22(newDict).dict
pDrop = bin.A31(newDict).dict['calculated']['pressureDrop']
print('Pressure Drop:',pDrop)
