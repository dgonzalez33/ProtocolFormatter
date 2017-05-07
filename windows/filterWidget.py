import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows.filterList import FilterList
from windows.filterRow import FilterRow
from FormatterSub.Filter import Filter
from windows.packetWidget import PacketWidget

class FilterWidget:

        def __init__(self):
            self.filterlist = []
            self.bpf = ""
            self.packetwidget = PacketWidget()
            
        def set_packet_widget(self, pwidget):
            self.packetwidget = pwidget

        def create_widget(self):
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            self.model_filter = Filter()
            bpfContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(bpfContainer,True,True,0)
            filterContainer = Gtk.Box(spacing=6)
            bpfLabel = Gtk.Label()
            bpfLabel.set_markup("<b>BPF Filter</b>")
            bpfLabel.set_alignment(xalign=0, yalign=0) 
            bpfContainer.pack_start(bpfLabel,False,False,0)
            bpfContainer.pack_start(filterContainer,True,True,0)
            self.expLists = FilterList()
            filterContainer.pack_start(self.expLists.getList(),True,True,0)
            self.filters = list()
            addFilter = Gtk.Button("->")
            addFilter.connect("clicked",self.on_addFilter_clicked)
            filterContainer.pack_start(addFilter,False,False,1)

            self.listbox = Gtk.ListBox()
            self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
            filterContainer.pack_start(self.listbox,True,True,0)
            self.context = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(self.context,False,False,0)
            contextLabel = Gtk.Label()
            contextLabel.set_markup("<b>Context FIlter</b>")
            contextLabel.set_alignment(xalign=0, yalign=1) 
            self.context.pack_start(contextLabel,False,False,0)
            self.includeWrapper = Gtk.Box(spacing=6)
            self.context.pack_start(self.includeWrapper,False,False,0)
            self.includeBut = Gtk.Button(label="Include")
            self.includeBut.connect("clicked", self.on_includeBut_clicked)
            self.includeWrapper.pack_start(self.includeBut,False,False,0)
            self.includeEntry = Gtk.Entry()
            self.includeEntry.set_text("<Enter String>")
            self.includeWrapper.pack_start(self.includeEntry,True,True,0)
            self.excludeWrapper = Gtk.Box(spacing=6)
            self.context.pack_start(self.excludeWrapper,False,False,0)
            self.excludeBut = Gtk.Button(label="Exclude")
            self.excludeBut.connect("clicked", self.on_excludeBut_clicked)
            self.excludeWrapper.pack_start(self.excludeBut,False,False,0)
            self.excludeEntry = Gtk.Entry()
            self.excludeEntry.set_text("<Enter String>")
            self.excludeWrapper.pack_start(self.excludeEntry,True,True,0)

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
        def askForValue(self):
            askWindow = Gtk.Window()
            askWindow.set_size_request(150, 75)
            askWindow.set_keep_above(True)
            valueWrapper = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            askWindow.connect("delete-event", Gtk.main_quit)
            self.valueEntry = Gtk.Entry()
            self.valueEntry.set_text("Value")
            button = Gtk.Button(label="Value")
            button.connect("clicked", self.finish)
            valueWrapper.pack_start(self.valueEntry,False,False,0)
            valueWrapper.pack_start(button,False,False,0)
            askWindow.add(valueWrapper)
            askWindow.show_all()
            Gtk.main()

        def finish(self,widget):
                self.primValue = self.valueEntry.get_text()
                row = FilterRow(self.listbox,self.expLists.getSelected()[0],self.primValue,self.filters)
                self.listbox.add(row.getRow())
                self.listbox.show_all()   
        def set_pdmlman(self, pdmlman):
            self.personalman = pdmlman
        def get_filter_list(self):
            return self.filterlist
        def get_filter(self):
            return self.bpf
        def on_butCreate_clicked(self, widget):
            first = True
            for row in self.filters:
                line = row[0] + " " + row[1]
                if(first):
                    self.bpf += line
                    first = False
                else:
                        self.bpf += " "+line
            print(self.bpf)
            print(self.model_filter)
            self.model_filter.set_pdmlman(self.personalman)
            self.model_filter.set_bpf_filter(self.bpf, "","")
            self.model_filter.saveFilter(self.customName.get_text())
            self.model_filter.applyFilter()
            self.filterlist = self.model_filter.getViewProtos()
            print(self.filterlist)
            self.packetwidget.set_filter_list(self.filterlist)
            print("Applying Filter!")
        def on_butReset_clicked(self, widget):
            self.includeEntry.set_text("")
            self.packetwidget.clear_filter_list()
            self.excludeEntry.set_text("")
            for row in self.listbox:
                self.listbox.remove(row)
        def on_includeBut_clicked(self, widget):
            print("Including!") 
        def on_excludeBut_clicked(self, widget):
            print("Including!") 
        def on_addFilter_clicked(self, widget):
            selected = self.expLists.getSelected()
            if(selected[1] == "Type"):
                self.askForValue()
            else:
                row = FilterRow(self.listbox,selected[0],selected[1],self.filters)
                self.listbox.add(row.getRow())
                self.listbox.show_all()    