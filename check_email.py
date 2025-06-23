valid_examples = ["ejemplo@ejemplo.com", "ejemplo@ejemplo.es", "mi.ejemplo@ejemplo.ai", "ejemplo+alias@ejemplo.com", "nomber_apellido-otroapellido@ejemplo.com", "1234567890@ejemplo.us"]
invalid_examples = ["ejemplo@.com", "ejemplo@es", "@ejemplo.comi", "ejemplo@", "ejemplo", "ejemplo@ejemplo..com"]


valid_domains =("ai", "es", "com", "us")
valid_characteres = ("abcdefghijklmnopqrstuvwxyz1234567890._+-")

def check_email(email:str) -> bool:
    email = email.lower()
    
    if email.count("@") == 1:
        username, domain = email.split("@")
    else:
        return False

    if domain.startswith(".") or domain.endswith(".") or ".." in domain:
        return False
    
    domain = domain.split(".")
    
    if len(domain) < 2 or domain[-1] not in valid_domains:
        return False
    
    for character in username:
        if character not in valid_characteres:
            return False
    
    for part in domain:
        for character in part:
            if character not in valid_characteres:
                return False
    
    return True

print("Valid:")
for email in valid_examples:
    print(check_email(email))

print("Invalid:")
for email in invalid_examples:
    print(check_email(email))