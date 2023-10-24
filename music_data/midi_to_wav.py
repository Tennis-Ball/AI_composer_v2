# courtesy of Dr. Christian Mayer
# Download https://github.com/FluidSynth/fluidsynth/wiki/Download
import os
from pydub import AudioSegment

def midi_to_wav(midi_file, soundfont, wav_file):
    # Convert MIDI to WAV using fluidsynth
    # wav_file = mp3_file.replace('.mp3', '.wav')
    os.system(f'fluidsynth -ni {soundfont} {midi_file} --fast-render={wav_file} -r 44100')

    audio = AudioSegment.from_wav(wav_file)
    audio.export(wav_file, format='wav')

    # Convert WAV to MP3 using pydub
'''    audio = AudioSegment.from_wav(wav_file)
    audio.export(mp3_file, format='mp3')

    # Remove temporary WAV file
    os.remove(wav_file)'''
