import oracledb


USUARIO = "system"
SENHA = "28012002"
HOST = "localhost"
PORTA = 1521
SERVICE_NAME = "codelogin"  

dsn = oracledb.makedsn(HOST,
    PORTA,
    service_name=SERVICE_NAME)

def conectar():
    return oracledb.connect(user=USUARIO,password=SENHA,dsn=ds)

def criar_tabela():
    pass

def inserir_usuario(nome, idade, sexo, altura, peso):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome, idade, sexo, altura, peso)
        VALUES (:1, :2, :3, :4, :5)
    """, (nome, idade, sexo, altura, peso))

    conn.commit()
    cursor.close()
    conn.close()

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, idade, sexo, altura, peso FROM usuarios")
    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados

def exportar_usuarios_txt():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, idade, sexo, altura, peso FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    with open("usuarios.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("ID | Nome | Idade | Sexo | Altura | Peso\n")
        arquivo.write("-" * 50 + "\n")

        for u in usuarios:
            linha = f"{u[0]} | {u[1]} | {u[2]} | {u[3]} | {u[4]} | {u[5]}\n"
            arquivo.write(linha)
