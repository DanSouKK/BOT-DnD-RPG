-- Banco de Dados para Sistema de Gerenciamento de RPG D&D 3.5

-- Tabela de Campanhas
CREATE TABLE Campanhas (
    campanha_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    sinopse TEXT,
    data_inicio DATE,
    status ENUM('Ativa', 'Concluída', 'Suspensa') DEFAULT 'Ativa'
);

-- Tabela de Jogadores
CREATE TABLE Jogadores (
    jogador_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Personagens
CREATE TABLE Personagens (
    personagem_id INT PRIMARY KEY AUTO_INCREMENT,
    jogador_id INT,
    campanha_id INT,
    nome VARCHAR(100) NOT NULL,
    raca VARCHAR(50),
    classe VARCHAR(50),
    nivel INT DEFAULT 1,
    pontos_vida INT,
    pontos_experiencia INT DEFAULT 0,
    forca INT,
    destreza INT,
    constituicao INT,
    inteligencia INT,
    sabedoria INT,
    carisma INT,
    FOREIGN KEY (jogador_id) REFERENCES Jogadores(jogador_id),
    FOREIGN KEY (campanha_id) REFERENCES Campanhas(campanha_id)
);

-- Tabela de NPCs
CREATE TABLE NPCs (
    npc_id INT PRIMARY KEY AUTO_INCREMENT,
    campanha_id INT,
    nome VARCHAR(100) NOT NULL,
    tipo ENUM('Aliado', 'Antagonista', 'Neutro') DEFAULT 'Neutro',
    descricao TEXT,
    historia TEXT,
    FOREIGN KEY (campanha_id) REFERENCES Campanhas(campanha_id)
);

-- Tabela de Cenários
CREATE TABLE Cenarios (
    cenario_id INT PRIMARY KEY AUTO_INCREMENT,
    campanha_id INT,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    tipo ENUM('Combate', 'Exploração', 'Roleplay', 'Social') DEFAULT 'Exploração',
    FOREIGN KEY (campanha_id) REFERENCES Campanhas(campanha_id)
);

-- Tabela de Sessões de Jogo
CREATE TABLE Sessoes (
    sessao_id INT PRIMARY KEY AUTO_INCREMENT,
    campanha_id INT,
    data_sessao DATETIME,
    resumo TEXT,
    progresso_narrativo TEXT,
    FOREIGN KEY (campanha_id) REFERENCES Campanhas(campanha_id)
);

-- Tabela de Combates
CREATE TABLE Combates (
    combate_id INT PRIMARY KEY AUTO_INCREMENT,
    sessao_id INT,
    cenario_id INT,
    data_inicio DATETIME,
    resultado ENUM('Em Andamento', 'Vitória Jogadores', 'Vitória NPCs', 'Empate') DEFAULT 'Em Andamento',
    FOREIGN KEY (sessao_id) REFERENCES Sessoes(sessao_id),
    FOREIGN KEY (cenario_id) REFERENCES Cenarios(cenario_id)
);

-- Tabela de Itens de Personagem
CREATE TABLE ItensPersonagem (
    item_personagem_id INT PRIMARY KEY AUTO_INCREMENT,
    personagem_id INT,
    nome VARCHAR(100),
    tipo VARCHAR(50),
    quantidade INT DEFAULT 1,
    descricao TEXT,
    FOREIGN KEY (personagem_id) REFERENCES Personagens(personagem_id)
);

-- Tabela de Log de Atividades
CREATE TABLE LogAtividades (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    campanha_id INT,
    personagem_id INT,
    tipo_atividade ENUM('Combate', 'Roleplay', 'Progressão', 'Decisão') NOT NULL,
    descricao TEXT,
    data_atividade TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campanha_id) REFERENCES Campanhas(campanha_id),
    FOREIGN KEY (personagem_id) REFERENCES Personagens(personagem_id)
);

-- Tabela de Registro de Chat
CREATE TABLE RegistroChat (
    registro_id INT PRIMARY KEY AUTO_INCREMENT,
    campanha_id INT,
    remetente_id INT,
    tipo_remetente ENUM('Jogador', 'NPC', 'Mestre') NOT NULL,
    mensagem TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campanha_id) REFERENCES Campanhas(campanha_id)
);

-- Índices para melhorar performance
CREATE INDEX idx_personagem_campanha ON Personagens(campanha_id);
CREATE INDEX idx_npc_campanha ON NPCs(campanha_id);
CREATE INDEX idx_sessao_campanha ON Sessoes(campanha_id);
CREATE INDEX idx_log_campanha ON LogAtividades(campanha_id);