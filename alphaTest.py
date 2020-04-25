#import sys
#sys.path.insert(0, '/bins/A21func/')
import math
import bin
#import suddenContractionKtRegression
name = input('Name of the component\n(See documentation for vaild names):\n')
#print(bin.A21(name).paramList)
def iterdict(d):
    for k,v in d.items():
        if k == 'CID':
            continue
        elif k == 'calculated':
            continue
        elif isinstance(v, dict):
            if k == 'contractionParameters' and d[k]['angle']:
                d[k] = contractionVals(v)
            else:
                iterdict(v)
        else:
            if v:
                d[k] = inputVal(k,v,d)
    return(d)
def contractionVals(d):
    typeOfContraction = input('Is the contraction ANGLED or '+
                                           'a sudden CURVED contraction?\n')
    d['contractionAngledOrCurved'] = checkContraction(typeOfContraction,d)
    for k,v in d.items():
        if k == 'contractionAngledOrCurved':
            continue
        elif (k == 'angle' or k == 'contractionLength') and d['contractionAngledOrCurved'] != 'angle':
            d[k] = False
        elif k == 'downstreamRadiusOfCurvature' and d['contractionAngledOrCurved'] != 'curve':
            d[k] = False
        else:
            d[k] = inputVal(k, v, d)
    return(d)
def checkExponent(string):
    if string.find('^') != -1:
        string = string.replace('^','**')
    return(string)
def checkContraction(string,v):
    string = string.upper()
    if string.find('A') != -1:
        string = 'angle'
        checkSum = 0
    elif string.find('C') != -1:
        string = 'curve'
    else:
        print('You did not give a valid entry. Please give "a" for '+
              'an angled contraction and "c" for a curved contraction.')
        string = contractionVals(v)
    return(string)
def floatInput(string,k,v,d):
    try:
        string = float(eval(string))
    except:
        print('You did not give a number - please review and try again')
        string = inputVal(k,v,d)
    return(string)
def inputVal(k,v,d):
    #input a value from the user
    output = input('Give a value for '+str(k)+': ')
    #Check if the user used '^' instead of '**'
    output = checkExponent(output)
    #Evaluate the string if it able to be and then float it:
    output = floatInput(output,k,v,d)
    return(output)
newDict = iterdict(bin.A21(name).paramList)      
newDict = bin.A22(newDict).dict
pDrop = bin.A31(newDict).dict['calculated']['pressureDrop']
print('Pressure Drop:',pDrop)
print('\n')
endVal = input('press enter to exit')
