import sys
class Calculator:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        
    def sum(self, n1, n2):
        """finds the sum of two given int()"""
        addition = n1 + n2
        print(f"ans:=> {addition}")
        return addition
        
    def subtract(self, n1, n2):
        """finds the difference of two given int()"""
        subtraction = n1 - n2
        print(f"ans:=> {subtraction}")
        return subtraction
        
    def product(self, n1, n2):
        """finds the product of two given int()"""
        multiplication = n1 * n2
        print(f"ans:=> {multiplication}")
        return multiplication
        
    def ratio(self, n1, n2):
        """finds the ratio of two given int()"""
        #division = n1 // n2
        division = round(n1 / n2, 4)
        print(f"ans:=> {division}")
        return division
        
    def evaluate(self):
       """provides an interface for user to evaluate an expression"""
       evaluation = eval(input('Enter expression: '))
       print(f"ans:=> {evaluation}")
       return evaluation
       
    def degree(self, n1, n2):
       """finds the exponent of a number"""
       exponent = n1**n2
       print(f"ans:=> {exponent}")
       return exponent
       
    def root(self, n1):
       """finds the square root of a number
       and returns a float()"""
       square_root = n1**0.5
       print(f"ans:=> {square_root}")
       return square_root
       
#object for the calculator class       
operation = Calculator()

#list of operational symbols
operation_symbols = ['+', '-', '*', '/', 'eval', 'n²', '√']
               
start_again = False
while not start_again: #loop for the start of the calculator
    history_answers = 0
    print("""tip: if you want to use evaluation,
     input first and second number as 0""")
    
    operand1 = float(input('First Number: '))
    print()
    operation_symbol = input("Enter operatiom symbol\n| +, -, *, /, eval, n², √ |: ")
    if operation_symbol not in operation_symbols:
        sys.exit(' No such operation symbol')
    print()
    operand2 = float(input('Second Number: '))
    
    match operation_symbol:
        #compares the user input with the operation symbols
        #and adds them to the history_answers
        case '+':
            history_answers += operation.sum(operand1, operand2)
        case '-':
            history_answers += operation.subtract(operand1, operand2)
        case '*':
            history_answers += operation.product(operand1, operand2)
        case '/':
            history_answers += operation.ratio(operand1, operand2)
        case 'eval':
            history_answers += operation.evaluate()
        case 'n²':
            history_answers += operation.degree(operand1, operand2)
        case '√':
            history_answers += operation.square_root(operand1, operand2)
    print('_____________________________________________')
    #prompt the user to enter a mode   
    calc_again = input('CALCULATOR\nEnter;\n\nC: to cancel\nANS: to continue\nAC: to start again\n                      : ').upper()
    
    if calc_again == "C":
        start_again = True #starts the loop if condition True
        print('THANKS FOR USING CALCULATOR')
    elif calc_again == 'AC':
        history_answers = 0
        pass #restarts the loop
        print()
    elif calc_again == 'ANS':
        #continues the loop for more calculations on stored answers
        print(f"continuing...")
        go_again = True
        while go_again: #begins a loop for more calculations 
            print()
            print(f'Existing no: {history_answers}')#prints out stored number
            operation_symbol2 = input("Enter operatiom symbol\n| +, -, *, /, eval, n², √ |: ")
            if operation_symbol2 not in operation_symbols:
                sys.exit('No such operation')
               
            print()
            operand3 = float(input('Enter value: ')) #input for third value
            #operation_symbol2 is the operation symbol input for further calculations 
            if operation_symbol2 == '+':
                history_answers += operand3
                print(f'ans:=> {history_answers}')
            elif operation_symbol2 == '-':
                history_answers -= operand3
                print(f'ans:=> {history_answers}') 
            elif operation_symbol2 == '*':
                history_answers *= operand3
                print(f'ans:=> {history_answers}')
            elif operation_symbol2 == '/':
                history_answers /= operand3
                print(f'ans:=> {history_answers}')
            elif operation_symbol2 == 'eval':
                history_answers += operation.evaluation(history_answers, operand3)
            elif operation_symbol2 == 'n²':
                history_answers **= operand3
                print(f'ans:=> {history_answers}')
            elif operation_symbol2 == '√':
                history_answers **= 0.5
                print(f'ans:=> {history_answers}')
            print('_____________________________________________')
            
            go_again_que= input('Continue: ').lower() # asks if the user wants to calculate again
            if go_again_que == 'yes':
               pass
            elif go_again_que == 'no': # if no, print the other mode options
               go_again = False
               
               calc_again = input('CALCULATOR\nEnter;\n\nC: to cancel\nAC: to start again\n                      : ').upper()
    
               if calc_again == "C":
                   start_again = True
                   print('THANKS FOR USING CALCULATOR')
               elif calc_again == 'AC':
                   pass
                   print()
            print('_____________________________________________')                
