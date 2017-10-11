class Person():
    def __init__(self, nm):
        self.name = nm;
        print ("My name is:", self.name);

    def updateYourName(self, newname):
        self.name = newname;
        print ("My new name is:", self.name);


def main():
    personInstance = Person("Ning");
    personInstance.updateYourName("NewNing");


if __name__ == "__main__":
    main()