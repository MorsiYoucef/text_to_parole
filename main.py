from gtts import gTTS
import os

# Texte que vous souhaitez convertir en parole
texte = "my name is joseph"

# Créer un objet gTTS
tts = gTTS(text=texte, lang='en')  # 'fr' pour le français, vous pouvez changer la langue

# Enregistrer le fichier audio
tts.save("output.mp3")

# Lire le fichier audio en utilisant le lecteur par défaut
os.system("start output.mp3")