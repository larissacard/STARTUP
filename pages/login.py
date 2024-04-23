from flet import *
import json

class Login(UserControl):
    def __init__(self, page):
        super(Login, self).__init__()
        self.email = TextField(
            label="Email", 
            hint_text="Digite aqui...",
            width=300, 
            height=30,
            border_radius=8, 
            border_color="#AAAABC"
            )
        self.password = TextField(
            label="Password", 
            hint_text="Digite aqui...",
            height=30, 
            width=300, 
            border_radius=8, 
            border_color="#AAAABC",
            password=True, 
            can_reveal_password=True, 
            )

    def build(self):
        image = Image(
            height=61,
            width=74,
            src="./logo.png"
        )

        logo_title =  Text(
            value="CARIRI360",
            color="#FFFFFF",
            size=32,
            font_family="Poppins"
        )

        logoBar = Column(
            spacing=2,
            alignment = MainAxisAlignment.CENTER,
            controls = [
                image,
                logo_title,
            ]
        )   

        title = Text(
            value="LOGIN",
            color="#C4C4C4",
            size=32,
        )

        login_button = FilledButton(
            text="Login",
            width="300",
            height="48",
            on_click= self.loginbtn,
            style= ButtonStyle(
                color={
                    MaterialState.DEFAULT: "#FFFFFF"
                },
                bgcolor={
                    MaterialState.DEFAULT: "#012E40"
                },
                side={
                    MaterialState.DEFAULT: RoundedRectangleBorder(radius=17)
                },
                elevation={"pressed": 0, "": 1},
            )
        )

        return Container(
            bgcolor="#161515",
            height=844,
            width=390,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    logoBar,
                    title,
                    self.email,
                    self.password,
                    login_button,
                ] 
            )
        )

    def loginbtn(self, e):
        with open("users.json", "r") as f:
            data = json.load(f)
        email = self.email.value
        password = self.password.value

        for user in data["users"]:
            if user["email"] == email and user["password"] == password:
                dataLogin = {
                    email: self.email.value
                }

                self.page.session.set("login", dataLogin)
                self.page.go("/test")
                print("Login autenticado!!")
            else:
                print("login errado!")



