# Rodar o projeto
1. Navegar até a pasta raiz do projeto, `fastapi-tutorial`
2. Rodar o comando `pip install -r requirements.txt` para instalar as dependêcias do projeto
3. Subir a aplicação com o comando `uvicorn blog.main:app --reload`
4. Caso queira exportar as bibliotecas e versões atuais do projeto, utilizar `pip freeze > nome_arquivo.txt`. O arquivo `requirements-dev.txt` foi gerado a partir desse mesmo comando.

# Configuração do modo debug

Caso queira adicionar argumentos ou mudar a porta do modo debug (VSCode), realize estes passos:
1. Abrir o painel 'Run and Debug' (`CTRL + Shift + D`)
2. Clicar nas opções `'create a launch.json file' > 'Python' > 'FastAPI'`
3. O arquivo será criado. Altere a lista de argumentos a partir de `'configuration.args'`:

```
"args": [
        "main:app",
        "--reload",
        "--port",
        "9000"
      ],
```

# Documentação da API

- [OpenAPI Documentation](http://localhost:8000/docs)

- [Redoc Documentation](http://localhost:8000/redoc)