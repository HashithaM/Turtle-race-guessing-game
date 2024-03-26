# Turtle-race-guessing-game
This is a game where user guesses the winner of the turtle race
This Python code is a simple turtle race game using the Turtle module in Python. Here's a breakdown of what the code does:

It imports the Turtle and Screen classes from the turtle module, as well as the random module.

It sets up the screen for the turtle race with a width of 500 pixels and a height of 400 pixels.

It prompts the user to input their bet on which turtle will win the race. The input is converted to lowercase for consistency.

It creates a list of colors representing the turtles and initializes an empty list turtle_list to hold the Turtle objects.

It initializes variables x and y for positioning the turtles on the screen.

It defines a class TurtleRace for organizing the turtle race logic.

Inside the class definition:

It creates six turtle objects, each with a different color from the color_list, and appends them to turtle_list. These turtles are positioned at different y-coordinates on the left side of the screen.
It sets the game_on variable to True if the user_bet has a value (i.e., the user has inputted a bet).
It enters a while loop (while game_on:) to run the race until a turtle reaches the finish line.

It iterates through each turtle in turtle_list.
If a turtle crosses the finish line (x-coordinate greater than 230), the race ends.
It determines the winning turtle's color and compares it with the user's bet.
It writes a message on the screen indicating whether the user won or lost based on their bet.
It sets game_on to False to end the race.
After the race ends, it waits for the user to click on the screen to exit the game (screen.exitonclick()).

Overall, this code simulates a simple turtle race game where the user can bet on which colored turtle will win the race, and the winner is determined randomly.
