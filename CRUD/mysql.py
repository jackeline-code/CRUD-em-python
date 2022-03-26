import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cadastro_bd',
)

cursor = conexao.cursor()

#CRUD

#CREATE
comando = f'INSERT INTO cadastro_pessoa (nome, sobrenome, cpf, nacionalidade, cep, estado, cidade, logradouro, email, telefone) VALUES ({nome}, {sobrenome}, {cpf}, {nacionalidade},{cep}, {estado}, {cidade}, {logradouro}, {email}, {telefone})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

#READ
comando = f'SELECT * FROM cadastro_pessoa'
cursor.execute(comando)
resultado = cursor.fatchall() # le o banco de dados
print(resultado)

#UPDATE
comando = f'UPDATE cadastro_pessoa SET id = {id} WHERE nome = "{nome}", sobrenome = "{sobrenome}", cpf = "{cpf}", nacionalidade = "{nacionalidade}", cep = {cep}, estado = "{estado}", cidade = "{cidade}", logradouro = "{logradouro}", email = "{email}, telefone = "{telefone}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

#DELETE
comando = f'DELETE FROM cadastro_pessoa WHERE id = {id}'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

cursor.close()
conexao.close()

