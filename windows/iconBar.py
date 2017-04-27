import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class iconBar:


	def create_widget(self):
		#vbox is the top_level parent
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

		#fullContainer is a container for the whole  widget
		fullContainer = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

		#buttonContainer contains the buttons
		buttonContainer = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

		#pack_start says fullContainer is now a child of vbox
		vbox.pack_start(fullContainer,True,True,0)

		box1 = Gtk.HBox(False, 0)
		#create an Open button

		o_image = Gtk.Image()
		o_image.set_from_file("../images/open.png")
		box1.pack_start(o_image, False, False, 3)
		
		o_image.show()
		
		openButton = Gtk.Button()
		openButton.set_alignment(xalign=0.5, yalign=1)
		openButton.connect("clicked",self.on_Open_clicked)
		#open button is now a child of the buttoncontainer 
		openButton.add(box1)
		
		#openButton.getChild().set_from_file("../images/open.png")
		buttonContainer.pack_start(openButton,False,False,5)

		box2 = Gtk.HBox(False, 0)		

		s_image = Gtk.Image()
		s_image.set_from_file("../images/save.png")
		box2.pack_start(s_image, False, False, 3)

		s_image.show()

		#create a Save button
		saveButton = Gtk.Button()

		#connect the button to a function 'on_Save_clicked'
		saveButton.connect("clicked",self.on_Save_clicked)
		saveButton.set_alignment(xalign=0.5, yalign=1)
		saveButton.add(box2) 

		#save button is now a child of the buttoncontainer
		buttonContainer.pack_start(saveButton,False,False,5)

		box3 = Gtk.HBox(False, 0)		

		f_image = Gtk.Image()
		f_image.set_from_file("../images/filter.png")
		box3.pack_start(f_image, False, False, 3)

		f_image.show()

		#create an Filter button 
		filterButton = Gtk.Button()

		#connect the button to a function 'on_Filter_clicked'
		filterButton.connect("clicked",self.on_Filter_clicked)
		filterButton.set_alignment(xalign=0.5, yalign=1) 
		filterButton.add(box3)

		#filter button is now a child of the buttoncontainer 
		buttonContainer.pack_start(filterButton,False,False,5)

		box4 = Gtk.HBox(False, 0)

		u_image = Gtk.Image()
		u_image.set_from_file("../images/undo.png")
		box4.pack_start(u_image, False, False, 3)

		u_image.show()

		#create an Undo button 
		undoButton = Gtk.Button()

		#connect the button to a function 'on_Undo_clicked'
		undoButton.connect("clicked",self.on_Undo_clicked)
		undoButton.set_alignment(xalign=0.5, yalign=1) 
		undoButton.add(box4)

		#undo button is now a child of the buttoncontainer 
		buttonContainer.pack_start(undoButton,False,False,5)

		box5 = Gtk.HBox(False, 0)		

		r_image = Gtk.Image()
		r_image.set_from_file("../images/redo.png")
		box5.pack_start(r_image, False, False, 3)

		r_image.show()

		#create an Redo button 
		redoButton = Gtk.Button()

		#connect the button to a function 'on_Redo_clicked'
		redoButton.connect("clicked",self.on_Redo_clicked)
		redoButton.set_alignment(xalign=0.5, yalign=1) 
		redoButton.add(box5)

		#redo button is now a child of the buttoncontainer 
		buttonContainer.pack_start(redoButton,False,False,5)

		#buttoncontainer is not a child of the fullcontainer
		fullContainer.pack_start(buttonContainer,True,False,0)

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

