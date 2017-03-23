import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from filterList import FilterList
from filterRow import FilterRow

class FormatterWidget:

        
            
        def create_widget(self):
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            appliedFormattersContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(bpfContainer,True,True,0)
            filterContainer = Gtk.Box(spacing=6)

            appliedFormattersLabel = Gtk.Label()
            appliedFormattersLabel.set_markup("<b>Applied Formatters</b>")
            appliedFormattersLabel.set_alignment(xalign=0, yalign=1) 
            appliedFormattersContainer.pack_start(appliedFormattersLabel,True,True,0)
            appliedFormattersContainer.pack_start(filterContainer,True,True,0)

            # self.expLists = FilterList()
            # filterContainer.pack_start(self.expLists.getList(),True,True,0)

            # addFilter = Gtk.Button("->")
            # addFilter.set_image(image)
            # addFilter.connect("clicked",self.on_addFilter_clicked)
            # filterContainer.pack_start(addFilter,False,False,1)

            self.listbox = Gtk.ListBox()
            self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
            filterContainer.pack_start(self.listbox,True,True,0)
            row = FilterRow(self.listbox,"proto","tcp")
            self.listbox.add(row.getRow())  

            self.context = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(self.context,False,False,0)
            contextLabel = Gtk.Label()
            contextLabel.set_markup("<b>Applied Rules for <Protocol X>Based on <Filter A> </b>")
            contextLabel.set_alignment(xalign=0, yalign=1) 
            self.context.pack_start(contextLabel,False,False,0)

            self.rulebox = Gtk.list
            # self.includeWrapper = Gtk.Box(spacing=6)
            # self.context.pack_start(self.includeWrapper,False,False,0)
            # self.includeBut = Gtk.Button(label="Include")
            # self.includeBut.connect("clicked", self.on_includeBut_clicked)
            # self.includeWrapper.pack_start(self.includeBut,False,False,0)
            # self.includeEntry = Gtk.Entry()
            # self.includeEntry.set_text("<Enter String>")
            # self.includeWrapper.pack_start(self.includeEntry,True,True,0)


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
            self.customName.set_text("<Name of filter>")
            self.box.pack_start(self.customName, False, False, 0)
            self.butCreate = Gtk.Button(label="Create|Apply Filter")
            self.butCreate.connect("clicked", self.on_butCreate_clicked)
            self.box.pack_start(self.butCreate,False,False,0)
            self.butReset = Gtk.Button(label="Reset Filter")
            self.butReset.connect("clicked",self.on_butReset_clicked)
            self.box.pack_start(self.butReset,False,False,0)
            
            return vbox
            
        def on_butCreate_clicked(self, widget):
            print("Applying Filter!")
        def on_butReset_clicked(self, widget):
            print("Resetting FIlter!")
        def on_includeBut_clicked(self, widget):
            print("Including!") 
        def on_excludeBut_clicked(self, widget):
            print("Including!") 
        def on_addFilter_clicked(self, widget):
            selected = self.expLists.getSelected()
            print(selected[0])
            row = FilterRow(self.listbox,selected[0],selected[1])
            self.listbox.add(row.getRow())
            self.listbox.show_all()    

