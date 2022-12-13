from rich.table import Table
from textual import events
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static, Placeholder, Input, Label, TextLog

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

    def on_ready(self) ->None:
        print("on_ready")
        data_log = self.query_one("#data_log_window", TextLog)
        data_log.write("Hello, world!")

class MainPanel(Static):
    def compose(self) -> ComposeResult:
        yield InstructionsWindow()
        yield DataWindow()
        yield OutputWindow()

class DataWindow(Static):
    def compose(self) -> ComposeResult:
        print("DataWindow compose()")
        yield TextLog(id="data_log_window")

    def _on_mount(self, event: events.Mount) -> None:
        log = self.query_one(TextLog)
        table = self.generate_data_table()
        log.write(table)
    def generate_data_table(self):
        df = load_data_frame()
        table = Table(title="Chemical Data")
        table.add_column('index')
        table.add_column('Name')
        table.add_column('formula')
        table.add_column('state')
        for index, row in df.iterrows():
            table.add_row(str(index), row["name"],row["formula"],row["state"] )
        return table

class InstructionsWindow(Static):

    WELCOME_MESSAGE = '''\
    These are the initial instructions
    '''
    def compose(self) -> ComposeResult:
        yield TextLog(id="instruction_log_window")

    def _on_mount(self, event: events.Mount) -> None:
        instructions_window = self.query_one("#instruction_log_window")
        instructions_window.write(self.WELCOME_MESSAGE)



















































class OutputWindow(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder()

class InputArea(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Some input")

