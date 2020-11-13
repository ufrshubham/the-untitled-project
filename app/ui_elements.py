"""
This file contains all the customized UI elements for this game.
"""

import arcade.gui
from arcade.gui.ui_style import UIStyle


class FlatButton(arcade.gui.UIFlatButton):
    """ Adds on click to arcade.gui.FlatButton. """

    def __init__(self,
                 text: str,
                 on_click_callback,
                 button_id: int,
                 center_x: int = 0,
                 center_y: int = 0,
                 width: int = 0,
                 height: int = 0,
                 align="center",
                 style: UIStyle = None,
                 **kwargs):
        """
        :param text: Text
        :on_click_callback: callback function to be called on button click,
        :button_id: input argument to callback function specified,
        :param center_x: center X of element
        :param center_y: center y of element
        :param width: width of element
        :param height: height of element
        :param align: align of text, requires set width
        :param style: style of :py:class:`arcade.gui.UIElement`
        :param kwargs: catches unsupported named parameters
        """
        super().__init__(text=text, center_x=center_x, center_y=center_y,
                         width=width, height=height, align=align, style=style, **kwargs)

        # Store the callback function and button id.
        self.on_click_callback = on_click_callback
        self.button_id = button_id

    def on_click(self):
        """ Gets call on button click with button id. """
        self.on_click_callback(self.button_id)
