import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

"""
Script Widget is a type of widget for our
protocol formatter window that allows
the user to open/edit/create a script
Widgets do not need windows and should
return a top_level Gtk.Box with all the 
contents of the widget as children 
"""
class ScriptWidget:
             
        def create_widget(self):
            
            #vbox is the top_level parent
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
            #fullContainer is a container for the whole  widget
            fullContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            #buttonContainer contains the buttons
            buttonContainer = Gtk.Box(spacing=6)
            
            #pack_start says fullContainer is now a child of vbox
            vbox.pack_start(fullContainer,True,True,0)
            
            #create an Open button 
            openButton = Gtk.Button("Open")
            
            #connect the button to a function 'on_Open_clicked'
            openButton.connect("clicked",self.on_Open_clicked)
            openButton.set_alignment(xalign=0, yalign=1) 
            
            #open button is now a child of the buttoncontainer 
            buttonContainer.pack_start(openButton,False,False,0)
            
            #create a New button
            newButton = Gtk.Button("New")
            
            #connect the button to a function 'on_New_clicked'
            newButton.connect("clicked",self.on_New_clicked)
            newButton.set_alignment(xalign=0, yalign=1) 
            
            #new button is now a child of the buttoncontainer
            buttonContainer.pack_start(newButton,False,False,0)
            
            #buttoncontainer is not a child of the fullcontainer
            fullContainer.pack_start(buttonContainer,False,False,0)
            
            #create a scrollable container (ScrolledWindow is not really a 'window')
            scrollContainer = Gtk.ScrolledWindow()
            
            #create a container for the script 
            scriptContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
            
            scriptBuffer = Gtk.TextBuffer()
            filetext = read_file(self, "../Scripts/testScript.py")
            scriptBuffer.set_text(filetext)
            
            #create a Textviewer
            scriptView = Gtk.TextView()
            scriptView.set_buffer(scriptBuffer)
            
            #scriptviewer is now a child of script container 
            scriptContainer.pack_start(scriptView, False, False, 0)
            
            #add the scriptview to the scroll window 
            scrollContainer.add(scriptContainer)
            
            #scroll window is now a child of the full container
            fullContainer.pack_start(scrollContainer,True,True,0)
            
            return vbox
                
        def on_Open_clicked(self, widget):
            print("open was clicked")
            
        def on_New_clicked(self, widget):
            print("new was clicked")

      
def read_file(self, filename):
    with open(filename, 'r') as myfile:
        data = myfile.read()
    return data


