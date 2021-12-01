import random
import string

def generate_password(size: int = 16) -> str:
    """Gera uma string aleatória como senha do usuário"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=size))
