import reflex as rx
import datetime

def footer() -> rx.Component:
    
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.link(
            f"2020 - {datetime.date.today().year} AlbertDev BY AlbertDev v1 Building Software",
            href="www.google.com",
            is_external=True
        ),
        rx.text("FROM BARCELONA TO THE WORLD")
    )