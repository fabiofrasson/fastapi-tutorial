from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definindo a URL do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

print("Database URL is ", SQLALCHEMY_DATABASE_URL)

# Criando o objeto Engine do SQLAlchemy para interagir com o banco de dados
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
)

# Criando uma fábrica de sessões para o SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarando uma classe Base para ser usada na definição de modelos
Base = declarative_base()

        # Explicando cada parte:

# - `create_engine`: Cria um objeto Engine que representa a interface entre o aplicativo e o banco de dados.
# - `SQLALCHEMY_DATABASE_URL`: A URL de conexão com o banco de dados SQLite.
# - `SessionLocal`: Uma fábrica de sessões que será usada para criar sessões do SQLAlchemy.
# - `autocommit=False`: Configuração para desativar a confirmação automática após cada transação.
# - `autoflush=False`: Configuração para desativar o flush automático, que sincroniza a sessão com o estado do banco de dados.
# - `Base`: Classe declarativa base que será usada como base para a definição de modelos SQLAlchemy.
