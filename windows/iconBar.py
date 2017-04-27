import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

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
		
		#==================================================================================================================
		o_imagebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		o_imagebox.set_border_width(2)
		o_image = Gtk.Image()
		o_label = Gtk.Label("Open")
		o_label.modify_font(Pango.FontDescription("sans 8"))
		o_image.set_from_file("../images/open.png")
		o_imagebox.pack_start(o_image, False, False, 0)
		o_imagebox.pack_start(o_label, False, False, 0)
		o_image.show()
		o_label.show()
		openButton = Gtk.Button()
		openButton.set_alignment(xalign=0.0, yalign=1)
		openButton.connect("clicked",self.on_Open_clicked)
		openButton.add(o_imagebox)
		buttonContainer.pack_start(openButton,False,False,2)
		
		s_imagebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		s_imagebox.set_border_width(2)
		s_image = Gtk.Image()
		s_label = Gtk.Label("Save")
		s_label.modify_font(Pango.FontDescription("sans 8"))
		s_image.set_from_file("../images/save.png")
		s_imagebox.pack_start(s_image, False, False, 0)
		s_imagebox.pack_start(s_label, False, False, 0)
		s_image.show()
		s_label.show()
		saveButton = Gtk.Button()
		saveButton.set_alignment(xalign=0.0, yalign=1)
		saveButton.connect("clicked",self.on_Save_clicked)
		saveButton.add(s_imagebox)
		buttonContainer.pack_start(saveButton,False,False,2)
		
		f_imagebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		f_imagebox.set_border_width(2)
		f_image = Gtk.Image()
		f_label = Gtk.Label("Filter")
		f_label.modify_font(Pango.FontDescription("sans 8"))
		f_image.set_from_file("../images/filter.png")
		f_imagebox.pack_start(f_image, False, False, 0)
		f_imagebox.pack_start(f_label, False, False, 0)
		f_image.show()
		f_label.show()
		filterButton = Gtk.Button()
		filterButton.set_alignment(xalign=0.0, yalign=1)
		filterButton.connect("clicked",self.on_Filter_clicked)
		filterButton.add(f_imagebox)
		buttonContainer.pack_start(filterButton,False,False,2)
		
		u_imagebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		u_imagebox.set_border_width(2)
		u_image = Gtk.Image()
		u_label = Gtk.Label("Undo")
		u_label.modify_font(Pango.FontDescription("sans 8"))
		u_image.set_from_file("../images/undo.png")
		u_imagebox.pack_start(u_image, False, False, 0)
		u_imagebox.pack_start(u_label, False, False, 0)
		u_image.show()
		u_label.show()
		undoButton = Gtk.Button()
		undoButton.set_alignment(xalign=0.0, yalign=1)
		undoButton.connect("clicked",self.on_Undo_clicked)
		undoButton.add(u_imagebox)
		buttonContainer.pack_start(undoButton,False,False,2)

		r_imagebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		r_imagebox.set_border_width(2)
		r_image = Gtk.Image()
		r_label = Gtk.Label("Redo")
		r_label.modify_font(Pango.FontDescription("sans 8"))
		r_image.set_from_file("../images/redo.png")
		r_imagebox.pack_start(r_image, False, False, 0)
		r_imagebox.pack_start(r_label, False, False, 0)
		r_image.show()
		r_label.show()
		redoButton = Gtk.Button()
		redoButton.set_alignment(xalign=0.0, yalign=1)
		redoButton.connect("clicked",self.on_Redo_clicked)
		redoButton.add(r_imagebox)
		buttonContainer.pack_start(redoButton,False,False,2)

		fullContainer.pack_start(buttonContainer,False,False,4)
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

