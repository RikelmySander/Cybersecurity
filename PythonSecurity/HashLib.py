from hashlib import sha256

while True:
    senha = input()
    senha = sha256(senha.encode('utf-8')).hexdigest()
    print(senha)