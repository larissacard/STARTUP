from flet import *
from views import views_handler

def main(page: Page):
    page.title = "CARIRI 360"
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.window_min_height = 900
    page.bgcolor = colors.AMBER

    image =  Image(
        height=61,
        width=74,
        src="./logo.png"
      )
      

    title =  Text(
        value="CARIRI 360",
        color="#FFFFFF",
        size=32,
    )
      

    description =  Text(
        value="Descubra lugares, atividades, hobbies em volta da sua cidade predileta. Aventure-se por onde nunca foi.",
        color="#FFFFFF",
        size=16,
        text_align= TextAlign.CENTER,

    )
      

    logoBar = Row(
        controls = [
            image,
            title,
        ]
    )
      
    bttn_start = ElevatedButton(
        text="Iniciar",
        bgcolor="#012E40",
        color="#FFFFFF",
        width="192",
        height="48",
        on_click= lambda _: page.go('/test')
    )


    layout = Container(
        height=844,
        width=390,
        image_src="./padre.jpg",
        image_fit="cover",
        bgcolor="#161515",
        padding= padding.all(38),
        content= Column( 
        alignment=MainAxisAlignment.END,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                logoBar,
                description,
                bttn_start
            ]
        )
    )

    page.add(layout)

app(target=main)