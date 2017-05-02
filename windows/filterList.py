import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

software_list = [("host","Type"),
                                ("net","Type"),
                                ("port","Type"),
                                ("portrange","Type"),
                                 ('src',"Dir"),
                                 ('dst',"Dir"),
                                 ('src and dst','Dir'),
                                 ('src or dst','Dir'),
                                 ('ether','Proto'),
                                ('fddi','Proto'),
                                ('tr','Proto'),
                                ('wlan','Proto'),
                                ('ip','Proto'),
                                ('ip6','Proto'),
                                ('arp','Proto'),
                                ('rarp','Proto'),
                                ('decnet','Proto'),
                                ('tcp','Proto'),
                                ('udp','Proto')]
class FilterList():
    def __init__(self):
        #Setting up the self.grid in which the elements are to be positionned
            self.grid = Gtk.Grid()
            self.grid.set_column_homogeneous(True)
            self.grid.set_row_homogeneous(True)

            #Creating the ListStore model
            software_liststore = Gtk.ListStore(str, str)
            for software_ref in software_list:
                    software_liststore.append(list(software_ref))
            current_filter_language = None

            #Creating the filter, feeding it with the liststore model
            language_filter = software_liststore.filter_new()
            #setting the filter function, note that we're not using the
            # self.language_filter.set_visible_func(self.language_filter_func)

            #creating the treeview, making it use the filter as a model, and adding the columns
            treeview = Gtk.TreeView.new_with_model(language_filter)
            for i, column_title in enumerate(["Primitive","Qualifier"]):
                    renderer = Gtk.CellRendererText()
                    column = Gtk.TreeViewColumn(column_title, renderer, text=i)
                    treeview.append_column(column)

            #setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
            scrollable_treelist = Gtk.ScrolledWindow()
            scrollable_treelist.set_vexpand(True)
            self.grid.attach(scrollable_treelist, 0, 0, 8, 10)
            scrollable_treelist.add(treeview)
            tree_selection = treeview.get_selection()
            def onSelectionChanged(tree_selection):
                (model, pathlist) = tree_selection.get_selected_rows()
                for path in pathlist :
                    tree_iter = model.get_iter(path)
                    value = model.get_value(tree_iter,0)
                    value2 = model.get_value(tree_iter,1)
                    self.selected = [value, value2]
            tree_selection.connect("changed", onSelectionChanged)

    def getList(self):
        return self.grid
    def getSelected(self):
        return self.selected    
    

