
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FilterBarWidget:

    def create_widget(self):
        hbox = Gtk.Box(spacing=6)
        filterEntry = Gtk.Entry()
        filterEntry.set_text("<Enter Filter>")
        hbox.pack_start(filterEntry,True,True,0)
        return hbox
