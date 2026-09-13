import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QWidget, QGridLayout, QPushButton

class MainWindow (QMainWindow):
    def __init__ (self):
        super(). __init__ ()

        #configure the container of the output label and buttons (numbers and operations) and put it in the MainWindow
        central_widget = QWidget ()                                    #create an instance of QWidget to hold the buttons and answer label
        self.setCentralWidget (central_widget)                         #put the central_widget in the MainApplication

        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #create the main vertical layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        #Create the output label
        answer_label = QLabel("0")
        answer_label.setFixedSize (5, 60)

        #Add the label to the vertical layout
        main_layout.addWidget(answer_label)

        #Create the calculator grid
        calculator_layout = QGridLayout()

        #Add the grid layout to the vertical layout
        main_layout.addLayout(calculator_layout)


        #set layout margins and spacing
        calculator_layout.setContentsMargins (0,0,0,0)
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

        #Add buttons to specific rows and columns
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



def main ():
    app     = QApplication (sys.argv)
    window  = MainWindow ()

    window.show()
    sys.exit(app.exec())

main()