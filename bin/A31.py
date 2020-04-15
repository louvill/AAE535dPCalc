#Subfunction A31 is responsible for inputting the component parameters
# and then using the information about the component to determine
# the pressure drop across that component

def A31(inputs):
    # ----------------------------------------------------------
    # Using data structure from issue #4 and #7. Recall that each
    # cell is labeled "False" if there is no data stored and thus
    # we can call "if arrayName" to see if anything is there.
    # ----------------------------------------------------------
    # FROM #4 and #7
    # dataFormat =
    # [IIN,CID,[
    #FIRST: See if we have a valve
    if inputs[3]:
        valveInfo = inputs[3]
    #SECOND: Is this some other odd component
    elif inputs[4]:
        miscInfo = inputs[4]
    #THIRD, see if we need other calculated values
    if inputs[6]:
        calcParam = inputs[6]
    #Finally, are the fluid terms included?
    if inputs[5]:
        fluidInfo = inputs[5]
    #First is Reynolds, f, and kt
    calcParam = inputs[6]
    #
    # DO SOME CALCULATIONS - To be coded later
    #
    calcParam[4] = 'IN PROGRESS: Program pressure calculations'
    output = [item for item in inputs]
    return(output)
    
