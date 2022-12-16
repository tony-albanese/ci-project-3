![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Introduction
Thermodynamic calculations are a part of every introductory high school chemistry class. Specifically, there are three 
quantities students are expected to calculate:
* Enthalpy Change $\Delta H$ or dH - This is the change in the total heat content of a system as reactants are converted into 
products in a chemical reaction.
* Free Energy Change $\Delta G$ or dG - Also called the Gibbs free energy change, this is a measure of the amount of useful work 
either absorbed or released from the system during a chemical reaction.
* Entropy $\Delta S$ or dS - This is a measure of the change in entropy in a chemical reaction as products are formed from reactions. Entropy is 
quantity that measures how much useful energy is unavailable for useful work (per unit temperature). 

The process by which the student calculates these quantities involves the following general steps:
1. The student must have a balanced chemical equation
2. The student must then look up the thermodynamic value for each chemical in the equation in a table. 
3. For reactants (these are on the left side of the reaction arrow), the student multiplies the coefficient of the chemical 
in the equation by the value of the thermodynamic quantity found in the table. This is repeated for the all the
reactants and products.
4. The energies the reactants are added. The energies of the products are added.
5. The change is determined by subtracting reactants from the products.
$$\Delta X = \Sigma E_{products} - \Sigma E_{reactants}$$
where $\Delta X$ is the change in energy quantity and $\Sigma E_{products}$ is the sum of the energies of the products
and $\Sigma E_{reactants}$ is the sum of the energies of the reactants.

This process is tedious and error-prone since students often misread data in the table, or make calculator mistakes as
they perform sums, and often confuse products with reactants.

My console app helps students perform these calculations. Students enter the reactants and products from
a data table (provided in the app) along with the coefficients from the balanced chemical equation and the values
of $\Delta H$, $\Delta G$, and $\Delta S$ are calculated and displayed neatly.

# User Stories
As a User I want to 
* Navigate the sections of the app with keyboard or mouse.
* Have the chemical data visible to me in the app.
* Scroll through the chemical data easily
* easily enter chemical quantities and formulas
* easily distinguish between products and reactants
* be aware of which chemicals I have selected
* clear my entries if I make a mistake
* have instructions readily available so I know what to do
* be given hints as to how to properly enter data
* be notified when I make an improper entry. I should not have to restart from the beginning if I make a mistake
* Have the results of the calculation clearly displayed and neatly formatted

# UI Design
There are two versions of the app for this project - both run in the terminal and both have exactly the same funtionality.
One version uses plain text output and is deployed on Heroku. The second version is also 100% terminal app but uses the 
textual and rich python libraries to display and style terminal widgets to give the user a better experience. 
The reason for the two versions has to do with deployment on Heroku. For the web deployment, Code Institute deploys a
mock terminal with a fixed size. The widgets are not displayed properly in the mock terminal. 

Therefore, there is the web version which can be found here: [Thermodynamic Calculator on Heroku](https://thermodynamic-calculator.herokuapp.com/) 
The binary versions using textual are available for download available here. 

## Features Heroku Versuion App
### Instructions
The instructions for the app are displayed when the app runs. The user can bring up the instructions at any point
by pressing i.  There is also a hint as to how to enter 
a formula.
![Heroku App Instructions](assets/screenshots/heroku_menu.png)
> have instructions readily available so I know what to do  
> be given hints as to how to properly enter data

The instructions also serve as a menu. The user is told what to enter in order to navigate through the app. This
is done entirely through the keyboard.
> Navigate the sections of the app with keyboard or mouse.
> be given hints as to how to properly enter data

### Data Scrolling
The user must have a way to see the data available so they know which chemicals they can perform calculation with. 
From the command prompt, the user can browse the chemical data at any time by pressing d.
Scrolling a long list of text is annoying. Therefore, the heroku version is designed to display five rows of data
at a time. They can exit the browsing feature by pressing enter.
![scrolling data](assets/screenshots/heroku_scroll.png)
> Scroll through the chemical data easily 
> Have the chemical data visible to me in the app.
### Data Entry
The user must enter the formula as it is displayed in the datatable to enter it for calculation. The reason to 
go by formula rather than name is mostly preference. The user will most likely be a student, and problems of this
type typically provide formulas rather than chemical names. In addition, formulas are universal - names are not.
Therefore, the user must enter the formula. There input is validated and if no chemical is found in the dataframe,
the user is notified. There is a message letting the user know if a chemical has been found and a prompt to 
enter the coeffient from the equation or 0 if they entered this formula in error.
![heroku data entry](assets/screenshots/heroku_entry.png)
> easily enter chemical quantities and formulas
> be given hints as to how to properly enter data
> clear my entries if I make a mistake
> be notified when I make an improper entry. I should not have to restart from the beginning if I make a mistak

Once the user enters a coefficient, they are given a prompt to enter it as either a product or a reactant.
![heroku enter chemical](assets/screenshots/heroku_enter_chemical.png)
> be given hints as to how to properly enter data  
> easily enter chemical quantities and formulas  
> easily distinguish between products and reactants  
### Product / Reactant List
From the command prompt, the user can see a list of products or reactants they have entered so far
by pressing the p or s keys respectively. 
![heroku lists](assets/screenshots/heroku_lists.png)
> easily distinguish between products and reactants 
### Clear / Reset
When the user has finished with a calculation (or if they are not satisfied with their entries), they can
clear their entries by typing "clear" from the Command: prompt.
![heroku list cleared](assets/screenshots/heroku_cleared.png)
> clear my entries if I make a mistake
### Chem Report
Once the user has entered the products and reactants, they can initialize the calculations by pressing
c from the Command: prompt. 
![heroku report](assets/screenshots/heroku_report.png)
If one of the lists is empty, the user is reminded that calculations cannot be performed if either the reactants
or products list is empty. 
![empty list warning](assets/screenshots/heroku_empty_data.png)
> be notified when I make an improper entry. I should not have to restart from the beginning if I make a mistake  
> Have the results of the calculation clearly displayed and neatly formatted 


## Features - Textual App
### Scrollable Data Table
A table displaying a list of all the chemicals available is shown at the center of the screen. The energy values
are not displayed to keep the screen compact and to enhance readability. After all, the purpose of the app is to
avoid having to work with the values directly. The user can scroll with a mouse or the arrow keys.
![chemical data table](assets/screenshots/data_table.png)
> Have the chemical data visible to me in the app.  
> Scroll through the chemical data easily  
> Navigate the sections of the app with keyboard or mouse.

### Instruction Section
There is a pane with a short description of how to use the app. It is easily visible and the content scrolls
if the screen is too small.
![instructions](assets/screenshots/instructions.png)
> have instructions readily available, so I know what to do  
> Navigate the sections of the app with keyboard or mouse.  

### Input Widgets
The user can enter input to select reactants and products by entering data into these two form input widgets. When the user hits 
Enter or clicks on the button with the mouse, the data is queried and the reactants and products are displayed in the 
respective output window. There is a hint to the user as to how to enter input correctly. The reactants and products are labelled
and color coded with different borders.
![input widgets](assets/screenshots/input_widgets.png)
> easily distinguish between products and reactants  
> be given hints as to how to properly enter data
> Navigate the sections of the app with keyboard or mouse.
### Output Panel
The output panel features three boxes. Two are labelled for reactants and products. The third is for output.
The borders of the reactant/product boxes match those of the input fields. If the user enters incorrect
input, they are notified in the third box. These windows will automatically have scrollbars if content goes 
offscreen. However, most chemical equations (especially those at an introductory level) rarely have more than two or
three products and reactants. Thus, for the vast majority of use cases, the content a user would enter will fit
on the screen.
![output panel](assets/screenshots/output_panel.png)
> easily distinguish between products and reactants  
> be aware of which chemicals I have selected  
> be notified when I make an improper entry. I should not have to restart from the beginning if I make a mistake

### Calculation Report
When the user clicks on or presses enter on the Calculate button, the chemicals selected as products
and reactants are used to perform a series of calculations using data in the dataframe. The results
are formatted and outputted to the output panel. In addition to the output values, the user is given 
a list of the reactants and products used. This is to help them ensure that the calculations are based on
the values they entered.
![calculation output](assets/screenshots/sample_calculation_output.png)
> Have the results of the calculation clearly displayed and neatly formatted  
> be aware of which chemicals I have selected  
> Navigate the sections of the app with keyboard or mouse.

### Action Buttons
There are two buttons. One labelled Calculate and the other Clear. When the user clicks on or presses enter
on the Calculate button, the calculations are executed and the results displayed. When the user presses or 
clicks on the Clear button, the input is cleared as is the text boxes for reactants and products.
![buttons](assets/screenshots/buttons.png)
> clear my entries if I make a mistake  
> Navigate the sections of the app with keyboard or mouse.


## Algorithm Design
This sections outlines the more important algorithms in the app using pseudocode. Trivial algorithms or those
achieved mainly through libraries are not mentioned.

### Main Program Flow
The program's execution is essentially an infinite while loop that polls the user for input. This is the outline
of the run loop in pseudocode.
```
load app
dislay welcome message
display instructions

while True:
  get user input
  if q
    break 
  if c
    perform calculations
  if i
    print instructions
  if 'clear'
    clear data
  if p
    print products
  if r
    print reactants
  if d
    display data
  else
    send input for further handling
```
### Scrolling Data Table (Heroku App)
Both versions of the app display the same data. The textual version has a table widget
to display the data. That is not possible on the emulated console. Therefore, the user must be displayed data
in small pages of five rows to prevent having to scroll (since the scroll behavior of the emulated terminal is
unknown). Also, the emulated terminal is very small and cannot be changed. The user should not be overwhelmed with
too much data on the screen at once. Here is the general algorithm for displaying the table in pages.
```
get reference to dataframe
  i = 0
  while i < dataframe.length
      loop i to i + 5 
        print the ith row of the dataframe
        i++
      get input
      if blank 
        break  
      otherwise continue the loop
```   
### Searching Data Table (Heroku App)
The method to search the dataframe for chemical formulas accepts the users search term as input
and uses it to search the dataframe column with the formula data. The results of this search are handled.
If nothing was found or if more than one entry is found, the user is notified as to what to do. (It
might be possible for a chemical to be in the table twice if it is in different states e.g. Br2 gas and Br2
liquid.)
```
strip search term of whitespace
query the 'formula' column of the dataframe
store indices of retrieved rows in a list
  if the list is empty
    tell user nothing was found
  if the list has more than one entry
    loop while user has not made proper choice
      user inputs index choice
      if index not in list of indices
        prompt again
      else
        store value
        break
  
  else 
    notify user match found
    store value
```
The logic to store the found chemical is simple
```
prompt user for coeffient
prompr user if product or reactant
  if product
    store in product list
  if reactant
    store in reactants list
```
### Validation of User Input (Heroku App)
Since the user is constantly typing in the heroku version of the app, their input must be continuously 
evaluated and handled if not valid.
Here are some of the key ways user input is validated.

+ When adding a chemical to the list. Method checks if coefficient is a number. If 0 or blank, the value is not
stored in the list. If invalid, the user is prompted again. If valid, the user is asked to store as a product
or reactant.
```
prompt user for coefficient
strip input of whitespace
input_processed_flag = False
  #Loop until user has entered valid input
  while not input_processed_flag
    if input is 0
      break 
    if input is not a number
      prompt again
    if input is blank
      break
      
    else
      while value not entered
        prompt p or r
        if p
          store in product list
          mark value as stored
        if r
          store in reactants list
          mark value as stored        
```
The algorithm to produce the list of selected reactants and products is similar in both versions of the app.
```
   #Loop over the reactants list
   for each reactant in reactants list
      retrieve formula from dataframe using index in reactant_formula_list
      store that formula in a list
      print list
      
   #Loop over the products list
      rerieve fromula from dataframe using index in product
      store that formula in a product_formula_list
      print list
  
```
### Creation of Data Table (Textual App)
This is the algorithm design for the creation of the datatable. It involves loading a dataframe (which is done using
the pandas library), creating a Table object from the Rich library, looping over the rows in the dataframe to add
the data from the rows to the Table. That table object is then written to the correct TextLog in the UI.
```
GET reference to dataframe
INITIALIZE Table object
   INITALIZE Column for Index, Name, Formula, State
LOOP over each row in the dataframe
   FOR each row in the dataframe
      retrieve index
      retrieve name
      retrieve formula
      retrieve state
      add these values to row in Table object
GET reference to TextLog widget
on widget mount to window:
   print table object to log
```
### Handling and Validation of User Input (Textual App)
This logic is handled by the _on_input_submitted() method which is part of the Textual library. This method
is called whenever the user hits the enter key on an Input object. The method is passed an Input.Submitted object
which contains data about the object and data submitted.
```
#Determine which input object was submitted
   GET message.id value
      IF input.id is reactant_input
         check if input is valid
         if valid
            retrieve data from dataframe
            add it to the list of reactants
            print the value to the reactant output window
         if not valid
            print error message to output log
      IF input.id is product_input
         check if input is valid
         if valid
            retrieve data from dataframe
            add it to the list of products
            print the value to the product output window
         if not valid
            print error message to output log
```
This is the logic employed to determine whether the input is valid. Two things need to be checked, the first
is whether the input is in the form of integer,integer. The second is whether the first integer, which 
is the index of the chemical is within range. In other words, if the user enters -5 for an index or 65 (which does not
exist), the input should be flagged as invalid. The method accepts the user_input as a parameter.
```
#Method to determine if user input matches pattenrn integer,integer using regex

initialize regex pattern [0-9]+,[1-9]+ #any number of digits,any number of digits
compare user input to regex expression
   if match
      return TRUE
   else 
      return FALSE
```
This is the logic to determine if the input index is within range. It will only be called if the input pattern
matches the requirment of being in the form integer,integer.
```
#split the user input into an array of two
split_string_aray = user_input.split(",")
index = split_string_array[0] #The first value is supposed to be the index
   if index < 0 OR index > dataframe size
      return FALSE
   else
      return TRUE
```
### Querying Data
The logic for retrieving data from a dataframe object is simple. One simply calls the _get_value() method on
the dataframe object and pass in the index of the row and name of the column as a string. 
### Event Handling (Textual App)
The Textual libraries built in widgets have a set of event handlers to respond to user events such as clicks, input
submission, and text changes. This is the logic that is executed by the library's on_button_pressed() method which
is called any time a user clicks on a button object with the mouse or presses the Enter key while a button object
has focus. The method is passed a Button.Pressed object which encapsulates information about the button that was clicked.
```
#Get the id value from the clicked button
if button.id == 'submit button'
   execute chemical calculations
if button.id == 'clear button'
   reset the value of products list
   reset the value of reactants list
   clear the reacts window
   clear the prodcuts window

```
### Calculation of Quantities (Both Textual and Heroku Versions)
This is the key algorithm in the app as it is responsible for producing the output that the user needs. The
general steps in the calculation of quantities and the production of hte output are as follows:
1. calculate the dH, dG, and dS
2. retrieve the formulas for the products
3. retrieve the formulas for the reactants
4. output the values

This is the algorithm for calculating dH, dG, and dS. The logic is the same for each. The method accepts a dataframe,
a list of products, and a list of reactants as input. The only thing that changes is the name of column from which
we want to retrieve data.
```
#We want to retrieve values from the dH column.
column = 'dH' 
sum_products = 0
sum_reactants = 0
   #loop over the reactants
   for each reactant in reactants:
      retrieve its energy value from dataframe column
      add that value to the sum_reactants
   
   #loop over products
   for each product in products
      retrieve its energy value from the dataframe column
      add that value to sum_products
   
   return sum_products - sum_reactants
```

This is the logic for producing the output:
```
calculate dH
calculate dG
calculate dS

product_formula_list
reactant_formula_list

#Retrieve the formulas for the reactants
   #Loop over the reactants list
   for each reactant in reactants list
      retrieve formula from dataframe using index in reactant_formula_list
      store that formula in a list
   #Loop over the products list
      rerieve fromula from dataframe using index in product
      store that formula in a product_formula_list

   write reactant_formula_list to output window
   write product_formula_list to output window
   
   write dH as formatted string with units to output window
   write dG as formatted string with units to output window
   write dS as formatted string with units to output window
```

# Testing
Although unit testing is ideal, this app used many libraries which themselves have been tested. The methods that were
developed to perform the chemical calculations are simple enough to be tested manually.
## Manual Testing Heroku App
| Test Description              | Test                                                                                                                        | Result |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------|--------|
| instructions are visible      | When the app is loaded <br> the instructions are visible                                                                    | PASSS  |
| instructions are visible      | When the user enters i on the command prompt <br> the instructions are printed                                              | PASS   |
| quit function                 | When the user presses q on the command prompt <br> the app quits                                                            | PASS   |
| display data                  | When the user presses d on the command primpt <br> the data table is displayed <br> five rows are displayed                 | PASS   |
| next set of data displayed    | When the user presses  <br> the next five rows of data are displayed. <br> if they hit enter, they return to command prompt | PASS   |
| user can see selections       | When user presses p on command prompt <bre> list of products is shown.                                                      | PASS   |
| user can see selections       | When user presses r on command prompt <br> list of reactants is shown.                                                      | PASS   |
| user can clear selections     | When user enters clear on command prompt <br> and then prints products or reactants <br> empty list is displayed            | PASS   |
| user gets calculation report  | When user enters c on command prompt <b> caluculation report is displayed with formatting <br> and selected chemicals       | PASS   |
| no calculations on empty list | If reactant or product list is empty <br> no calculations are performed <br> user is notified                               | PASS   |
| invalid input is handled      | When the user enters invalid coefficient <br> the user is notified and asked again                                          | PASS   |
| invalid input is handled      | When the user enters non existent formula <br> the user is notified and returned to command prompt                          | PASS   |
| invalid input is handled      | When the user enters invalid index when more than one match is found <br> the user is notified and asked again              | PASS   |
| invalid input is handled      | When the user enters invalid choice for product or reactant <br> the user is notified and asked again                        | PASS   |

## Manual Testing Textual App
| Test Description                               | Test                                                                                                                                                                                                                                | Result |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Instructions are visible                       | When the app is run<br> Then the instructions are clearly visible in the left panel.                                                                                                                                                | PASS   |
| Chemical data is readily available             | When the app is run <br> Then the chemical data table is loaded <br> The table is scrollable with mouse or keyboard <br> It is in the center panel                                                                                  | PASS   |
| Products appear in the product panel           | When the user provides correct input in the product input field <br> The product appears in the product window.                                                                                                                     | PASS   |
| Reactants appear in the product panel          | When the user provides correct input in the reactant input field <br> The reactant appears in the product window.                                                                                                                   | PASS   |
| The Clear button functions                     | When the user clicks on the Clear button <br>The products, reactants, and output window are cleared.                                                                                                                                | PASS   |
| The Calculate button functions                 | When the user enters valid data for products and reactants<br>and clicks on the Calculate button <br> The result of the calculation is displayed in the output window.                                                              | PASS   |
| Invalid input is handled gracefully            | When the user enters anything not in the form of number,number <br> in either the product or reactant input field <br> then the user is notified with a message in the output panel. <br> The input is cleared from the input field | PASS   |
| Invalid index values are gracefully handled    | When the user enters a negative number for the index <br> then an error message is displayed in the output <br> and the input is cleared                                                                                            | PASS   |
| The input fields are cleared after entry       | When the user enters input (valid or not) <br> and then presses enter  <br> The input is cleared from the input field.                                                                                                              | PASS   |
| The results are displayed in the output window | When the user enters valid input <br> and presses the calculate button  <br> The results of the calculation are showed in the output window.                                                                                        | PASS   |
| The results are neatly formatted               | When the results are displayed in the output panel <br> The selected products are printed on one new line. <br> The selected reactants are printed on one new line.                                                                 | PASS   |
| The results are neatly formatted               | When the results are displayed in the output panel <br> The result of the calculation for dH, dG, and dS are shown.<br>Each is on a separate line.                                                                                  | PASS   |
| The results are neatly formatted               | When the results are displayed in the output panel <br> The units for each quantity of dH, dG, and dS are shown.                                                                                                                    | PASS   |
| The calculations are accurate                  | When the user enters valid input <br> and presses the Calculate button <br> the output value for dH, dG, and dS are correct                                                                                                         | PASS   |
# Features left to implement
The following features would be a good additions to the app:
+ Validation of chemical input. As of now, the app calculates the quantities based on what the user enters. However, if 
the user enters a set of products and reactants that do not constitute a valid chemical reaction, the program will perform these calculations
regardless even though the values will not have physical meaning. This is similar to the student incorrectly entering digits and operations on
a calculator - the machine simply performs the calculations based on the input. The user must evaluate the reasonableness of the output themselves.
+ Entering data directly from the table. It would be nice if the user could simply highlight the chemical in the table and either
by hitting enter or some other key add it to the list of products or reactants. The Table object in the Rich library does have
responsive elements. However, the requirement of quantities in addition to the chemical requires a non-trivial handling of user keyboard input.

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
many built in widgets such as loggers, buttons, form inputs, etc. that are ready to use with built-in event handlers. 
This library also has a layout and styling mechanism that is based on CSS that makes placing and styling the widgets
relatively easy.
+ [pandas](https://pandas.pydata.org/) This python library is used by data scientists to display, query, and manipulate 
large sets of data. The data in this project is accessed and queried as a pandas dataframe.

# Deployment
+ Create a repository dedicated for deployment using the [python project template](https://github.com/Code-Institute-Org/python-essentials-template) provided by 
CodeInstitute.
+ Create workspace in GitPod from new repository. 
+ Update requirements.txt
```
pip3 freeze > requirements.txt
```

## Project Creation
* The project was started by navigating to the [template](https://github.com/Code-Institute-Org/gitpod-full-template) and clicking 'Use this template'. Under Repository name I input ci-project-3. I then navigated to the new [repository for project 3](https://github.com/tony-albanese/ci-project-3). 
* I then cloned the repository into PyCharm by doing the following:
  * Open PyCharm
  * Click on the "Get from VCS" button
  * Copied the [clone url](https://github.com/tony-albanese/ci-project-3.git) for the repository
  * Selected an empty project folder
  * Clicked on the Clone button at the bottom of the dialog
## Heroku
# Version Control Strategy
Git was employed in this project and the project code hosted on [GitHub](https://github.com/). I used branches in order to keep the main branch as "pure" as possible. The strategy was to have each branch dedicated to one feature or fix.  Once I was satisfied at a particular stage of a branch, I would navigate to GitHub, click on my repository, select the branch, and create a pull request. GitHub would then check if there are no conflicts and indicate if the branch could be merged into main. (One can choose which branch to merge into.) Once the pull request is created, I navigated down, wrote a comment, and clicked on the green Merge button and the commits would be merged into the main branch.
I tried to keep commits as atomic as possible - focusing only on one element or feature at a time. This was not always the case, but most of the commits are relatively small changes.
## VCS in PyCharm
To make a commit, I clicked the Git menu item in PyCharm, followed by Commit. In the side panel, I selected the files I wished to commit.
I then typed a commit message and pressed the Commit button in the lower left corner of the panel.
To push to GitHub, I clicked on the Git menu item in PyCharm and then selected Push

# Credits
The chemical data was taken from the [International Baccalaureate](https://www.ibo.org/)'s Chemistry Data Booklet. 