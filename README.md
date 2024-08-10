# STRAT: Screen Translation and Real-Time Audio Text-to-Speech:
This Python project provides real-time translation of text captured from your screen and converts it into speech. Using OCR (Optical Character Recognition) and translation APIs, the tool identifies text within a user-specified screen region, translates it into a target language, and plays the translated text using a text-to-speech model.

# Features
- Multiple Voice Support: Allows users to select different voices for text-to-speech conversion.
- OCR and Translation: Utilizes Tesseract for OCR and Google Translator for language translation.
- Audio Playback: Uses playsound to play the generated speech audio.
- Flexible Language Selection: Supports up to [16 languages](#Languages) for speech output.

# Setup (only on Python 3.8-3.11)
1. Clone this git repository.
2. If you haven't already install nvcc : https://developer.nvidia.com/cuda-downloads .
3. run setup.bat .
4. Install the appropriate version of pytorch for cuda by running setupCuda.bat (replace the url in the .bat file with the appropriate version)
5. Download and setup Tesseract OCR (Note the installation path.) : https://digi.bib.uni-mannheim.de/tesseract/
6. Run "run.bat".

# Usage:
1. Run "run.bat".
2. If prompted, enter the Tesseract installation path.
3. Choose a voice from the available options.
4. Select a target language for translation.
5. Position the mouse at the top-left and bottom-right corners of the region to capture. ![howto](https://github.com/user-attachments/assets/3127470a-c7bc-48ba-8478-8b7538b5b076)
6. Press the alt key to capture text, translate it, and hear the output.

# Voice cloning:
1. Record at least a 30-second long sample of your voice.
2. Save the recording as a .wav file.
3. Place the .wav file in the targets directory.

# Languages
- "Arabic": "ar",
- "Chinese": "zh-cn",
- "Czech": "cs",
- "Dutch": "nl",
- "English": "en",
- "French": "fr",
- "German": "de",
- "Hungarian": "hu",
- "Italian": "it",
- "Japanese": "ja",
- "Korean": "ko",
- "Polish": "pl",
- "Portuguese": "pt",
- "Russian": "ru",
- "Spanish": "es",
- "Turkish": "tr"

# Model 
The model used is `tts_models/multilingual/multi-dataset/xtts_v2`. For more details, refer to [Hugging Face - XTTS-v2](https://huggingface.co/coqui/XTTS-v2) and its specific version [XTTS-v2 Version 2.0.2](https://huggingface.co/coqui/XTTS-v2/tree/v2.0.2).

# Credits
- Heavily based on https://github.com/kanttouchthis/text_generation_webui_xtts/ and https://github.com/BoltzmannEntropy/xtts2-ui

# Author
Created by Máté Jakus
