import random
import unicodedata

def normalize(text):
    """Remove acentos e converte para minúsculas."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower()

class DnDCharacter:
    def __init__(self):
        # Informações básicas do personagem
        self.name = ""
        self.size = ""
        self.age = 0
        self.weight = 0
        self.height = 0
        self.sex = ""
        self.race = ""
        self.character_class = ""
        self.level = 1

        # Lista padrão de atributos
        self.attribute_names = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        # Valores base (antes dos bônus)
        self.base_attributes = {attr: 0 for attr in self.attribute_names}
        # Valores finais dos atributos (após bônus)
        self.attributes = {attr: 0 for attr in self.attribute_names}
        # Bônus aplicados de cada atributo
        self.racial_applied = {attr: 0 for attr in self.attribute_names}

        # Bônus raciais (7 básicas + 10 adicionais, totalizando 17 opções)
        self.racial_bonuses = {
            "Human": {"bonus_feat": True, "extra_skill_points": 1},
            "Elf": {"Destreza": 2, "Constituição": -2},
            "Dwarf": {"Constituição": 2, "Carisma": -2},
            "Halfling": {"Destreza": 2, "Força": -2},
            "Meio-Orc": {"Força": 2, "Inteligência": -2, "Carisma": -2},
            "Meio-Elfo": {},
            "Gnome": {"Constituição": 2, "Força": -2},
            # Raças adicionais
            "Drow": {"Destreza": 2, "Constituição": -2, "Carisma": 2},
            "Tiefling": {"Inteligência": 2, "Carisma": -2},
            "Aasimar": {"Sabedoria": 2, "Carisma": 2, "Constituição": -2},
            "Elfo da Floresta": {"Destreza": 2, "Sabedoria": 1, "Constituição": -2},
            "Elfo do Sol": {"Destreza": 1, "Inteligência": 2, "Constituição": -2},
            "Meio-Dragão": {"Força": 2, "Constituição": 2, "Carisma": -2},
            "Lizardman": {"Força": 2, "Constituição": 2, "Inteligência": -2},
            "Kobold": {"Destreza": 2, "Constituição": -2},
            "Orc": {"Força": 2, "Destreza": -2, "Inteligência": -2},
            "Centaur": {"Força": 2, "Destreza": 2, "Inteligência": -2, "Carisma": -2}
        }

        # Dados de vida por classe
        self.class_hit_dice = {
            "Barbaro": 12,
            "Bardo": 6,
            "Clerigo": 8,
            "Druida": 8,
            "Guerreiro": 10,
            "Monge": 8,
            "Paladino": 10,
            "Ranger": 10,
            "Ladino": 6,
            "Feiticeiro": 4,
            "Mago": 4
        }

    def collect_basic_info(self):
        print("--- Criação de Personagem D&D 3.5 ---")
        self.name = input("Nome do personagem: ")
        self.age = int(input("Idade do personagem: "))
        self.weight = float(input("Peso do personagem (kg): "))
        self.height = float(input("Altura do personagem (cm): "))
        self.sex = input("Sexo do personagem: ")
        self.level = int(input("Qual nivel do personagem: "))

        # Seleção de raça (17 opções: 7 básicas + 10 adicionais)
        print("\nEscolha uma raça:")
        races = list(self.racial_bonuses.keys())
        for i, race in enumerate(races, 1):
            print(f"{i}. {race}")
        race_choice = int(input("Selecione o número da raça: "))
        self.race = races[race_choice - 1]

        # Seleção de classe
        print("\nEscolha uma classe:")
        classes = list(self.class_hit_dice.keys())
        for i, cls in enumerate(classes, 1):
            print(f"{i}. {cls}")
        class_choice = int(input("Selecione o número da classe: "))
        self.character_class = classes[class_choice - 1]

    def generate_character(self):
        # Método principal para gerar o personagem completo
        self.collect_basic_info()

        # Escolha do método de geração de atributos
        print("\nMétodo de geração de atributos:")
        print("1. Aleatório (4d6, descartando o menor)")
        print("2. Manual")
        print("3. Distribuição de pontos")
        method_choice = input("Escolha o método (1/2/3): ")

        if method_choice == '1':
            method = 'random'
        elif method_choice == '2':
            method = 'manual'
        elif method_choice == '3':
            method = 'points'
        else:
            print("Opção inválida. Usando método manual por padrão.")
            method = 'manual'

        self.generate_attributes(method)
        self.apply_racial_modifiers()
        self.calculate_modifiers()
        self.calculate_hp()
        self.print_character_sheet()

    def generate_attributes(self, method='random'):
        if method == 'random':
            print("\nGerando atributos (4d6, descartando o menor):")
            def roll_4d6_drop_lowest():
                rolls = [random.randint(1, 6) for _ in range(4)]
                rolls.remove(min(rolls))
                return sum(rolls)

            # Gera 6 valores e os ordena de forma decrescente
            attribute_values = [roll_4d6_drop_lowest() for _ in range(6)]
            attribute_values.sort(reverse=True)
            print("Valores gerados:", attribute_values)
            print("\nSelecione onde atribuir cada valor:")
            temp_attributes = {attr: 0 for attr in self.attribute_names}
            for value in attribute_values:
                print(f"\nValor: {value}")
                available_attrs = [attr for attr, val in temp_attributes.items() if val == 0]
                print("Atributos disponíveis:")
                for attr in available_attrs:
                    print(f"- {attr}")
                while True:
                    chosen_input = input("Escolha um atributo para este valor (3 primeiras letras): ")
                    normalized_input = normalize(chosen_input)
                    matched_attr = None
                    for attr in available_attrs:
                        if normalize(attr).startswith(normalized_input):
                            matched_attr = attr
                            break
                    if matched_attr:
                        temp_attributes[matched_attr] = value
                        break
                    else:
                        print("Atributo inválido ou já preenchido.")
            self.base_attributes = temp_attributes.copy()

        elif method == 'manual':
            print("\nPreenchimento manual de atributos:")
            for attr in self.attribute_names:
                while True:
                    try:
                        valor = int(input(f"Valor para {attr}: "))
                        self.base_attributes[attr] = valor
                        break
                    except ValueError:
                        print("Por favor, insira um número válido.")

        elif method == 'points':
            print("\nDistribuição de pontos entre atributos:")
            while True:
                try:
                    total_pontos = int(input("Quantos pontos deseja distribuir entre os atributos? "))
                    if total_pontos < 0:
                        print("O total de pontos deve ser um número não negativo.")
                    else:
                        break
                except ValueError:
                    print("Por favor, insira um número válido.")

            temp_attributes = {}
            for attr in self.attribute_names:
                while True:
                    try:
                        print(f"\nAtributo: {attr}")
                        print(f"Pontos restantes: {total_pontos}")
                        pontos = int(input(f"Quantos pontos deseja alocar para {attr}? "))
                        if pontos < 0:
                            print("Valor inválido. Deve ser um número não negativo.")
                        elif pontos > total_pontos:
                            print("Você não possui pontos suficientes para essa alocação.")
                        else:
                            temp_attributes[attr] = pontos
                            total_pontos -= pontos
                            break
                    except ValueError:
                        print("Por favor, insira um número válido.")

            if total_pontos > 0:
                print(f"\nVocê ainda tem {total_pontos} pontos restantes. Eles serão alocados automaticamente no primeiro atributo ({self.attribute_names[0]}).")
                temp_attributes[self.attribute_names[0]] += total_pontos
            self.base_attributes = temp_attributes.copy()
        else:
            print("Método desconhecido. Não foi possível gerar os atributos.")

    def apply_racial_modifiers(self):
        # Aplica os bônus raciais diretamente nos atributos base
        race_mods = self.racial_bonuses.get(self.race, {})
        for attr, bonus in race_mods.items():
            if attr in self.base_attributes:
                self.base_attributes[attr] += bonus  # Modifica o atributo base
        # Atualiza os atributos finais (para garantir consistência)
        self.attributes = self.base_attributes.copy()
        # Atualiza os bônus aplicados para exibição (opcional)
        self.racial_applied = race_mods.copy()

    def calculate_modifiers(self):
        # Calcula o modificador para cada atributo com base no valor final
        self.modifiers = {}
        for attr in self.attribute_names:
            self.modifiers[attr] = (self.attributes[attr] - 10) // 2
    
    def calculate_hp(self):
        # Obtém o hit die da classe
        self.hit_dice = self.class_hit_dice.get(self.character_class, 8)
        
        # Calcula HP: primeiro nível recebe máximo do dado + mod constituição
        constitution_mod = self.modifiers.get("Constituição", 0)
        
        # HP para o primeiro nível (máximo)
        self.hp = self.hit_dice + constitution_mod
        
        # Se nível > 1, adiciona HP para níveis adicionais
        if isinstance(self.level, str):
            try:
                self.level = int(self.level)
            except ValueError:
                self.level = 1
        
        # Adiciona HP para níveis adicionais (simplificado usando média)
        if self.level > 1:
            avg_roll = (self.hit_dice + 1) // 2  # Média arredondada para baixo
            self.hp += (self.level - 1) * (avg_roll + constitution_mod)
            
        # HP mínimo é 1
        self.hp = max(1, self.hp)

    def print_character_sheet(self):
        nome_formatado = self.name.title()
        sexo_input = self.sex.strip().lower()
        sexo_formatado = "Masculino" if sexo_input in ['m', 'masculino'] else "Feminino" if sexo_input in ['f', 'feminino'] else self.sex.capitalize()

        print("\n--- Ficha do Personagem ---")
        print(f"Nome: {nome_formatado}")
        print(f"Idade: {self.age}  /  Peso: {self.weight} kg  /  Altura: {self.height} cm  /  Sexo: {sexo_formatado}")
        # condicional para imprimir a raça junto com seu bonus racial de atributos. 
        if self.racial_applied:
            bonus_str = ", ".join(
                [f"{attr[:3]} {'+' if bonus_val >= 0 else ''}{bonus_val}" 
                for attr, bonus_val in self.racial_applied.items()]
            )
            print(f"Raça: {self.race} ({bonus_str})")
        else:
            print(f"Raça: {self.race}")
        print(f"Classe: {self.character_class}")
        print(f"Nível: {self.level}")
        print(f"PV Máximo: {self.hp}  (Hit Dice: d{self.hit_dice})")
        print("\nAtributos:")
        for attr in self.attribute_names:
            final_value = self.attributes[attr]
            modifier = self.modifiers[attr]
            mod_str = f"(+{modifier})" if modifier >= 0 else f"({modifier})"
            print(f"{attr}: {final_value} {mod_str}")


def main():
    character = DnDCharacter()
    character.generate_character()

if __name__ == "__main__":
    main()