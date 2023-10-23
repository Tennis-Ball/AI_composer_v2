import midi_to_mp3
import composer_list

# this code will not work if you do not have the files/FluidSynth INstalled
for name in composer_list.mozart_list:
    # 38 because in composer list, the link has 38 characters before the filename
    midi_to_mp3.midi_to_mp3(f'music_data/music/{name[38:]}', 'music_data/GeneralUser_GS_1.471/GeneralUser_GS_v1.471.sf2', f'{name[38:46]}.wav')