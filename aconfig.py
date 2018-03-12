#coding:utf-8
import sys
import pyaudio
import json

sample_width = 1
unsigned = False
channels = 1
rate = 8000
chunk = 512
device_index = 0
duration = -1;

with open('aconfig.json') as f:
    config = json.load(f)
    sample_width = config['sample_width']
    unsigned = config['unsigned']
    channels = config['channels']
    rate = config['rate']
    chunk = config['chunk']
    device_index = config['device_index']
    duration = config['duration']

def get_count():
    return int(rate / chunk * duration)
  