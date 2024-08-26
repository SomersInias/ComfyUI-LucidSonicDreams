import requests

Stylegan2ModelList= ["/content/drive/MyDrive/sonic/iniasstylefinal.pkl", "/content/drive/MyDrive/sonic/DorfinalModel.pkl", "/content/drive/MyDrive/sonic/VisionaryArtm.pkl", "/content/drive/MyDrive/sonic/wikiart.pkl" , "/content/drive/MyDrive/wikiart.pkl"]

class InputParamLucid:
    @classmethod
    def INPUT_TYPES(cls):
           
        


        data_in = {
            "required": {
                "styleganmodel": (Stylegan2ModelList,),
                "start": (
                    "INT",
                    {
                        "default": 0,
                        "min": 0,
                        "max": 86400,
                        "step": 10,
                    },
                ),
                "duration": (
                    "INT",
                    {
                        "default": 20,
                        "min": 0,
                        "max": 120,
                        "step": 5,
                    },
                ),
                "speed_fpm": ("INT", {"default": 20}),
                "pulse_percussive": ("BOOLEAN", {"default": True}),
                "pulse_harmonic": ("BOOLEAN", {"default": False}),
                "pulse_react": (
                    "FLOAT",
                    {
                        "default": 0.5,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.1,
                    },
                ),
                "motion_harmonic": ("BOOLEAN", {"default": True}),
                "motion_percussive": ("BOOLEAN", {"default": False}),
                "motion_react": (
                    "FLOAT",
                    {
                        "default": 0.5,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.1,
                    },
                ),
                "fps": ("INT", {"default": 24}),
            }
        }
        return data_in

    RETURN_TYPES = (
        "STYLE_GAN_MODEL",
        "START",
        "DURATION",
        "SPEED_FPM",
        "PULSE_PERCUSSIVE",
        "PULSE_HARMONIC",
        "PULSE_REACT",
        "MOTION_HARMONIC",
        "MOTION_PERCUSSIVE",
        "MOTION_REACT",
        "FPS",
    )

    RETURN_NAMES = (
        "styleganmodel",
        "start",
        "duration",
        "speed_fpm",
        "pulse_percussive",
        "pulse_harmonic",
        "pulse_react",
        "motion_harmonic",
        "motion_percussive",
        "motion_react",
        "fps",
    )

    FUNCTION = "PassTheParam"
    CATEGORY = "🎶 LucidSonicDream"


    def PassTheParam(
        self,
        styleganmodel,
        start,
        duration,
        speed_fpm,
        pulse_percussive,
        pulse_harmonic,
        pulse_react,
        motion_harmonic,
        motion_percussive,
        motion_react,
        fps,
    ):
        return (
            styleganmodel,
            start,
            duration,
            speed_fpm,
            pulse_percussive,
            pulse_harmonic,
            pulse_react,
            motion_harmonic,
            motion_percussive,
            motion_react,
            fps,
        )



class InputParamLucidSecond:
    @classmethod
    def INPUT_TYPES(cls):
           
        #Stylegan2ModelList= ["/content/drive/MyDrive/sonic/iniasstylefinal.pkl", "/content/drive/MyDrive/sonic/DorfinalModel.pkl", "/content/drive/MyDrive/sonic/VisionaryArtm.pkl", "/content/drive/MyDrive/sonic/wikiart.pkl" , "/content/drive/MyDrive/wikiart.pkl"]


        data_in = {
            "required": {
                "styleganmodel_prev": ("STYLE_GAN_MODEL",), # This can be adjusted based on the actual data type
                "start_prev": ("START",),
                "duration_prev": ("DURATION",),
                "speed_fpm_prev": ("SPEED_FPM",),
                "pulse_percussive_prev": ("PULSE_PERCUSSIVE",),
                "pulse_harmonic_prev": ("PULSE_HARMONIC",),
                "pulse_react_prev": ("PULSE_REACT",),
                "motion_harmonic_prev": ("MOTION_HARMONIC",),
                "motion_percussive_prev": ("MOTION_PERCUSSIVE",),
                "motion_react_prev": ("MOTION_REACT",),
                "fps_prev": ("FPS",),
                "styleganmodel": (Stylegan2ModelList,),
                "rangestep": ( 
                    "INT",
                    {
                        "default": 10,
                    },
                ),
                "usenewmodel": ("BOOLEAN", {"default": False}),
                "usenewparam": ("BOOLEAN", {"default": False}),
                "duration": (
                    "INT",
                    {
                        "default": 20,
                        "min": 0,
                        "max": 120,
                        "step": 5,
                    },
                ),
                "speed_fpm": ("INT", {"default": 20}),
                "pulse_percussive": ("BOOLEAN", {"default": True}),
                "pulse_harmonic": ("BOOLEAN", {"default": False}),
                "pulse_react": (
                    "FLOAT",
                    {
                        "default": 0.5,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.1,
                    },
                ),
                "motion_harmonic": ("BOOLEAN", {"default": True}),
                "motion_percussive": ("BOOLEAN", {"default": False}),
                "motion_react": (
                    "FLOAT",
                    {
                        "default": 0.5,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.1,
                    },
                ),
                "fps": ("INT", {"default": 24}),
            }
        }
        return data_in

    RETURN_TYPES = (
        "STYLE_GAN_MODEL",
        "START",
        "DURATION",
        "SPEED_FPM",
        "PULSE_PERCUSSIVE",
        "PULSE_HARMONIC",
        "PULSE_REACT",
        "MOTION_HARMONIC",
        "MOTION_PERCUSSIVE",
        "MOTION_REACT",
        "FPS",
    )

    RETURN_NAMES = (
        "styleganmodel",
        "start",
        "duration",
        "speed_fpm",
        "pulse_percussive",
        "pulse_harmonic",
        "pulse_react",
        "motion_harmonic",
        "motion_percussive",
        "motion_react",
        "fps",
    )

    FUNCTION = "ParamUpdate"
    CATEGORY = "🎶 LucidSonicDream"


    def ParamUpdate(
        self,
        styleganmodel_prev,
        styleganmodel,
        start_prev,
        duration_prev,
        speed_fpm_prev,
        pulse_percussive_prev,
        pulse_harmonic_prev,
        pulse_react_prev,
        motion_harmonic_prev,
        motion_percussive_prev,
        motion_react_prev,
        fps_prev,
        rangestep,
        duration,
        speed_fpm,
        pulse_percussive,
        pulse_harmonic,
        pulse_react,
        motion_harmonic,
        motion_percussive,
        motion_react,
        fps,
        usenewparam,
        usenewmodel,
    ):
        
        newstart = start_prev + duration_prev - rangestep
        
        if usenewmodel:
            newmodel = styleganmodel
        else:
            newmodel = styleganmodel_prev

        if usenewparam:

            return (
                newmodel,
                newstart,
                duration,
                speed_fpm,
                pulse_percussive,
                pulse_harmonic,
                pulse_react,
                motion_harmonic,
                motion_percussive,
                motion_react,
                fps,
            )
        else:

            return (
                newmodel,
                newstart,
                duration_prev,
                speed_fpm_prev,
                pulse_percussive_prev,
                pulse_harmonic_prev,
                pulse_react_prev,
                motion_harmonic_prev,
                motion_percussive_prev,
                motion_react_prev,
                fps_prev,
            )


import cv2
import numpy as np
import torch
import requests

def video_to_frames(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    frames = []
    frame_count = 0

    # Loop until the end of the video
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        # Convert the frame to an array-like object (NumPy array)
        frame_array = np.array(frame)
        frames.append(frame_array)
        frame_count += 1
    
    # Release the video capture object
    video.release()
    
    return frames

import time
import torch
import io
import soundfile as sf

class APICallNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio" : ("AUDIO",),
                "styleganmodel": ("STYLE_GAN_MODEL",), # This can be adjusted based on the actual data type
                "start": ("START",),
                "duration": ("DURATION",),
                "speed_fpm": ("SPEED_FPM",),
                "pulse_percussive": ("PULSE_PERCUSSIVE",),
                "pulse_harmonic": ("PULSE_HARMONIC",),
                "pulse_react": ("PULSE_REACT",),
                "motion_harmonic": ("MOTION_HARMONIC",),
                "motion_percussive": ("MOTION_PERCUSSIVE",),
                "motion_react": ("MOTION_REACT",),
                "fps": ("FPS",),
                
                
                "api_url": (
                    "STRING",
                    {
                        "default": "https://667d-34-82-59-195.ngrok-free.app/run",
                    },
                ),
                "song": (
                    "STRING",
                    {
                        "default": "/content/testambiant.mp4",
                    },
                ),
                "outputfilename": (
                    "STRING",
                    {
                        "default": "/content/resultvideo1.mp4",
                    },
                ),
                 "sendaudio":("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("BYTESVID",)
    RETURN_NAMES = ("video",)
    FUNCTION = "makeApiCall"
    CATEGORY = "🎶 LucidSonicDream"

    def makeApiCall(
        self,audio, styleganmodel, start, duration, speed_fpm, pulse_percussive, pulse_harmonic, 
        pulse_react, motion_harmonic, motion_percussive, motion_react, fps, api_url, song, outputfilename, sendaudio
    ):
        # Prepare the JSON body for the GET request
        json_body = {
        #data = {
            #"song": song,
            "style": styleganmodel,
            "file_name": outputfilename,
            "start": start,
            "duration": duration,
            "speed_fpm": speed_fpm,
            "pulse_percussive": pulse_percussive,
            "pulse_harmonic": pulse_harmonic,
            "pulse_react": pulse_react,
            "motion_harmonic": motion_harmonic,
            "motion_percussive": motion_percussive,
            "motion_react": motion_react,
            "fps": fps
        }
        

        # New variables for the /run and /video endpoints
        run_url = f"{api_url}/run"
        video_url = f"{api_url}/video"

        # Add a unique query parameter to avoid cached responses
        #unique_query_param = f"timestamp={int(time.time())}"
        #full_url = f"{api_url}?{unique_query_param}"
       
        
         # Send the POST request
        if sendaudio:#audio:
            print(f"The type of the audio variable is: {type(audio)}")
            # Extract the waveform and sample rate
            waveform = audio['waveform']
            sample_rate = audio['sample_rate']

# Convert the waveform Tensor to a numpy array
            numpy_waveform = waveform.squeeze().numpy()  # Remove the batch dimension if needed

# Ensure numpy_waveform is 2D
            if numpy_waveform.ndim == 1:
                numpy_waveform = np.expand_dims(numpy_waveform, axis=0)

# Convert the numpy array to a WAV file in memory
            audio_bytes = io.BytesIO()

# Write to BytesIO
            try:
                sf.write(audio_bytes, numpy_waveform.T, sample_rate, format='WAV')  # Transpose if needed
            except Exception as e:
                print(f"Error writing to BytesIO: {e}")

            audio_bytes.seek(0)  # Move to the start of the BytesIO object



            files = {'audio_file': ('audio.wav', audio_bytes)}
            response = requests.post(run_url, data=json_body, files=files, timeout=3600) #data=data, files=files) 
        else:
            response = requests.post(run_url, data=json_body, timeout=3600)#json=json_body) 



        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            response_data = response.json()

            # Check if the message is "script initialized"
            if response_data.get("message") == "script initialized":
                print("script initialized")
            else:
                print("Unexpected message:", response_data.get("message"))
        else:
            print(f"Failed to initialize script. Status code: {response.status_code}")
        
        #added some pause because the script needs some time to initialize so no need to send get requests in the beginning
        time.sleep(120)
        
        # Initialize a flag to track when the video is received
        video_received = False

        # Loop until the video is ready
        while not video_received:
            # Send the GET request to check the video status
            response = requests.get(video_url)
    
            # Check if the request was successful
            if response.status_code == 200:
                # If the video is ready, download the video and break the loop
                video_bytes = response.content
                print("Video received")
                return (video_bytes,)
            elif response.status_code == 202:
                # If the video is not ready yet, print the message and wait
                response_data = response.json()
                print(response_data.get("message", "Video is not ready yet"))
        
                # Wait for 30 seconds before the next request
                time.sleep(30)
            else:
                # If there was an error, print the error and wait before retrying
                print(f"Failed to check video status. Status code: {response.status_code}")
                
        # Check if the request was successful older code
        #if response.status_code == 200:
         #   print("success")
          #  video_bytes = response.content

           # return (video_bytes,)
     
    #    else:
     #       raise Exception(f"API request failed with status code {response.status_code}")
        



import cv2
import os
import shutil
import tempfile
import random
import base64
from moviepy.editor import VideoFileClip, AudioFileClip

class SimpleSaveVideoNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_video_bytes": ("BYTESVID",),
                "filename_prefix": ("STRING", {"default": "video"}),
                #"save_video": ("BOOLEAN", {"default": False}),
                "output_path": ("STRING", {"default": "Downloads"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("videopath",)
    FUNCTION = "saveVideo"
    OUTPUT_NODE = True
    CATEGORY = "🎶 LucidSonicDream"

    def saveVideo(self, input_video_bytes, output_path, filename_prefix):
    # Ensure output directory exists
        if not os.path.exists(output_path):
            os.makedirs(output_path)

    # Create a temporary file to store the input video
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video_file:
            temp_video_file.write(input_video_bytes)
            temp_video_file.close()

            # Load the video
            video_clip = VideoFileClip(temp_video_file.name)
            fps = video_clip.fps

            # Generate file paths
            video_file_path = os.path.join(output_path, f"{filename_prefix}.mp4")
            #preview_video_path = os.path.join(output_path, f"{filename_prefix}_preview.mp4")

            # Add audio if available
            temp_audio_file = temp_video_file.name.replace(".mp4", ".mp3")
            if os.path.exists(temp_audio_file):
                audio_clip = AudioFileClip(temp_audio_file)
                video_clip = video_clip.set_audio(audio_clip)

        # Always save and display the preview video
            #video_clip.write_videofile(preview_video_path, fps=fps)
            #print(f"Video preview saved to {preview_video_path}")

        # Optionally save the final video
            #if save_video:
            video_clip.write_videofile(video_file_path, fps=fps)
            print(f"Video saved to {video_file_path}")

        # Clean up the temporary file
            os.remove(temp_video_file.name)
            if os.path.exists(temp_audio_file):
                os.remove(temp_audio_file)

        # Return the path to the preview video and optionally the saved video
            #result_paths = [preview_video_path]
            #if save_video:
             #   result_paths.append(video_file_path)

        #return {"ui": {"video": result_paths}}
        prefix = "F:\\Users\\inias\\AI\\ComfyUI\\ComfyUI_test\\ComfyUI\\"
        full_path = prefix + video_file_path
        print(full_path)
        print(video_file_path)

        # Pause the program for 1 second
        time.sleep(2)
        return (str(full_path),)

    


        
        


