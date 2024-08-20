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
        unique_query_param = f"timestamp={int(time.time())}"
        full_url = f"{api_url}?{unique_query_param}"
       
         # Send the POST request
        response = requests.post(full_url, json=json_body)

        # Check if the request was successful
        if response.status_code == 200:
            print("success")
            video_bytes = response.content

            return (video_bytes,)
     
        else:
            raise Exception(f"API request failed with status code {response.status_code}")
        



import cv2
import os
import shutil
import tempfile
import random
from moviepy.editor import VideoFileClip, AudioFileClip

class SimpleSaveVideoNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_video_bytes": ("BYTESVID",),
                "filename_prefix": ("STRING", {"default": "video"}),
                "save_video": ("BOOLEAN", {"default": False}),
                "output_path": ("STRING", {"default": "Downloads"}),
            }
        }

    RETURN_TYPES = ("VIDEOVID",)
    RETURN_NAMES = ("video",)
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

            # Save and display the preview video
            video_clip.write_videofile(preview_video_path, fps=fps)
            file_name = preview_video_path  # For UI display

            # Optionally save the final video
            if save_video:
                video_clip.write_videofile(video_file_path, fps=fps)
                file_name = video_file_path  # Update for final video

            # Clean up the temporary files
            os.remove(temp_video_file.name)
            if os.path.exists(temp_audio_file):
                os.remove(temp_audio_file)

            

# Open the video file
            print("This is printed immediately.")
            time.sleep(5)  # Wait for 2 seconds
            print("This is printed after a 2-second delay.")
            print(video_file_path)
            cap = cv2.VideoCapture(video_file_path)

# Check if video opened successfully
            if not cap.isOpened():
                print("Error: Could not open video.")
                exit()

# Read and display the video frames
            while cap.isOpened():
                ret, frame = cap.read()
    
                if not ret:
                    print("Reached the end of the video.")
                    break
    
    # Display the frame
                cv2.imshow('Video', frame)
    
    # Press 'q' to exit the video
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

# Release the video capture object and close all windows
            cap.release()
            cv2.destroyAllWindows()

        # Return the path to the preview video or final video for UI display
        return (video_clip,)
    






    #test


import os
import tempfile
import shutil
from moviepy.editor import VideoFileClip, AudioFileClip
import random
import cv2
import numpy as np
from PIL import Image

class SaveVideoTEST:
    def __init__(self):
        self.type = "output"

    @classmethod
    def INPUT_TYPES(s):
        frames_output_dir = "frames_output"
        try:
            shutil.rmtree(frames_output_dir)
            os.mkdir(frames_output_dir)
        except:
            pass

        return {
            "required": {
                "input_video_bytes": ("BYTESVID",),
                "SaveVideo": ("BOOLEAN", {"default": False}),
                "SaveFrames": ("BOOLEAN", {"default": False}),
                "filename_prefix": ("STRING", {"default": "video"}),
                "CompressionLevel": ("INT", {"default": 2, "min": 0, "max": 9, "step": 1}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    RETURN_TYPES = ("VIDEOVID",)
    RETURN_NAMES = ("video",)
    FUNCTION = "save_video2"
    OUTPUT_NODE = True
    CATEGORY = "🎶 LucidSonicDream"

    def save_video2(self, input_video_bytes, SaveVideo, SaveFrames, filename_prefix, CompressionLevel, prompt=None, extra_pnginfo=None):
        videos_output_dir = "videos_output"
        video_preview_output_temp_dir = "video_preview_output_temp"
        frames_output_dir = "frames_output"
        os.makedirs(videos_output_dir, exist_ok=True)
        os.makedirs(video_preview_output_temp_dir, exist_ok=True)
        os.makedirs(frames_output_dir, exist_ok=True)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video_file:
            temp_video_file.write(input_video_bytes)
            temp_video_file.close()

            video_clip = VideoFileClip(temp_video_file.name)

            # Extract frames
            cap = cv2.VideoCapture(temp_video_file.name)
            frame_count = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                if SaveFrames:
                    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                    img.save(os.path.join(frames_output_dir, f"frame_{frame_count:05d}.png"), compress_level=CompressionLevel)
                frame_count += 1
            cap.release()

            self.video_file_path = os.path.join(videos_output_dir, f"{filename_prefix}.mp4")

            temp_audio_file = temp_video_file.name.replace(".mp4", ".mp3")
            if os.path.exists(temp_audio_file):
                audio_clip = AudioFileClip(temp_audio_file)
                video_clip = video_clip.set_audio(audio_clip)

            if SaveVideo:
                video_clip.write_videofile(self.video_file_path)
                file_name = os.path.basename(self.video_file_path)
            else:
                for file in os.listdir(video_preview_output_temp_dir):
                    if file.startswith("video_preview"):
                        os.remove(os.path.join(video_preview_output_temp_dir, file))
                
                suffix = str(random.randint(1, 100000))
                file_name = f"video_preview_{suffix}.mp4"
                preview_path = os.path.join(video_preview_output_temp_dir, file_name)
                video_clip.write_videofile(preview_path)

            os.remove(temp_video_file.name)
            if os.path.exists(temp_audio_file):
                os.remove(temp_audio_file)

        return video_clip
    




def extract_frames_from_video(video_path, output_folder=None, target_fps=30, use_ram=True):
    frames = []
    list_files = []
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    # Ottieni il framerate originale del video
    original_fps = int(cap.get(cv2.CAP_PROP_FPS))
    # Calcola il rapporto per ridurre il framerate
    frame_skip_ratio = original_fps // target_fps
    real_frame_count = 0
  
    if not use_ram:
        if output_folder is None:
            raise ValueError("output_folder must be specified if use_ram is False")
    if output_folder is not None:
        os.makedirs(output_folder, exist_ok=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # Estrai solo ogni "frame_skip_ratio"-esimo fotogramma
        if frame_count % frame_skip_ratio == 0:
            if use_ram:
                frames.append(frame)
            else:
                frame_filename = os.path.join(output_folder, f"{frame_count:07d}.png")
                list_files.append(frame_filename)
                cv2.imwrite(frame_filename, frame)
            real_frame_count += 1



import folder_paths

input_dir = os.path.join(folder_paths.get_input_directory(),"n-suite")
output_dir = os.path.join(folder_paths.get_output_directory(),"n-suite","frames_out")
temp_output_dir = os.path.join(folder_paths.get_temp_directory(),"n-suite","frames_out")
frames_output_dir = os.path.join(folder_paths.get_temp_directory(),"n-suite","frames")
videos_output_dir = os.path.join(folder_paths.get_output_directory(),"n-suite","videos")
audios_output_temp_dir = os.path.join(folder_paths.get_temp_directory(),"audio.mp3")
videos_output_temp_dir = os.path.join(folder_paths.get_temp_directory(),"video.mp4")
video_preview_output_temp_dir = os.path.join(folder_paths.get_output_directory(),"n-suite","videos")
_resize_type = ["none","width", "height"]
_framerate = ["original","half", "quarter"]
_choice = ["Yes", "No"]
try:
    os.makedirs(input_dir)
except:
    pass


class LoadVideotest:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {"required": {"video": ("VIDEOVID",), 
                            "local_url": ("STRING",  {"default": ""} ),  
                            "framerate": (_framerate, {"default": "original"} ), 
                            "resize_by": (_resize_type,{"default": "none"} ),
                              "size": ("INT", {"default": 512, "min": 512, "step": 64}),
                              "images_limit": ("INT", {"default": 0, "min": 0, "step": 1}),
                              "batch_size": ("INT", {"default": 0, "min": 0, "step": 1}),
                              "starting_frame": ("INT", {"default": 0, "min": 0, "step": 1}), 
                              "autoplay":("BOOLEAN",{"default": True} ),
                              "use_ram": ("BOOLEAN", {"default": False}),

                            },}


    RETURN_TYPES = ()
    OUTPUT_IS_LIST = (True, True, False, False,False,False,False, )   
    CATEGORY = "🎶 LucidSonicDream"
    FUNCTION = "load_video"
   


    def load_video(self, video, framerate, local_url, use_ram):
        file_path = folder_paths.get_annotated_filepath(os.path.join("n-suite", video))
        cap = cv2.VideoCapture(file_path)
        # Check if the video was opened successfully
        if not cap.isOpened():
            print("Unable to open the video.")
        else:
            # Get the FPS of the video
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            print(f"The video has {fps} frames per second.")

        try:
            shutil.rmtree(os.path.join(temp_output_dir, video.split(".")[0]))
        except:
            print("Video Path already deleted")

        full_temp_output_dir = os.path.join(temp_output_dir, video.split(".")[0])
        
        # Set new framerate
        if "half" in framerate:
            fps = fps // 2
            print(f"The video has been reduced to {fps} frames per second.")
        elif "quarter" in framerate:
            fps = fps // 4
            print(f"The video has been reduced to {fps} frames per second.")

        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension in [".mp4", ".webm"]:
            list_files = extract_frames_from_video(file_path, full_temp_output_dir, fps, use_ram)
            
            audio_clip = VideoFileClip(file_path).audio
            try:
                # Save audio
                audio_clip.write_audiofile(os.path.join(temp_output_dir, video.split(".")[0], "audio.mp3"))
            except:
                print("Could not save audio")
                pass      
        else:
            print("Format not supported. Please provide an MP4 or GIF file.")

        return list_files, fps


        
        


