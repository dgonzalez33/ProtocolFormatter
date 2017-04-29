import sys
from gi.overrides.Gtk import Window
sys.path.insert(0, '../')
import gi
from numpy import empty
from threading import Thread
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from windows.scriptWidget import ScriptWidget
from windows.filterWidget import FilterWidget
from windows.hookWidget import HookWidget
from windows.CommandLineWidget import CommandLineWidget
from windows.HistoricalCopyWidget import HistoricalCopyWidget
from windows.editorWidget import EditorWidget
from windows.packetWidget import PacketWidget
from windows.formatterWidget import FormatterWidget
from windows.menuBar import menuBar
from windows.iconBar import iconBar
from windows.FilterBarWidget import FilterBarWidget
from RestofSystem.Controller import controller

"""
Because our windows need to be customizable 
we have a Windowcontroller
With this controller we can create 
a window with a widget or multiple widgets 
"""

filterOpen = False
editorOpen = False
scriptOpen = False
hookOpen = False
commOpen = False
histOpen = False

class WindowController:
    
    
    """
    The __init__ constructor is currently being used 
    as a way to start our windows but we should only 
    construct the default window here in the future 
    Other windows will be created via button press 
    """


    def __init__(self):
        #external controller
        self.maincontroller = controller()
        
        #Dialog Window
        self.chosenfile = ""
        self.opendialog = Gtk.FileChooserDialog("Please choose a file", None,
                Gtk.FileChooserAction.OPEN,
                (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                 Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        
        #containers
        self.second_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.third_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.fourth_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

        #Widgets
        self.icon_widget = iconBar()
        self.filter_widget = FilterBarWidget()
        self.packet_widget = PacketWidget()
        self.formatter_widget = FormatterWidget()
        self.editor_widget = EditorWidget()
        self.script_widget = ScriptWidget()
        self.filter_widget = FilterWidget()
        self.filterbar_widget = FilterBarWidget()
        self.hook_widget = HookWidget()
        self.command_widget = CommandLineWidget()
        self.history_widget = HistoricalCopyWidget()
        
        #boxes
        self.icon_box = self.icon_widget.create_widget()
        self.filter_box = self.filter_widget.create_widget()
        self.packet_box = self.packet_widget.create_widget()
        self.formatter_box = self.formatter_widget.create_widget()
        self.editorbox = self.editor_widget.create_widget()
        self.scriptbox = self.script_widget.create_widget()
        self.filterbox = self.filter_widget.create_widget()
        self.filterbarbox = self.filterbar_widget.create_widget()
        self.hookbox = self.hook_widget.create_widget()
        self.commandbox = self.command_widget.create_widget()
        self.historybox = self.history_widget.create_widget()

        #Windows
        self.window_main = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.create_default_window()


    
    """
    This function creates the default window
    by combining 5 widget in 4 containers 
    """
    def create_default_window(self):


        #create main window
        self.title = "Protocol Formatter System"
        self.window_main.set_title(self.title)
        self.window_main.set_size_request( 1000, 800)
        self.window_main.connect("destroy", self.destroy)
        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        self.menu_bar = Gtk.MenuBar()

        #create file drop down menu
        file_menu = Gtk.Menu()
           
        #begin creating items for the drop down menu 
        open_item = Gtk.MenuItem("Open")
        open_item.connect_object("activate",self.on_Open_clicked, "open")

        save_item = Gtk.MenuItem("Save")
        save_item.connect_object("activate",self.on_Save_clicked, "save")

        close_item = Gtk.MenuItem("Close")
        close_item.connect_object("activate",self.on_Close_clicked, "close")
        
        #insert items into the drop down menu
        file_menu.append(open_item)
        file_menu.append(save_item)
        file_menu.append(close_item)
        
        open_item.show()
        save_item.show()
        close_item.show()
        
        #create edit drop down menu
        edit_menu = Gtk.Menu()
            
        #begin creating items for the drop down menu
        undo_item = Gtk.MenuItem("Undo")
        undo_item.connect_object("activate",self.on_Undo_clicked, "undo")

        redo_item = Gtk.MenuItem("Redo")
        redo_item.connect_object("activate",self.on_Redo_clicked, "redo")

        copy_item = Gtk.MenuItem("Copy")
        copy_item.connect_object("activate",self.on_Copy_clicked, "copy")

        cut_item = Gtk.MenuItem("Cut")
        cut_item.connect_object("activate",self.on_Cut_clicked, "cut")

        paste_item = Gtk.MenuItem("Paste")
        paste_item.connect_object("activate",self.on_Paste_clicked, "paste")

        restore_item = Gtk.MenuItem("Restore")
        restore_item.connect_object("activate",self.on_Restore_clicked, "restore")
        
        #insert items into the drop down menu
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

        #begin creating items for the drop down menu            
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

        #insert items into the drop down menu        
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
        help_root.connect("activate", self.on_Help_clicked)
        
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
        self.mainbox.pack_start(menu_bar, False, False, 2)
        
        menu_bar.show()
        
        menu_bar.append(file_root)
        menu_bar.append(edit_root)
        menu_bar.append(window_root)
        menu_bar.append(help_root)
        
        

        #Create icon bar  
        self.insert_widget_to_Frame_Contracted("<Mode of Operation>", self.icon_box,
                                    self.second_container, self.mainbox)
          
         
        self.insert_widget_to_Frame_Contracted("Filter Bar",self.filterbarbox,
                                    self.third_container, self.mainbox)
           
#          
        self.insert_widget_to_Frame_Expanded("Packet Window", self.packet_box, 
                                    self.fourth_container, self.mainbox)
           
          
        self.insert_widget_to_same_Frame("Formatter Window",self.formatter_box,
                                    self.fourth_container, self.mainbox)

        
        self.window_main.show_all()
    
    
    def update_packet_widget(self, value):
        fourth_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.packet_widget.set_packet_window_text(value)
        self.insert_widget_to_Frame("Packet Window", self.packet_box, 
                                    fourth_container, self.mainbox)
        print("totally worked!")
        return 0
    
    def refresh_all_windows(self):
        print("refreshed")
        self.window_main.show_all()
        self.editor_window.show_all()
        self.script_window.show_all()
        self.filter_window.show_all()
        self.hook_window.show_all()
        self.command_window.show_all()
        self.history_window.show_all()
    
    """
    create stand alone widget windows 
    by declaring a function like these 
    """
    def create_editor_window(self, widget):
        global editorOpen
        if(not editorOpen):
            self.editor_window = Gtk.Window()
            self.packet_widget.set_editor_widget(self.editor_widget)
            self.editorbox = self.editor_widget.create_widget()
            self.insert_widget_to_window("Editor Window", self.editorbox, self.editor_window)
            editorOpen = True
            
    def create_script_window(self, widget):
        global scriptOpen
        if(not scriptOpen):
            self.script_window = Gtk.Window()
            self.scriptbox = self.script_widget.create_widget()
            self.insert_widget_to_window("Script Window", self.scriptbox, self.script_window)
            scriptOpen = True
        
    def create_filter_window(self, widget):
        global filterOpen
        if(not filterOpen):
            self.filter_window = Gtk.Window()
            self.filterbox = self.filter_widget.create_widget()
            self.insert_widget_to_window("Filter Window", self.filterbox, self.filter_window)
            filterOpen = True

    def create_hook_window(self, widget):
        global hookOpen
        if(not hookOpen):
            self.hook_window = Gtk.Window()
            self.hookbox = self.hook_widget.create_widget()
            self.insert_widget_to_window("Hook Window", self.hookbox, self.hook_window)
            hookOpen = True

    def create_commandline_window(self,widget):
        global commOpen
        if(not commOpen):
            self.command_window = Gtk.Window()
            self.commandbox = self.command_widget.create_widget()
            self.insert_widget_to_window("Command Line Window", self.commandbox, self.command_window)
            commOpen = True

    def create_historical_window(self,widget):
        global histOpen
        if(not histOpen):
            self.history_window = Gtk.Window()
            self.historybox = self.history_widget.create_widget()
            self.insert_widget_to_window("Historical Copy Window", self.historybox, self.history_window)
            histOpen = True
    
    
    def on_Help_clicked(self, widget):
        print("help was clicked")
    
    def on_Undo_clicked(self, widget):
        print("undo was clicked")
        
    def on_Redo_clicked(self, widget):
        print("redo was clicked")
        
    def on_Save_clicked(self, widget):
        print("save was clicked")
    
    def on_Copy_clicked(self, widget):
        print("copy was clicked")
        
    def on_Cut_clicked(self, widget):
        print("cut was clicked")
        
    def on_Paste_clicked(self, widget):
        print("paste was clicked")
        
    def on_Restore_clicked(self, widget):
        print("restore was clicked")
        
    def on_Close_clicked(self, widget):
        print("close was clicked")

    def on_Open_clicked(self, widget):
        w = Gtk.Window(Gtk.WindowType.POPUP)
        self.opendialog = Gtk.FileChooserDialog("Please choose a file", w,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        self.opendialog.set_transient_for(w)
        w.add(self.opendialog)
        response = self.opendialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            self.chosenfile = self.opendialog.get_filename()
            print("filename chosen",self.chosenfile)
            self.maincontroller.set_pdml_file(self.chosenfile)
            self.packet_widget.clear_list()
            packets = self.maincontroller.get_all_packets()
            x = 0
            while(x < len(packets)):
                rowvalue = []
                if(x < 10):
                    rowvalue.append("0"+str(packets[x].get_packet_id()))
                else:
                    rowvalue.append(""+str(packets[x].get_packet_id()))
                mainproto = packets[x].get_packet_main_proto()
                protovals = mainproto.proto_attributes_values
                rowvalue.extend(protovals)
                while(len(rowvalue) < 5):
                    rowvalue.append("")
                print(rowvalue)
                self.packet_widget.add_to_list(rowvalue)
                x+=1  
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        self.opendialog.destroy()
        w.destroy()
        
        
    def main(self):
        Gtk.main()
        
    def destroy(self, w):
        print("main destroyed! \m/")

    def destroyComm(self, w):
        print("comm destroyed! \m/")
        global commOpen
        commOpen = False

    def destroyEditor(self, w):
        print("editor destroyed! \m/")
        global editorOpen
        editorOpen = False   

    def destroyFilter(self, w):
        print("filter destroyed! \m/")
        global filterOpen
        filterOpen = False 

    def destroyHook(self, w):
        print("hook destroyed! \m/")
        global hookOpen
        hookOpen = False 

    def destroyHist(self, w):
        print("hist destroyed! \m/")
        global histOpen
        histOpen = False 

    def destroyScript(self, w):
        print("script destroyed! \m/")
        global scriptOpen
        scriptOpen = False 

    """
    Given a widget, we can place 
    it on a window on a default frame
    """
    def insert_widget_to_window(self, windowtitle, widget, window):
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        title = windowtitle
        window.set_title(title)
        window.set_size_request( -1, -1)
        if(title == "Command Line Window"):
            window.connect("destroy", self.destroyComm)
        elif(title == "Editor Window"):
            window.connect("destroy", self.destroyEditor)
        elif(title == "Filter Window"):
            window.connect("destroy", self.destroyFilter)
        elif(title == "Hook Window"):
            window.connect("destroy", self.destroyHook)
        elif(title == "Historical Copy Window"):
            window.connect("destroy", self.destroyHist)
        elif(title == "Script Window"):
            window.connect("destroy", self.destroyScript)
        else:
            window.connect("destroy", self.destroy)
        window.add(vbox)
        first_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.insert_widget_to_Frame_Expanded(windowtitle, widget, 
                                    first_container, vbox)
        window.show_all()
    """
    Given a widget and a particular container and window
    we can create more complicated windows 
    """
    def insert_widget_to_Frame_Contracted(self,label, vbox,frameContainer, wbox):
        wbox.pack_start(frameContainer, False, True, 6)
        v_widget = vbox
        frameContainer.add(v_widget)
        v_widget.show()
        
        
    def insert_widget_to_Frame_Expanded(self,label, vbox,frameContainer, wbox):
        
        wbox.pack_start(frameContainer, True, True, 6)
        frame = Gtk.Frame()
        frame.set_label(label)
        frame.set_label_align( 0.5, 0)
        frame.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
        frame.show()
        v_widget = vbox
        frame.add(v_widget)
        frameContainer.pack_start(frame, True, True, 6)
        v_widget.show()
        
    def insert_widget_to_same_Frame(self,label, vbox,frameContainer, wbox):
        frame = Gtk.Frame()
        frame.set_label(label)
        frame.set_label_align( 0.5, 1)
        frame.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)
        frame.show()
        v_widget = vbox
        frame.add(v_widget)
        frameContainer.pack_start(frame, False, True, 6)
        v_widget.show()
        
    def remove_packet_widget_from_Frame(self):
        self.fourth_container.remove(self.packet_box)
        self.mainbox.remove(self.fourth_container)
        self.insert_widget_to_Frame("Packet Window", self.packet_box, 
                                    self.fourth_container, self.mainbox)
        
    


if(__name__ == "__main__"):
    settings = Gtk.Settings.get_default()
    settings.set_property("gtk-application-prefer-dark-theme", True)
    d = WindowController()
    d.main()
