from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

INCREMENT = 1

CONVERSION = 1.609


class ConvertMilesApp(App):
    """ ConvertMilesApp is a Kivy App for converting miles to km """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (700, 400)  # 200, 100
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_up(self, value):
        """Handle 'Up' button press, add 1 to number in field"""
        miles = self.convert_to_number(value) + INCREMENT
        self.root.ids.input_number.text = str(miles)

    def handle_down(self, value):
        """Handle 'Down' button press, subtract 1 to number in field"""
        miles = self.convert_to_number(value) - INCREMENT
        self.root.ids.input_number.text = str(miles)

    def handle_calculate(self, value):
        """ handle calculation, output result to label widget """
        try:
            result = float(value) * CONVERSION
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

    @staticmethod
    def convert_to_number(value):
        """Convert value to 0 when input is invalid"""
        try:
            return float(value)
        except ValueError:
            return 0.0

ConvertMilesApp().run()
