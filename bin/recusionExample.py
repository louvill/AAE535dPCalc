#This is a recursive test. We have a dictionary of dictionaries and we
# need to get every single value in this dictionaries of dictionaries
# that doesn't read false. The 'iterdict' function below recursively
# goes through every dictionary and finds the values we need (both the
# number, and the label).

#Play with this a bit! See if you can break something or if you can
# make it work for even super complicated structures

test = {
    '1' : 1,
    '2' : {
        '2.1' : 2.1,
        '2.2' : {
            '2.21' : 2.21,
            '2.22' : False,
            '2.23' : 2.23
            },
        '2.3' : False
        },
    '3' : {
        '3.1' : 3.1,
        '3.2' : False
        },
    '4' : 4
    }
def iterdict(d):
    for k,v in d.items():
        if isinstance(v, dict):
            iterdict(v)
        else:
            if v:
                print(str(k+':'+str(v)))
iterdict(test)
