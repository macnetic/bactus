import numpy as np
import numpy.ma as ma

from filterData import getFilterParam, filterData

test_params = [[20,40],
               [0.3,0.4],
               [1,3]]
tr, gr, bt = test_params

testData = np.array(
    [[10,20,30,40,50,60],
     [0.1,0.2,0.3,0.4,0.5,0.6],
     [1,2,3,4,1,2]]
)
testData = testData.transpose()

f_data = filterData(testData, test_params)

test_params = [[20,40],
               [0.3,0.4],
               [1,3]]
tr, gr, bt = test_params

k_data = filterData(testData, )

#f_data[:,0] = ma.masked_outside(f_data,*tr)
print(type(f_data))
print(f_data)