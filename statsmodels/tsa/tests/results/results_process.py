import numpy as np
from numpy import array


class Holder(object):
    pass


armarep = Holder()
armarep.comment = 'mlab.garchma(-res_armarep.ar[1:], res_armarep.ma[1:], 20)' +\
'mlab.garchar(-res_armarep.ar[1:], res_armarep.ma[1:], 20)'
armarep.marep = array([[-0.1             ],
       [-0.77            ],
       [-0.305           ],
       [ 0.4635          ],
       [ 0.47575         ],
       [-0.132925        ],
       [-0.4470625       ],
       [-0.11719125      ],
       [ 0.299054375     ],
       [ 0.2432801875    ],
       [-0.11760340625   ],
       [-0.253425853125  ],
       [-0.0326302015625 ],
       [ 0.18642558171875],
       [ 0.11931695210938],
       [-0.08948198932031],
       [-0.14019455634766],
       [ 0.00148831328242],
       [ 0.11289980171934],
       [ 0.05525925023373]])
armarep.ar = array([ 1. , -0.5,  0.8])
armarep.ma = array([ 1.  , -0.6 ,  0.08])
armarep.name = 'armarep'
armarep.arrep = array([[ -1.00000000000000e-01],
       [ -7.80000000000000e-01],
       [ -4.60000000000000e-01],
       [ -2.13600000000000e-01],
       [ -9.13600000000000e-02],
       [ -3.77280000000000e-02],
       [ -1.53280000000000e-02],
       [ -6.17856000000000e-03],
       [ -2.48089600000000e-03],
       [ -9.94252799999999e-04],
       [ -3.98080000000000e-04],
       [ -1.59307776000000e-04],
       [ -6.37382655999999e-05],
       [ -2.54983372800000e-05],
       [ -1.01999411200000e-05],
       [ -4.08009768959999e-06],
       [ -1.63206332416000e-06],
       [ -6.52830179327999e-07],
       [ -2.61133041663999e-07],
       [ -1.04453410652160e-07]])
