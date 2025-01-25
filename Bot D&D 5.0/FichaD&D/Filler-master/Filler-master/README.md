<h1>RPG Filler</h1>
<p>
	Programa para automatizar a criação de personagens do RPG D&D 3.5
</p>
<p>
	O RPG Filler é um conjunto de scripts feitos em Python, então para poder executá-lo é necessário ter o Python instalado no seu computador. Caso não tenha acesse <a href="https://www.python.org/">https://www.python.org/</a> para baixar
</p>
<h2>Como utilizar</h2>
<ul>
	<li>
		<h4>Download</h4>
		<p>
			Realize o download zip desse reposítorio e extraia-o em qualquer pasta de seu computador
		</p>
	</li>
	<li>
		<h4>Executar</h4>
		<p>
			Dentro da pasta extraída, há um arquivo chamado "RPGFiller.py". Este é o arquivo 'executável'
		</p>
		<ul>
			<li>
				<h4>Windows</h4>
				<p>
					Abra um terminal na pasta extraída e execute o comando "python RPGFiller.py"
				</p>
				<ul>
					<li>
						<h5>Erro: "python não é reconhecido como um comando interno"</h5>
						<p>
							Caso ocorra esse erro ao executar o comando "python RPGFiller.py", dê uma olhada nesse <a href="http://stackoverflow.com/questions/7054424/python-not-recognised-as-a-command">fórum</a>
						</p>
					</li>
				</ul>
			</li>
			<li>
				<h4>Linux</h4>
				<p>
					Abra um terminal na pasta extraída e execute o comando "./RPGFiller.py" ou "python RPGFiller.py"
				</p>
			</li>
		</ul>
	</li>
	<li>
		<h4>Informações sobre o RPG Filler</h4>
		<p>
			O RPG Filler automatiza a criação de um personagem de D&D 3.5 calculando automaticamente o BBA, life e testes de resistência com base nas classes inseridas no personagem. 
			As classes disponíveis são:
		</p>
		<ul>
			<li>Bárbaro</li>
			<li>Bardo</li>
			<li>Clérigo</li>
			<li>Druida</li>
			<li>Guerreiro</li>
			<li>Ladino</li>
			<li>Mago</li>
			<li>Monge</li>
			<li>Paladino</li>
			<li>Ranger</li>
		</ul>
	</li>
</ul>
<h2>DEV's</h2>
<ul>
	<li>
		<h3>Classes Implementadas</h3>
		<ul>
			<li>
				<b>BBA</b>: classes que implementam os valores da BBA boa (de guerreiros e etc) e da BBA ruim (de magos e etc) do nível 0 ao nível 20. Servem apenas para armazenar tais valores e não são instânciadas. Implementada no arquivo "BBA.py"
			</li>
			<li>
				<b>Resist</b>: classes que implementam os valores da resisência boa e da resisência ruim do nível 0 ao nível 20. Servem apenas para armazenar tais valores e não são instânciadas. Implementada no arquivo "Resist.py"
			</li>
			<li>
				<b>Class</b>: classe "Ser Superior" abstrata que será herdada pelas classes descritas abaixo. Possui a lógico de cálculo da BBA e testes de resistência para determinado nível. Implementada no arquivo "Classes.py"
				<ul>
					<li>
						<b>Bárbaro</b>: classe que implementa as características (dado de vida da classe, lista de perícias da classe, quantidade de perícias por nivel, qual tipo de BBA é a da classe e quais tipos de testes de resistência são da classe) do Bárbaro. Implementada no arquivo "Classes.py"
					</li>
					<li>
						<b>Bardo</b>: classe que implementa as características (dado de vida da classe, lista de perícias da classe, quantidade de perícias por nivel, qual tipo de BBA é a da classe e quais tipos de testes de resistência são da classe) do Bardo. Implementada no arquivo "Classes.py"
					</li>
					<li>
						<b>Clérigo</b>: classe que implementa as características (dado de vida da classe, lista de perícias da classe, quantidade de perícias por nivel, qual tipo de BBA é a da classe e quais tipos de testes de resistência são da classe) Clérigo. Implementada no arquivo "Classes.py"
					</li>
					<li>
						<b>Druida</b>: classe que implementa as características (dado de vida da classe, lista de perícias da classe, quantidade de perícias por nivel, qual tipo de BBA é a da classe e quais tipos de testes de resistência são da classe) Druida. Implementada no arquivo "Classes.py"
					</li>
					<li>
						<b>Guerreiro</b>: classe que implementa as características (dado de vida da classe, lista de perícias da classe, quantidade de perícias por nivel, qual tipo de BBA é a da classe e quais tipos de testes de resistência são da classe) Guerreiro. Implementada no arquivo "Classes.py"
					</li>
					<li>
						<b>Ladino</b>: classe que implementa as características (dado de vida da classe, lista de perícias da classe, quantidade de perícias por nivel, qual tipo de BBA é a da classe e quais tipos de testes de resistência são da classe) Ladino. Implementada no arquivo "Classes.py"
					</li>
					<li>
						<b>Mago</b>: classe que implementa as características (dado de vida da classe, lista de perícias da classe, quantidade de perícias por nivel, qual tipo de BBA é a da classe e quais tipos de testes de resistência são da classe) Mago. Implementada no arquivo "Classes.py"
					</li>
					<li>
						<b>Monge</b>: classe que implementa as características (dado de vida da classe, lista de perícias da classe, quantidade de perícias por nivel, qual tipo de BBA é a da classe e quais tipos de testes de resistência são da classe) do Monge. Implementada no arquivo "Classes.py"
					</li>
					<li>
						<b>Paladino</b>: classe que implementa as características (dado de vida da classe, lista de perícias da classe, quantidade de perícias por nivel, qual tipo de BBA é a da classe e quais tipos de testes de resistência são da classe) do Paladino. Implementada no arquivo "Classes.py"
					</li>
					<li>
						<b>Ranger</b>: classe que implementa as características (dado de vida da classe, lista de perícias da classe, quantidade de perícias por nivel, qual tipo de BBA é a da classe e quais tipos de testes de resistência são da classe) do Ranger. Implementada no arquivo "Classes.py"
					</li>
				</ul>
			</li>
			<li>
				<b>Personagem</b>: classe que implementa um personagem. Um personagem pode ter várias <i>classes</i>. 
				<p>
					<h5>Métodos da classe</h5>
					<ul>
						<li>
							set_class(obj): método que recebe um obj da especialização da classe <i>Class</i> e armazena numa lista
						</li>
						<li>
							atualizar(): método para chamar os métodos update_personagem() e salvar()
						</li>
						<li>
							update_personagem(): método que recalcula todas as informações do personagem
						</li>
						<li>
							salvar(): método que passa a instância do personagem pra classe <i>Writer</i>
						</li>
					</ul>
				</p>
			</li>
			<li>
				<b>Situacao</b>: classe que implementa uma situação de retorno (uma tupla de bool e string)
			</li>
			<li>
				<b>Writer</b>: classe responsável pela persistência do do objeto da classe Personagem em um arquivo JSON
			</li>
			<li>
				<b>Application</b>: classe que implementa a GUI utilizando a biblioteca TKinter
			</li>
			<li>
				<b>MenuBar</b>: classe que implementa uma barra de menu da GUI
			</li>
		</ul>
	</li>
	<li>
		<h3>Persistência de dados</h3>
		<p>
			A persistência foi feita atrávez de arquivos em formato JSON, localizados dentro da pasta "personagens"
		</p>
	</li>
</ul>







