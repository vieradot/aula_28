def validar_senha(senha):
    # Verificar o comprimento da senha
    if len(senha) < 6 or len(senha) > 32:
        return False
    
    # Verificar se há pelo menos uma letra maiúscula, uma letra minúscula e um número
    has_upper = False
    has_lower = False
    has_digit = False
    for char in senha:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    if not (has_upper and has_lower and has_digit):
        return False
    
    # Verificar se não há caracteres de pontuação, acentuação ou espaço
    for char in senha:
        if not char.isalnum():
            return False
    
    return True

if __name__ == "__main__":
    while True:
        try:
            senha = input()
            if validar_senha(senha):
                print("Senha valida.")
            else:
                print("Senha invalida.")
        except EOFError:
            break
