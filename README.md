# Painel SSH

Este é um projeto simples de painel SSH desenvolvido com Flask. Ele permite que os usuários se conectem a um servidor remoto via SSH, executem comandos e visualizem os resultados diretamente em uma interface web.

## Funcionalidades

- **Login SSH**: Conecte-se a um servidor remoto fornecendo o host, usuário e senha.
- **Execução de Comandos**: Execute comandos diretamente no servidor remoto.
- **Dashboard**: Visualize informações do sistema, como IP, uptime, memória, disco e usuários logados.
- **Logout**: Desconecte-se da sessão SSH.

## Estrutura do Projeto

```
ssh-panel/
├── app.py                
├── ssh_utils.py          
├── requirements.txt         
├── templates/
│   ├── index.html        
│   ├── panel.html        
```

## Requisitos

- Python 3.10 ou superior
- Bibliotecas Python:
  - `Flask`
  - `paramiko`

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/TheEddu/ssh-panel.git
   cd ssh-panel
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o projeto:
   ```bash
   python app.py
   ```

5. Acesse a aplicação no navegador:
   ```
   http://127.0.0.1:5000
   ```

## Uso

1. **Login**: Insira o host, usuário e senha para se conectar ao servidor remoto (Nesse caso, usei uma VM no VirtualBox).
2. **Painel de Comandos**:
   - Digite comandos no campo de entrada e clique em "Executar".
   - Use o botão "Ver Dashboard" para visualizar informações do sistema.

3. **Logout**: Clique em "Desconectar" para encerrar a sessão.

## Segurança

- **Chave Secreta**: Substitua a chave secreta em `app.py` (`app.secret_key`) por uma chave segura antes de usar em produção.
- **Senhas**: As senhas são armazenadas na sessão apenas durante a execução, isso é apenas um lab local, mas não é seguro para ambientes reais.