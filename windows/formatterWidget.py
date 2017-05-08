import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows.filterList import FilterList
from windows.formatterRow import FormatterRow
from FormatterSub.Formatter import Formatter
from FormatterSub.Rule import Rule
from FormatterSub.HidingAction import HidingAction

class FormatterWidget:

        
            
        def create_widget(self):
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            self.formatterList = list()
            self.ruleList = list()
            self.actionList = list()
            self.currentSelected = -1
            self.formatters = list()
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
            self.appliedlistbox = Gtk.ListBox()
            self.appliedlistbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
            self.appliedlistbox.connect("row-selected",self.formatter_select)
            filterContainer.pack_start(self.appliedlistbox,True,True,0)

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
            actionsLabel.set_markup("<b>Construction of new Rule</b>")
            actionsLabel.set_alignment(xalign=0.5, yalign=0)
            self.actionsscrollContainer = Gtk.ScrolledWindow()
            appliedFormattersContainer.pack_start(actionsLabel, False, False,0)
            appliedFormattersContainer.pack_start(self.actionsscrollContainer,True,True,0)
            self.actionsscrollContainer.add(actionContainer)
            self.actionsListbox = Gtk.ListBox()
            self.actionsListbox.set_selection_mode(Gtk.SelectionMode.NONE)
            actionContainer.pack_start(self.actionsListbox, True, True, 0)

            buttonCont = Gtk.Box(spacing=6)
            vbox.pack_start(buttonCont,False,True,0)
            applyRule = Gtk.Button(label="Apply Formatter")
            applyRule.connect("clicked", self.on_Apply_clicked)
            buttonCont.pack_start(applyRule,False,True,0)
            createRule = Gtk.Button(label="Create Rule")
            createRule.connect("clicked", self.on_Create_clicked)
            buttonCont.pack_start(createRule,False,True,0)
            deleteRule = Gtk.Button(label="Delete Rule")
            deleteRule.connect("clicked", self.on_Delete_clicked)
            buttonCont.pack_start(deleteRule,True,True,0)

            return vbox
        def formatter_select(self, list_box, row):
            self.currentSelected = row.get_index()
            print(self.currentSelected)
            ruleString = self.formatters[row.get_index()].get_rules_in_string()
            self.ruleList = self.formatters[row.get_index()].get_rules()
            ruleIndex = 0
            for rs in ruleString:
                  row = FormatterRow(self.rulesListbox,rs,self.ruleList, ruleIndex)
                  self.rulesListbox.add(row.getRow())
                  ruleIndex+=1
            self.rulesListbox.show_all()
        def set_pdmlman(self, pdmlman):
            self.personalman = pdmlman
            protocols = self.personalman.get_all_protocol_names()
            for proto in protocols:
                  self.formatters.append(Formatter(self.personalman,proto))
                  row = FormatterRow(self.appliedlistbox,proto,self.formatterList,-1)
                  self.appliedlistbox.add(row.getRow())
            self.appliedlistbox.show_all() 
        def on_Apply_clicked(self, widget):
            if(self.currentSelected >=0):
                  
                  self.formatters[self.currentSelected].applyFormatter()
            
        def on_Create_clicked(self, widget):
            if(self.currentSelected >=0):
                  nxtRule = Rule()
                  nxtact = HidingAction("True", "ip.id")
                  nxtRule.setFilter("ip src net 192 or tcp","","")
                  nxtRule.addAction(nxtact)
                  self.formatters[self.currentSelected].addRule(nxtRule)
                  ruleString = self.formatters[self.currentSelected].get_rules_in_string()
                  row = FormatterRow(self.rulesListbox,ruleString[-1],self.ruleList, len(ruleString)-1)
                  self.rulesListbox.add(row.getRow())
                  self.rulesListbox.show_all()

        def on_Delete_clicked(self, widget):
            print("Deleting Rule!") 
