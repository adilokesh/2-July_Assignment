#!/usr/bin/env python
# coding: utf-8

# # Q1. Explain what inheritance is in object-oriented programming and why it is used.

# Inheritance is a feature of object-oriented programming that allows you to create new classes that reuse, extend, and modify the behavior and properties of existing classes. The existing class is called the base class or superclass, and the new class is called the derived class or subclass. Inheritance forms a hierarchy of classes and enables an object created from a derived class to acquire all the attributes and methods of the base class, except for some specific cases.
# 
# Inheritance is used for several purposes, such as:
# 
# * To achieve code reuse and avoid duplication. By inheriting from a base class, you can use its existing code and add new features or override existing ones without rewriting the whole code.
# * To implement polymorphism and abstraction. By inheriting from a base class, you can define different behaviors for different subclasses that share a common interface. This allows you to treat objects of different subclasses as if they were objects of the base class, and to use abstract classes or interfaces to specify the general behavior of a group of classes without providing a concrete implementation.
# * To model real-world relationships and concepts. By inheriting from a base class, you can represent the is-a relationship between classes and objects. For example, you can create a class called Animal that has attributes and methods common to all animals, and then create subclasses like Dog, Cat, Bird, etc. that inherit from Animal and have their own specific attributes and methods.

# # Q2. Discuss the concept of single inheritance and multiple inheritance, highlighting theirdifferences and advantages.

# Single inheritance and multiple inheritance are two types of inheritance in object-oriented programming. Inheritance is a feature that allows a class to acquire the properties and methods of another class, called the base class or superclass. The class that inherits from the base class is called the derived class or subclass. Inheritance helps to achieve code reuse, polymorphism, and abstraction.
# 
# Single inheritance is when a derived class inherits from only one base class. For example, in Python, you can create a class called Animal that has attributes and methods common to all animals, and then create subclasses like Dog, Cat, Bird, etc. that inherit from Animal and have their own specific attributes and methods. Single inheritance is simple and easy to implement, but it may not capture the complex relationships between classes in some cases.
# 
# Multiple inheritance is when a derived class inherits from more than one base class. For example, in C++, you can create a class called Button that inherits from both classes Rectangle (for appearance) and Clickable (for functionality/input handling), and classes Rectangle and Clickable both inherit from the Object class. Multiple inheritance allows you to combine features from different hierarchies, but it may also introduce ambiguity and complexity in situations such as the "diamond problem", where it may be unclear which version of a method or attribute the derived class inherits if more than one base class implements it.
# 
# The advantages and disadvantages of single and multiple inheritance depend on the programming language, the design of the classes, and the problem domain. Some general points are:
# 
# - Single inheritance is more straightforward and less prone to errors than multiple inheritance. It follows the principle of "is-a" relationship between classes, which is easy to understand and maintain.
# - Multiple inheritance is more expressive and flexible than single inheritance. It allows you to model multiple aspects or roles of a class without creating intermediate classes or duplicating code. It follows the principle of "has-a" or "mix-in" relationship between classes, which can be more natural and realistic in some scenarios.
# - Single inheritance may not be sufficient to represent some complex scenarios where a class needs to inherit features from more than one unrelated or partially related classes. For example, a FlyingFish may need to inherit from both Fish and Bird classes, which are not directly related.
# - Multiple inheritance may cause conflicts or confusion when there are overlapping or inconsistent features among the base classes. For example, if both Rectangle and Clickable classes have a method called draw(), which one should the Button class inherit? This can be resolved by using explicit resolution rules, such as the C3 linearization algorithm in Python², or by using virtual inheritance in C++³.
# 
# 

# # Q3. Explain the terms "base class" and "derived class" in the context of inheritance.

# Base class and derived class are two terms that are used in the context of inheritance, which is a feature of object-oriented programming that allows a class to acquire the properties and methods of another class. A class is a blueprint or template for creating objects, which are data structures that have their own attributes and behaviors.
# 
# A base class, also known as a superclass or a parent class, is a class that provides the common characteristics and behaviors for other classes that inherit from it. A base class can be abstract, which means it cannot be instantiated as an object, but only serves as a general specification for its subclasses. A base class can also be concrete, which means it can be instantiated as an object, and can have its own instances as well as subclasses.
# 
# A derived class, also known as a subclass or a child class, is a class that inherits from one or more base classes and can add, modify, or override the features of the base classes. A derived class can access and use the attributes and methods of the base classes, except for some specific cases such as private or protected members. A derived class can also define its own attributes and methods that are specific to its own functionality.
# 
# The purpose of using base classes and derived classes in inheritance is to achieve code reuse, polymorphism, and abstraction. Code reuse means that you can avoid duplication and use the existing code from the base classes in the derived classes. Polymorphism means that you can treat objects of different derived classes as if they were objects of the base classes, and use the same interface for different behaviors. Abstraction means that you can hide the implementation details of the base classes and only expose the relevant features to the derived classes.
# 
# 

# # Q4. What is the significance of the "protected" access modifier in inheritance? How does it differ from "private" and "public" modifiers?

# The “protected” access modifier in inheritance is a way of controlling the visibility and accessibility of the members (attributes and methods) of a class from its subclasses and other classes. The “protected” modifier allows the members of a class to be accessed by its subclasses, either in the same package or in a different package, but not by any other classes outside the inheritance hierarchy. This means that the subclasses can inherit and use the protected members of their base class, but they cannot expose them to the outside world.
# 
# The “protected” modifier differs from the “private” and “public” modifiers in the following ways:
# 
# The “private” modifier is the most restrictive one, as it only allows the members of a class to be accessed within the same class. The subclasses cannot inherit or access the private members of their base class, nor can any other classes outside the class. The “private” modifier is used to hide the implementation details of a class and to prevent unauthorized access or modification12.
# The “public” modifier is the least restrictive one, as it allows the members of a class to be accessed by any other classes, either in the same package or in a different package. The subclasses can inherit and access the public members of their base class, and they can also expose them to the outside world. The “public” modifier is used to define the interface or contract of a class and to provide access to its essential features.

# # Q5. What is the purpose of the "super" keyword in inheritance? Provide an example.

# The purpose of the “super” keyword in inheritance is to refer to the parent class of a subclass and access its members, such as attributes, methods, and constructors. The “super” keyword can be used to:
# 
# Call a parent class constructor from a subclass constructor using the syntax super(arguments). This is useful when you want to initialize the parent class attributes and invoke its logic before defining the subclass-specific behavior. For example, in Java, you can create a subclass called Dog that inherits from a parent class called Animal and call its constructor using the “super” keyword

# In[3]:


# Define a parent class called Animal
class Animal:
    # Define an attribute called name
    def __init__(self, name):
        # Assign the name argument to the name attribute
        self.name = name

# Define a subclass called Dog that inherits from Animal
class Dog(Animal):
    # Define an attribute called breed
    def __init__(self, name, breed):
        # Call the parent class constructor with the name argument using the super keyword
        super().__init__(name)
        # Assign the breed argument to the breed attribute
        self.breed = breed

    # Define a method that prints the dog's information
    def show_info(self):
        # Access the parent class attribute using the super keyword
        print(f"This dog's name is {super().name} and its breed is {self.breed}.")


# # Q6. Create a base class called "Vehicle" with attributes like "make", "model", and "year". Then, create a derived class called "Car" that inherits from "Vehicle" and adds an attribute called "fuel_type". Implement appropriate methods in both classes.

# In[5]:


# Define a base class called Vehicle
class Vehicle:
    # Define the __init__ method that runs when an object is created
    def __init__(self, make, model, year):
        # Assign values to the attributes of the object
        self.make = make
        self.model = model
        self.year = year

    # Define a method that displays the information about the vehicle
    def show_info(self):
        print(f"This vehicle is a {self.make} {self.model} from {self.year}.")

# Define a derived class called Car that inherits from Vehicle
class Car(Vehicle):
    # Define the __init__ method that runs when an object is created
    def __init__(self, make, model, year, fuel_type):
        # Call the __init__ method of the base class with the make, model, and year arguments
        super().__init__(make, model, year)
        # Assign values to the attributes of the object
        self.fuel_type = fuel_type

    # Override the show_info method of the base class
    def show_info(self):
        print(f"This car is a {self.make} {self.model} from {self.year} that runs on {self.fuel_type}.")


# # Q7. Create a base class called "Employee" with attributes like "name" and "salary." Derive two classes, "Manager" and "Developer," from "Employee." Add an additional attribute called "department" for the "Manager" class and "programming_language" for the "Developer" class.

# In[8]:



# Define a base class called Employee
class Employee:
    # Define the __init__ method that runs when an object is created
    def __init__(self, name, salary):
        # Assign values to the attributes of the object
        self.name = name
        self.salary = salary

    # Define a method that displays the information about the employee
    def show_info(self):
        print(f"This employee's name is {self.name} and their salary is ${self.salary}.")

# Define a derived class called Manager that inherits from Employee
class Manager(Employee):
    # Define the __init__ method that runs when an object is created
    def __init__(self, name, salary, department):
        # Call the __init__ method of the base class with the name and salary arguments
        super().__init__(name, salary)
        # Assign values to the attributes of the object
        self.department = department

    # Override the show_info method of the base class
    def show_info(self):
        print(f"This manager's name is {self.name}, their salary is ${self.salary}, and they work in the {self.department} department.")

# Define a derived class called Developer that inherits from Employee
class Developer(Employee):
    # Define the __init__ method that runs when an object is created
    def __init__(self, name, salary, programming_language):
        # Call the __init__ method of the base class with the name and salary arguments
        super().__init__(name, salary)
        # Assign values to the attributes of the object
        self.programming_language = programming_language

    # Override the show_info method of the base class
    def show_info(self):
        print(f"This developer's name is {self.name}, their salary is ${self.salary}, and they use {self.programming_language} as their programming language.")


# # Q8. Design a base class called "Shape" with attributes like "colour" and "border_width." Create derived classes, "Rectangle" and "Circle," that inherit from "Shape" and add specific attributes like "length" and "width" for the "Rectangle" class and "radius" for the "Circle" class.

# In[9]:


# Define a base class called Shape
class Shape:
    # Define the __init__ method that runs when an object is created
    def __init__(self, colour, border_width):
        # Assign values to the attributes of the object
        self.colour = colour
        self.border_width = border_width

    # Define a method that displays the information about the shape
    def show_info(self):
        print(f"This shape has {self.colour} colour and {self.border_width} border width.")

# Define a derived class called Rectangle that inherits from Shape
class Rectangle(Shape):
    # Define the __init__ method that runs when an object is created
    def __init__(self, colour, border_width, length, width):
        # Call the __init__ method of the base class with the colour and border_width arguments
        super().__init__(colour, border_width)
        # Assign values to the attributes of the object
        self.length = length
        self.width = width

    # Override the show_info method of the base class
    def show_info(self):
        print(f"This rectangle has {self.colour} colour, {self.border_width} border width, {self.length} length, and {self.width} width.")

# Define a derived class called Circle that inherits from Shape
class Circle(Shape):
    # Define the __init__ method that runs when an object is created
    def __init__(self, colour, border_width, radius):
        # Call the __init__ method of the base class with the colour and border_width arguments
        super().__init__(colour, border_width)
        # Assign values to the attributes of the object
        self.radius = radius

    # Override the show_info method of the base class
    def show_info(self):
        print(f"This circle has {self.colour} colour, {self.border_width} border width, and {self.radius} radius.")


# # Q9. Create a base class called "Device" with attributes like "brand" and "model." Derive two classes, "Phone" and "Tablet," from "Device." Add specific attributes like "screen_size" for the "Phone" class and "battery_capacity" for the "Tablet" class.

# In[10]:


# Define a base class called Device
class Device:
    # Define the __init__ method that runs when an object is created
    def __init__(self, brand, model):
        # Assign values to the attributes of the object
        self.brand = brand
        self.model = model

    # Define a method that displays the information about the device
    def show_info(self):
        print(f"This device is a {self.brand} {self.model}.")

# Define a derived class called Phone that inherits from Device
class Phone(Device):
    # Define the __init__ method that runs when an object is created
    def __init__(self, brand, model, screen_size):
        # Call the __init__ method of the base class with the brand and model arguments
        super().__init__(brand, model)
        # Assign values to the attributes of the object
        self.screen_size = screen_size

    # Override the show_info method of the base class
    def show_info(self):
        print(f"This phone is a {self.brand} {self.model} with a {self.screen_size}-inch screen.")

# Define a derived class called Tablet that inherits from Device
class Tablet(Device):
    # Define the __init__ method that runs when an object is created
    def __init__(self, brand, model, battery_capacity):
        # Call the __init__ method of the base class with the brand and model arguments
        super().__init__(brand, model)
        # Assign values to the attributes of the object
        self.battery_capacity = battery_capacity

    # Override the show_info method of the base class
    def show_info(self):
        print(f"This tablet is a {self.brand} {self.model} with a {self.battery_capacity}-mAh battery.")


# # Q10. Create a base class called "BankAccount" with attributes like "account_number" and "balance." Derive two classes, "SavingsAccount" and "CheckingAccount," from "BankAccount." Add specific methods like "calculate_interest" for the "SavingsAccount" class and "deduct_fees" for the "CheckingAccount" class.

# In[11]:


# Define a base class called BankAccount
class BankAccount:
    # Define the __init__ method that runs when an object is created
    def __init__(self, account_number, balance):
        # Assign values to the attributes of the object
        self.account_number = account_number
        self.balance = balance

    # Define a method that deposits an amount to the account
    def deposit(self, amount):
        # Check if the amount is positive
        if amount > 0:
            # Add the amount to the balance
            self.balance += amount
            # Print a message to confirm the deposit
            print(f"You have deposited ${amount} to your account {self.account_number}. Your new balance is ${self.balance}.")
        else:
            # Print a message to inform that the amount is invalid
            print(f"Sorry, you cannot deposit a negative or zero amount.")

    # Define a method that withdraws an amount from the account
    def withdraw(self, amount):
        # Check if the amount is positive and less than or equal to the balance
        if 0 < amount <= self.balance:
            # Subtract the amount from the balance
            self.balance -= amount
            # Print a message to confirm the withdrawal
            print(f"You have withdrawn ${amount} from your account {self.account_number}. Your new balance is ${self.balance}.")
        else:
            # Print a message to inform that the amount is invalid or insufficient
            print(f"Sorry, you cannot withdraw a negative, zero, or greater than your balance amount.")

    # Define a method that displays the information about the account
    def show_info(self):
        print(f"This bank account has number {self.account_number} and balance ${self.balance}.")

# Define a derived class called SavingsAccount that inherits from BankAccount
class SavingsAccount(BankAccount):
    # Define the __init__ method that runs when an object is created
    def __init__(self, account_number, balance, interest_rate):
        # Call the __init__ method of the base class with the account_number and balance arguments
        super().__init__(account_number, balance)
        # Assign values to the attributes of the object
        self.interest_rate = interest_rate

    # Define a method that calculates and returns the interest earned for a given period in months
    def calculate_interest(self, months):
        # Calculate the interest earned by multiplying the balance, interest rate, and months and dividing by 12
        interest = (self.balance * self.interest_rate * months) / 12
        # Return the interest value
        return interest

    # Override the show_info method of the base class
    def show_info(self):
        print(f"This savings account has number {self.account_number}, balance ${self.balance}, and interest rate {self.interest_rate}%.")

# Define a derived class called CheckingAccount that inherits from BankAccount
class CheckingAccount(BankAccount):
    # Define the __init__ method that runs when an object is created
    def __init__(self, account_number, balance, monthly_fee):
        # Call the __init__ method of the base class with the account_number and balance arguments
        super().__init__(account_number, balance)
        # Assign values to the attributes of the object
        self.monthly_fee = monthly_fee

    # Define a method that deducts the monthly fee from the balance
    def deduct_fees(self):
        # Check if the balance is greater than or equal to the monthly fee
        if self.balance >= self.monthly_fee:
            # Subtract the monthly fee from the balance
            self.balance -= self.monthly_fee
            # Print a message to confirm the deduction
            print(f"You have deducted ${self.monthly_fee} from your account {self.account_number} as monthly fee. Your new balance is ${self.balance}.")
        else:
            # Print a message to inform that the balance is insufficient for deduction
            print(f"Sorry, you do not have enough funds in your account {self.account_number} to pay for the monthly fee.")

    # Override the show_info method of the base class
    def show_info(self):
        print(f"This checking account has number {self.account_number}, balance ${self.balance}, and monthly fee ${self.monthly_fee}.")


# In[ ]:




