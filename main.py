#Liam's favorite Smash character is Jigglypuff.

#This is the main function that will read all of the other subfunctions
#
#As of right now (April 15) this function is a skelleton and not a
# functional script. Futher work will need to be completed once
# milestone "Sub Function Definitions" is completed.

import bin
import json

def main(jsonInput):
    #Method for converting json to python arrays
    #data = doing stuff to .json file
    #-------------
    #
    pDrops = []
    componentList = jsonInput["componentList"]
    for item in componentList:
        A22Output = bin.A22(item).dict
        A23Output = bin.A23(item).dict
        A31Output = bin.A31(A23Output).dict
        pDrops.append(A31Output["values"]["calculated"]["pressureDrop"]["value"])
    A32Output = bin.A32(pDrops,componentList).output
    calc_json = json.dumps(A32Output)
    output_file = open("saves/testOutput.json", "w")
    n = output_file.write(calc_json)
    output_file.close()
    
    
    #Calling of subfunctions
    #A11Output = A11(data)
    #
    #A21Output = A21(data)
    #
    #A22Output = A22(data)
    #
    #There will probably be a for loop for function A31
    #that will need to put into a single array
    #pDropArray = ['',[]]
    #for component in A22Output:
    #   A31Output = A31(component)
        #Take in all of the data from A31 and turn it into a single array
        # where A22Output[0] is the IIN of the component
    #   pDropArray[1].append([A22Output[0],A31Output])
    #
    #A32 will sum up the pressure drops and then format the data in a
    #.json that can read back into Electron
    #A32Output = A32(pDropArray)
    #setting A32Output to be an empty string for testing
    A32Output = ''
    #
    return(A32Output)

#### MAIN ####
with open('saves/testSave.json') as f:
    data = json.load(f)
main(data)
