texto = str(input("Digite o texto a ser revisado: "))
plv_sub = str(input("Qual palavra deseja substituir? "))
plv_nova = str(input("Qual a nova palavra? "))

texto_novo = f"{plv_sub}".replace(f"{plv_sub}", f"{plv_nova}")

print(f"O dia está {texto_novo}, tudo está {texto_novo}")