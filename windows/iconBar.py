import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class iconBar:
             
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
            
            #create a Save button
            saveButton = Gtk.Button("Save")
            
            #connect the button to a function 'on_Save_clicked'
            saveButton.connect("clicked",self.on_Save_clicked)
            saveButton.set_alignment(xalign=0, yalign=1) 
            
            #save button is now a child of the buttoncontainer
            buttonContainer.pack_start(saveButton,False,False,0)

	    #create an Filter button 
            filterButton = Gtk.Button("Filter")
            
            #connect the button to a function 'on_Filter_clicked'
            filterButton.connect("clicked",self.on_Filter_clicked)
            filterButton.set_alignment(xalign=0, yalign=1) 
            
            #filter button is now a child of the buttoncontainer 
            buttonContainer.pack_start(filterButton,False,False,0)

	    #create an Undo button 
            undoButton = Gtk.Button("Undo")
            
            #connect the button to a function 'on_Undo_clicked'
            undoButton.connect("clicked",self.on_Undo_clicked)
            undoButton.set_alignment(xalign=0, yalign=1) 
            
            #undo button is now a child of the buttoncontainer 
            buttonContainer.pack_start(undoButton,False,False,0)

	    #create an Redo button 
            redoButton = Gtk.Button("Redo")
            
            #connect the button to a function 'on_Redo_clicked'
            redoButton.connect("clicked",self.on_Redo_clicked)
            redoButton.set_alignment(xalign=0, yalign=1) 
            
            #redo button is now a child of the buttoncontainer 
            buttonContainer.pack_start(redoButton,False,False,0)
            
            #buttoncontainer is not a child of the fullcontainer
            fullContainer.pack_start(buttonContainer,False,False,0)
            
            return vbox
                
        def on_Open_clicked(self, widget):
            print("open was clicked")
            
        def on_Save_clicked(self, widget):
            print("save was clicked")

	def on_Filter_clicked(self, widget):
            print("filter was clicked")

	def on_Undo_clicked(self, widget):
            print("undo was clicked")

	def on_Redo_clicked(self, widget):
            print("redo was clicked")

