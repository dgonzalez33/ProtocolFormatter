import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from scriptWidget import ScriptWidget
from FilterBarWidget import FilterBarWidget
from filterWidget import FilterWidget
from hookWidget import HookWidget
from CommandLineWidget import CommandLineWidget
from HistoricalCopyWidget import HistoricalWidget
from editorWidget import EditorWidget
from packetWidget import PacketWidget
from formatterWidget import FormatterWidget
from CommandLineWidget import CommandLineWidget
from HistoricalCopyWidget import HistoricalCopyWidget
from menuBar import menuBar
from iconBar import iconBar

"""
Because our windows need to be customizable 
we have a Windowcontroller
With this controller we can create 
a window with a widget or multiple widgets 
"""
class WindowController:
    
    """
    The __init__ constructor is currently being used 
    as a way to start our windows but we should only 
    construct the default window here in the future 
    Other windows will be created via button press 
    """
    def __init__(self):
        self.create_default_window()
#         self.create_script_window()
#         self.create_filter_window()
#         self.create_editor_window()

    
    """
    This function creates the default window
    by combining 5 widget in 4 containers 
    """
    def create_default_window(self):

	# create main window
        self.window_main = Gtk.Window()
        self.title = "Protocol Formatter System"
        self.window_main.set_title(self.title)
        self.window_main.set_size_request( 1000, 500)
        self.window_main.connect("destroy", self.destroy)
        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        self.menu_bar = Gtk.MenuBar()

	# create file drop down menu
        file_menu = Gtk.Menu()
           
	# begin creating items for the drop down menu 
        open_item = Gtk.MenuItem("Open")
        open_item.connect_object("activate",self.on_Open_clicked, "open")

        save_item = Gtk.MenuItem("Save")

        close_item = Gtk.MenuItem("Close")
        
	# insert items into the drop down menu
        file_menu.append(open_item)
        file_menu.append(save_item)
        file_menu.append(close_item)
        
        open_item.show()
        save_item.show()
        close_item.show()
        
	# create edit drop down menu
        edit_menu = Gtk.Menu()
            
	# begin creating items for the drop down menu
        undo_item = Gtk.MenuItem("Undo")

        redo_item = Gtk.MenuItem("Redo")

        copy_item = Gtk.MenuItem("Copy")

        cut_item = Gtk.MenuItem("Cut")

        paste_item = Gtk.MenuItem("Paste")

        restore_item = Gtk.MenuItem("Restore")
        
	# insert items into the drop down menu
        edit_menu.append(undo_item)
        edit_menu.append(redo_item)
        edit_menu.append(copy_item)
        edit_menu.append(cut_item)
        edit_menu.append(paste_item)
        edit_menu.append(restore_item)
        
        undo_item.show()
        redo_item.show()
        copy_item.show()
        cut_item.show()
        paste_item.show()
        restore_item.show()
        
        # create window drop down menu
        window_menu = Gtk.Menu()

	# begin creating items for the drop down menu            
        filter_item = Gtk.MenuItem("Filter")
        filter_item.connect("activate",self.create_filter_window)

        editor_item = Gtk.MenuItem("Editor")
        editor_item.connect("activate",self.create_editor_window)

        script_item = Gtk.MenuItem("Script")
        script_item.connect("activate",self.create_script_window)

        hook_item = Gtk.MenuItem("Hook")
        hook_item.connect("activate",self.create_hook_window)

        commandline_item = Gtk.MenuItem("CommandLine")
	commandline_item.connect("activate",self.create_commandline_window)

        historical_item = Gtk.MenuItem("Historical")
	historical_item.connect("activate", self.create_historical_window)

	# insert items into the drop down menu        
        window_menu.append(filter_item)
        window_menu.append(editor_item)
        window_menu.append(script_item)
        window_menu.append(hook_item)
        window_menu.append(commandline_item)
        window_menu.append(historical_item)
        
        filter_item.show()
        editor_item.show()
        script_item.show()
        hook_item.show()
        commandline_item.show()
        historical_item.show()
        
        # insert drop down menus into the menu bar
        file_root = Gtk.MenuItem("File")
        edit_root = Gtk.MenuItem("Edit")
        window_root = Gtk.MenuItem("Window")
        help_root = Gtk.MenuItem("Help")
        
        file_root.show()
        edit_root.show()
        window_root.show()
        help_root.show()
        
        file_root.set_submenu(file_menu)
        edit_root.set_submenu(edit_menu)
        window_root.set_submenu(window_menu)
        
        self.window_main.add(self.mainbox)
        self.mainbox.show()
        
        menu_bar = Gtk.MenuBar()
        self.mainbox.pack_start(menu_bar, False, False, 0)
        
        menu_bar.show()
        
        menu_bar.append(file_root)
        menu_bar.append(edit_root)
        menu_bar.append(window_root)
        menu_bar.append(help_root)

	# Create icon bar  
        second_widget = iconBar().create_widget()
        second_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.insert_widget_to_Frame("<Mode of Operation>", second_widget,
                                    second_container, self.mainbox)
         
        third_widget = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        third_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.insert_widget_to_Frame("Filter Bar",third_widget,
                                    third_container, self.mainbox)
         
        fourth_widget = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        fourth_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.insert_widget_to_Frame("Packet Window", fourth_widget, 
                                    fourth_container, self.mainbox)
         
        fifth_widget = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.insert_widget_to_Frame("Formatter Window",fifth_widget,
                                    fourth_container, self.mainbox)
#         
        self.window_main.show_all()
    
    """
    create stand alone widget windows 
    by declaring a function like these 
    """
    def create_editor_window(self, widget):
        self.editorbox = EditorWidget().create_widget()
        self.insert_widget_to_window("Editor Window", self.editorbox)
            
    def create_script_window(self, widget):
        self.scriptbox = ScriptWidget().create_widget()
        self.insert_widget_to_window("Script Window", self.scriptbox)
        
    def create_filter_window(self, widget):
        self.filterbox = FilterWidget().create_widget()
        self.insert_widget_to_window("Filter Window", self.filterbox)

    def create_hook_window(self, widget):
        self.hookbox = HookWidget().create_widget()
        self.insert_widget_to_window("Hook Window", self.hookbox)

    def create_commandline_window(self,widget):
	self.commandbox = CommandLineWidget().create_widget()
	self.insert_widget_to_window("Command Line Window", self.commandbox)

    def create_historical_window(self,widget):
	self.historybox = HistoricalWidget().create_widget()
	self.insert_widget_to_window("Historical Copy Window", self.historybox)



    def on_Open_clicked(self, widget):
            print("Open was clicked")
        
    def main(self):
        Gtk.main()
        
    def destroy(self, w):
        #Gtk.main_quit()
        print("destroyed! \m/")
    
    """
    Given a widget, we can place 
    it on a window on a default frame
    """
    def insert_widget_to_window(self, windowtitle, widget):
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        window= Gtk.Window()
        title = windowtitle
        window.set_title(title)
        window.set_size_request( 500, 350)
        window.connect("destroy", self.destroy)
        window.add(vbox)
        first_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.insert_widget_to_Frame(windowtitle, widget, 
                                    first_container, vbox)
        window.show_all()
    """
    Given a widget and a particular container and window
    we can create more complicated windows 
    """
    def insert_widget_to_Frame(self,label, vbox,frameContainer, wbox):
        
        wbox.pack_start(frameContainer, True, True, 6)
        frame = Gtk.Frame()
        frame.set_label(label)
        frame.set_label_align( 0.5, 0)
        frame.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
        frame.show()
        v_widget = vbox
        frame.add(v_widget)
        frameContainer.pack_start(frame, True, True, 0)
        v_widget.show()
    
if(__name__ == "__main__"):
    d = WindowController()
    d.main()

