CREATE DATABASE saep_db;
USE saep_db;

CREATE TABLE tipo (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(255)
);

CREATE TABLE equipamento (
	 id INT PRIMARY KEY,
	tipo_id INT,
	tensao FLOAT,
	peso_U FLOAT,
	altura_u FLOAT,
	largura_u FLOAT,
	profundidade_u FLOAT,
	resolucao float,
	armazenamento INT,
	conectividade TINYINT(1),
	FOREIGN KEY (tipo_id) REFERENCES tipo(id)
);

CREATE TABLE movimentacao (
	id INT PRIMARY KEY,
	equipamento_id INT,
	quantidade INT,
	data_mov DATE,
	fornecedor VARCHAR(255),
	lote VARCHAR(255),
	tipo_operacao VARCHAR(255)
	FOREIGN KEY (equipamento_id) REFERENCES equipamento(id)
)

