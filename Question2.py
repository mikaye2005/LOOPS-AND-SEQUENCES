def prompt_user():
    # Start a loop that will run indefinitely
    while True:
        # Ask the user for input
        user_input = input("Enter a word (type 'exit' to quit): ")

        # Check if the user entered "exit" to break out of the loop
        if user_input.lower() == "exit":
            print("Exiting the program.")
            break  # Exit the loop if "exit" is entered

        # Print the user input
        print("You entered:", user_input)


# Call the function to start prompting the user
prompt_user()
