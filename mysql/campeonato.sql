-- Exercício 1:
-- Campeonato: Um campeonato possui vários times. Um time pode estar em mais de um campeonato ao mesmo tempo. 
-- Cada time possui várias pessoas jogadoras. Uma pessoa jogadora só pode estar em um time.

create database campeonatos;

use campeonatos;

create table campeonatos (
id integer primary key auto_increment,
nome varchar(50) not null,
cidade varchar(40),
numero_rodadas integer not null,
premio integer not null
);

create table times (
id integer primary key auto_increment,
nome varchar(40) not null,
cidade varchar(40)
);

create table jogadoras (
	id integer primary key auto_increment,
    nome varchar(50) not null,
    idade integer not null,
    posicao varchar(40) not null,
    id_time int,
    foreign key (id_time) references times (id)
);

create table campeonatos_times (
    id_campeonato int,
    id_time int,
	foreign key (id_campeonato) references campeonatos (id),
    foreign key (id_time) references times (id)
);

-- Para adicionar a chave estrangeira após a criação da tabela:
-- alter table jogadoras add id_time int;
-- alter table jogadoras add constraint id_time foreign key (id_time) references times (id);

-- Exercício 2:
-- Inserir 3 times, inserir 4 registros na tabela joagadoras, inserir 2 campeonatos, relacionar os 3 times nos 2 campeonatos disponíveis, deletar um time

-- inserir 3 times
insert into times (nome, cidade) values
("Palmeiras", "São Paulo"), ("Flamengo", "Rio de Janeiro"), ("São Paulo", "São Paulo");

-- inserir 4 registros na tabela joagadoras
insert into jogadoras (nome, idade, posicao, id_time) values
("Gabriela Nogueira", 29, "lateral", 2), ("Larissa Arruda", 29, "atacante", 2), ("Wanessa Lino", 25, "zagueiro", 3), ("Pamella Farias", 25, "volante", 1);

-- inserir 2 campeonatos
insert into campeonato (nome, cidade, numero_rodadas, premio) values
("Brasileirão", "Várias", 10, 100000), ("Carioca", "Rio de Janeiro", 5, 50000);

-- relacionar os 3 times nos 2 campeonatos disponíveis
insert into campeonato_times (id_campeonato, id_time) values
(1,1), (2,2),(1,3);

-- deletar um time
delete from campeonato_times where id_time = 1;
delete from jogadoras where id_time = 1;
delete from times where id = 1;