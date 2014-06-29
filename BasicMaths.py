# Class Construction

class BasicMaths():
    #Method 1
    def display(self, result):
        print "The Result is: " + str(result)

    #Method 2
    def calculate(self, option, x, y):
        #Addition
        if option == 1:
            return x + y
        #Multiplication
        elif option == 2:
            return x * y
        #Subtraction
        elif option == 3:
            return x - y
        #Division
        elif option == 4:
            return x / y
        #Modulo
        elif option == 5:
            return x % y
        #opther options
        else:
            return None


if __name__ == "__main__":
    #Construct an instance of the class
    print "\n1. Addition\n2. Multiplication\n3. Subtraction\n4. Division\n5. Modulo"
    print "Enter your choice:"
    opt = input()
    print "Enter X:"
    x = input()
    print "Enter Y:"
    y = input()
    inst = BasicMaths()
    res = inst.calculate(opt, x, y)
    if res is not None:
        inst.display(res)
    #alternate of the above 4 lines can be as follows:
    # inst = BasicMaths()
    # res = BasicMaths.calculate(inst, opt, x, y) #inst is assigned to self
    # if res is not None:
    #     BasicMaths.display(inst, res)
