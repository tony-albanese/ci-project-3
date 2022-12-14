![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Introduction
Thermodynamic calculations are a part of every introductory high school chemistry class. Specifically, there are three 
quantities students are expected to calculate:
* Enthalpy Change (dH) - This is the change in the total heat content of a system as reactants are converted into 
products in a chemical reaction.
* Free Energy Change (dG) - Also called the Gibbs free energy change, this is a measure of the amount of useful work a 
either abosrbed or released from the system during a chemical reaction.
* Entropy (dS) - This is a measure of the change in entropy in a chemical reaction as products are formed from reactions. Entropy is 
quantity that measures how much useful energy is unavailable for useful work (per unit temperature). 

The process by which the student calculates these quantities involves the following general steps:
1. The student must have a balanced chemical equation
2. The student must then look up the thermodynamic value for each chemical in the equation in a table. 
3. For reactants (these are on the left side of the reaction arrow), the student multiplies the coeffiecient of the chemical 
in the equation by the value of the thermodynamic quantity found in the table. This is repeated for the all the
reactants and products.
4. The energies the reactants are added. The energies of the prodcuts are added.
5. The change is determined by subtracting reactants from the products.
   - sum of products - sum of reactants [//]:#(Add LaTex formula) 

This process is tedious and error-prone since students often misread data in the table, or make calculator mistakes as
they perform sums, and often confuse products with reactants.

My console app helps students perform these calculations. Students enter the reactants and products from
a data table (provided in the app) along with the coefficients from the balanced chemical equation and the values
of dH, dG, and dS are calculated and displayed neatly.

# User Stories
As a User I want to 
* Have the chemical data visible to me in the app.
* Scroll through the chemical data easily
* easiy enter chemical quantities and formulas
* easily distinguish between products and reactants
* clear my entries if I make a mistake
* have instructions readily available so I know what to do
* given hints as to how to properly enter data
* be notified when I make an improper entry. I should not have to restart from the beginning if I make a mistake
* Have the results of the calculation clearly displayed and neatly formatted

# UI Design
## Features

## Algorithms

# Testing
Although unit testing is ideal, this app used many libraries which themselves have been tested. The methods that were
developed to perform the chemical calculations are simple enough to be tested manually.
## Manual testing
| Test Description                         | Test                                                                                                                                                                                                                                | Result |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Instructions are visible                 | When the app is run<br> Then the instructions are clearly visible in the left panel.                                                                                                                                                | PASS   |
| Chemical data is readily available       | When the app is run <br> Then the chemical data table is loaded <br> The table is scrollable with mouse or keyboard <br> It is in the center panel                                                                                  | PASS   |
| Products appear in the product panel     | When the user provides correct input in the product input field <br> The product appears in the product window.                                                                                                                     | PASS   |
| Reactants appear in the product panel    | When the user provides correct input in the reactant input field <br> The reactant appears in the product window.                                                                                                                   | PASS   |
| The Clear button functions               | When the user clicks on the Clear button <br>The products, reactants, and output window are cleared.                                                                                                                                | PASS   |
| The Calculate button functions           | When the user enters valid data for products and reactants<br>and clicks on the Calculate button <br> The result of the calculation is displayed in the output window.                                                              | PASS   |
| Invalid input is handled gracefully      | When the user enters anything not in the form of number,number <br> in either the product or reactant input field <br> then the user is notified with a message in the output panel. <br> The input is cleared from the input field | PASS   |
| The input fields are cleared after entry | When the user enters input (valid or not) <br> and then presses enter  <br> The input is cleard from the input field.                                                                                                               | PASS   |

# Features left to implement

# Unresolved bugs

# Technology Used
+ [PyCharm IDE](https://www.jetbrains.com/pycharm/) An IDE designed specifically for Python developers. This is developed
by JetBrains.
+ [Google Sheets](https://www.google.com/sheets/about/) This online spreadsheet was used to organize the chemical data
into rows and columns that could easily be exported into CSV (comma separated value) text format which can be 
easily loaded in Python.

## Python Libraries
The Python community is quite large and as a result, there are numerous libraries (almost all freely available) that 
help make a developer's life much easier. The following libraries were used in this project.

+ [Rich](https://rich.readthedocs.io/en/stable/introduction.html) is a Python library for displaying rich text
in the console. The table for the chemical data was created with Rich.
+ [Textualize](https://www.textualize.io/) is a library to make beautiful console applications. The library features
many built in widgets such as loggers, buttons, form inputs, etc that are ready to use with built in event handlers. 
This library also has a layout and styling mechanism that is based on CSS that makes placing and styling the widgets
relatively easy.
+ [pandas](https://pandas.pydata.org/) This python library is used by data scientists to display, query, and manipualte 
large sets of data. The data in this project is accessed and queried as a pandas dataframe.

# Deployment
# Version Control Strategy
# Credits
The chemical data was taken from the [International Baccalaureate](https://www.ibo.org/)'s Chemistry Data Booklet. 