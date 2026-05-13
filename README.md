# Meu primeiro app em Django

Projetinho bem simples com o propósito de estudar e praticar o uso do framework Django. Por mais simples que pareça este projeto me ensinou sobre como funciona o design pattern MTV (Model Template View) e o ciclo de vida de uma requisição.

## Estrutura:

```
app/
├── migrations/
├── templates/
│   └── users/
│       ├── confirm_delete.html
│       ├── form.html
│       └── list.html
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── urls.py
└── views.py
config/
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
manage.py
pyproject.toml
```

## Para rodar o projeto:
Certifique-se que o Python está instalado e em seguida rode os seguintes comandos no terminal:

```bash
uv venv
source .venv/Scripts/activate
uv add django
uv run manage.py migrate
uv run manage.py runserver
```

## Para interagir com as rotas acesse o projeto localmente através do link: 
http://localhost:8000/users/

ou

http://127.0.0.1/users/

## Como funciona o projeto:

O projeto é composto por duas partes principais:

### /app:
1. **views.py**: Responsável por gerenciar as requisições e respostas. Em resumo é onde fica a "lógica" da aplicação.
2. **urls.py**: Mapeia as rotas para as views.
3. **models.py**: Modela as tabelas do banco de dados.
4. **/templates**: Renderiza as páginas HTML.
5. **forms.py**: Gerencia os formulários de criação e edição de usuários.
6. **admin.py**: Gerencia o painel administrativo das permissões do admin, também é onde se registra os modelos que vão aparecer no painel administrativo.
7. **/migrations**: Pasta que gerencia o versionamento das migrações do banco de dados.
8. **__init__.py**: Torna a pasta um pacote Python.
9. **apps.py**: Configurações da própria aplicação, raramente usado.
10. **tests.py**: Onde ficam os testes automatizados para o app. (Não usei até o momento)


### /config:
1. **settings.py**: Define o banco de dados, apps instalados, arquivos estáticos, etc. Basicamente o coração do projeto.
2. **urls.py**: Roteador principal, basicamente é aqui que as urls são mapeadas e as views são chamadas. Também é responsável por importas as urls de outros apps.
3. **wsgi.py**: Interface entre o servidor e o Django (requisições síncronas).
4. **asgi.py**: Interface entre o servidor e o Django (requisições assíncronas).
5. **__init__.py**: Torna a pasta um pacote Python.

### /root: <--- Raíz do projeto
1. **manage.py**: Responsável por gerenciar todo o projeto.
2. **pyproject.toml**: Gerenciador de dependências.
3. **README.md**: Documentação do projeto.
4. **db.sqlite3**: Banco de dados do projeto. (Apenas se o banco de dados for sqlite)
5. **.venv:** Ambiente virtual do projeto.
6. **.gitignore**: Arquivos que devem ser ignorados pelo git.


## Rotas:
A rota http://localhost:8000/users/ é responsável por listar todos os usuários cadastrados no sistema. 

A rota http://localhost:8000/users/new/ é responsável por criar um novo usuário. 

A rota http://localhost:8000/users/(id)/edit/ é responsável por editar um usuário específico. 

A rota http://localhost:8000/users/(id)/delete/ é responsável por deletar um usuário específico. 

