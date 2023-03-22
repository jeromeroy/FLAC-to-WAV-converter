# FLAC-to-WAV-converter
Simple code that converts all .flac files from a folder to .aiff or .wav files.

When the code is executed, in the pop-up window select the folder that contains the .flac files you would like to convert.
The program will then loop through the folder, detect and convert every FLAC file into AIFF or WAV. Sample rate and bit depth are not modified.

The FLAC files are then automatically moved to the trash.

Required Python packages: **numpy**, **soundfile**, **Send2Trash**
* pip install numpy
* pip install soundfile