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
        yield InputArea(id="input")

    #Handle the user input
    def on_input_submitted(self, message: Input.Submitted) -> None:
        """A coroutine to handle a text changed message."""
        if message.value:
            log = self.query_one("#products")
            log.write(message.value)
class MainPanel(Static):
    def compose(self) -> ComposeResult:
        yield InstructionsWindow()
        yield DataWindow()
        yield OutputPanel()

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

class OutputPanel(Static):
    def compose(self) -> ComposeResult:
        yield TextLog(id="products")
        yield TextLog(id = "reactants")
        yield TextLog(id= "output")




class CalcHandler():
    def __init__(self, input_window: Input, product_window: TextLog, reactant_window: TextLog, message_window: TextLog):
        self.input_window = input_window
        self.product_window = product_window
        self.reactant_window = reactant_window
        self.message_window = message_window
        pass
















































class OutputWindow(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder()

class InputArea(Static):
    def compose(self) -> ComposeResult:
        yield Label("Reactants")
        yield Input(placeholder="(Example input: 3,2", id="reactant_input")
        yield Label("Products")
        yield Input(placeholder="Example 2,3", id="product_input")
