#Command line widget
#python 3.5
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class HistoricalWidget:

    def create_widget(self):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        title = Gtk.Label()
        title.set_markup("<b>Command Line</b>")
        title.set_alignment(xalign=0, yalign=1)
        contextLabel = Gtk.Label()
        contextLabel.set_markup("<b>Command available: </b>")
        contextLabel.set_alignment(xalign=0, yalign=1)
        vbox.pack_start(contextLabel, False, False, 0)
        self.includeEntry = Gtk.Entry()
        self.includeEntry.set_text(">/")
        vbox.pack_start(self.includeEntry,True,True,0)
        return vbox

    def Historical_copy(self):
        read_file = open("name of file" , "rb")
        data = read_file.read()
        read_file.close()
        create_file = open("Historical copy", "wb")
        create_file.write(data)
        create_file.close()