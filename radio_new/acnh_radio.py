#!/usr/bin/python3

import shout
import random
from time import sleep
from sys import stderr
#import string

prefix = "/icecast/acnh_radio/"
log_path = "/icecast/acnh-radio-log.txt"
log_file = open(log_path, "w")

def play_file(fa, si):
    print("opening file %s" % fa, file=log_file, flush=True)
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
    print("Reading playlist file %s" % fa, file=log_file, flush=True)
    f = open(fa)
    files = f.read().split("\n")[:-1]
    f.close()
    return [prefix + x for x in files]

music_files = read_file(prefix + "music.txt")
ads_files = read_file(prefix + "ads.txt")
dj_kk_files = read_file(prefix + "dj_kk.txt")
dj_kk_emotes_files = read_file(prefix + "dj_kk_emotes.txt")
jingles_files = read_file(prefix + "jingles_normal.txt")

playlist = music_files.copy()
random.shuffle(playlist)
print("Initial Playlist: ",playlist, file=log_file, flush=True)

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

s.open()

print("Connection Status: ", s.get_connected(), file=stderr)

sleep(5)

while True:
    if len(playlist) < 5:
        print(len(playlist), "songs left", file=log_file, flush=True)
        print("Reshuffling Playlist", file=log_file, flush=True)
        playlist = music_files.copy()
        random.shuffle(playlist)
        print(playlist, file=log_file, flush=True)

    for i in range(random.randint(3,5)):
        play_file(playlist.pop(), s)

    play_file(random.choice(dj_kk_emotes_files), s)
    play_file(random.choice(jingles_files), s)
    play_file(random.choice(ads_files), s)
    play_file(random.choice(dj_kk_files), s)
