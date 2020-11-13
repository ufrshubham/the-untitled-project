"""
This file contains all the view classes for this game.
"""

import enum
import arcade
import arcade.gui
from arcade.gui import UIManager
import ui_elements


class ButtonID(enum.Enum):
    """ Button ID for clickable buttons. """
    Play = 0
    Exit = 1


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.ui_manager = UIManager()

    def on_click(self, button_id):
        """ Callback function to be called when any of the buttons on this view gets pressed. """
        if button_id == ButtonID.Play:
            game_view = GameView(self.width, self.height)
            game_view.setup()
            self.window.show_view(game_view)
        elif button_id == ButtonID.Exit:
            self.window.close()

    def setup(self):
        """ Sets up the UI for this view. """
        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height // 5
        left_column_x = self.window.width // 4

        play_button = ui_elements.FlatButton(
            'Play',
            self.on_click,
            ButtonID.Play,
            center_x=left_column_x,
            center_y=y_slot * 2,
        )

        self.ui_manager.add_ui_element(play_button)

        self.ui_manager.add_ui_element(ui_elements.FlatButton(
            'Exit',
            self.on_click,
            ButtonID.Exit,
            center_x=left_column_x,
            center_y=y_slot,
        ))

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Snakes and Ladders",
                         self.window.width // 2,
                         (5 * self.window.height // 6),
                         arcade.color.WHITE,
                         font_size=30,
                         anchor_x="center")

        arcade.draw_text("Main Menu", (self.window.width // 4), (self.window.height // 5) * 3,
                         arcade.color.WHITE_SMOKE, font_size=25, anchor_x="center")


class GameView(arcade.View):
    """ Manage the 'game' view for our program. """

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.ui_manager = UIManager()

    def setup(self):
        """ This should set up your game and get it ready to play """
        self.ui_manager.purge_ui_elements()

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.ORANGE_PEEL)
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        arcade.draw_text("Game - press SPACE to advance", self.width/2, self.height/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, symbol, _modifiers):
        """ Handle keypresses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if symbol == arcade.key.SPACE:
            game_over_view = GameOverView(self.width, self.height)
            self.window.show_view(game_over_view)


class GameOverView(arcade.View):
    """ Class to manage the game over view """

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.ui_manager = UIManager()

    def setup(self):
        """ This should set up your game over view. """
        self.ui_manager.purge_ui_elements()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)
        self.setup()

    def on_draw(self):
        """ Draw the game over view """
        arcade.start_render()
        arcade.draw_text("Game Over - press ESCAPE to advance", self.width/2, self.height/2,
                         arcade.color.WHITE, 30, anchor_x="center")

    def on_key_press(self, symbol, _modifiers):
        """ If user hits escape, go back to the main menu view """
        if symbol == arcade.key.ESCAPE:
            menu_view = MenuView(self.width, self.height)
            self.window.show_view(menu_view)
