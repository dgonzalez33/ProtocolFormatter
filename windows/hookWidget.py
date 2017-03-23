import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from filterList import FilterList
from filterRow import FilterRow

class HookWidget:

        
            
        def create_widget(self):
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            fieldContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(fieldContainer,True,True,0)

            fieldLabel = Gtk.Label()
            fieldLabel.set_markup("<b>Field(s) Selector</b>")
            fieldLabel.set_alignment(xalign=0, yalign=1) 
            fieldContainer.pack_start(fieldLabel,True,True,0)

            self.expLists = FilterList()
            hoodAdd = Gtk.Box(spacing = 6)
            fieldContainer.pack_start(hoodAdd,True,True,0)
            hoodAdd.pack_start(self.expLists.getList(),True,True,0)

            addField = Gtk.Button("->")
            # addFilter.set_image(image)
            addField.connect("clicked",self.on_addField_clicked)
            hoodAdd.pack_start(addField,False,False,1)

            self.listbox = Gtk.ListBox()
            self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
            hoodAdd.pack_start(self.listbox,True,True,0)
            row = FilterRow(self.listbox,"proto","tcp")
            self.listbox.add(row.getRow())  

            self.context = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(self.context,False,False,0)
            contextLabel = Gtk.Label()
            contextLabel.set_markup("<b>Script Selector</b>")
            contextLabel.set_alignment(xalign=0, yalign=1) 
            self.context.pack_start(contextLabel,False,False,0)
            self.scriptWrapper = Gtk.Box(spacing=6)
            self.context.pack_start(self.scriptWrapper,False,False,0)
            self.createBut = Gtk.Button(label="Create Script")
            self.createBut.connect("clicked", self.on_includeBut_clicked)
            self.scriptWrapper.pack_start(self.createBut,False,False,0)
            self.scriptPathEntry = Gtk.Entry()
            self.scriptPathEntry.set_text("<File Path>")
            self.scriptWrapper.pack_start(self.scriptPathEntry,True,True,0)


            # self.excludeWrapper = Gtk.Box(spacing=6)
            # self.context.pack_start(self.excludeWrapper,False,False,0)
            # self.excludeBut = Gtk.Button(label="Exclude")
            # self.excludeBut.connect("clicked", self.on_excludeBut_clicked)
            # self.excludeWrapper.pack_start(self.excludeBut,False,False,0)
            # self.excludeEntry = Gtk.Entry()
            # self.excludeEntry.set_text("<Enter String>")
            # self.excludeWrapper.pack_start(self.excludeEntry,True,True,0)

            self.box = Gtk.Box(spacing=6)
            vbox.pack_start(self.box,False,False,0)
            customLabel = Gtk.Label("Custom Name: ")
            self.box.pack_start(customLabel,False,False,0)
            self.customName = Gtk.Entry()
            self.customName.set_text("<Name of Hook>")
            self.box.pack_start(self.customName, False, False, 0)
            self.butCreate = Gtk.Button(label="Create Hook")
            # self.butCreate.connect("clicked", self.on_butCreate_clicked)
            self.box.pack_start(self.butCreate,False,False,0)
            self.butCancel = Gtk.Button(label="Cancel")
            # self.butCancel.connect("clicked",self.on_butReset_clicked)
            self.box.pack_start(self.butCancel,False,False,0)
            
            return vbox
            
        def on_butCreate_clicked(self, widget):
            print("Applying Filter!")
        def on_butReset_clicked(self, widget):
            print("Resetting FIlter!")
        def on_includeBut_clicked(self, widget):
            print("Including!") 
        def on_excludeBut_clicked(self, widget):
            print("Including!") 
        def on_addField_clicked(self, widget):
            selected = self.expLists.getSelected()
            print(selected[0])
            row = FilterRow(self.listbox,selected[0],selected[1])
            self.listbox.add(row.getRow())
            self.listbox.show_all()    

