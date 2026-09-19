import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QWidget, QGridLayout, QPushButton

class MainWindow (QMainWindow):
    def __init__ (self):
        super(). __init__ ()

        #confiigure the window name
        self.setWindowTitle ("PyCalc-OOP-GUI")

        #configure the container of the output label and buttons (numbers and operations) and put it in the MainWindow
        central_widget = QWidget ()                                    #create an instance of QWidget to hold the buttons and answer label
        self.setCentralWidget (central_widget)                         #put the central_widget in the MainApplication

        #create the main vertical layout to  hold the answer label
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        #Create the output label
        self.answer_label = QLabel("0")
        self.answer_label.setFixedSize (200, 60)

        #Add the output label to the vertical layout
        main_layout.addWidget(self.answer_label)

        #Create the calculator grid to hold buttons
        calculator_layout = QGridLayout()

        #Add the grid layout to the vertical layout
        main_layout.addLayout(calculator_layout)


        #set layout margins and spacing
        calculator_layout.setContentsMargins (0,0,0,0)          #define the  spacing between the buttons
        calculator_layout.setSpacing(0)
        
        #create buttons as instances of QPushButtons to represent the expected results
        button_1 = QPushButton ("7")
        button_2 = QPushButton ("8")
        button_3 = QPushButton ("9")
        button_4 = QPushButton ("DEL")
        button_5 = QPushButton ("AC")

        button_6 = QPushButton ("4")
        button_7 = QPushButton ("5")
        button_8 = QPushButton ("6")
        button_9 = QPushButton ("x")
        button_10 = QPushButton ("/")
        
        button_11 = QPushButton ("1")
        button_12 = QPushButton ("2")
        button_13 = QPushButton ("3")
        button_14 = QPushButton ("+")
        button_15 = QPushButton ("-")
        
        button_16 = QPushButton ("0")
        button_17 = QPushButton (".")
        button_18 = QPushButton ("frac")
        button_19 = QPushButton ("ans")
        button_20 = QPushButton ("=")

        #add buttons to specific rows and columns
        #the buttons created are addded to the calculator grid and the layout of each button is  determined by the row and column number - using  grid-like index positioning
        calculator_layout.addWidget(button_1, 0, 0)
        calculator_layout.addWidget(button_2, 0, 1)
        calculator_layout.addWidget(button_3, 0, 2)
        calculator_layout.addWidget(button_4, 0, 3)
        calculator_layout.addWidget(button_5, 0, 4)
        
        calculator_layout.addWidget(button_6, 1, 0)
        calculator_layout.addWidget(button_7, 1, 1)
        calculator_layout.addWidget(button_8, 1, 2)
        calculator_layout.addWidget(button_9, 1, 3)
        calculator_layout.addWidget(button_10, 1, 4)
        
        calculator_layout.addWidget(button_11, 2, 0)
        calculator_layout.addWidget(button_12, 2, 1)
        calculator_layout.addWidget(button_13, 2, 2)
        calculator_layout.addWidget(button_14, 2, 3)
        calculator_layout.addWidget(button_15, 2, 4)
        
        calculator_layout.addWidget(button_16, 3, 0)
        calculator_layout.addWidget(button_17, 3, 1)
        calculator_layout.addWidget(button_18, 3, 2)
        calculator_layout.addWidget(button_19, 3, 3)
        calculator_layout.addWidget(button_20, 3, 4)

        #create a string to store the calculation output
        self.expression = ""

        #group number buttons using a list and link their response when clicked to number_pressed method
        number_buttons = [ button_1, button_2, button_3, button_6, button_7, button_8, button_11, button_12, button_13, button_16]

        for button in number_buttons:
            button.clicked.connect(self.number_pressed)     #when a button is clicked envoke number_pressed method

        #group operator buttons to using a list and link their response when  clicked to an operator_pressed method
        operator_buttons = [
                button_9,   #x
                button_10,  #/
                button_14,  #+
                button_15   #-
              ]

        for button in operator_buttons:
            button.clicked.connect(self.numeric_operator_pressed)  #when an operaor button is clicked envoke operator_pressed

        #link other non_numeric operations and equal
        button_17.clicked.connect(self.decimal_pressed)
        button_4.clicked.connect(self.delete_pressed)
        button_5.clicked.connect(self.clear_pressed)
        button_20.clicked.connect(self.equals_pressed)
    
    #link the basic operations with button clicked
    def numeric_operator_pressed (self):
        button = self.sender()
        operation = button.text()
        
        self.expression += operation
        self.answer_label.setText(self.expression)
        
    #clear the output label
    def clear_pressed (self):
        self.expression = " "

    #create numbers button functions - event action when the button is clicked
    def number_pressed(self):
        button = self.sender()          #find which button was clicked using .sender method
        number = button.text()          #get the button's displayed text using .text() method

       #concatenate the clicked button text on self.expression
        if self.expression == "0":
            self.expression = number
        else:
            self.expression += number

        self.answer_label.setText(self.expression)      #update the output label by assigning it with the self.expression

        #create operators button functions - event action when the button is clicked
    def operator_pressed(self):
        button = self.sender()          #find which button was clicked using .sender method
        operator = button.text()        #get the button's displayed text using .text() method

        if self.expression:
            self.expression += f" {operator} "
            self.answer_label.setText(self.expression)

    #create the decimal button event action
    def decimal_pressed(self):
        self.expression += "."
        self.answer_label.setText(self.expression)

    #create a delete button event action
    def delete_pressed(self):
        self.expression = self.expression[:-1]
        self.answer_label.setText(self.expression if self.expression else "0")

    def equals_pressed(self):
        try:
            #replace calculator's multiplication symbol with Python's
            expression = self.expression.replace("x", "*")

            result = eval(expression)                       #calculate the expression

            self.expression = str(result)                   #store the result as a string object
            self.answer_label.setText(self.expression)      #display the result

        except Exception:
            self.expression = ""                            #clear the expression if there is an error
            self.answer_label.setText("Error")              #display an error message


def main ():
    app     = QApplication (sys.argv)
    window  = MainWindow ()

    window.show()
    sys.exit(app.exec())

main()