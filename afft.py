#coding:utf-8
import sys
import numpy as np
import aconfig as config

axis = np.fft.fftfreq(config.chunk, d=1.0/config.rate)
n = config.chunk/2
nstart = 0
nstop = n
sys.stderr.write(','.join(map(lambda f: '{:.1f}'.format(f), axis[nstart:nstop])) + "\n")

count = config.get_count()
index = 0
while True:
    try:
        data = sys.stdin.read(config.chunk)
        data = np.frombuffer(data, dtype="int8")/(1.0*pow(2, 8*config.sample_width)/2)
        data = np.hamming(len(data)) * data
        data = np.fft.fft(data)
        data = np.abs(data)
	print(','.join(map(lambda f: '{:.2f}'.format(f), data[nstart:nstop])))
        index += 1
    except:
        break
    if count > 0 and index > count: break

