#Kamen Skare Papir Guster Spock

Igrac1 = input("Neka igrač broj 1, pokaže što želi (kamen, skare, papir, guster, spock):  ")
Igrac2 = input("Neka igrač broj 2, pokaže što želi (kamen, skare, papir, guster, spock):  ")

if Igrac1 == "kamen" and Igrac2 == "skare":
    print('Igrač 1 je pobijedio!!')
elif Igrac1 == "kamen" and Igrac2 == "guster":
    print('Igrač 1 je pobijedio!!')
elif Igrac1 == "kamen" and Igrac2 == "papir":
    print('Igrač 2 je pobijedio!!')
elif Igrac1 == "kamen" and Igrac2 == "spock":
    print('Igrač 2 je pobijedio!!')

elif Igrac1 == "skare" and Igrac2 == "papir":
    print('Igrač 1 je pobijedio!!')
elif Igrac1 == "skare" and Igrac2 == "guster":
    print('Igrač 1 je pobijedio!!')
elif Igrac1 == "skare" and Igrac2 == "kamen":
    print('Igrač 2 je pobijedio!!')
elif Igrac1 == "skare" and Igrac2 == "spock":
    print('Igrač 2 je pobijedio')

elif Igrac1 == "spock" and Igrac2 == "skare":
    print('Igrač 1 je pobijedio!!')
elif Igrac1 == "spock" and Igrac2 == "kamen":
    print('Igrač 1 je pobijedio!!')
elif Igrac1 == "spock" and Igrac2 == "guster":
    print('Igrač 2 je pobijedio!!')
elif Igrac1 == "spock" and Igrac2 == "papir":
    print('Igrač 2 je pobijedio!!')

elif Igrac1 == "guster" and Igrac2 == "papir":
    print('Igrač 1 je pobijedio!!')
elif Igrac1 == "guster" and Igrac2 == "spock":
    print('Igrač 1 je pobijedio!!')
elif Igrac1 == "guster" and Igrac2 == "skare":
    print('Igrač 2 je pobijedio!!')
elif Igrac1 == "guster" and Igrac2 == "kamen":
    print('Igrač 2 je pobijedio')

elif Igrac1 == "papir" and Igrac2 == "kamen":
    print('Igrač 1 je pobijedio!!')
elif Igrac1 == "papir" and Igrac2 == "spock":
    print('Igrač 1 je pobijedio!!')
elif Igrac1 == "papir" and Igrac2 == "guster":
    print('Igrač 2 je pobijedio!!')
elif Igrac1 == "papir" and Igrac2 == "skare":
    print('Igrač 2 je pobijedio!!')
else:
    print('Neriješeno')
