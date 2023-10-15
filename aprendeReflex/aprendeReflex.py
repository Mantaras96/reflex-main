import reflex as rx
from aprendeReflex.components.navbar import navbar
from aprendeReflex.views.header.header import header
from aprendeReflex.views.links.links import links
from aprendeReflex.components.footer import footer

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
    )

app = rx.App()
app.add_page(index)
app.compile()