ip_test = "192.168.1.222"

def ip_tester(ip):
    octetos = ip.split(".")
    if len(octetos) != 4:
        return False
    for octeto in octetos:
        try:
            octeto = int(octeto)
        except ValueError:
            return False
        if octeto > 255 or octeto < 0:
                return False
    return True

print(ip_tester(ip_test))