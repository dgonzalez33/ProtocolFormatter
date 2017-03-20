import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ScriptWindow(Gtk.Window):

        def read_file(self, filename):
            file_object = open(filename, "r+")
            return file_object
        
        def __init__(self):
                Gtk.Window.__init__(self, title="Script Window")
                self.set_default_size(500,300)
                vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                self.set_border_width(10)
                self.add(vbox)
                
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
                
                self.scrollContainer = Gtk.ScrolledWindow()
                self.scriptContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
                
                self.scriptBuffer = Gtk.TextBuffer()
                filetext = read_file(self, 'filterWindow.py')
                self.scriptBuffer.set_text(filetext)
                self.scriptView = Gtk.TextView()
                self.scriptView.set_buffer(self.scriptBuffer)
                self.scriptContainer.pack_start(self.scriptView, False, False, 0)
                self.scrollContainer.add(self.scriptContainer)
                fullTopContainer.pack_start(self.scrollContainer,True,True,0)
                
        def on_Open_clicked(self, widget):
            print("open was clicked")
            
        def on_New_clicked(self, widget):
            print("new was clicked")
            
        
        

                
                
def read_file(self, filename):
    with open(filename, 'r') as myfile:
        data = myfile.read()
    return data


win = ScriptWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()