import pandas

from term_app_helper_methods import *
class TerminalChemApp():

    welcome_message = '''
        This app allows you to perform thermodynamic calculations by 
        selecting chemicals from a data table.
    '''

    def __init__(self) -> None:
        self.products = []
        self.reactants = []
        self.data = load_data_frame()
        self.truncated_data = self.data[['name', 'formula', 'state']]

    def get_instructions(self) -> str:
        instructions = '''
        Enter a formula like this: NH3 
        To see the data, enter "d" and hit Enter. 
        To exit, enter "e" and hit Enter.
        '''
        return instructions

    def display_data(self):
        i = 0
        while i < len(self.truncated_data):
            for i in range(i, i +5):
                row = f"{self.truncated_data.loc[i, 'name']} {self.truncated_data.loc[i, 'formula']} {self.truncated_data.loc[i, 'state']}"
                print(row)
                i = i + 1
            key = input("Press c to continue. Or press enter to go back.\n")
            if key == '' or key == ' ':
                break

    def print_data_frame(self, df: pandas.DataFrame):
        print(df)
    def handle_user_input(self, entry: str):
        #remove leading whitespace
        entry = entry.strip()
        #search the dataframe
        result = self.data.loc[self.data['formula'] == entry]

        if result.empty :
            print("No data found")
        elif len(result) > 1:
            print(f"More than one result.")
            self.print_data_frame(result)
            list_of_indices = []
            for row in result.index:
                list_of_indices.append(row)
            choice_is_made = False
            while not choice_is_made:
                index = input("Which do you want? Enter the index: ")
                if not index.isdigit() or not (int(index) in list_of_indices):
                    print("That is not a valid entry.")
                else:
                    choice_is_made = True
                    print(f"You chose {index}")
        else:
            print("Found something!")
            self.print_data_frame(result)


    def run(self):
        print(self.welcome_message)
        print(self.get_instructions())

        while True:
            entry = input("Enter chemical formula: \n") #Don't forget backspace before entry.
            if entry == 'e':
                break
            elif entry == 'd':
                self.display_data()
            else:
                self.handle_user_input(entry)


    def clear_chemical_lists(self):
        self.products.clear()
        self.reactants.clear()