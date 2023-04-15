import mysql.connector

conn = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='biblioteca')

mycursor = conn.cursor()

################################ Create Tables ################################

mycursor.execute("CREATE TABLE IF NOT EXISTS Bibliotecarios("
	"idBibliotecarios INT NOT NULL PRIMARY KEY,"
    "nome VARCHAR(45) NOT NULL,"
    "endereco VARCHAR(255) NOT NULL,"
    "email VARCHAR(255) NOT NULL,"
    "dataNascimento DATE NOT NULL);")

mycursor.execute("CREATE TABLE IF NOT EXISTS Estudantes("
	"idEstudante INT NOT NULL PRIMARY KEY,"
    "nome VARCHAR(45) NOT NULL,"
    "turma VARCHAR(45) NOT NULL,"
    "periodoEscolar VARCHAR(45) NOT NULL,"
    "email VARCHAR(255) NOT NULL,"
    "dataNascimento DATE NOT NULL);")
    
mycursor.execute("CREATE TABLE IF NOT EXISTS Tipo("
	"idTipo INT NOT NULL PRIMARY KEY,"
    "tipo VARCHAR(45) NOT NULL);")
    
mycursor.execute("CREATE TABLE IF NOT EXISTS Doacao("
	"idDoacao INT NOT NULL PRIMARY KEY,"
    "nomeDoacao VARCHAR(45) NOT NULL,"
    "nomeDoador VARCHAR(45) NOT NULL,"
    "dataDoacao DATE NOT NULL);")
    
mycursor.execute("CREATE TABLE IF NOT EXISTS Acervos("
	"idAcervo INT NOT NULL PRIMARY KEY,"
    "nome VARCHAR(45) NOT NULL,"
    "quantidade INT NOT NULL,"
    "tipoObra INT,"
    "doacao INT,"
    "FOREIGN KEY (tipoObra) REFERENCES tipo(idTipo),"
    "FOREIGN KEY (doacao) REFERENCES doacao(idDoacao));")
    
mycursor.execute("CREATE TABLE IF NOT EXISTS Emprestimos("
	"idEmprestimos INT NOT NULL PRIMARY KEY,"
    "campus VARCHAR(45) NOT NULL,"
    "dataEmprestimo DATE NOT NULL,"
    "dataDevolucao DATE NOT NULL,"
    "bibliotecarios INT,"
    "acervos INT,"
    "Estudantes INT,"
    "FOREIGN KEY (bibliotecarios) REFERENCES Bibliotecarios(idBibliotecarios),"
    "FOREIGN KEY (acervos) REFERENCES Acervos(idAcervos),"
    "FOREIGN KEY (estudantes) REFERENCES Estudantes(idEstudantes));")
    
#########################################################################   
    
    
    
    
    
    
    
################################ Inserts ################################   
    
mycursor.execute("INSERT INTO Bibliotecarios(idBibliotecarios, nome,endereco,email,dataNascimento)VALUES(777, \"Rafael Moreira\",\"Rua das Dores, 477\",\"raffa777moreira@ig.com\",'1977-07-07');")
mycursor.execute("INSERT INTO Bibliotecarios(idBibliotecarios, nome,endereco,email,dataNascimento) VALUES(546, \"Ricardo Batista\",\"Av. Coronel Teófilo Leme, 1042\",\"RicBat123@outlook.com\",'1988-04-05');")
mycursor.execute("INSERT INTO Bibliotecarios(idBibliotecarios, nome,endereco,email,dataNascimento) VALUES(784, \"Maria Raimunda da Cruz\",\"Alameda dos Mares,1477 \",\"Raimunda_da_cruz_1962@yahoo.com.br\",'1962-12-02');")
mycursor.execute("INSERT INTO Bibliotecarios(idBibliotecarios, nome,endereco,email,dataNascimento) VALUES(932, \"Dolores das Dores Silva\",\"Rua Oswaldo Russomano, 43\",\"dasDoresDolores_99@gmail.com\",'1999-05-02');")
mycursor.execute("INSERT INTO Bibliotecarios(idBibliotecarios, nome,endereco,email,dataNascimento) VALUES(003, \"José Aparecido Gomes\",\"Rua Zenovia Cioban, 13\",\"zeAparecido7@uol.com.br\",'1959-03-02');")

mycursor.execute("INSERT INTO Estudantes(idEstudante,nome,turma,periodoEscolar,email,dataNascimento) VALUES(265,\"Jairo Gomes\",\"1º Info\",\"Integral\",\"x1EzzLixinho@gmail.com\",'2003-12-07');")
mycursor.execute("INSERT INTO Estudantes(idEstudante,nome,turma,periodoEscolar,email,dataNascimento) VALUES(554,\"Luane Silva\",\"3º Eletro\",\"Integral\",\"LuaneBieber2015@gmail.com\",'2001-11-05');")
mycursor.execute("INSERT INTO Estudantes(idEstudante,nome,turma,periodoEscolar,email,dataNascimento) VALUES(835,\"Gustavo Almeida\",\"2º Mec\",\"Integral\",\"GustavoMainYasuo77@gmail.com\",'2000-05-09');")
mycursor.execute("INSERT INTO Estudantes(idEstudante,nome,turma,periodoEscolar,email,dataNascimento) VALUES(951,\"Alice Leite\",\"3º Mec\",\"Integral\",\"Alice99Leite@gmail.com\",'2002-02-11');")
mycursor.execute("INSERT INTO Estudantes(idEstudante,nome,turma,periodoEscolar,email,dataNascimento) VALUES(357,\"Kevin Souza\",\"2º Info\",\"Integral\",\"KevinS_@outlook.com\",'1999-07-12');")

mycursor.execute("INSERT INTO Tipo(idTipo,tipo) VALUES(0,\"Livro\");")
mycursor.execute("INSERT INTO Tipo(idTipo,tipo) VALUES(1,\"Fone\");")
mycursor.execute("INSERT INTO Tipo(idTipo,tipo) VALUES(2,\"Mapa\");")
mycursor.execute("INSERT INTO Tipo(idTipo,tipo) VALUES(3,\"Jogo\");")
mycursor.execute("INSERT INTO Tipo(idTipo,tipo) VALUES(4,\"Apostila\");")

mycursor.execute("INSERT INTO Doacao(idDoacao,nomeDoacao,nomeDoador,dataDoacao) VALUES(0,\"O Ladrão de Raios\",\"Guilherme Leite\",'2019-01-01');")
mycursor.execute("INSERT INTO Doacao(idDoacao,nomeDoacao,nomeDoador,dataDoacao) VALUES(1,\"Violão\",\"Guilherme Leite\",'2019-01-01');")
mycursor.execute("INSERT INTO Doacao(idDoacao,nomeDoacao,nomeDoador,dataDoacao) VALUES(2,\"A Maldição do Titã\",\"Guilherme Leite\",'2019-01-01');")
mycursor.execute("INSERT INTO Doacao(idDoacao,nomeDoacao,nomeDoador,dataDoacao) VALUES(3,\"A Batalha do Labirinto\",\"Guilherme Leite\",'2019-01-01');")
mycursor.execute("INSERT INTO Doacao(idDoacao,nomeDoacao,nomeDoador,dataDoacao) VALUES(4,\"O Último Olimpiano\",\"Guilherme Leite\",'2019-01-01');")

mycursor.execute("INSERT INTO Acervos(idAcervo,nome,quantidade,tipoObra,doacao) VALUES(1, \"A Batalha do Labirinto\", 1, 0, 3);")
mycursor.execute("INSERT INTO Acervos(idAcervo,nome,quantidade,tipoObra,doacao) VALUES(2, \"O Último Olimpiano\", 2, 0,4);")
mycursor.execute("INSERT INTO Acervos(idAcervo,nome,quantidade,doacao) VALUES(3, \"Violão\", 1,1);")
mycursor.execute("INSERT INTO Acervos(idAcervo,nome,quantidade,tipoObra) VALUES(4, \"Jogo da Vida\", 10, 3);")
mycursor.execute("INSERT INTO Acervos(idAcervo,nome,quantidade) VALUES(5, \"Regador\",2);")

mycursor.execute("INSERT INTO Emprestimos(idEmprestimos,campus,dataEmprestimo,dataDevolucao,bibliotecarios,acervos,estudantes) VALUES(1,\"Bragança Paulista\",'2019-07-10','2019-07-15',777,1,1);")
mycursor.execute("INSERT INTO Emprestimos(idEmprestimos,campus,dataEmprestimo,dataDevolucao,bibliotecarios,acervos,estudantes) VALUES(2,\"Birigui\",'2019-07-10','2019-07-15',546,2,3);")
mycursor.execute("INSERT INTO Emprestimos(idEmprestimos,campus,dataEmprestimo,dataDevolucao,bibliotecarios,acervos,estudantes) VALUES(3,\"Araraquara\",'2019-08-10','2019-08-15',784,1,4);")
mycursor.execute("INSERT INTO Emprestimos(idEmprestimos,campus,dataEmprestimo,dataDevolucao,bibliotecarios,acervos,estudantes) VALUES(4,\"Caraguatatuba\",'2019-09-09','2019-09-16',932,3,2);")
mycursor.execute("INSERT INTO Emprestimos(idEmprestimos,campus,dataEmprestimo,dataDevolucao,bibliotecarios,acervos,estudantes) VALUES(5,\"Registro\",'2019-07-10','2019-07-15',003,5,5);")

#########################################################################  




################################ Selects ################################  

mycursor.execute("SELECT * FROM Bibliotecarios;")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")

mycursor.execute("SELECT * FROM Estudantes;")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")

mycursor.execute("SELECT * FROM Tipo;")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")

mycursor.execute("SELECT * FROM Doacao;")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")

mycursor.execute("SELECT * FROM Acervos;")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")

mycursor.execute("SELECT * FROM Emprestimos;")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")

mycursor.execute("SELECT * FROM Emprestimos e INNER JOIN Acervos a on e.acervos=a.idAcervo WHERE (a.nome like \"A%\");")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")

mycursor.execute("SELECT * FROM Acervos a INNER JOIN Doacao d on a.doacao=d.idDoacao WHERE (d.nomeDoacao like \"O%\");")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")

mycursor.execute("SELECT * FROM Acervos a INNER JOIN Tipo t on a.tipoObra=t.idTipo WHERE (t.tipo like \"livro\") ORDER BY nome;")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")

mycursor.execute("SELECT nome FROM Estudantes WHERE(nome like \"%a%\");")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")

mycursor.execute("SELECT * FROM Acervos Where(quantidade>1);")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")

mycursor.execute("SELECT idEmprestimos,campus FROM Emprestimos WHERE (campus like \"a%\");")
myresult = mycursor.fetchall()
print("#######################################")
for x in myresult:
  print(x)
print("#######################################\n\n")



mycursor.execute("DROP TABLE Bibliotecarios;")
mycursor.execute("DROP TABLE Estudantes;")
mycursor.execute("DROP TABLE Tipo;")
mycursor.execute("DROP TABLE Doacao;")
mycursor.execute("DROP TABLE Acervos;")
mycursor.execute("DROP TABLE Emprestimos;")


