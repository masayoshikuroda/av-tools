import sys
import wave

fname = sys.argv[1]
w = wave.open(fname, mode='rb')
print("channels  = " + str(w.getnchannels()))
print("sampwidth = " + str(w.getsampwidth()))
print("framerate = " + str(w.getframerate()))
print("nframes   = " + str(w.getnframes()))
print("duration  = " + str(w.getnframes()/w.getframerate()) + "i seconds")
print("comptype  = " + str(w.getcomptype()))
w.close()
