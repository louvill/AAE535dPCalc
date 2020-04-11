#Using the alternative method from Issue #7
#def A21Func():


data = {'line': [['deltaX','deltaZ'],
                 ['insideArea','mass flow','D_h'],
                 ['rho','mu','T'],
                 ['Rey','f','deltaP']
                 ],
        'bend': [['deltaX','deltaZ'],
                 ['insideArea','mass flow','D_h','radius','angle'],
                 ['rho','mu','T'],
                 ['Rey','f','deltaP']
                 ]
        }

print(data['line'][0])
