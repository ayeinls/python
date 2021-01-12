import hashlib
print("Bienvenue sur l'interface\n");
accounts = ["" for x in range(2*2)];

#Here are the passwords
accounts = "admin user".split(" ");
passwords = "e64b78fc3bc91bcbc7dc232ba8ec59e0 ee11cbb19052e40b07aac0ca060c23ee".split(" ");

#User interface
credentials = ["" for x in range(2)];
credentials[0] = input("login: ");
#This time with hash
credentials[1] = hashlib.md5(input("password: ").encode()).hexdigest();

#Where cheking the account
for i, account in enumerate(accounts):
    if account == credentials[0] and passwords[i] == credentials[1]:
    	print("Vous avez reussi le challenge le mot de passe du chalenge est le mot de passe admin&Vous êtes connecté en tant qu'utilisateur".split("&")[i]);
    	exit(0);
print("Les informations fournie sont incorrecte");