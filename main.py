# FLAC to AIFF converter
# Desciption:   Converts all .flac files into .aiff or .wav
#
# Author:       Jérôme Roy
# Date:         22.03.23
# Update:       22.03.23

import os
import soundfile as sf
import tkinter as tk
from tkinter import filedialog

# Create a file dialog to select the directory containing the FLAC files
root = tk.Tk()
root.withdraw()
flac_dir = filedialog.askdirectory()

# Loop through all files in the directory
for filename in os.listdir(flac_dir):
    # Check if the file is a FLAC file
    if filename.endswith(".flac"):
        # Build the full path to the FLAC file
        flac_path = os.path.join(flac_dir, filename)

        # Build the full path to the AIFF file
        wav_path = os.path.join(flac_dir, os.path.splitext(filename)[0] + ".aiff") #change to .wav if you want .wav files

        # Load the FLAC file and write it to a AIFF file
        data, samplerate = sf.read(flac_path)
        sf.write(wav_path, data, samplerate)