from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static, Placeholder, Input, Label

from list_item import ListItem
from list_view_class import ListView
from data_set import *


class ChemApp(App):
    CSS_PATH = "chem_ui.css"
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield MainPanel()
        yield InputArea()

class MainPanel(Static):
    def compose(self) -> ComposeResult:
        yield InstructionsWindow()
        yield DataWindow()
        yield OutputWindow()


class InstructionsWindow(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder()

class DataWindow(Static):
    def compose(self) -> ComposeResult:
        list_view = ListView()
        items = self.generate_list()
        for item in items:
            list_view.append(item)
        yield list_view
    def generate_list(self):

        df = load_data_frame()


        labels = []
        for index, row in df.iterrows():
            item = ListItem(Label(f'{row["name"]}\t{row["formula"]}'))
            labels.append(item)
        return labels

class OutputWindow(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder()

class InputArea(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Some input")

