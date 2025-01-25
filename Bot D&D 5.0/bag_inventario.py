import random

# Dicionário de itens com peso e descrição
itens_disponiveis = {
    "poção de cura pequena": {"peso": 0.5, "descricao": "Restaura 10 pontos de vida"},
    "poção de mana pequena": {"peso": 0.5, "descricao": "Restaura 10 pontos de mana"},
    "erva medicinal": {"peso": 0.2, "descricao": "Pode ser usada para preparar curativos"},
    "pedra de amolar": {"peso": 1.0, "descricao": "Útil para afiar armas"},
    "tocha": {"peso": 0.5, "descricao": "Ilumina ambientes escuros"},
    "corda": {"peso": 2.0, "descricao": "Útil para escalar ou prender algo"},
    "rações de viagem": {"peso": 1.5, "descricao": "Alimento para dias de jornada"},
    "pergaminho em branco": {"peso": 0.1, "descricao": "Usado para escrever magias ou mensagens"},
    "pederneira": {"peso": 0.3, "descricao": "Ajuda a fazer fogo"},
}

class Inventario:
    def __init__(self, capacidade_maxima=int(input("Digite o tamanho da mochila: "))):        
        # Inicializa o inventário com capacidade máxima definida pelo usuário.
        # :param capacidade_maxima: Limite de peso que a mochila pode carregar   
             
        self.itens = {}  # Dicionário para armazenar itens e suas quantidades
        self.capacidade_maxima = capacidade_maxima  # Limite máximo de peso
        self.peso_atual = 0.0  # Peso atual dos itens na mochila
    
    def adicionar_item(self, item, quantidade=1):
        
        # Adiciona um item ao inventário, verificando peso e disponibilidade.        
        # Verificar se o item existe na lista de itens disponíveis
        if item not in itens_disponiveis:
            print(f"Item {item} não existe!")
            return False
        
        # Calcular peso total a ser adicionado
        peso_item = itens_disponiveis[item]["peso"]
        peso_total = peso_item * quantidade
        
        # Verificar capacidade do inventário
        if self.peso_atual + peso_total > self.capacidade_maxima:
            print("\nInventário cheio! Não é possível adicionar o item.")
            return False
        
        # Adicionar item ao inventário
        if item in self.itens:
            self.itens[item] += quantidade
        else:
            self.itens[item] = quantidade
        
        # Atualizar peso
        self.peso_atual += peso_total
        print(f"{quantidade}x {item} adicionado(a) ao inventário.")
        return True
    
    def remover_item(self, item, quantidade=1):
        # Remove um item do inventário.        
        if item not in self.itens:
            print(f"Item {item} não encontrado no inventário.")
            return False
        
        if self.itens[item] < quantidade:
            print(f"Quantidade insuficiente de {item} no inventário.")
            return False
        
        # Calcular peso a ser removido
        peso_item = itens_disponiveis[item]["peso"]
        peso_total = peso_item * quantidade
        
        # Remover item
        self.itens[item] -= quantidade
        if self.itens[item] == 0:
            del self.itens[item]
        
        # Atualizar peso
        self.peso_atual -= peso_total
        print(f"{quantidade}x {item} removido(a) do inventário.")
        return True
    
    def listar_itens(self):
        
        # Lista todos os itens no inventário com suas descrições e quantidades.
        print("\n--- Inventário ---")
        if not self.itens:
            print("\nInventário vazio.")
            return
        
        for item, quantidade in self.itens.items():
            descricao = itens_disponiveis[item]["descricao"]
            print(f"{item} (x{quantidade}): {descricao}")
        
        print(f"\nPeso atual: {self.peso_atual:.1f}/{self.capacidade_maxima}")
    
    def aumentar_capacidade(self, adicional):
        
        # Aumenta a capacidade máxima do inventário.
        try:
            adicional = float(adicional)
            if adicional <= 0:
                print("A capacidade adicional deve ser um número positivo.")
                return False
            
            self.capacidade_maxima += adicional
            print(f"Capacidade do inventário aumentada para {self.capacidade_maxima}")
            return True
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")
            return False
    
    def diminui_capacidade(self, adicional):
        
        # Reduz a capacidade máxima do inventário com validações de segurança.
        # param adicional: Quantidade a ser removida da capacidade
              
        try:
            adicional = float(adicional)
            if adicional <= 0:
                print("A capacidade a ser reduzida deve ser um número positivo.")
                return False
            
            # Calcular a nova capacidade proposta
            nova_capacidade = self.capacidade_maxima - adicional
            
            # Verificar se a nova capacidade é menor que o peso atual dos itens
            if nova_capacidade < self.peso_atual:
                print("Não é possível reduzir a capacidade. Os itens atuais excedem a nova capacidade.")
                print(f"Peso atual dos itens: {self.peso_atual}")
                print(f"Capacidade atual: {self.capacidade_maxima}")
                return False
            
            # Verificar se há espaço vazio na mochila para reduzir
            espaco_vazio = self.capacidade_maxima - self.peso_atual
            if adicional > espaco_vazio:
                print("\nNão é possível reduzir mais do que o espaço vazio na mochila.")
                print(f"Espaço VAZIO atual: {espaco_vazio}")
                return False
            
            # Se passou por todas as verificações, reduz a capacidade
            self.capacidade_maxima = nova_capacidade
            print(f"Capacidade do inventário reduzida para {self.capacidade_maxima}")
            return True
        
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")
            return False
    
    def encontrar_item_aleatorio(self):
        
        # Seleciona um item aleatório da lista de itens disponíveis.            
        
        item = random.choice(list(itens_disponiveis.keys()))
        return item

def menu_inventario(inventario):
    
    # Menu interativo para gerenciamento do inventário.      
    while True:
        print("\n==========================")
        print("======Mochila Aberta======")
        print("==========================\n")        
        print("1. Adicionar Item")
        print("2. Remover Item")
        print("3. Listar Itens")
        print("4. Adicionar Item Aleatório")
        print("5. Modificar mochila")
        print("6. Voltar")
        
        escolha = input("Escolha uma opção: ")
        
        # Tratamento das opções do menu principal
        if escolha == '1':
            print("\nItens disponíveis:")
            for item in itens_disponiveis:
                print(item)
            item = input("\nDigite o nome do item para adicionar: ")
            try:
                quantidade = int(input("Digite a quantidade: "))
                inventario.adicionar_item(item, quantidade)
            except ValueError:
                print("\nPor favor, insira uma quantidade válida.")
        
        elif escolha == '2':
            item = input("\nDigite o nome do item para remover: ")
            try:
                quantidade = int(input("Digite a quantidade: "))
                inventario.remover_item(item, quantidade)
            except ValueError:
                print("\nPor favor, insira uma quantidade válida.")
        
        elif escolha == '3':
            inventario.listar_itens()
        
        elif escolha == '4':
            item_aleatorio = inventario.encontrar_item_aleatorio()
            quantidade = random.randint(1, 3)
            inventario.adicionar_item(item_aleatorio, quantidade)

        # Modificar tamanho da mochila
        elif escolha == '5':
            print("\n==========================")
            print("======Mochila Aberta======")
            print("==========================\n")
            print("1. Aumentar capacidade")
            print("2. Diminuir capacidade")
            print("3. Voltar")
            
            sub_escolha = input("Escolha uma opção: ")
            
            if sub_escolha == '1':
                try:
                    capacidade_adicional = int(input("Digite a capacidade ADICIONAL para a mochila: "))
                    inventario.aumentar_capacidade(capacidade_adicional)
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
            
            elif sub_escolha == '2':
                try: 
                    capacidade_adicional = int(input("Digite a capacidade REMOVIDA da mochila: "))
                    inventario.diminui_capacidade(capacidade_adicional)
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
            
            elif sub_escolha == '3':
                continue
            
            else:
                print("Opção inválida!")
        
        elif escolha == '6':
            print("\n===== Mochila Fechada ===========")
            break
        
        else:
            print("Opção inválida!")

def main():   
    # Criando um inventário inicial com capacidade padrão
    inventario_personagem = Inventario()
    
    # Menu interativo para gerenciar o inventário
    menu_inventario(inventario_personagem)

if __name__ == "__main__":
    main()