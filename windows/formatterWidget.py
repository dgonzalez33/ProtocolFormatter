import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows.filterList import FilterList
from windows.formatterRow import FormatterRow
from FormatterSub.Formatter import Formatter
from FormatterSub.Rule import Rule
from FormatterSub.HidingAction import HidingAction

class FormatterWidget:
        def __init__(self,formatterApplied):
            self.formatterApplied = formatterApplied
            
        def create_widget(self):
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            self.formatterList = list()
            self.ruleList = list()
            self.actionList = {}
            self.currentSelected = -1
            self.formatters = list()
            self.filter = None
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
        def set_filter(self, filter):
            self.filter = filter
        def update_actions(self):

            if(self.currentSelected >=0):
                  for i in range(0, len(self.actionsListbox)):
                         self.actionsListbox.remove(self.actionsListbox.get_row_at_index(i))
                  formatter = self.formatters[self.currentSelected]
                  for key in self.actionList.keys():
                        if(formatter.get_name() == key):
                              index = 0
                              print(self.actionList[key])
                              for action in self.actionList[key]:
                                    row = FormatterRow(self.actionsListbox, type(action).__name__,self.actionList[key], index )
                                    index += 1
                                    self.actionsListbox.add(row.getRow())
                  self.actionsListbox.show_all()
        def set_action_list(self, actionList):
            self.actionList = actionList
            self.update_actions()
        def formatter_select(self, list_box, row):
            self.currentSelected = row.get_index()
            print(self.currentSelected)
            ruleString = self.formatters[row.get_index()].get_rules_in_string()
            self.ruleList = self.formatters[row.get_index()].get_rules()
            ruleIndex = 0
            for i in range(0, len(self.rulesListbox)):
                   self.rulesListbox.remove(self.rulesListbox.get_row_at_index(i))
            for rs in ruleString:
                  row = FormatterRow(self.rulesListbox,rs,self.ruleList, ruleIndex)
                  self.rulesListbox.add(row.getRow())
                  ruleIndex+=1
            self.rulesListbox.show_all()
            self.update_actions()
        def set_pdmlman(self, pdmlman):
            self.personalman = pdmlman
            protocols = self.personalman.get_all_protocol_names()
#             for i in range(0, len(self.appliedlistbox)):
#                          #self.appliedlistbox.remove(self.appliedlistbox.get_row_at_index(i))
            for proto in protocols:
                  self.formatters.append(Formatter(self.personalman,proto))
                  row = FormatterRow(self.appliedlistbox,proto,self.formatterList,-1)
                  self.appliedlistbox.add(row.getRow())
            self.appliedlistbox.show_all() 
        def on_Apply_clicked(self, widget):
            if(self.currentSelected >=0):
                  self.formatters[self.currentSelected].applyFormatter()
                  for i in range(0,len(self.formatters[self.currentSelected].get_rules())):
                        print(i)
                        self.formatterApplied.append(self.formatters[self.currentSelected])

        def on_Create_clicked(self, widget):

            if(self.currentSelected >=0):
                  nxtRule = Rule()
                  if(self.filter == None):
                        nxtRule.setFilter("","","")
                  else:
                        filterSet = self.filter.get_filter()
                        nxtRule.setFilter(filterSet[0],filterSet[1],filterSet[2])
                  for acts in self.actionList[self.formatters[self.currentSelected].get_name()]:
                        nxtRule.addAction(acts)
                  self.formatters[self.currentSelected].addRule(nxtRule)
                  ruleString = self.formatters[self.currentSelected].get_rules_in_string()
                  row = FormatterRow(self.rulesListbox,ruleString[-1],self.ruleList, len(ruleString)-1)
                  self.rulesListbox.add(row.getRow())
                  self.rulesListbox.show_all()

                  for i in range(0, len(self.actionsListbox)):
                         self.actionsListbox.remove(self.actionsListbox.get_row_at_index(i))
                         self.actionList[self.formatters[self.currentSelected].get_name()].pop()

        def on_Delete_clicked(self, widget):
            for i in range(0, len(self.actionsListbox)):
                  self.actionsListbox.remove(self.actionsListbox.get_row_at_index(i))
                  self.actionList[self.formatters[self.currentSelected].get_name()].pop()
