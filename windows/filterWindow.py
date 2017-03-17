import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

software_list = [("eth.addr", 'Ethernet'),
                 ('eth.dst', 'Ethernet'),
                 ('eth.len', 'Ethernet'),
                 ('arp.dst.hw_mac', 'ARP'),
                 ('arp.hw.size', 'ARP'),
                 ('ip.addr', 'IPv4'),
                 ('ip.checksum', 'IPv4'),
                 ('ipv6.addr', 'IPv6'),
                 ('ipv6.class', 'IPv6'),
                 ('tcp.ack', 'TCP'),
                 ('tcp.len', 'TCP')]

class FilterWindow(Gtk.Window):

        def __init__(self):
                Gtk.Window.__init__(self, title="Filter Window")
             # self.set_size_request(200, 100)
                vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                self.add(vbox)

                bpfContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                vbox.pack_start(bpfContainer,True,True,0)
                filterContainer = Gtk.Box()

                bpfLabel = Gtk.Label()
                bpfLabel.set_markup("<b>BPF Filter</b>")
                bpfLabel.set_alignment(xalign=0, yalign=1) 
                bpfContainer.pack_start(bpfLabel,True,True,0)
                bpfContainer.pack_start(filterContainer,True,True,0)

                 #Setting up the self.grid in which the elements are to be positionned
                self.grid = Gtk.Grid()
                self.grid.set_column_homogeneous(True)
                self.grid.set_row_homogeneous(True)
                filterContainer.pack_start(self.grid,True,True,0)

                #Creating the ListStore model
                self.software_liststore = Gtk.ListStore(str, str)
                for software_ref in software_list:
                    self.software_liststore.append(list(software_ref))
                self.current_filter_language = None

                #Creating the filter, feeding it with the liststore model
                self.language_filter = self.software_liststore.filter_new()
                #setting the filter function, note that we're not using the
                # self.language_filter.set_visible_func(self.language_filter_func)

                #creating the treeview, making it use the filter as a model, and adding the columns
                self.treeview = Gtk.TreeView.new_with_model(self.language_filter)
                for i, column_title in enumerate(["Filter/Expression","Protocol"]):
                    renderer = Gtk.CellRendererText()
                    column = Gtk.TreeViewColumn(column_title, renderer, text=i)
                    self.treeview.append_column(column)

                #setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
                self.scrollable_treelist = Gtk.ScrolledWindow()
                self.scrollable_treelist.set_vexpand(True)
                self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
                self.scrollable_treelist.add(self.treeview)
                self.show_all()

                 # an image widget to contain the pixmap
                image = Gtk.Image()
                image.set_from_file("../images/arrow.png")
                image.show()   
              # a button to contain the image widge
                addFilter = Gtk.Button()
                addFilter.add(image)
                addFilter.connect("clicked",self.on_addFilter_clicked)
                filterContainer.pack_start(addFilter,True,True,0)

                listbox = Gtk.ListBox()
                listbox.set_selection_mode(Gtk.SelectionMode.NONE)
                filterContainer.pack_start(listbox,True,True,0)
                row = Gtk.ListBoxRow()

                expression = Gtk.Box(spacing=6)
                field = Gtk.Label()
                field.set_text("Proto")
                value = Gtk.Label()
                value.set_text("tcp")
                delete = Gtk.Button("X")
                expression.pack_start(field,True,True,0)
                expression.pack_start(value,True,True,0)
                expression.pack_start(delete,True,True,0)
                row.add(expression)
                listbox.add(row)

                self.context = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                vbox.pack_start(self.context,True,True,0)
                contextLabel = Gtk.Label()
                contextLabel.set_markup("<b>Context FIlter</b>")
                contextLabel.set_alignment(xalign=0, yalign=1) 
                self.context.pack_start(contextLabel,True,True,0)
                self.includeWrapper = Gtk.Box(spacing=6)
                self.context.pack_start(self.includeWrapper,True,True,0)
                self.includeBut = Gtk.Button(label="Include")
                self.includeBut.connect("clicked", self.on_includeBut_clicked)
                self.includeWrapper.pack_start(self.includeBut,True,True,0)
                self.includeEntry = Gtk.Entry()
                self.includeEntry.set_text("<Enter String>")
                self.includeWrapper.pack_start(self.includeEntry,True,True,0)


                self.excludeWrapper = Gtk.Box(spacing=6)
                self.context.pack_start(self.excludeWrapper,True,True,0)
                self.excludeBut = Gtk.Button(label="Exclude")
                self.excludeBut.connect("clicked", self.on_excludeBut_clicked)
                self.excludeWrapper.pack_start(self.excludeBut,True,True,0)
                self.excludeEntry = Gtk.Entry()
                self.excludeEntry.set_text("<Enter String>")
                self.excludeWrapper.pack_start(self.excludeEntry,True,True,0)

                self.box = Gtk.Box(spacing=6)
                vbox.pack_start(self.box,True,True,0)
                customLabel = Gtk.Label("Custom Name: ")
                self.box.pack_start(customLabel,True,True,0)
                self.customName = Gtk.Entry()
                self.customName.set_text("<Name of filter>")
                self.box.pack_start(self.customName, True, True, 0)
                self.butCreate = Gtk.Button(label="Create|Apply Filter")
                self.butCreate.connect("clicked", self.on_butCreate_clicked)
                self.box.pack_start(self.butCreate,True,True,0)
                self.butReset = Gtk.Button(label="Reset Filter")
                self.butReset.connect("clicked",self.on_butReset_clicked)
                self.box.pack_start(self.butReset,True,True,0)
        def on_butCreate_clicked(self, widget):
                print("Applying Filter!")
        def on_butReset_clicked(self, widget):
            print("Resetting FIlter!")
        def on_includeBut_clicked(self, widget):
            print("Including!") 
        def on_excludeBut_clicked(self, widget):
            print("Including!") 
        def on_addFilter_clicked(self, widget):
            print("Adding Filter!")   

win = FilterWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()