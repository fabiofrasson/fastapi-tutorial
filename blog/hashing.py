from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    # anotação sugerida pelo sonarlint
    @staticmethod
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    # anotação sugerida pelo sonarlint
    @staticmethod
    def verify(req_pwd: str, db_pwd: str):
        return pwd_cxt.verify(req_pwd, db_pwd)
