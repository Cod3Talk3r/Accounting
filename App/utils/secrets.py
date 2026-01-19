from passlib.context import CryptContext

passwordManager = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")
