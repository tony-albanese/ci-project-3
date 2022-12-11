from chemlib import Compound, Reaction

def enter_formulas():
    compounds = []
    while True:
        formula = input("Enter a formula: ")
        if(formula=='done'):
            break
        try:
            compound = Compound(formula)
            compounds.append(compound)
        except:
            print("I don't think you entered a valid formula.")
    return compounds

def balance_reaction(reactants: list, products: list):
    reaction: Reaction = Reaction(reactants, products)
    try:
        reaction.balance()
        return ChemResult(True, reaction)
    except:
        return ChemResult(False, reaction)


class ChemResult:
    def __init__(self, status: bool, reaction: Reaction):
        self.status = status
        self.reaction = reaction

