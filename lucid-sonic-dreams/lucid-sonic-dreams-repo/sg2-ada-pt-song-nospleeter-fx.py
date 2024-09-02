import numpy as np 
from skimage.transform import swirl
from lucidsonicdreams import EffectsGenerator
from lucidsonicdreams import LucidSonicDream

def swirl_func(array, strength, amplitude):
  swirled_image = swirl(array, 
                        rotation = 0, 
                        strength = 100 * strength * amplitude,
                        radius=650)
  return (swirled_image*255).astype(np.uint8)

swirl_effect = EffectsGenerator(swirl_func,
                                audio = 'song.mp3', 
                                strength = 0.2, 
                                percussive = False)
                                

L = LucidSonicDream(song = 'song.mp3',
                     # pulse_audio = 'drums.wav' # Ignore other pulse settings and use this audio track to pulse
                     # motion_audio = 'other.wav'
                     # contrast_audio = 'bass.wav'
                     # flash_audio = 'vocals.wav'
                     style = 'stylegan2/training-runs/00006-BigGAN_512-mirror-stylegan2-batch16-resumecustom/network-snapshot-000912.pkl')                     


L.hallucinate(file_name = 'song.mp4',
             fps = 60, # Actual video FPS. Was: fps=self.sr/self.frame_duration. frame_dur=int(sr/fps - (sr/fps % 64)) (sr = sample rate)
             speed_fpm = 12,
             truncation = 1, # Between 0 and 1
             
             pulse_react = 0.62,
             pulse_percussive = True, # If True while pulse_harmonic is False, pulse reacts to the audio's percussive elements.
             pulse_harmonic = False, # If True while pulse_percussive is False, pulse reacts to the audio's harmonic elements

             motion_react = 0.42,
             motion_percussive = False,
             motion_harmonic = True,
             motion_randomness = 0.42, # Between 0 and 1

             contrast_percussive = True,
             contrast_strength = 0.76,
             
             flash_percussive = False,
             flash_strength = 0.05,
             
             #custom_effects = [swirl_effect],
                          
             save_frames = False # Does nothing now
             ) 
