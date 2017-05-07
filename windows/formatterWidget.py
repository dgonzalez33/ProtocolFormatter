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
            appliedFormattersLabel.set_alignment(xalign=0.5, yalign=0) 
            self.appliedscrollContainer = Gtk.ScrolledWindow()
            appliedFormattersContainer.pack_start(appliedFormattersLabel,True,True,0)
            appliedFormattersContainer.pack_start(self.appliedscrollContainer,True,True,0)
            self.appliedscrollContainer.add(filterContainer)
            self.listbox = Gtk.ListBox()
            self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
            filterContainer.pack_start(self.listbox,True,True,0)


            rulesContainer = Gtk.Box(spacing=6)
            appliedRulesLabel = Gtk.Label()
            appliedRulesLabel.set_markup("<b>Applied Rules</b>")
            appliedRulesLabel.set_alignment(xalign=0.5, yalign=0)
            self.rulesscrollContainer = Gtk.ScrolledWindow()
            appliedFormattersContainer.pack_start(appliedRulesLabel, False, False,0)
            appliedFormattersContainer.pack_start(self.rulesscrollContainer,True,True,0)
            self.rulesscrollContainer.add(rulesContainer)
            self.rulesListbox = Gtk.ListBox()
            self.rulesListbox.set_selection_mode(Gtk.SelectionMode.NONE)
            rulesContainer.pack_start(self.rulesListbox, True, True, 0)
            
            
            actionContainer = Gtk.Box(spacing=6)
            actionsLabel = Gtk.Label()
            actionsLabel.set_markup("<b>Construction of new Rule with Filter A</b>")
            actionsLabel.set_alignment(xalign=0.5, yalign=0)
            self.actionsscrollContainer = Gtk.ScrolledWindow()
            appliedFormattersContainer.pack_start(actionsLabel, False, False,0)
            appliedFormattersContainer.pack_start(self.actionsscrollContainer,True,True,0)
            self.actionsscrollContainer.add(actionContainer)
            self.actionsListbox = Gtk.ListBox()
            self.actionsListbox.set_selection_mode(Gtk.SelectionMode.NONE)
            actionContainer.pack_start(self.actionsListbox, True, True, 0)

#             conRule = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
#             vbox.pack_start(conRule,False,False,0)
#             conLabel = Gtk.Label()
#             conLabel.set_markup("<b>Construction of new Rule with Filter A</b>")
#             conLabel.set_alignment(xalign=0, yalign=1) 
#             conRule.pack_start(conLabel,False,True,0)
#             actionEx = Gtk.Label()
#             actionEx.set_markup("Action 3.1")
#             actionEx.set_alignment(xalign=0, yalign=1) 
#             conRule.pack_start(actionEx,False,True,0)
#             actionEx2 = Gtk.Label()
#             actionEx2.set_markup("Action 3.2")
#             actionEx2.set_alignment(xalign=0, yalign=1) 
#             conRule.pack_start(actionEx2,False,True,0)
#             buttonCont = Gtk.Box(spacing=6)
#             vbox.pack_start(buttonCont,False,True,0)
#             createRule = Gtk.Button(label="Create Rule")
#             buttonCont.pack_start(createRule,False,True,0)
#             deleteRule = Gtk.Button(label="Delete Rule")
#             buttonCont.pack_start(deleteRule,True,True,0)

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
            row = FilterRow(self.listbox,selected[0],selected[1],list())
            self.listbox.add(row.getRow())
            self.listbox.show_all()    

