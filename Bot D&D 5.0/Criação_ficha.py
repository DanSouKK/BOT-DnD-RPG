import random

class DnDCharacter:
    def __init__(self):
        # Basic character information
        self.name = ""
        self.size = ""
        self.age = 0
        self.weight = 0
        self.height = 0
        self.sex = ""
        self.race = ""
        self.character_class = ""
        self.level = 1

        # Attributes
        self.attributes = {
            "Força": 0,
            "Destreza": 0,
            "Constituição": 0,
            "Inteligencia": 0,
            "Sabedoria": 0,
            "Carisma": 0
        }

        # Racial bonuses
        self.racial_bonuses = {
            "Human": {"bonus_feat": True, "extra_skill_points": 1},
            "Elf": {"Destreza": 2, "Constituicao": -2},
            "Dwarf": {"Constituicao": 2, "Carisma": -2},
            "Halfling": {"Destreza": 2, "Forca": -2},
            "Meio-Orc":{"Forca":2, "Inteligencia": -2, "Carisma": -2}, 
            "Meio-Elfo":{None},
            "Gnome":{"Constituicao": 2, "Forca": -2}

            # Add more races as needed
        }

        # Class information
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
        #Collect basic character information from the user.
        print("--- Criação de Personagem D&D 3.5 ---")
        self.name = input("Nome do personagem: ")        
        self.age = int(input("Idade do personagem: "))
        self.weight = float(input("Peso do personagem (kg): "))
        self.height = float(input("Altura do personagem (cm): "))
        self.sex = input("Sexo do personagem: ")
        
        # Race selection
        print("\nEscolha uma raça:")
        races = list(self.racial_bonuses.keys())
        for i, race in enumerate(races, 1):
            print(f"{i}. {race}")
        race_choice = int(input("Selecione o número da raça: "))
        self.race = races[race_choice - 1]
        
        # Class selection
        print("\nEscolha uma classe:")
        classes = list(self.class_hit_dice.keys())
        for i, cls in enumerate(classes, 1):
            print(f"{i}. {cls}")
        class_choice = int(input("Selecione o número da classe: "))
        self.character_class = classes[class_choice - 1]
        
        # Level (for now, keeping it at 1)
        self.level = 1

    def generate_attributes(self, method='random'):
        """Generate character attributes based on user's preferred method."""
        def roll_4d6_drop_lowest():
            # Standard D&D 3.5 attribute generation method.
            rolls = [random.randint(1, 6) for _ in range(4)]
            rolls.remove(min(rolls))
            return sum(rolls)

        if method == 'random':
            print("\nGerando atributos (4d6, descartando o menor):")
            attribute_values = [roll_4d6_drop_lowest() for _ in range(6)]
            attribute_values.sort(reverse=True)
            
            print("Valores gerados:", attribute_values)
            print("\nSelecione onde atribuir cada valor:")
            
            for value in attribute_values:
                print("\nValor:", value)
                print("Atributos disponíveis:")
                for attr in self.attributes.keys():
                    if self.attributes[attr] == 0:
                        print(f"- {attr}")
                
                while True:
                    chosen_attr = input("Escolha um atributo para este valor: ")
                    if chosen_attr in self.attributes and self.attributes[chosen_attr] == 0:
                        self.attributes[chosen_attr] = value
                        break
                    else:
                        print("Atributo inválido ou já preenchido.")
        
        elif method == 'manual':
            print("\nPreenchimento manual de atributos:")
            for attr in self.attributes.keys():
                self.attributes[attr] = int(input(f"Valor para {attr}: "))

    def apply_racial_modifiers(self):
        # Apply racial attribute modifiers
        race_mods = self.racial_bonuses.get(self.race, {})
        for attr, bonus in race_mods.items():
            if attr in self.attributes:
                self.attributes[attr] += bonus

    def calculate_modifiers(self):
        # Calculate attribute modifiers
        self.modifiers = {}
        for attr, value in self.attributes.items():
            self.modifiers[attr] = (value - 10) // 2

    def generate_character(self):
        #Main method to generate the entire character
        self.collect_basic_info()
        
        # Attribute generation method
        print("\nMétodo de geração de atributos:")
        print("1. Aleatório (4d6, descartando o menor)")
        print("2. Manual")
        method_choice = input("Escolha o método (1/2): ")
        
        method = 'random' if method_choice == '1' else 'manual'
        self.generate_attributes(method)
        
        self.apply_racial_modifiers()
        self.calculate_modifiers()

        print("\n--- Resumo do Personagem ---")
        print(f"Nome: {self.name}")
        print(f"Raça: {self.race}")
        print(f"Classe: {self.character_class}")
        print("\nAtributos:")
        for attr, value in self.attributes.items():
            print(f"{attr}: {value}")

def main():
    character = DnDCharacter()
    character.generate_character()

if __name__ == "__main__":
    main()