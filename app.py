import mysql.connector
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
db_host = "db"
db_user = "root"
db_password = "your_password"
db_name = "crud_db"


# Rota principal para exibir os registros do banco de dados
@app.route("/")
def index():
    conn = mysql.connector.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return render_template("index.html", rows=rows)


# Rota para adicionar um novo registro ao banco de dados
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    email = request.form["email"]

    conn = mysql.connector.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    conn.close()

    return redirect("/")


# Rota para excluir um registro do banco de dados
@app.route("/delete/<int:id>")
def delete(id):
    conn = mysql.connector.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
