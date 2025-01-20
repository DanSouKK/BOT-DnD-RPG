# Para capturar áudio de entrada e convertê-lo em texto:
# 1. Instale o pacote SpeechRecognition.
#    pip install SpeechRecognition

import speech_recognition as sr

# Inicializar o reconhecedor
recognizer = sr.Recognizer()

# Capturar áudio do microfone
with sr.Microphone() as source:
    print("Fale algo...")
    audio = recognizer.listen(source)

# Converter o áudio em texto
try:
    text = recognizer.recognize_google(audio, language="pt-BR")
    print("Você disse: " + text)
except sr.UnknownValueError:
    print("Não foi possível entender o áudio.")
except sr.RequestError:
    print("Erro ao conectar com o serviço de reconhecimento de fala.")

# Integração Completa:
# Passos para integrar texto, áudio e IA:
# 1. Capture áudio do usuário com SpeechRecognition.
# 2. Converta o áudio em texto.
# 3. Envie o texto para a API OpenAI para obter uma resposta.
# 4. Converta a resposta da IA em áudio com gTTS.
# 5. Reproduza o áudio para o usuário.
