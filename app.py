from flask import Flask, render_template, request, redirect, url_for, session
from ssh_utils import ssh_execute_command

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_segura'  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Recebe os dados da primeira etapa (login SSH)
        session['host'] = request.form['host']
        session['user'] = request.form['user']
        session['password'] = request.form['password']
        return redirect(url_for('panel'))
    return render_template('index.html')

@app.route('/panel', methods=['GET', 'POST'])
def panel():
    output = None

    # Definindo o diretório inicial na primeira requisição
    if 'cwd' not in session:
        session['cwd'] = "~" 

    if request.method == 'POST':
        command = request.form['command']
        if command.strip() == "dashboard":
            dashboard_cmd = (
                "echo 'IP: ' && hostname -I && "
                "echo 'Uptime: ' && uptime && "
                "echo 'Memória: ' && free -h && "
                "echo 'Disco: ' && df -h / && "
                "echo 'Usuários logados: ' && who"
            )
            full_command = f"cd {session['cwd']} && {dashboard_cmd}"
            output = ssh_execute_command(
                session.get('host'),
                session.get('user'),
                session.get('password'),
                full_command
            )

        if command.strip().startswith('cd'):
            parts = command.strip().split()
            if len(parts) > 1:
                new_dir = parts[1]
                # Atualiza o cwd para o novo caminho
                if new_dir == "..":
                    session['cwd'] = f"{session['cwd']}/.."
                elif new_dir.startswith("/"):
                    session['cwd'] = new_dir
                else:
                    session['cwd'] = f"{session['cwd']}/{new_dir}"
            output = f"Diretório alterado para: {session['cwd']}"
        else:
            # Executa o comando com base no diretório atual
            full_command = f"cd {session['cwd']} && {command}"
            output = ssh_execute_command(
                session.get('host'),
                session.get('user'),
                session.get('password'),
                full_command
            )

    return render_template('panel.html', output=output)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
