for letter in string.ascii_uppercase:
    with open(letter+".text","w") as f:
        f.writelines(letter)