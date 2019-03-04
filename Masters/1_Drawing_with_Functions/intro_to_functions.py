import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()