from Flask import flask, render_template, url_for



@app.routes('/')
def agendamento():
    render_template('agendamento.html')

@app.routes('/formsCadastrar')
def cadastroLogin():
    render_template('formsCadastrar.html')

