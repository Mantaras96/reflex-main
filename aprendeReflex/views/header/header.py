import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
       rx.avatar(
           name="Albert Mantaras",
           size="xl"
       ),
       rx.text("@Albert Mantaras"),
       rx.text("Hola mi nombre es Albert Mantaras"),
       rx.text("""Soy desarrallador desde hace mas de 5 años.
               Actualmente trabajo como full-stack para la empresa Aluvisa
               Aqui podeis encontrar mi portfilio""")
    )
    
