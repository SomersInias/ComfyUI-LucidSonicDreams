from lucidsonicdreams import LucidSonicDream

# bass, drums, other, vocals
L = LucidSonicDream(song = 'song.mp3',
                     pulse_audio = 'drums.wav', # Ignore other pulse settings and use this audio track to pulse
                     motion_audio = 'other.wav',
                     contrast_audio = 'bass.wav',
                     flash_audio = 'vocals.wav',
                     style = 'stylegan2/training-runs/00004-face-paintings-styleaug_512-later/network-snapshot-000768.pkl')
                     
L.hallucinate(file_name = 'song.mp4',
             fps = 30, # fps is not the true fps. fps=self.sr/self.frame_duration. frame_dur=int(sr/fps - (sr/fps % 64)) (sr = sample rate)
             speed_fpm = 15,
             truncation = 1, # Between 0 and 1
             
             pulse_react = 0.7,
             pulse_percussive = False, # If True while pulse_harmonic is False & no pulse_audio, pulse reacts to the audio's percussive elements.
             pulse_harmonic = False, # If True while pulse_percussive is False & no pulse_audio, pulse reacts to the audio's harmonic elements.

             motion_react = 0.7,
             motion_percussive = False,
             motion_harmonic = True,
             motion_randomness = 0.7, # Between 0 and 1

             contrast_percussive = True,
             contrast_strength = 0.6,
             
             flash_percussive = True,
             flash_strength = 0.4,
                          
             save_frames = False
             ) 
