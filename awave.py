#coding:utf-8
import sys
import wave
import aconfig as config

WAVE_FILE = 'awave.wav'

wf = wave.Wave_write(WAVE_FILE)
wf.setnchannels(config.channels)
wf.setsampwidth(config.sample_width)
wf.setframerate(config.rate)

count = config.get_count()
index = 0
while True:
    try:
        data = sys.stdin.read(config.chunk)
        wf.writeframes(data)
        index += 1
    except:
        break
    if count > 0 and index > count: break
wf.close()
