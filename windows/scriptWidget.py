import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ScriptWidget:
             
        def create_widget(self):
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                
            fullTopContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            buttonContainer = Gtk.Box(spacing=6)
            vbox.pack_start(fullTopContainer,True,True,0)
            
            openButton = Gtk.Button("Open")
            openButton.connect("clicked",self.on_Open_clicked)
            openButton.set_alignment(xalign=0, yalign=1) 
            buttonContainer.pack_start(openButton,False,False,0)
            
            newButton = Gtk.Button("New")
            newButton.connect("clicked",self.on_New_clicked)
            newButton.set_alignment(xalign=0, yalign=1) 
            buttonContainer.pack_start(newButton,False,False,0)
            fullTopContainer.pack_start(buttonContainer,False,False,0)
            
            scrollContainer = Gtk.ScrolledWindow()
            scriptContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
            
            scriptBuffer = Gtk.TextBuffer()
            filetext = read_file(self, 'scriptWidget.py')
            scriptBuffer.set_text(filetext)
            scriptView = Gtk.TextView()
            scriptView.set_buffer(scriptBuffer)
            scriptContainer.pack_start(scriptView, False, False, 0)
            scrollContainer.add(scriptContainer)
            fullTopContainer.pack_start(scrollContainer,True,True,0)
            
            return vbox
                
        def on_Open_clicked(self, widget):
            print("open was clicked")
            
        def on_New_clicked(self, widget):
            print("new was clicked")
            
def read_file(self, filename):
    with open(filename, 'r') as myfile:
        data = myfile.read()
    return data


