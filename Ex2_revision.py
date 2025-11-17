# -------------------------------------------
# Exercise 2: Functions Revision
# -------------------------------------------
# In this exercise, you'll work in groups of 2–3.
# We're going to practise FUNCTIONS again with more guidance.
#
# **If you are working alone:** You can ignore the "SWAP COMPUTERS" 
# instructions throughout this exercise. Just complete each task in order 
# and commit your work after each task.
#
# Remember:
# - Functions are reusable blocks of code
# - They help us organise our program
# - They make code easier to read and maintain
#
# Basic function structure:
# def function_name():
#     # code goes here
#     print("This is what the function does")
#
# Function with parameters (inputs):
# def greet(name):
#     print(f"Hello, {name}!")
#
# Function that returns a value (gives back a result):
# def add(a, b):
#     return a + b
#
# Each learner will build on the previous one's work.
# -------------------------------------------
# GROUP INSTRUCTIONS
# -------------------------------------------
# Work in groups of 2–3. Share the same GitHub repository.
# Roles:
# - One learner acts as the DRIVER (types the code and runs commands).
# - The other learners are NAVIGATORS (observe, guide, and provide suggestions).
#
# After each task:
# - Current learner: git add, commit, and push
# - Next learner: git pull origin main
#
# **If working alone:** Complete each task and commit after finishing it.
# -------------------------------------------


# Task 1: Simple Functions with Parameters
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Simple Functions with Parameters\n"
    + "-------------------------------------------")
# Let's start by creating functions that take information and display it.
# A parameter is like a variable that gets a value when you call the function.
#
# TODO:
# 1. Create a function called 'print_welcome' that:
#    - Takes ONE parameter called 'name'
#    - Prints: "Welcome to the Cinema Booking System, [name]!"
#    
#    EXAMPLE:
#    def print_welcome(name):
#        print(f"Welcome to the Cinema Booking System, {name}!")
#
# 2. Create a function called 'print_movie_info' that:
#    - Takes TWO parameters: title, duration
#    - Prints:
#      "Movie: [title]"
#      "Duration: [duration] minutes"
#
# 3. Create a function called 'print_booking_summary' that:
#    - Takes THREE parameters: name, movie, seats
#    - Prints:
#      "--- Booking Summary ---"
#      "Customer: [name]"
#      "Movie: [movie]"
#      "Seats: [seats]"
#      "-----------------------"
#
# 4. Test your functions by calling them:
#    - print_welcome("Sarah")
#    - print_movie_info("The Matrix", 136)
#    - print_booking_summary("Sarah", "The Matrix", 2)
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes
# 2. Commit with an appropriate message
# 3. Push to the repository
# The next learner must pull the latest version before continuing
# -------------------------------------------


# Task 2: Functions that Get Input and Return Values
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 2: Functions that Get Input and Return Values\n"
    + "-------------------------------------------")
# Functions can ask the user for information and RETURN it so we can use it later.
# The RETURN keyword sends a value back to wherever the function was called.
#
# TODO:
# 1. Create a function called 'get_customer_name' that:
#    - Uses input() to ask: "Enter your name: "
#    - RETURNS the answer
#
#    EXAMPLE:
#    def function_name_here():
#        name = input("Enter your name: ")
#        return name
#
# 2. Create a function called 'get_movie_title' that:
#    - Uses input() to ask: "Enter movie title: "
#    - Returns the answer
#
# 3. Create a function called 'get_number_of_seats' that:
#    - Uses input() to ask: "How many seats? "
#    - Converts the input to an integer using int()
#    - Returns the integer
#
#    HINT: return int(input("How many seats? "))
#
# 4. TEST your functions:
#    - Call get_customer_name() and store the result: customer = get_customer_name()
#    - Call get_movie_title() and store the result: movie = get_movie_title()
#    - Call get_number_of_seats() and store the result: seats = get_number_of_seats()
#    - Use print_booking_summary() from Task 1 to display all three values
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes
# 2. Commit with an appropriate message
# 3. Push to the repository
# The next learner must pull the latest version before continuing
# -------------------------------------------


# Task 3: Functions that Calculate and Return Results
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 3: Functions that Calculate and Return Results\n"
    + "-------------------------------------------")
# Functions can do calculations and return the result!
# This makes our code more organised and reusable.
#
# TODO:
# 1. Create a function called 'calculate_ticket_cost' that:
#    - Takes TWO parameters: num_seats, price_per_seat
#    - Calculates the total: num_seats * price_per_seat
#    - Returns the result
#
#    EXAMPLE:
#    def calculate_ticket_cost(num_seats, price_per_seat):
#        total = num_seats * price_per_seat
#        return total
#
# 2. Create a function called 'apply_discount' that:
#    - Takes TWO parameters: total, discount_percent
#    - Calculates the discount amount: total * (discount_percent / 100)
#    - Subtracts the discount from the total
#    - Returns the new total
#
#    HINT: new_total = total - (total * (discount_percent / 100))
#
# 3. Create a function called 'display_price' that:
#    - Takes ONE parameter: price
#    - Prints: "Total cost: £[price]"
#    - (Just prints, doesn't return anything)
#
# 4. TEST your functions:
#    - Create a variable: seats = 3
#    - Calculate cost: cost = calculate_ticket_cost(seats, 12)
#    - Apply 10% discount: final_cost = apply_discount(cost, 10)
#    - Display the result: display_price(final_cost)
#    - Try with different numbers of seats and discounts!
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes
# 2. Commit with an appropriate message
# 3. Push to the repository
# The next learner must pull the latest version before continuing
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Building a Booking Dictionary
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 1: Building a Booking Dictionary\n"
    + "-------------------------------------------")
# Let's combine everything we've learnt to create complete booking records!
# A dictionary stores related information together using keys and values.
#
# TODO:
# 1. Create a function called 'create_booking' that:
#    - Takes FOUR parameters: customer_name, movie_title, num_seats, total_cost
#    - Creates a dictionary with these keys: "customer", "movie", "seats", "cost"
#    - Returns the dictionary
#
#    EXAMPLE:
#    def create_booking(customer_name, movie_title, num_seats, total_cost):
#        booking = {
#            "customer": customer_name,
#            "movie": movie_title,
#            "seats": num_seats,
#            "cost": total_cost
#        }
#        return booking
#
# 2. Create a function called 'display_booking' that:
#    - Takes ONE parameter: booking (which will be a dictionary)
#    - Prints the information nicely using the dictionary keys
#    - Example: print(f"Customer: {booking['customer']}")
#    - Display all four pieces of information
#
# 3. TEST by:
#    - Calling get_customer_name(), get_movie_title(), and get_number_of_seats()
#    - Calculating the cost using calculate_ticket_cost() with price £12 per seat
#    - Creating a booking dictionary with create_booking()
#    - Displaying it with display_booking()
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes
# 2. Commit with an appropriate message
# 3. Push to the repository
# The next learner must pull the latest version before continuing
# -------------------------------------------


# Extension 2: Storing Multiple Bookings
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 2: Storing Multiple Bookings\n"
    + "-------------------------------------------")
# Now let's store many booking records in a list!
# Lists allow us to keep track of multiple items.
#
# TODO:
# 1. At the top of this section, create an empty list: bookings = []
#
# 2. Create a function called 'add_booking' that:
#    - Calls get_customer_name(), get_movie_title(), and get_number_of_seats()
#    - Calculates cost using calculate_ticket_cost() with £12 per seat
#    - Creates a booking dictionary using create_booking()
#    - Adds that dictionary to the bookings list using .append()
#    - Prints "Booking added successfully!"
#    - Prints "Total bookings: [number]" (use len(bookings))
#
# 3. Create a function called 'display_all_bookings' that:
#    - Prints "=== ALL CINEMA BOOKINGS ==="
#    - If bookings list is empty, print "No bookings yet."
#    - Otherwise, loop through bookings and display each one using display_booking()
#    - Print a separator line after each booking
#    - Print "Total bookings: [number]" at the end
#
# 4. TEST by:
#    - Calling add_booking() twice with different information
#    - Then calling display_all_bookings()
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes
# 2. Commit with an appropriate message
# 3. Push to the repository
# The next learner must pull the latest version before continuing
# -------------------------------------------


# Extension 3: Calculate Total Revenue
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 3: Calculate Total Revenue\n"
    + "-------------------------------------------")
# Let's create a function that adds up all the money from bookings!
#
# TODO:
# Create a function called 'calculate_total_revenue' that:
# - If bookings list is empty, print "No bookings to calculate revenue."
# - Otherwise:
#   * Create a variable total_revenue = 0
#   * Loop through each booking in bookings
#   * Add the cost from each booking to total_revenue
#   * After the loop, print "Total revenue: £[total_revenue]"
#
# HINT: To get the cost from a booking dictionary, use: booking["cost"]
# 
# TEST by:
# - Making sure you have at least 2 bookings in your list (from Extension 2)
# - Calling calculate_total_revenue()
# - It should add up all the costs and display the total
#
# CHALLENGE: Also display the average booking value!
# - Divide total_revenue by len(bookings)
# - Print "Average booking value: £[average]"
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes
# 2. Commit with an appropriate message
# 3. Push to the repository
# The next learner must pull the latest version before continuing
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY
# -------------------------------------------
print("-------------------------------------------\n"
    + "ADVANCED ACTIVITY\n"
    + "-------------------------------------------")
# Create a complete menu-driven cinema booking system!
#
# TODO:
# 1. Create a function called 'display_menu' that prints:
#    "=== CINEMA BOOKING SYSTEM ==="
#    "1. Make new booking"
#    "2. View all bookings"
#    "3. Calculate total revenue"
#    "4. Exit"
#
# 2. Create a function called 'get_menu_choice' that:
#    - Uses a while loop to keep asking for input
#    - Asks "Choose option (1-4): "
#    - If input is "1", "2", "3", or "4", return it
#    - Otherwise print "Invalid choice! Please enter 1, 2, 3, or 4."
#
# 3. Create a function called 'main' that:
#    - Calls print_welcome() with "Manager" as the name
#    - Uses a while True loop (runs forever until we break)
#    - Displays the menu using display_menu()
#    - Gets the user's choice using get_menu_choice()
#    - If choice is "1": calls add_booking()
#    - If choice is "2": calls display_all_bookings()
#    - If choice is "3": calls calculate_total_revenue()
#    - If choice is "4": prints "Goodbye!" and breaks
#    - Prints a blank line after each action for readability
#
# 4. At the VERY BOTTOM of the file, call main() to start the program
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Use Git to:
# 1. Stage your final changes
# 2. Commit with an appropriate message
# 3. Push your final version to the repository
# -------------------------------------------
