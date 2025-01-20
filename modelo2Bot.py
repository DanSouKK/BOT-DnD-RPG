
# Opção 2: Usar alternativas Open Source como GPT-Neo ou GPT-J da EleutherAI.

# Como usar GPT-Neo com Python:
# 1. Instale o pacote 'transformers':
#    pip install transformers

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Carregando o modelo e o tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = GPT2LMHeadModel.from_pretrained("EleutherAI/gpt-neo-1.3B")

# Gerando texto com o modelo
inputs = tokenizer(
    "Você é o mestre de um jogo de RPG. Descreva um monstro que aparece diante dos aventureiros.",
    return_tensors="pt"
)
outputs = model.generate(**inputs, max_length=150)

# Exibe o texto gerado
print(tokenizer.decode(outputs[0], skip_special_tokens=True))