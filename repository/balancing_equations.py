from chemlib import Compound

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

def balance_equation():
    pass

