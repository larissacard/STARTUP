from flet import *
from views import views_handler

def main(page: Page):
  page.title = "CARIRI 360"
  page.horizontal_alignment = MainAxisAlignment.CENTER
  page.vertical_alignment = MainAxisAlignment.CENTER
  page.window_min_width = 500
  page.window_min_height = 900
  page.fonts = {
    "Poppins": "https://github.com/google/fonts/blob/main/ofl/poppins/Poppins-Regular.ttf",
    "Poppins Bold": "https://github.com/google/fonts/blob/main/ofl/poppins/Poppins-BoldItalic.ttf"
  }

  def route_change(route):
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