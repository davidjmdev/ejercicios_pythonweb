# Validos:
# ["ejemplo@ejemplo.com,
# "ejemplo@ejemplo.es",
# "mi.ejemplo@ejemplo.ai",
# "ejemplo+alias@ejemplo.com",
# "nomber_apellido-otroapellido@ejemplo.com",
# "1234567890@ejemplo.us"]

# Invalidos:
# ["ejemplo@.com,
# "ejemplo@es",
# "@ejemplo.comi",
# "ejemplo@",
# "ejemplo",
# "ejemplo@.ejemplo.es",
# "ejemplo@ejemplo..com"]

valid_domains =("ai", "es", "com")
valid_characteres = ("abcdefghijklmnopqrstuvwxyz._+-")

def check_email(email:str) -> bool:
    email = email.lower()

    try:
        username, domain = email.split("@")
    except:
        return False
    
    try:
        domain_name, domain = domain.split(".")
    except:
        return False
    
    if domain not in valid_domains:
        return False
    
    for character in username:
        if character not in valid_characteres:
            return False
    
    for character in domain_name:
        if character not in valid_characteres:
            return False
    
    return True

print(check_email("prueba@jdo@dsd.com"))