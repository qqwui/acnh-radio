#!/usr/bin/python3

import shout
import random
from time import sleep
from sys import stderr
#import string

prefix = "/icecast/acnh_radio/"

def play_file(fa, si):
    #print("opening file %s" % fa)
    f = open(fa, 'rb')
    si.set_metadata({'song': fa})

    nbuf = f.read(4096)
    while 1:
        buf = nbuf
        nbuf = f.read(4096)
        if len(buf) == 0:
            break
        si.send(buf)
        si.sync()
    f.close()

def read_file(fa):
    f = open(fa)
    files = f.read().split("\n")[:-1]
    f.close()
    return [prefix + x for x in files]

music_files = read_file(prefix + "music.txt")
ads_files = read_file(prefix + "ads.txt")
dj_kk_files = read_file(prefix + "dj_kk.txt")
dj_kk_emotes_files = read_file(prefix + "dj_kk_emotes.txt")
jingles_files = read_file(prefix + "jingles_normal.txt")

#print(music_files)
#print(ads_files)
#print(dj_kk_files)
#print(jingles_files)

s = shout.Shout()
print("Using libshout version %s" % shout.version(), file=stderr)

s.host = 'localhost'
s.port = 8000
s.user = 'source'
s.password = 'hackme'
s.mount = "/acnh-radio"
s.format = 'vorbis' # vorbis | mp3
s.protocol = 'http' #'http' | 'xaudiocast' | 'icy'
s.name = 'ACNH Radio'
s.description = 'Animal Crossing New Horizons radio simulation complete with "ads" and "commentary"'
s.public = 0  # 0 | 1
"""
s.audio_info = {shout.SHOUT_AI_BITRATE:'128',
                shout.SHOUT_AI_SAMPLERATE:'44100',
                shout.SHOUT_AI_CHANNELS:'2'}
"""
# (keys are shout.SHOUT_AI_BITRATE, shout.SHOUT_AI_SAMPLERATE,
#  shout.SHOUT_AI_CHANNELS, shout.SHOUT_AI_QUALITY)
while 1:
  sleep(5)
  try:
    s.open()
  except:
    print("Connection failed, retrying", file=stderr)
  else:
    if s.get_connected() == -7:
    	break

print(s.get_connected(), file=stderr)

while True:
    for i in range(random.randint(2,4)):
        play_file(random.choice(music_files), s)
    play_file(random.choice(dj_kk_emotes_files), s)
    play_file(random.choice(jingles_files), s)
    play_file(random.choice(ads_files), s)
    play_file(random.choice(dj_kk_files), s)
