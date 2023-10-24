from pydub import AudioSegment 
from pydub.utils import make_chunks
import os

def process_sudio(file_name):
    try:
        myaudio = AudioSegment.from_file(file_name, "wav")
    except:
        myaudio = AudioSegment.from_file(file_name, format="mp4")
    chunk_length_ms = 10000 # pydub calculates in millisec 
    chunks = make_chunks(myaudio,chunk_length_ms) #Make chunks of one sec 
    for i, chunk in enumerate(chunks): 
        chunk_name = file_name + "_{0}.wav".format(i) 
        print ("exporting", chunk_name) 
        chunk.export(chunk_name, format="wav") 

all_file_names = os.listdir('music_data/music_wav')

for i in range(len(all_file_names)):
    all_file_names[i] = 'music_data/music_wav/' + all_file_names[i]

print(all_file_names)

for each_file in all_file_names:
    if ('.wav' in each_file):
        process_sudio(each_file)