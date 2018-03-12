#coding:utf-8
import sys
import math
import numpy as np
import aconfig as config

count = config.rate/config.chunk
averages = []
while True:
    try:
        data = sys.stdin.read(config.chunk)
        data = np.frombuffer(data, dtype="int8")/(1.0*pow(2, 8*config.sample_width)/2)
        average = np.average(np.absolute(data))
        averages.append(average)
        if len(averages) >= count:
            average = np.average(averages)
            level = 10 * math.log10( average * average )
            print(level)
            averages = []
    except:
	raise
        break

