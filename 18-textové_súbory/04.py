f_mena = open("mena.txt", "r", encoding="utf-8")
f_priezviska = open("priezviska.txt", "r", encoding="utf-8")
f_mena_priezviská = open("mena_priezviska.txt", "w", encoding="utf-8")

for meno in f_mena:
    priezvisko = f_priezviska.readline()
    print(f"{meno.strip()} {priezvisko.strip()}")
    print(f"{meno.strip()} {priezvisko.strip()}", file=f_mena_priezviská)
f_mena.close()
f_priezviska.close()
f_mena_priezviská.close()