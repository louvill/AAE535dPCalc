#The A32 function will sum up the pressure drop for each component and
# then attach that as a .json file as well as the pressure drops for
# each component.

#might need to import the json package here
import json

#A function to change a list of lists into a dictionary
def Convert(lst):
    res_dct = {item[0]: item[1] for item in lst}
    return(res_dct)

def A32(inputs):
    #The original inputs will be ['',[[IIN,pdrop1],[IIN,pdrop2],...]
    pressureArray = ['',Convert(inputs[1])]
    deltaP = sum(pressureArray[1][key] for key in pressureArray[1])
    pressureArray[0] = deltaP
    output = json.dumps(pressureArray)
    return(output)

#here is our test case
testArray = ['',[['001', 1], ['002', 2],[ '003', 3]]]
print(A32(testArray))
    
    
