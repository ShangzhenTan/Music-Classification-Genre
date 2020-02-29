# Music-Classification-Genre


## Packages:
Python 3, SciPy, Soundfile, Numpy, Matplotlib


## Dataset:
### Brief
* The Free Music Archive (FMA) dataset was used for this project: https://github.com/mdeff/fma
* The dataset consists of legally free songs and rich metadata 

### Details:
* The datset consists of 30 second clips from 8000 songs in 8 genres
* All tracks are mp3-encoded, most of them with sampling rate of 44,100 Hz, bit rate 320 kbit/s (263 kbit/s on average)
* The metadata is in csv files which contains various information about the songs such as artist, genre, and record date
* Many features have been pre-computed like the Mel-Frequency Cepstral Coefficients (MFCC), Tempo, and Root Mean Square Energy (RMSE)
* Details about the FMA dataset can be found in the official [paper](https://arxiv.org/pdf/1612.01840.pdf)
* Please download the small compressed dataset file ([fma_small.zip](https://os.unil.cloud.switch.ch/fma/fma_small.zip)) which is 7.2 GB
* Please download the meta-data and features for all tracks ([fma_metadata.zip](https://os.unil.cloud.switch.ch/fma/fma_metadata.zip)) which is 342 MB


