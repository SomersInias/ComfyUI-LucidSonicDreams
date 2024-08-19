import requests


class InputParamLucid:
    @classmethod
    def INPUT_TYPES(cls):
           
        Stylegan2ModelList= ["model1", "model2", "model3"]


        data_in = {
            "required": {
                "model": (Stylegan2ModelList,),
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
                        "step": 10,
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
        "MODEL",
        "INT",
        "INT",
        "INT",
        "BOOLEAN",
        "BOOLEAN",
        "FLOAT",
        "BOOLEAN",
        "BOOLEAN",
        "FLOAT",
        "INT",
    )

    RETURN_NAMES = (
        "model",
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
        model,
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
            model,
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



import requests

class APICallNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),  # This can be adjusted based on the actual data type
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
            }
        }

    RETURN_TYPES = ("VIDEO",)
    RETURN_NAMES = ("video",)
    FUNCTION = "makeApiCall"
    CATEGORY = "🎶 LucidSonicDream"

    def makeApiCall(
        self, model, start, duration, speed_fpm, pulse_percussive, pulse_harmonic, 
        pulse_react, motion_harmonic, motion_percussive, motion_react, fps, api_url, song
    ):
        # Prepare the JSON body for the GET request
        json_body = {
            "song": song,
            "style": "/content/drive/MyDrive/sonic/iniasstylefinal.pkl",
            "file_name": "/content/beet3.mp4",
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

        # Send the GET request
        response = requests.get(api_url, json=json_body)

        if response.status_code == 200:
            video = response.content
            return (video,)
        else:
            raise Exception(f"API request failed with status code {response.status_code}")


