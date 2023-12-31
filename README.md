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

# Informações adicionais sobre o tutorial:

- A atualização dos registros no banco é feita utilizando o objeto Query, que atualmente é [depreciado](https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html#legacy-query-methods).
O método atual para upserts e deletes é [este](https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html#orm-update-and-delete-with-custom-where-criteria).
- A query de update retorna com 'internal server error'. Um comentário no vídeo menciona como corrigir o problema:

> Update - When using db.query(models.Blog).filter(models.Blog.id == id).update(request) you are saying to attempt and update every item that would be passed in the request. In doing this you allow it to attempt and change attributes that have no data or attributes that you may not think exist. This is what causes the crash here (again hidden by --reload). You can fix this with a minor change to the statement -> 
db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())

- a configuração de ORM Mode (abaixo) no schema 'BlogResponse' não foi necessária. A chamada funcionou normalmente apenas deixando o conteúdo do schema como `pass`.
```
class Config:
        orm_mode = True
``` 
- Caso prefira setar as versões das libs do projeto, é possível utilizar o comando `pip freeze`, contido [neste artigo](https://note.nkmk.me/en/python-pip-install-requirements/#:~:text=First%2C%20redirect%20the%20output%20of,a%20file%20named%20requirements.txt%20.&text=Next%2C%20copy%20or%20move%20this,it%20to%20install%20the%20packages.&text=By%20following%20these%20steps%2C%20you,from%20one%20environment%20to%20another).
- Foi criada uma classe (hashing.py) reponsável pela encriptação da senha na criação de usuário. O Sonarlint sugeriu converter a função principal para um método estático para não precisar indicar um primeiro argumento implícito: 
> Convert a function to be a static method. A static method does not receive an implicit first argument.
>To declare a static method, use this idiom:
>```
>class C:
>        @staticmethod def f(arg1, arg2, argN):
>        ...
>```
- A configuração 'orm_mode' em schemas foi atualizada para 'from_attributes':
>UserWarning: Valid config keys have changed in V2:
>* 'orm_mode' has been renamed to 'from_attributes'
  warnings.warn(message, UserWarning)
- Aproximadamente em [3:45 de vídeo](https://youtu.be/7t2alSnE2-I?si=5ZHwRqr511yBrAcc&t=13551), quando a autenticação é testada na documentação OpenAPI, a aplicação lançou um erro:
>RuntimeError: Form data requires "python-multipart" to be installed.    
>You can install "python-multipart" with:
>pip install python-multipart

Esse erro foi corrigido adicionando-se a lib sugerida em requirements e rodando o comando para instalar suas dependências: `pip3 install -r requirements.txt`.

# Próximos passos

1. Refatorar o projeto considerando boas práticas para o framework/linguagem;
2. Verificar os templates presentes na [documentação](https://fastapi.tiangolo.com/project-generation/), e organizar próximos projetos de maneira similar.
3. Inteirar-se sobre como é feito um deploy.