# Rodar o projeto
1. Navegar até a pasta raiz do projeto, `fastapi-tutorial`
2. Rodar o comando:
    uvicorn `main:app --reload`

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