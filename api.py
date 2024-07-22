import pyautogui as pyautogui
import torch
import platform
import random
import json
from pathlib import Path
from TTS.api import TTS
import uuid
import html
import soundfile as sf
from playsound import playsound
import keyboard
from pytesseract import pytesseract
import cv2
from deep_translator import GoogleTranslator

def is_mac_os():
    return platform.system() == 'Darwin'

params = {
    "activate": True,
    "autoplay": True,
    "show_text": False,
    "remove_trailing_dots": False,
    "voice": "Rogger.wav",
    "language": "English",
    "model_name": "tts_models/multilingual/multi-dataset/xtts_v2",
}

# SUPPORTED_FORMATS = ['wav', 'mp3', 'flac', 'ogg']
SAMPLE_RATE = 16000
device = None

# Set the default speaker name
default_speaker_name = "Rogger"

if is_mac_os():
    device = torch.device('cpu')
else:
    device = torch.device('cuda:0')

# Load model
tts = TTS(model_name=params["model_name"]).to(device)

def gen_voice(string, spk, speed, english):
    string = html.unescape(string)
    short_uuid = str(uuid.uuid4())[:8]
    fl_name='outputs/' + spk + "-" + short_uuid +'.wav'
    output_file = Path(fl_name)
    this_dir = str(Path(__file__).parent.resolve())
    tts.tts_to_file(
        text=string,
        speed=speed,
        file_path=output_file,
        speaker_wav=[f"{this_dir}/targets/" +spk + ".wav"],
        language=languages[english]
    )
    return output_file
def update_speakers():
    speakers = {p.stem: str(p) for p in list(Path('targets').glob("*.wav"))}
    return list(speakers.keys())
try:
    with open("pytess.save", "r+") as pytessSav:
        lines = pytessSav.readlines()
        if len(lines) > 0:
            pytessPATH = lines[0].strip()
        else:
            pytessPATH = input("Please insert the location of the pytesseract terminal (Example: C:\\Program Files\\Tesseract-OCR\\tesseract.exe): ")
            pytessSav.write(pytessPATH + '\n')
except FileNotFoundError:
    with open("pytess.save", "w") as pytessSav:
        pytessPATH = input("Please insert the location of the pytesseract terminal (Example: C:\\Program Files\\Tesseract-OCR\\tesseract.exe): ")
        pytessSav.write(pytessPATH + '\n')

emberek = update_speakers()
for em in emberek:
    print (em)
ember = input("Voice: ")

#Set region
print("Please set the scann region by moving your mouse to the top left and bottom right corners of the area and then press the alt key.")
poses = []
while len(poses) != 2:
    key = keyboard.read_key()
    if (key == 'alt'):
        poses.append(pyautogui.position())
        try:
            playsound("click-button-app-147358.wav")
        except:
            pass
        print(pyautogui.position())
        print(len(poses))
print(f"left:{poses[0].x} top:{poses[0].y} {poses[1].x - poses[0].x} {poses[1].y - poses[0].y}")


# Load the language data
with open(Path('languages.json'), encoding='utf8') as f:
    languages = json.load(f)
langs = []
for lang in languages:
    langs.append(lang)
for lang in range(0, len(langs)-1):
    print(f"{lang+1}. {langs[lang]}")
langnum = int(input("Please select the target language (number): ")) -1
pytesseract.tesseract_cmd = pytessPATH
pytessSav.close()
lang_short = [
"ar",
  "zh-cn",
  "cs",
  "nl",
  "en",
  "fr",
  "de",
  "hu",
  "it",
  "ja",
  "ko",
  "pl",
    "pt",
"ru",
  "es",
  "tr"
]
welcome = [
    "alnamudhaj jahizi! liltarjamati, adghat ealaa miftah alt baed alsaafirati.",
    "Móxíng zhǔnbèi hǎole! Yào jìnxíng fānyì, qǐng zài tīng dào fēng míng shēng hòu àn alt jiàn.",
    "Model je připraven! Chcete-li přeložit, stiskněte po pípnutí klávesu alt.",
    "Het model is klaar! Om te vertalen drukt u na de pieptoon op de alt-toets.",
    "The model is ready! To translate, press the alt key after the beep.",
    "Le modèle est prêt ! Pour traduire, appuyez sur la touche Alt après le bip.",
    "Das Modell ist fertig! Zum Übersetzen drücken Sie nach dem Signalton die Alt-Taste.",
    "A modell készen áll! A fordításhoz nyomja meg az alt gombot a hangjelzés után.",
    "Il modello è pronto! Per tradurre, premere il tasto Alt dopo il segnale acustico.",
    "Moderu no junbi ga dekimashita! Hon'yaku suru ni wa, bīpu-on no nochi ni aruto kī o oshimasu.",
    "model-i junbidoeeossseubnida! beon-yeoghalyeomyeon gyeong-go-eum-i ullin hu Alt kileul nuleuseyo.",
    "Model jest gotowy! Aby przetłumaczyć, naciśnij klawisz alt po sygnale dźwiękowym.",
    "O modelo está pronto! Para traduzir, pressione a tecla Alt após o sinal sonoro.",
    "Model' gotova! Dlya perevoda nazhmite klavishu Alt posle zvukovogo signala.",
    "¡El modelo está listo! Para traducir, presione la tecla alt después del pitido.",
    "Model hazır! Çevirmek için bip sesinden sonra alt tuşuna basın."
]
playsound(gen_voice(welcome[langnum], ember, 0.8, langs[langnum]))
try:
    playsound("click-button-app-147358.wav")
except:
    pass

while True:
    key = keyboard.read_key()
    if (key == 'alt'):
        image = pyautogui.screenshot(region=(poses[0].x, poses[0].y, (poses[1].x - poses[0].x), (poses[1].y - poses[0].y)))
        words = pytesseract.image_to_string(image)
        wordsl = str.split(words,"\n")
        words = ""
        for word in wordsl:
            words = f"{words} {word}"
        translated = GoogleTranslator(source='auto', target=lang_short[langnum]).translate(words)
        print(translated)
        playsound(gen_voice(translated, ember, 0.8, langs[langnum]))
    