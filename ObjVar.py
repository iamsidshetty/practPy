__author__ = 'sid'

# Just an example of Object variable and class varaiable

class Obejct_And_Class_Variable:
    # class to count the population
    population = 0

    # Similar to constructor
    def __init__(self, name):
        self.name = name
        print "Initializing %s " % self.name
        Obejct_And_Class_Variable.population += 1

    def __del__(self):
        print "%s is dead" % self.name
        Obejct_And_Class_Variable.population -= 1

        if Obejct_And_Class_Variable.population == 0:
            print "Every one is dead!!"
        else:
            print "Population is %d" % Obejct_And_Class_Variable.population

    def Greeting(self):
        print "Hello ji, myself %s, How are you ji?" % self.name


    def popCount(self):
        if Obejct_And_Class_Variable.population == 0:
            print "Every one is dead!!"
        else:
            print "Population is %d" % Obejct_And_Class_Variable.population


if __name__ == "__main__":
    Sid = Obejct_And_Class_Variable('Sudarshan')
    Sid.Greeting()
    Sid.popCount()

    Raj = Obejct_And_Class_Variable('Raj')
    Raj.Greeting()
    Raj.popCount()

    Sid.Greeting()
    Sid.popCount()

    """
    Note, object that are no longer in use are destroyed using del,
    which is similar to destructor.
    """



