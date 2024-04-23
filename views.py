from flet import *
from pages.home import Home
from pages.test import Test
from pages.login import Login

def views_handler(page):
  return {
    '/home':View(
        route='/',
        controls=[
          Home(page)
        ]
      ),
    '/login':View(
        route='/login',
        controls=[
          Login(page)
        ]
      ),
      '/test': View(
        route='/test',
        controls=[
          Test(page)
        ]
      )
  }