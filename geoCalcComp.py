# -*- coding: utf-8 -*-
"""
Let's build an interactive geometry menu!

@author: CS 5045 Fall 2026
"""

# %reset (in console)
#   Using consol in general
# deleting variables
# restarting kernel

# Initialize choice value
choice = 0

# Loop until user exits
while choice != 5:

    # Main menu
    print("MAIN MENU\n\n")
    print("Welcome to the menu for the geometry calculator!")
    print("")
    print("Choose a number from the following options:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Square")
    print("5. Exit")
    
    # Get selection from the user
    # NOTE: Input() always returns a string
    choice = input("Select which the shape number you would like to calculate: ")
    # Convert user input var type if necessary
    if choice.isnumeric():
        choice = int(choice)   
    
        
    # SUBMENUS
    
    
    # Choice 1 Rectangle
    if choice == 1:
        print("You have selected rectangle!")
        
        width = 'a'
        # Get width, loop until no input error, i.e., number
        while not width.isnumeric():    
            width = input("Give me the rectangle's width: ")
        # Convert var type if necessary
        width = int(width)

        length = 'a'
        # Get length, loop until no input error, i.e., number
        while not length.isnumeric():    
            length = input("Give me the rectangle's length: ")
        # Convert var type if necessary
        length = int(length)
        
        # Rectangle options menu
        print("")
        print("What number operation do you want to run?")
        print("1. Compute the area")
        print("2. Compute the perimeter")    
        print("3. Exit")
        
        # Get subchoice selection from the user
        subchoice = input("Enter your selection here: ")
        # Error correct user input
        if subchoice.isnumeric():
            subchoice = int(subchoice)
            
        # Rectangle area
        if subchoice == 1:
            area = length * width
            print("The area of your rectangle is", area)
        
        # Rectangle Perimeter
        elif subchoice == 2:
            perimeter = (2 * width) + (2 * length)
            print("The perimeter of your rectangle is", perimeter)
        
        # Exit AND non-valid inputs
        else:
            print("\nOK, returning to main menu.")
            
        
    # Choice 2 Triangle
    elif choice == 2:
        print("You have selected triangle!")
        
        base = 'a'
        # Get base, loop until no input error, i.e., number
        while not base.isnumeric():  
            base = input("Give me the base of the triangle: ")
        # Convert var type if necessary
        base = int(base)

        height = 'a'
        # Get height, loop until no input error, i.e., number
        while not height.isnumeric():  
            height = input("Give me the height of the triangle: ")
        # Convert var type if necessary
        height = int(height)
        
        # Get 3 side lengths
        side = 'a'
        sides = []
        for count in range(3):
            # Get side, loop until no input error, i.e., number
            while not side.isnumeric():  
                side = input("Give me the length of a side: ")
                # Let user know when number is not valid
                if not side.isnumeric():
                    print ("That is not a valid length. Try again.")
            # Convert var type if necessary
            side = int(side)
            # Add side to list
            sides.append(side)
            # Reinitialize string variable for next loop
            side = 'a'
        
        # Traingle options menu
        print("")
        print("What operation do you want to run?")
        print("1. Compute the area")
        print("2. Compute the perimeter") 
        print("3. Exit")
        
        # Get subchoice selection from the user
        subchoice = input("Enter your selection here: ")
        # Error correct user input
        if subchoice.isnumeric():
            subchoice = int(subchoice)
        
        # Traingle area
        if subchoice == 1:
            area = 0.5 * base * height
            print("The area of your triangle is", area)
        
        # Rectangle Perimeter
        elif subchoice == 2:
            perimeter = 0
            # Loop through sides and add them to perimeter
            for count in range (3):
                perimeter += sides[count]
            print("The perimeter of your rectangle is", perimeter)
            
        # Exit AND non-valid inputs
        else:
            print("\nOK, returning to main menu.")
        
        
    # Choice 3 Circle    
    elif choice == 3:
        print("Your have selected circle!")
        
        radius = 'a'
        # Get radius, loop until no input error, i.e., number
        while not radius.isnumeric():  
            radius = input("Give me the radius of the circle: ")
        # Convert var type if necessary
        radius = int(radius)

        # Circle options menu
        print("")
        print("What operation do you want to run?")
        print("1. Compute the area")
        print("2. Compute the circumference")    
        print("3. Exit")
        
        # Get subchoice selection from the user
        subchoice = input("Enter your selection here: ")
        # Error correct user input
        if subchoice.isnumeric():
            subchoice = int(subchoice)
        
        # Circle area
        if subchoice == 1:
            area = 3.14159 * radius ** 2
            print("The area of your circle is", area)
        
        # Circle circumference
        elif subchoice == 2:
            circumference = 2 * 3.14 * radius
            print("The circumference of your circle is", circumference)
        
        # Exit AND non-valid inputs
        else:
            print("\nOK, returning to main menu.")
    
    
    # Choice 4 Square
    elif choice == 4:
        print("You have selected square!")
        
        side = 'a'
        # Get side, loop until no input error, i.e., number
        while not side.isnumeric():  
            side = input("Give me the length of a side: ")
        # Convert var type
        side = int(side)

        
        # Square options menu
        print("")
        print("What operation do you want to run?")
        print("1. Compute the area")
        print("2. Compute the perimeter")
        print("3. Exit")
        
        # Get subchoice selection from the user
        subchoice = input("Enter your selection here: ")
        # Error correct user input
        if subchoice.isnumeric():
            subchoice = int(subchoice)
        
        # Calculate area
        if subchoice == 1:
            area = side * side
            print("The area of your circle is", area)
            
        # Calculate Perimeter
        if subchoice == 2:
            perimeter = 0
            # Create loop to add all 4 sides
            for counter in range(4):
                perimeter = perimeter + side
            print("The perimeter of your square is", perimeter)
        
        # Exit AND non-valid inputs
        else:
            print("/nOK, returning to main menu.")
    
    
    # Choice 5 Exit
    elif choice == 5:
        print("\nOK, exiting now...")
    
    
    # Non-valid inputs
    else: 
        print("\nYou didn't select a valid menu option.  Try again!")
        # Tell user to use numbers
        shapes = ["Rectangle", "Triangle", "Circle", "Square"]
        for option in shapes:
            if choice == option:
                print ("\nPlease select a number not a shape.")
        
        
    # Reload main menu
    print("\n\n")
    
