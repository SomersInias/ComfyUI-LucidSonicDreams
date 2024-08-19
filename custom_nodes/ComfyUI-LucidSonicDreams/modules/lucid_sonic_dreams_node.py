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






