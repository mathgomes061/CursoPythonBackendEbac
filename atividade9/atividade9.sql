CREATE TABLE Livros(
    id int PRIMARY KEY,
    titulo varchar(100),
    autor varchar(100),
    ano int,
    genero varchar(100),
    disponivel boolean
);

INSERT INTO Livros VALUES(
    1,
    'Harry Potter e a Pedra Filosofal',
    'J. K. Rowling',
    1997,
    'Fantasia',
    TRUE
);

INSERT INTO Livros VALUES(
    2,
    'O Diário de Anne Frank',
    'Anne Frank',
    1947,
    'Autobiografia',
    FALSE
);

INSERT INTO Livros VALUES(
    3,
    'E o Vento Levou',
    'Margaret Mitchell',
    1936,
    'Romance',
    TRUE
);

INSERT INTO Livros VALUES(
    4,
    'Jogos Vorazes',
    'Suzanne Collins',
    2008,
    'Ficção Distópica',
    TRUE
);

INSERT INTO Livros VALUES(
    5,
    'Orgulho e Preconceito',
    'Jane Austen',
    1813,
    'Romance',
    FALSE
);

SELECT * FROM Livros WHERE disponivel = TRUE;

UPDATE Livros SET disponivel = FALSE WHERE id = 4;

SELECT * FROM Livros ORDER BY ano DESC;

DELETE FROM Livros WHERE ano < 1940;

DROP TABLE Livros;

CREATE TABLE Livros(
    id int PRIMARY KEY,
    titulo varchar(100),
    autor varchar(100),
    ano int,
    genero varchar(100),
    disponivel boolean
);
