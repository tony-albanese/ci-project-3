from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static, Placeholder

class ChemApp(App):
    CSS_PATH = "chem_ui.css"
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield InputArea()
        yield  MainPanel()


class InstructionsWindow(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder()

class DataWindow(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder()

class OutputWindow(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder()

class MainPanel(Static):
    def compose(self) -> ComposeResult:
        yield Container(InstructionsWindow(), DataWindow(), OutputWindow())

class InputArea(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder()