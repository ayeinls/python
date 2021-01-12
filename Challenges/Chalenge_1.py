def obfuscate(byt):
    mask = b'keyword'
    lmask = len(mask)
    return bytes(c ^ mask[i % lmask] for i, c in enumerate(byt))
string = obfuscate(b'=\n\x0c\x04O\x13\x12\x0e\x1fY\x05\n\x07\x17\x18\x0cY\x1b\nR\x07\x03\x04\x15\x1b\n\x1c\x03\x0eE\x15\x12O\x1f\x0b\x1fE\x1d\x12O\x02\x05\x18\x16\x1cW\x0b\x07D\x08\r\x18\x1b\n\x1c\x03\x0eE\x1c\x04\x1bR\x08\x0eE\x14\x18\x1bR\x00\x0eE\t\x16\x1c\x01\x01K\x04\x1d\x1a\x06\x1cB=\n\x0c\x04O\xb1\xce\x1f\x00\nW\x0c\x1d\n\x05\x00\x1a\x03\nR\x01\x05E\r\x16\x01\x06D\x1a\x10^\x02\x1b\x1b\x08\x02\x16\x18\x03\n\x07\x16').decode();

print("Bienvenue sur l'interface\n");
accounts = ["" for x in range(2*2)];

#Here are the passwords
accounts = "admin user".split(" ");
passwords = "MotDePasseAdmin user".split(" ");

#User interface
credentials = ["" for x in range(2)];
credentials[0] = input("login: ");
credentials[1] = input("password: ");

#Where cheking the account
for i, account in enumerate(accounts):
    if account == credentials[0] and passwords[i] == credentials[1]:
    	print(string.split("&")[i]);
    	exit(0);
print("Les informations fournie sont incorrecte");