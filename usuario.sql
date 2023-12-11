-- Active: 1702319944877@@172.20.0.2@3306
CREATE DATABASE IF NOT EXISTS sys_ceu;

USE sys_ceu;

CREATE TABLE IF NOT EXISTS usuario (
    id int AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(250) NOT NULL,
    data_nascimento VARCHAR(10)
);

INSERT INTO usuario(nome, data_nascimento)
VALUE("Gustavo","20/07/1998")