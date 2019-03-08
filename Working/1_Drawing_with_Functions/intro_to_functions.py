import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions
def draw_cloud():
    arcade.draw_circle_filled(position_cloud - 65, 500, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(position_cloud, 500, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(position_cloud + 65, 500, 50, arcade.color.WHITE)

def draw_rolling_hills():
    arcade.draw_circle_filled(50, -100, 400, arcade.color.GREEN)
    arcade.draw_circle_filled(700, -50, 300, arcade.color.GREEN)
    arcade.draw_circle_filled(400, 50, 200, arcade.color.GREEN)

def draw_tree():
    arcade.draw_triangle_filled(100, 410, 50, 360, 150, 360, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(100, 385, 40, 335, 160, 335, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(100, 360, 30, 310, 170, 310, arcade.color.DARK_GREEN)
    arcade.draw_rectangle_filled(100, 290, 25, 40, arcade.color.BROWN)

def draw_sun():
    arcade.draw_circle_filled(400, position_sun, 100, arcade.color.SUNSET_ORANGE)

def on_draw(delta_time):
    global position_cloud, position_sun, speed_cloud, speed_sun
    arcade.start_render()
    draw_tree()
    draw_sun()
    position_sun += speed_sun
    draw_rolling_hills()
    draw_cloud()
    position_cloud += speed_cloud

position_sun = 0
position_cloud = 0
speed_sun = 1
speed_cloud = 2

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_sun()
    draw_cloud()
    draw_rolling_hills()
    draw_tree()

    # Finish and run
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()

# Call the main function to get the program started.
main()