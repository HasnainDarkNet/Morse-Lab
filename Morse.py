import base64
import os

# ===== COLORS =====
G = "\033[92m"   # green
R = "\033[91m"   # red
Y = "\033[93m"   # yellow
B = "\033[94m"   # blue
W = "\033[0m"    # reset

# ===== BANNER =====
def banner():
    os.system("clear")
    print(G + """
███╗   ███╗ ██████╗ ██████╗ ███████╗███████╗
████╗ ████║██╔═══██╗██╔══██╗██╔════╝██╔════╝
██╔████╔██║██║   ██║██████╔╝███████ █████╗  
██║╚██╔╝██║██║   ██║██╔══██╗     ██ ██╔══╝  
██║ ╚═╝ ██║╚██████╔╝██║  ██║███████╗███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
        
""" + W)
    print(Y + "     🔐 HASNAIN DARK NET CYBER TOOLKIT 🔐\n" + W)

# ===== MORSE =====
MORSE = {
 'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
 'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
 'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
 'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
 'Y':'-.--','Z':'--..',' ':'/'
}
REVERSE = {v:k for k,v in MORSE.items()}

def to_morse(text):
    return " ".join(MORSE.get(i.upper(), '?') for i in text)

def from_morse(code):
    return "".join(REVERSE.get(i, '') for i in code.split())

# ===== BASE64 =====
def b64_enc(t):
    return base64.b64encode(t.encode()).decode()

def b64_dec(t):
    return base64.b64decode(t.encode()).decode()

# ===== FILE EXTRACT =====
def extract():
    path = input(Y+"Enter file path: "+W)
    try:
        with open(path,'r') as f:
            print(G+"\n--- FILE CONTENT ---\n"+W)
            print(f.read())
    except:
        print(R+"File not found!"+W)

# ===== MENU =====
while True:
    banner()
    print(B+"[1] Morse Encode")
    print("[2] Morse Decode")
    print("[3] Base64 Encode")
    print("[4] Base64 Decode")
    print("[5] File Extractor")
    print("[6] Exit"+W)

    ch = input(Y+"\nSelect option: "+W)

    if ch == "1":
        t = input("Text: ")
        print(G+to_morse(t)+W)
        input("\nPress Enter...")

    elif ch == "2":
        t = input("Morse: ")
        print(G+from_morse(t)+W)
        input("\nPress Enter...")

    elif ch == "3":
        t = input("Text: ")
        print(G+b64_enc(t)+W)
        input("\nPress Enter...")

    elif ch == "4":
        t = input("Base64: ")
        print(G+b64_dec(t)+W)
        input("\nPress Enter...")

    elif ch == "5":
        extract()
        input("\nPress Enter...")

    elif ch == "6":
        print(R+"Exiting..."+W)
        break

    else:
        print(R+"Invalid Option"+W)



