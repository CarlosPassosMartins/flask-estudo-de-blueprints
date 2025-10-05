# flask-estudo-de-blueprints

Este projeto é um **exemplo de aplicação Flask** que implementa um sistema de **login FAKE** com um dashboard, utilizando **Blueprits** para organizar melhor as rotas e separar responsabilidades.

O objetivo principal é estudar e entender como os **Blueprints** funcionam no Flask, permitindo modularizar rotas, templates e arquivos estáticos de maneira organizada.

---

## Funcionalidades

- Registro de usuários (simples, em memória via lista `Data`).
- Login e logout de usuários.
- Redirecionamento para o dashboard (`home`) após login.
- Dashboard personalizado exibindo o nome do usuário logado.
- Estrutura modular utilizando Blueprints (`auth` e `home`).

---

## Tecnologias utilizadas

- Python 3.x
- Flask
- HTML, CSS, JS (templates simples)
- Sessões do Flask para gerenciar login de usuários
- Estrutura de Blueprints para modularizar rotas

---

## Estrutura do projeto

```
flask-estudo-de-blueprints/
│
├─ app.py                  # Arquivo principal da aplicação Flask
├─ data.py                 # Lista de usuários (simulando um banco de dados)
│
├─ auth/
│   ├─ routes.py           # Rotas de autenticação (login, cadastro, logout)
│   ├─ template/           # Templates HTML relacionados ao auth
│   │   └─ login_form.html
│   └─ static/             # Arquivos estáticos do auth (CSS, JS, imagens)
│
├─ home/
│   ├─ routes.py           # Rotas do dashboard/home
│   ├─ template/           # Templates HTML relacionados ao home
│   │   └─ home.html
│   └─ static/             # Arquivos estáticos do home
│
└─ README.md
```

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/flask-estudo-de-blueprints.git
cd flask-estudo-de-blueprints
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install flask
```

---

## Como usar

1. Execute a aplicação:

```bash
python app.py
```

2. Acesse no navegador:

```
http://127.0.0.1:5000/
```

3. Você será redirecionado para a tela de login. A partir daqui é possível:

- Cadastrar um novo usuário (via rota `/cadastro`).
- Fazer login com usuário existente.
- Acessar o dashboard (`/home`) após login.
- Fazer logout (via `/logout`).
- verificar a lista de usuarios em (`/lista`)

---

## Notas sobre o projeto

- Os dados dos usuários estão **armazenados em memória** (`data.py`) e **não persistem** após o encerramento do servidor.
- Os Blueprints foram utilizados para **separar o módulo de autenticação (`auth`) do módulo do dashboard (`home`)**.
- Cada Blueprint possui seu próprio diretório de **templates** e **arquivos estáticos**, permitindo maior modularidade.

---

## Estrutura dos Blueprints

- **Auth Blueprint (`auth`)**
  - Rotas de login (`/login`), cadastro (`/cadastro`) e logout (`/logout`).
  - Template: `login_form.html`.
  - Static: CSS e JS específicos do auth.
  
- **Home Blueprint (`home`)**
  - Rota principal `/home/`.
  - Template: `home.html`.
  - Static: CSS e JS específicos do home.

---

## Melhorias para o futuro

- Substituir a lista `Data` por um **banco de dados real** (SQLite, PostgreSQL, etc.).
- Adicionar validação de formulários (Flask-WTF).
- Implementar hash de senhas (para não armazenar senhas em texto plano).
- Criar um sistema de permissões e roles.
- Melhorar o design e implementar as outras áreas do dashboard.

---

## Licença

Este projeto é **open-source** e pode ser usado para fins de estudo.
