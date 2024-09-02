from lucidsonicdreams import LucidSonicDream

L = LucidSonicDream(song = '/content/yoursong.mp4', #mp3,mp4,wav here
                    style = '/content/drive/MyDrive/StyleGAN2/wikiart.pkl') #pkl path here

L.hallucinate(file_name = '/content/outputvideo.mp4', #output path here
              start = 0,
              duration=30,  
              speed_fpm = 20,
              pulse_percussive = True,
              pulse_harmonic= False,
              pulse_react = 1,
              motion_harmonic = True,
              motion_percussive = False,
              motion_react = 0.5,
              fps = 24, 
              ) 
     
