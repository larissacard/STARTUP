from flet import *


class Test(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
    
    def build(self):
        return Container(
            bgcolor="red",
            content= Column(
                controls=[
                    Text("Logado!")
                ]
            )
        )
