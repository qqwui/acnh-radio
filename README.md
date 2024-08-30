# Animal Crossing New Horizons Radio
These are the scripts I used to make the ACNH internet radio. This is an archive, I'm not developing these further in favour of a setup using liquidsoap.

*Songs must be added yourself. I am not responsible for Nintendo nuking your home*

## radio_old
This is the old python script used to queue songs. It requires some textfiles containing the *file names* of sound files for things like the fake ads and music. Examples can be seen in the directory. Options such as base directory and icecast server location are configired in the acnh_radio.py script itself. `jingles_morining.txt` and `jingles_night.txt` are currently unused.

## radio_new
The same as radio_old but uses a new system that prevents songs potentially repeating .

# radio_hifi
I just used `ices` for this. Its mainly for archival purposes.
