import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows.filterList import FilterList
from windows.filterRow import FilterRow

class FormatterWidget:

        
            
        def create_widget(self):
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            appliedFormattersContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(appliedFormattersContainer,True,True,0)
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

            # self.context = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            # vbox.pack_start(self.context,False,False,0)
            # contextLabel = Gtk.Label()
            # contextLabel.set_markup("<b>Applied Rules for <Protocol X>Based on <Filter A> </b>")
            # contextLabel.set_alignment(xalign=0, yalign=1) 
            # self.context.pack_start(contextLabel,False,False,0)

            # appliedRulesContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            
            #vbox.pack_start(appliedFormattersContainer,True,True,0)
            RulesContainer = Gtk.Box(spacing=6)

            appliedRulesLabel = Gtk.Label()
            appliedRulesLabel.set_markup("<b>Applied Rules</b>")
            appliedRulesLabel.set_alignment(xalign=0, yalign=1)
            appliedFormattersContainer.pack_start(appliedRulesLabel, True, True,0)
            # appliedFormattersContainer.pack_start(appliedRulesContainer, True, True, 0)
            appliedFormattersContainer.pack_start(RulesContainer, True, True, 0)

            self.rulesListbox = Gtk.ListBox()
            self.rulesListbox.set_selection_mode(Gtk.SelectionMode.NONE)
            RulesContainer.pack_start(self.rulesListbox, True, True, 0)
            Rulerow = FilterRow(self.listbox,"Rule","action")
            self.rulesListbox.add(Rulerow.getRow())

            conRule = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(conRule,False,False,0)
            conLabel = Gtk.Label()
            conLabel.set_markup("<b>Construction of new Rule with Filter A</b>")
            conLabel.set_alignment(xalign=0, yalign=1) 
            conRule.pack_start(conLabel,False,False,0)
            actionEx = Gtk.Label()
            actionEx.set_markup("Action 3.1")
            actionEx.set_alignment(xalign=0, yalign=1) 
            conRule.pack_start(actionEx,False,False,0)
            actionEx2 = Gtk.Label()
            actionEx2.set_markup("Action 3.2")
            actionEx2.set_alignment(xalign=0, yalign=1) 
            conRule.pack_start(actionEx2,False,False,0)
            buttonCont = Gtk.Box(spacing=6)
            vbox.pack_start(buttonCont,False,False,0)
            createRule = Gtk.Button(label="Create Rule")
            buttonCont.pack_start(createRule,False,False,0)
            deleteRule = Gtk.Button(label="Delete Rule")
            buttonCont.pack_start(deleteRule,False,False,0)

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

