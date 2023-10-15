import reflex as rx
from aprendeReflex.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://www.google.com"),
        link_button("YouTube", "https://www.google.com"),
        link_button("YouTube (Sec)", "https://www.google.com"),
        link_button("Disocrds", "https://www.google.com")
    )