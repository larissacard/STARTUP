from flet import *
from views import views_handler

def main(page: Page):

  def mudancas_de_rotas(rota):
    print(page.rota)
    page.views.clear()
    page.views.append(
      views_handler(page)[page.rota]
    )


  page.on_mudancas_de_rotas = mudancas_de_rotas
  page.go('/home')



app(target=main)