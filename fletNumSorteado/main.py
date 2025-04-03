import flet as ft
import random
def main(page: ft.Page):
    page.title= f'Acerte os Números'
    page.window.width = 400
    page.window.height = 500
    campo_texto = ft.TextField(label='Digite um número...') # variavel para guardar texto

    resultado_text = ft.Text("") # text para guardar o resultado
    imagem = ft.Image(src='flork.png', width=300, height=600, visible=False)

    num_sort = random.randint(0,100)
    def on_click(e):
        nonlocal num_sort # Permite alterar a variável dentro da função
        try:
            numero = int(campo_texto.value)
            if numero == num_sort:
                resultado_text.value = f'Você acertou!'
                imagem.visible = True
            elif numero > num_sort:
                resultado_text.value = f'O número é menor'
            elif numero < num_sort:
                resultado_text.value = f'O número é maior'
            else:
                resultado_text.value = f'Você errou!'
        except ValueError:
            resultado_text.value = f'Por favor, digite um número válido!'

        page.update()
    botao = ft.ElevatedButton(text='Enviar', on_click=on_click)

    page.add(campo_texto, botao, resultado_text, imagem)


ft.app(target=main)

