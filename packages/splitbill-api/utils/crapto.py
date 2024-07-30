from uuid import uuid4
import settings

def hash_password(passowrd):
  salt = uuid.uuid4().hex
  return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
  
def check_password(hashed_password, user_password):
  password, salt = hashed_password.split(':')
  return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
