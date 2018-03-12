#coding:utf-8
import sys
import pyaudio
import json
import aconfig as config
  
audio  = pyaudio.PyAudio()
format = audio.get_format_from_width(config.sample_width, config.unsigned)
stream = audio.open(
    format = format,
    channels = config.channels,
    rate = config.rate,
    input = True,
    input_device_index = config.device_index,
    frames_per_buffer = config.chunk)

count = config.get_count()
index = 0
while True:
    data = stream.read(config.chunk)
    sys.stdout.write(data)
    index += 1
    if count > 0 and index > count: break