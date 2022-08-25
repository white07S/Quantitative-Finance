from mpl_toolkits.mplot3d import Axes3D
import copy as copylib

import numpy
from utils import *
import pandas as pd
import matplotlib.pyplot as plt
numpy.random.seed(0)


dataframe =  pd.read_csv('hjm_data.csv').set_index('time') / 100

hist_timeline = list(dataframe.index)
tenors = [eval(x) for x in dataframe.columns]
hist_rates = numpy.matrix(dataframe)


# plt.plot(hist_rates)
# plt.xlabel(r'Time $t$') 
# plt.title(r'Historical $f(t,\tau)$ by $t$') 
# plt.show();


# plt.plot(tenors, hist_rates.transpose())
# plt.xlabel(r'Tenor $\tau$')
# plt.title(r'Historical $f(t,\tau)$ by $\tau$');
# plt.show()

diff_rates = numpy.diff(hist_rates, axis=0)
assert(hist_rates.shape[1]==diff_rates.shape[1])

# plt.plot(diff_rates)
# plt.xlabel(r'Time $t$')
# plt.title(r'$df(t,\tau)$ by $t$');
# plt.show()

# Calculate covariance matrix
sigma = numpy.cov(diff_rates.transpose())
# anuual market days = 251 or 252
sigma *= 252

eigval, eigvec = numpy.linalg.eig(sigma)
eigvec=numpy.matrix(eigvec)
assert type(eigval) == numpy.ndarray
assert type(eigvec) == numpy.matrix

#  determine principle coponents
factors=3
index_eigvec = list(reversed(eigval.argsort()))[:factors]
princ_eigval = numpy.array([eigval[i] for i in index_eigvec])
princ_comp = numpy.hstack([eigvec[:,i] for i in index_eigvec])

# plt.plot(princ_comp, marker='.')
# plt.title('Principal components')
# plt.xlabel(r'Time $t$');
# plt.show()



# Calculate discretized volatility function from principal components
sqrt_eigval = numpy.matrix(princ_eigval ** .5)
tmp_m = numpy.vstack([sqrt_eigval for _ in range(princ_comp.shape[0])])
vols = numpy.multiply(tmp_m, princ_comp) # multiply matrice element-wise

# plt.plot(vols, marker='.')
# plt.xlabel(r'Time $t$')
# plt.ylabel(r'Volatility $\sigma$')
# plt.title('Discretized volatilities')
# plt.show()