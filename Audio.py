# Importing modules
from captcha.audio import AudioCaptcha

# Creating an audio object
audio = AudioCaptcha()

# Audio captcha text
captcha_text = "1223"

# generate the audio of the given text
audio_data = audio.generate(captcha_text)

# Naming the audio file
audio_file = "audio" + captcha_text + '.wav'

# writing the audio file and saving it
audio.write(captcha_text, audio_file)
