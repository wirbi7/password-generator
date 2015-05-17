from gi.repository import Gtk, Pango
from random import choice
import os

capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letters   = 'abcdefghijklmnopqrstuvwxyz'
digits          = '1234567890'
symbols         = '!"#;%:?*()_+=-~/\<>,.[]{}'

builder = Gtk.Builder()


class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def generate(self, button):
        string = ''
        if builder.get_object('checkCapital').get_active():
            string += capital_letters

        if builder.get_object('checkLower').get_active():
            string += lower_letters

        if builder.get_object('checkDigits').get_active():
            string += digits

        if builder.get_object('checkSymbols').get_active():
            string += symbols

        lenght = int(builder.get_object('scaleLenght').get_value())
        count  = int(builder.get_object('scaleCount').get_value())

        if string:
            text = ''
            for i in range(count):
                for k in range(lenght):
                    text += choice(string)
                text += "\n"

            builder.get_object('textbuffer').set_text(text)


def main():
    builder.add_from_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pasgen.glade"))
    builder.connect_signals(Handler())

    builder.get_object("textview").modify_font(Pango.FontDescription('monospace'))
    Handler().generate(None)

    window = builder.get_object("windowMain")
    window.show_all()

    Gtk.main()