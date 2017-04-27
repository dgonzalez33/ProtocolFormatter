import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class menuBar:
             
        def create_widget(self):
            
            #vbox is the top_level parent
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
            #fullContainer is a container for the whole  widget
            fullContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            #buttonContainer contains the buttons
            buttonContainer = Gtk.Box(spacing=6)
            
            #pack_start says fullContainer is now a child of vbox
            vbox.pack_start(fullContainer,True,True,0)
            
            #create an File button 
            fileButton = Gtk.Button("File")
            
            #connect the button to a function 'on_File_clicked'
            fileButton.connect("clicked",self.on_File_clicked)
            fileButton.set_alignment(xalign=0, yalign=1) 
            
            #file button is now a child of the buttoncontainer 
            buttonContainer.pack_start(fileButton,False,False,0)
            
            #create a Edit button
            editButton = Gtk.Button("Edit")
            
            #connect the button to a function 'on_Edit_clicked'
            editButton.connect("clicked",self.on_Edit_clicked)
            editButton.set_alignment(xalign=0, yalign=1) 
            
            #edit button is now a child of the buttoncontainer
            buttonContainer.pack_start(editButton,False,False,0)

            #create an Window button 
            windowButton = Gtk.Button("Window")
            
            #connect the button to a function 'on_Window_clicked'
            windowButton.connect("clicked",self.on_Window_clicked)
            windowButton.set_alignment(xalign=0, yalign=1) 
            
            #window button is now a child of the buttoncontainer 
            buttonContainer.pack_start(windowButton,False,False,0)

            #create an Help button 
            helpButton = Gtk.Button("Help")
            
            #connect the button to a function 'on_Help_clicked'
            helpButton.connect("clicked",self.on_Help_clicked)
            helpButton.set_alignment(xalign=0, yalign=1) 
            
            #help button is now a child of the buttoncontainer 
            buttonContainer.pack_start(helpButton,False,False,0)
            
            #buttoncontainer is not a child of the fullcontainer
            fullContainer.pack_start(buttonContainer,False,False,0)
            
            return vbox
                
        def on_File_clicked(self, widget):
            print("File was clicked")
            
        def on_Edit_clicked(self, widget):
            print("edit was clicked")

        def on_Window_clicked(self, widget):
            print("window was clicked")

        def on_Help_clicked(self, widget):
            print("help was clicked")

