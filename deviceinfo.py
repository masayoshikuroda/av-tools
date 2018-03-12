#coding:utf-8
import pyaudio

audio = pyaudio.PyAudio()
count = audio.get_device_count()
for i in range(0, count):
    info = audio.get_device_info_by_index(i)
    print "Device information({0})".format(i)
    for k, v in info.items():
        print "    {0:<26} : {1}".format(k, v)