from __future__ import print_function
import numpy as np
import tensorflow as tf

from edward.stats import invgamma
from scipy import stats

sess = tf.Session()

def _test(a, scale, size):
    val_est = invgamma.rvs(a, scale, size=size).shape
    val_true = (size, ) + np.asarray(a).shape
    assert val_est == val_true

def test_scalar():
    _test(0.5, 0.5, 1)
    _test(np.array(0.5), np.array(0.5), 1)

def test_1d():
    _test(np.array([0.5]), np.array([0.5]), 1)
    _test(np.array([0.5]), np.array([0.5]), 5)
    _test(np.array([0.2, 0.8]), np.array([0.2, 0.8]), 1)
    _test(np.array([0.2, 0.8]), np.array([0.2, 0.8]), 10)

#def test_2d():
#    _test(np.array([[0.5]]), np.array([[0.5]]), 1)
#    _test(np.array([[0.5]]), np.array([[0.5]]), 5)
#    _test(np.array([[0.2, 0.8]]), np.array([[0.2, 0.8]]), 1)
#    _test(np.array([[0.2, 0.8]]), np.array([[0.2, 0.8]]), 10)
#    _test(np.array([[0.2, 0.8], [0.7, 0.6]]), np.array([[0.2, 0.8], [0.7, 0.6]]), 1)
#    _test(np.array([[0.2, 0.8], [0.7, 0.6]]), np.array([[0.2, 0.8], [0.7, 0.6]]), 10)
