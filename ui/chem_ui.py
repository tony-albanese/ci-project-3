from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static

class ChemApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()



