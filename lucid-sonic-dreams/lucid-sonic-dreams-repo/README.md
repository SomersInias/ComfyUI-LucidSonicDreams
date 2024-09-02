# Lucid Sonic Dreams
Lucid Sonic Dreams syncs GAN-generated visuals to music!

By default, it uses [NVLabs StyleGAN2-ada-pytorch](https://github.com/NVlabs/stylegan2-ada-pytorch).
It can also use pre-trained models lifted from [Justin Pinkney's consolidated repository](https://github.com/justinpinkney/awesome-pretrained-stylegan2), but
these are untested.

"save_frames" is no longer used as this version works in RAM and doesn't save frames to disk.

Sample output can be found on [YouTube](https://www.youtube.com/watch?v=SDf7a28cSVs).

## Installation  
  
This implementation has been tested on Python 3.9. It now uses the PyTorch implementation of StyleGAN2-ada, and works with Ampere cards.

To install:
git clone this repo and change directory into your newly created directory:

```
git clone https://github.com/nerdyrodent/lucid-sonic-dreams.git
cd lucid-sonic-dreams
```

It is suggested that Anaconda or Miniconda be used to create a new, virtual Python environment with a name of your choice. For example:

```
conda create --name sonicstylegan-pt python=3.9
conda activate sonicstylegan-pt
```

Install the packages required for both stylegan2-ada-pytorch and this repo:

```
pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
pip install click requests ninja imageio imageio-ffmpeg tqdm psutil scipy pyspng
```

(Optional) If you already have stylegan2-ada-pytorch (recommended for training your own networks), create a symbolic link to it:

`ln -s ../stylegan2-ada-pytorch stylegan2`


## Usage

Refer to the [Lucid Sonic Dreams Tutorial Notebook](https://colab.research.google.com/drive/1Y5i50xSFIuN3V4Md8TB30_GOAtts7RQD?usp=sharing) for full parameter descriptions and sample code templates. A basic visualization snippet is also found below.

### Basic Visualization

```
from lucidsonicdreams import LucidSonicDream


L = LucidSonicDream(song = 'song.mp3',
                    style = 'abstract photos')

L.hallucinate(file_name = 'song.mp4') 
```
sg2-ada-pt-song-spleeter.py is an example with a variety of configuration options as defaults, based on the audio being split into 4 stems using spleeter - https://github.com/deezer/spleeter

