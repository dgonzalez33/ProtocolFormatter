#Command line widget
#python 3.5
import gi
import difflib
import sys
#from difflib_data import *
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class HistoricalCopyWidget:

    def __init__(self):
        self.liststore = Gtk.ListStore(str, str, str)
        self.listofiterators = []
        self.resulting_lines = []
        

    def create_widget(self):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            
        appliedFormattersContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        self.label = Gtk.Label()
        self.label.set_text("")
        self.label.show()
        
        submitbutton = Gtk.Button("Show/Hide Only Difference")
        submitbutton.connect("clicked", self.update_filter)
        submitbutton.show()
        
        appliedFormattersContainer.add(self.label)
        appliedFormattersContainer.add(submitbutton)
        vbox.pack_start(appliedFormattersContainer,True,True,0)
        filterContainer = Gtk.Box(spacing=0)
        self.scrollContainer = Gtk.ScrolledWindow()
        
        appliedFormattersContainer.pack_start(self.scrollContainer,True,True,0)
        
        restorebutton = Gtk.Button("Restore Original")
        restorebutton.connect("clicked", self.restore_orig)
        restorebutton.show()
        appliedFormattersContainer.add(restorebutton)
        
        self.current_filter_language = None
        
        self.language_filter = self.liststore.filter_new()
        self.language_filter.set_visible_func(self.language_filter_func)
        
        self.treeview = Gtk.TreeView()
        self.sorted = Gtk.TreeModelSort(self.language_filter)
        self.treeview.set_model(self.sorted)
        
        tree_selection = self.treeview.get_selection()
        tree_selection.set_mode(Gtk.SelectionMode.MULTIPLE)
        tree_selection.connect("changed", self.packet_tree_clicked)
        
        self.add_columns_to_list("Historical Difference", 0, 0) 

        frame = Gtk.Frame()
        frame.add(filterContainer)
        
        self.scrollContainer.add(self.treeview)
        
        return vbox
    
    def update_label(self, value):
        self.label.set_text(value)
    
    def language_filter_func(self, model, iter, data):
        if self.current_filter_language is None or self.current_filter_language == "None":
            return True
        else:
            return model[iter][2] == self.current_filter_language
        
    def packet_tree_clicked(self, tree_selection):
#             print(tree_selection)
        (model, pathlist) = tree_selection.get_selected_rows()
        for path in pathlist :
            tree_iter = model.get_iter(path)
            value = model.get_value(tree_iter,0)
            print(value)

        

    def add_columns_to_list(self, name, num, s_id):
        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn(name, renderer_text, text=num, foreground=1) 
        column_text.set_clickable(True)
        column_text.set_sort_column_id(s_id)
        self.treeview.append_column(column_text)
        
    def add_to_list(self):
        x = 0
        y=0
        prev = 0
        triggernextline = 0
        while(x < len(self.resulting_lines)):
            self.templist = []
            curstr = self.resulting_lines[x]
            if(curstr != ""):
                if(curstr[0][0] == '+'):
                   
                    self.liststore.append(["("+str(y)+")"+self.resulting_lines[x], '#00FF00', "True"])
                elif(curstr[0][0] == '-'):
                    
                    y+=1
                    self.liststore.append(["("+str(y)+")"+self.resulting_lines[x], '#FF0000', "True"])
                elif(curstr[0][0] == '?'):
                    self.liststore.append(["("+str(y)+")"+self.resulting_lines[x], '#FFFF00', "True"])
                    
                    prev = y
                else:
                    y+=1
                    self.liststore.append(["("+str(y)+")"+self.resulting_lines[x], '#FFFFFF', "False"])
            x+=1
    def refilter_list(self):
        print("%s language selected!" % self.current_filter_language)
        self.language_filter.refilter()    
    
    def add_column(self, colname):
        self.linecolumn = Gtk.TreeViewColumn()
        self.linecolumn.set_title(colname)
    
    def set_wiget_labels(self, firstfilename, secondfilename):
        self.filelabel.set_text(firstfilename)
        self.originallabel.set_text(secondfilename)
        
    def update_filter(self, stuff):
        if(self.current_filter_language == None):
            self.current_filter_language = "True"
            self.refilter_list()
            return
        if(self.current_filter_language == "True"):
            self.current_filter_language = None
            self.refilter_list()
            return
    def restore_orig(self, stuff):   
        print("restore was pressed") 
        
    def clear_list(self):
        self.liststore.clear()   
        
    def create_historical_copy(self, file1path, file2path):
        file1 = open(file1path , "r")
        file2 = open(file2path , "r")
        line1 = file1.readlines()
        line2 = file2.readlines()
        d = difflib.Differ()
        diff = d.compare(line2, line1)
        self.result = ""
        self.result = ''.join(diff)
        self.resulting_lines = self.result.split('\n')
        self.clear_list()
        self.add_to_list()


