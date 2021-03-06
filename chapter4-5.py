#-*-coding:utf-8-*-
inputfile='leleccum.mat'

from scipy.io import loadmat
mat = loadmat(inputfile)#用来加载matlab文件
signal = mat['leleccum'][0]

import pywt #导入PyWavelets
coeffs = pywt.wavedec(signal, 'bior3.7', level = 5)
#返回结果为level+1个数字，第一个数组为逼近系数数组，后面的依次是细节系数数组