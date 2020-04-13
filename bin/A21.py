#Using the alternative method from Issue #7
#def A21Func():
#Values that are not required for a component are set to False
# This allows the loop to only require numbers that DON'T have
# False as their value.

cTypes = {
    'line': ['LNE',
             ['deltaX','deltaZ',False, False],
             ['insideArea','mass flow','D_h'],
             False, #no valve parameters
             False, #not contraction/expansion
             ['rho','mu','T'],
             ['Rey','f',False,'deltaP']
             ],
    'bend': ['BND',
             ['deltaX','deltaZ','radius', 'angle'],
             ['insideArea','mass flow','D_h'],
             False, #not a valve
             False, #not contraction/expansion
             ['rho','mu','T'],
             ['Rey','f','kt','deltaP']
             ],
    'valve': ['VLV',
              False, #no distance
              False, #no component dimensions
              ['valveCoefficient','specificGravity','N'],
              False, #not contraction/expansion
              False, #no fluid properties required
              [False,False,False, 'deltaP']
              ],
    'tubeSplit' : ['SPL',
                   ['deltaX', 'deltaZ',False,False],
                   ['insideArea','massFlow','D_h',],
                   False, #Not a valve
                   False, #Not Contraction/Expansion
                   ['rho', 'mu', 'T'],
                   ['rey', 'f','kt', 'deltaP']
                   ],
    'tubeJoin' : ['JON',
                  ['deltaX', 'deltaZ',False,False],
                  ['insideArea','massFlow','D_h',],
                  False, #Not a valve
                  False, #Not Contraction/Expansion
                  ['rho', 'mu', 'T'],
                  ['rey', 'f','kt', 'deltaP']
                  ],
    'suddenExpansion' : ['EXP',
                         False, #Don't need distances
                         [False,'massFlow',False,],
                         False, #Not a valve
                         ['upstreamArea','downstreamArea',False,False],
                         ['rho', 'mu', 'T'],
                         ['rey', 'f','kt', 'deltaP']
                         ],
    'suddenContraction' : ['CON',
                           False, #Don't need distances
                           [False,'massFlow',False,],
                           False, #Not a valve
                           ['upstreamArea','downstreamArea','contractionType (a or c)',['contractionParameters']],
                           ['rho', 'mu', 'T'],
                           ['rey', 'f','kt', 'deltaP']
                           ]
    #The next three will be odd for calculating pressure drop for them.
    # They will (probably) not use the typical values herein.
    'orifice' : ['ORF',
                 False,
                 False,
                 False,
                 False,
                 False,
                 False,
                 ],
    'injector' : ['INJ',
                  False,
                  False,
                  False,
                  False,
                  False,
                  False,
                  ],
    'catalystBed' : ['BED',
                     False,
                     False,
                     False,
                     False,
                     False,
                     False,
                     ]
}
