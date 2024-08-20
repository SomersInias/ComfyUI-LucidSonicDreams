import requests


class InputParamLucid:
    @classmethod
    def INPUT_TYPES(cls):
           
        Stylegan2ModelList= ["/content/drive/MyDrive/sonic/iniasstylefinal.pkl", "/content/drive/MyDrive/sonic/DorfinalModel.pkl", "/content/drive/MyDrive/sonic/VisionaryArtm.pkl", "/content/drive/MyDrive/sonic/wikiart.pkl"]


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

class APICallNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
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
            }
        }

    RETURN_TYPES = ("BYTESVID",)
    RETURN_NAMES = ("video",)
    FUNCTION = "makeApiCall"
    CATEGORY = "🎶 LucidSonicDream"

    def makeApiCall(
        self, styleganmodel, start, duration, speed_fpm, pulse_percussive, pulse_harmonic, 
        pulse_react, motion_harmonic, motion_percussive, motion_react, fps, api_url, song, outputfilename
    ):
        # Prepare the JSON body for the GET request
        json_body = {
            "song": song,
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

        # Add a unique query parameter to avoid cached responses
        #unique_query_param = f"timestamp={int(time.time())}"
        #full_url = f"{api_url}?{unique_query_param}"
       
         # Send the POST request
        response = requests.post(api_url, json=json_body)

        # Check if the request was successful
        if response.status_code == 200:
            print("success")
            video_bytes = response.content

            return (video_bytes,)
     
        else:
            raise Exception(f"API request failed with status code {response.status_code}")
        




import os
import tempfile
from moviepy.editor import VideoFileClip, AudioFileClip

class SimpleSaveVideoNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_video_bytes": ("BYTESVID",),
                "filename_prefix": ("STRING", {"default": "video"}),
                "save_video": ("BOOLEAN",{"default": False} ),
                "output_path": ("STRING", {"default": "Downloads"}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "saveVideo"
    OUTPUT_NODE = True
    CATEGORY = "🎶 LucidSonicDream"

    
    def saveVideo(self, input_video_bytes, output_path, save_video, filename_prefix):
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
            preview_video_path = os.path.join(output_path, f"{filename_prefix}_preview.mp4")

            # Add audio if available
            temp_audio_file = temp_video_file.name.replace(".mp4", ".mp3")
            if os.path.exists(temp_audio_file):
                audio_clip = AudioFileClip(temp_audio_file)
                video_clip = video_clip.set_audio(audio_clip)

        # Always save and display the preview video
            video_clip.write_videofile(preview_video_path, fps=fps)
            print(f"Video preview saved to {preview_video_path}")

        # Optionally save the final video
            if save_video:
                video_clip.write_videofile(video_file_path, fps=fps)
                print(f"Video saved to {video_file_path}")

        # Clean up the temporary file
            os.remove(temp_video_file.name)
            if os.path.exists(temp_audio_file):
                os.remove(temp_audio_file)

        # Return the path to the preview video and optionally the saved video
            result_paths = [preview_video_path]
            if save_video:
                result_paths.append(video_file_path)

        return {"ui": {"video": result_paths}}

        
        


