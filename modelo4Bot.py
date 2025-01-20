# Criar uma IA baseada em regras para RPG.
# Essa abordagem envolve usar regras pré-definidas e bibliotecas como 'random'
# para decisões aleatórias (exemplo: simulação de dados).

# Ferramentas para automação de RPG como Roll20 API ou Foundry VTT.
# Você pode usar essas plataformas para criar scripts personalizados.

# Para gerar áudio com as respostas da IA:
# 1. Use o pacote gTTS (Google Text-to-Speech).
#    pip install gTTS

from gtts import gTTS
import os

# Texto gerado pela IA
texto_ia = "Você entrou em uma caverna escura. Ao longe, você ouve o som de correntes..."

# Converter texto em fala
tts = gTTS(texto_ia, lang='pt')  # 'pt' para português
tts.save("resposta.mp3")

# Reproduzir o áudio
os.system("start resposta.mp3")  # No Windows, use 'start'