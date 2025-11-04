from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 1

        # Create second grid layout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Add widgets
        self.top_grid.add_widget(Label(text="Name: ", font_size=32))
        # Add Input Box
        self.name = TextInput(multiline=False, font_size=32)
        self.top_grid.add_widget(self.name)

        # Add widgets
        self.top_grid.add_widget(Label(text="Favourite Pizza: ", font_size=32))
        # Add Input Box
        self.pizza = TextInput(multiline=False, font_size=32)
        self.top_grid.add_widget(self.pizza)

        # Add widgets
        self.top_grid.add_widget(Label(text="Favourite Color: ", font_size=32))
        # Add Input Box
        self.color = TextInput(multiline=False, font_size=32)
        self.top_grid.add_widget(self.color)

        # Add the new top_grid to the app
        self.add_widget(self.top_grid)

        # Create a Submit button
        self.submit = Button(text="Submit", font_size=64)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        """
        print(
            f"Hello {name}, you like {pizza} pizza, and your favourite color is {color}",
        )
        """
        self.add_widget(
            Label(
                text=f"Hello {name}, you like {pizza} pizza, and your favourite color is {color}",
                font_size=32,
            )
        )

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
