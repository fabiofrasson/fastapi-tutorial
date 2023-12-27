Run project: uvicorn `main:app --reload`

Caso queira adicionar argumentos ou mudar a porta do modo debug, realize este caminho:
1. Abrir o painel 'Run and Debug' (`CTRL + Shift + D`);
2. Clicar em `'create a launch.json file' > 'Python' > 'FastAPI'`; 
3. O arquivo será criado. Altere a lista de argumentos a partir de `'configuration.args'`:
    "args": [
            "main:app",
            "--reload",
            "--port",
            "9000"
          ],

[OpenAPI Documentation](http://localhost:8000/docs)

[Redoc Documentation](http://localhost:8000/redoc)