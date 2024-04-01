from flet import *

def main(page: Page):
    page.window_width = 500
    page.window_height = 700
    page.title = "Bem Vindo!"
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER

    btn_login = ElevatedButton(
        text="Login",
        bgcolor="#012E40",
        color="#FFFFFF",
        width="220",
        height="48",
        on_click= lambda _: page.go("/home")
    )
    image_texto = Image(
        height=33,
        width=262,
        src="./imgs/CRAJUBAR360.png"
    )
    
    image_logo = Image(
        height=61,
        width=74,
        src="./imgs/Country.png"
    )
    
    txt_login = TextField(
        label='Digite seu login...',
        width = 333,
        height=42,
        text_align= TextAlign.CENTER,
    )
    
    txt_senha = TextField(
        label='Digite sua senha...',
        width = 333,
        height=42,
        text_align= TextAlign.CENTER,
    )
    
    topo = Column(
        controls = [
        image_logo,
        image_texto,
        ]
    )
    
    baixo = Column(
        controls = [
        txt_login,
        txt_senha,
        btn_login
        ]
    )

    layout = Container( 
        height=700,
        width=500,
        image_src="imgs/fundo.png",
        image_fit="cover",
        bgcolor="#161515",
        padding= padding.all(38),
            content = Column( 
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.END,
            controls=[
                topo,
                baixo
            ]  
            )
        )  

    page.add(layout)


app(target=main)