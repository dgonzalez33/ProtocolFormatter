#Command line widget
#python 3.5
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CommandLineWidget:

    def create_widget(self):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        title = Gtk.label()
        title.set_markup("<b>Command Line</b>")
        title.set_alignment(xalign=0, yalign=1)
        contextLabel = Gtk.Label()
        contextLabel.set_markup("<b>Command available: </b>")
        contextLabel.set_alignment(xalign=0, yalign=1)
        self.context.pack_start(contextLabel, False, False, 0)
        self.includeEntry = Gtk.Entry()
        self.includeEntry.set_text(">/")
        self.includeWrapper.pack_start(self.includeEntry,True,True,0)
        return vbox
