from flet import *
from views import views_handler

def main(page: Page):

  def route_change(route):
    print(page.route)
    page.views.clear()
    page.views.append(
      views_handler(page)[page.route]
    )
    page.update()

  def view_pop(view):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)


  page.on_route_change = route_change
  page.on_view_pop = view_pop
  page.go('/home')



app(target=main)