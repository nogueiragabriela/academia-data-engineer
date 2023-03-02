CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE cidade(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    cidade VARCHAR(50) NOT NULL,
	uf VARCHAR(2) NOT NULL
);

CREATE TABLE leitor(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
	data_nascimento DATE NOT NULL,
	logradouro VARCHAR(60) NOT NULL,
    numero INTEGER,
    id_cidade INTEGER,
    FOREIGN KEY (id_cidade) REFERENCES cidade (id)
);

CREATE TABLE telefone(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    telefone VARCHAR(50) NOT NULL,
    id_leitor INTEGER,
    FOREIGN KEY (id_leitor) REFERENCES leitor (id)
);

CREATE TABLE livro(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
	numero_paginas INTEGER NOT NULL
);

CREATE TABLE autor(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE livro_autor(
	id_livro INTEGER,
    id_autor INTEGER,
	FOREIGN KEY (id_livro) REFERENCES livro (id),
    FOREIGN KEY (id_autor) REFERENCES autor (id)
);

CREATE TABLE emprestimo(
	id_livro INTEGER,
    id_leitor INTEGER,
    data_emprestimo DATE,
	FOREIGN KEY (id_livro) REFERENCES livro (id),
    FOREIGN KEY (id_leitor) REFERENCES leitor (id)
);

-- cidade
INSERT INTO cidade (cidade, uf)
VALUES ('Natal', 'RN');

INSERT INTO cidade (cidade, uf)
VALUES ('Recife', 'PE');

INSERT INTO cidade (cidade, uf)
VALUES ('Rio de Janeiro', 'RJ');

INSERT INTO cidade (cidade, uf)
VALUES ('São Paulo', 'SP');

-- leitor
INSERT INTO leitor (nome, data_nascimento, logradouro, numero, id_cidade)
VALUES ('José Andradas', '2000-05-11', 'Rua 01', '430', 3);

INSERT INTO leitor (nome, data_nascimento, logradouro, numero, id_cidade)
VALUES ('Ana Silva', '2000-11-11', 'Rua ABC', '430', 4);

INSERT INTO leitor (nome, data_nascimento, logradouro, numero, id_cidade)
VALUES ('Joana Marques', '2005-08-05', 'Rua XYZ', '430', 1);

INSERT INTO leitor (nome, data_nascimento, logradouro, numero, id_cidade)
VALUES ('Pedro Santana', '2002-12-09', 'Rua 05', '430', 2);

INSERT INTO leitor (nome, data_nascimento, logradouro, numero, id_cidade)
VALUES ('João André', '2001-04-01', 'Rua 100', '430', 3);

-- telefone
INSERT INTO telefone (telefone, id_leitor)
VALUES ('11111111', 1);

INSERT INTO telefone (telefone, id_leitor)
VALUES ('3333333', 1);

INSERT INTO telefone (telefone, id_leitor)
VALUES ('2222222', 2);

INSERT INTO telefone (telefone, id_leitor)
VALUES ('4444444', 3);

INSERT INTO telefone (telefone, id_leitor)
VALUES ('666666', 3);

INSERT INTO telefone (telefone, id_leitor)
VALUES ('55555555', 4);

INSERT INTO telefone (telefone, id_leitor)
VALUES ('88888888', 5);

INSERT INTO telefone (telefone, id_leitor)
VALUES ('9999999', 5);

INSERT INTO telefone (telefone, id_leitor)
VALUES ('0000000', 5);

-- livro
INSERT INTO livro (titulo, numero_paginas)
VALUES ('O Código da Vinci', 300);

INSERT INTO livro (titulo, numero_paginas)
VALUES ('Fortaleza Digital', 280);

INSERT INTO livro (titulo, numero_paginas)
VALUES ('O Cortiço', 330);

INSERT INTO livro (titulo, numero_paginas)
VALUES ('Dom Casmurro', 400);

-- autor
INSERT INTO autor (nome)
VALUES ('Dan Brown');

INSERT INTO autor (nome)
VALUES ('Eça de Queiroz');

INSERT INTO autor (nome)
VALUES ('Machado de Assis');

-- livro_autor
INSERT INTO livro_autor (id_livro, id_autor)
VALUES (1, 1);

INSERT INTO livro_autor (id_livro, id_autor)
VALUES (2, 1);

INSERT INTO livro_autor (id_livro, id_autor)
VALUES (3, 2);

INSERT INTO livro_autor (id_livro, id_autor)
VALUES (4, 3);

-- emprestimo
INSERT INTO emprestimo (id_livro, id_leitor, data_emprestimo)
VALUES (1, 1, '2023-01-04');

INSERT INTO emprestimo (id_livro, id_leitor, data_emprestimo)
VALUES (2, 2, '2023-01-06');

INSERT INTO emprestimo (id_livro, id_leitor, data_emprestimo)
VALUES (3, 3, '2023-01-06');

INSERT INTO emprestimo (id_livro, id_leitor, data_emprestimo)
VALUES (1, 4, '2023-01-07');

INSERT INTO emprestimo (id_livro, id_leitor, data_emprestimo)
VALUES (4, 5, '2023-01-10');
