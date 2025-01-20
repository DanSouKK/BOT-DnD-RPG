# Opção 1: Usar o OpenAI API para integrar um modelo GPT-3 ou GPT-4 como mestre de RPG.

# Passos iniciais para usar o OpenAI API:
# 1. Acesse o site da OpenAI e crie uma conta.
# 2. Obtenha sua chave de API.
# 3. Instale o pacote 'openai' no Python:
#    pip install openai

import openai

# Configure sua chave de API
openai.api_key = 'sua-chave-api-aqui'

# Exemplo de solicitação à API OpenAI
response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    prompt="Você é o mestre de um jogo de RPG. Descreva uma caverna misteriosa que os jogadores estão explorando.",
    max_tokens=150
)

# Exibe a resposta da IA
print(response.choices[0].text.strip())
