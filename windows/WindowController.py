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
    
    maincontroller = controller()
    
    opendialog = Gtk.FileChooserDialog("Please choose a file", None,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
    
    #containers
    second_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    third_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    fourth_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

    
    
    #Widgets
    icon_widget = iconBar()
    filter_widget = FilterBarWidget()
    packet_widget = PacketWidget()
    formatter_widget = FormatterWidget()
    editor_widget = EditorWidget()
    script_widget = ScriptWidget()
    filter_widget = FilterWidget()
    filterbar_widget = FilterBarWidget()
    hook_widget = HookWidget()
    command_widget = CommandLineWidget()
    history_widget = HistoricalCopyWidget()
    
    
    
    #boxes
    icon_box = icon_widget.create_widget()
    filter_box = filter_widget.create_widget()
    packet_box = packet_widget.create_widget()
    packet_box.set_size_request(200,50)
    formatter_box = formatter_widget.create_widget()
    editorbox = editor_widget.create_widget()
    scriptbox = script_widget.create_widget()
    filterbox = filter_widget.create_widget()
    filterbarbox = filterbar_widget.create_widget()
    hookbox = hook_widget.create_widget()
    commandbox = command_widget.create_widget()
    historybox = history_widget.create_widget()
    
    
    #Dialog Window
    
    chosenfile = ""
    
    
    
    #Windows
    window_main = Gtk.Window()
    editor_window = Gtk.Window()
    script_window = Gtk.Window()
    filter_window = Gtk.Window()
    hook_window = Gtk.Window()
    command_window = Gtk.Window()
    history_window = Gtk.Window()
    
    
    
    
    
    """
    The __init__ constructor is currently being used 
    as a way to start our windows but we should only 
    construct the default window here in the future 
    Other windows will be created via button press 
    """


    def __init__(self):
        self.create_default_window()
       # GObject.timeout_add(100, self.refresh_all_windows)
#         self.create_script_window()
#         self.create_filter_window()
#         self.create_editor_window()

    
    """
    This function creates the default window
    by combining 5 widget in 4 containers 
    """
    def create_default_window(self):


        #create main window
        self.title = "Protocol Formatter System"
        self.window_main.set_title(self.title)
        self.window_main.set_size_request( 400, 400)
        self.window_main.connect("destroy", self.destroy)
        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        self.menu_bar = Gtk.MenuBar()

        #create file drop down menu
        file_menu = Gtk.Menu()
           
        #begin creating items for the drop down menu 
        open_item = Gtk.MenuItem("Open")
        open_item.connect_object("activate",self.on_Open_clicked, "open")

        save_item = Gtk.MenuItem("Save")

        close_item = Gtk.MenuItem("Close")
        
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

        redo_item = Gtk.MenuItem("Redo")

        copy_item = Gtk.MenuItem("Copy")

        cut_item = Gtk.MenuItem("Cut")

        paste_item = Gtk.MenuItem("Paste")

        restore_item = Gtk.MenuItem("Restore")
        
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
        self.insert_widget_to_Frame("<Mode of Operation>", self.icon_box,
                                    self.second_container, self.mainbox)
         
        
        self.insert_widget_to_Frame("Filter Bar",self.filterbarbox,
                                    self.third_container, self.mainbox)
         
        
        self.insert_widget_to_Frame("Packet Window", self.packet_box, 
                                    self.fourth_container, self.mainbox)
         
        
        self.insert_widget_to_Frame("Formatter Window",self.formatter_box,
                                    self.fourth_container, self.mainbox)
#         
#         dRecieved = ""
#         self.update = Thread(target=self.update_packet_widget, args=(dRecieved,))
#         self.update.setDaemon(True)
#         self.update.start()
        
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
            self.insert_widget_to_window("Editor Window", self.editorbox, self.editor_window)
            editorOpen = True
            
    def create_script_window(self, widget):
        global scriptOpen
        if(not scriptOpen):
            self.insert_widget_to_window("Script Window", self.scriptbox, self.script_window)
            scriptOpen = True
        
    def create_filter_window(self, widget):
        global filterOpen
        if(not filterOpen):
            self.insert_widget_to_window("Filter Window", self.filterbox, self.filter_window)
            filterOpen = True

    def create_hook_window(self, widget):
        global hookOpen
        if(not hookOpen):
            self.insert_widget_to_window("Hook Window", self.hookbox, self.hook_window)
            hookOpen = True

    def create_commandline_window(self,widget):
        global commOpen
        if(not commOpen):
            self.insert_widget_to_window("Command Line Window", self.commandbox, self.command_window)
            commOpen = True

    def create_historical_window(self,widget):
        global histOpen
        if(not histOpen):
            self.insert_widget_to_window("Historical Copy Window", self.historybox, self.history_window)
            histOpen = True



    def on_Open_clicked(self, widget):
        self.opendialog = Gtk.FileChooserDialog("Please choose a file", None,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        self.opendialog.set_size_request(300, 200)
        w = Gtk.Window()
        w.add(self.opendialog)
        #self.packet_widget.set_packet_window_text("yaaaass")
        
        response = self.opendialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + self.opendialog.get_filename())
            self.chosenfile = self.opendialog.get_filename()
            self.maincontroller.set_pdml_file(self.chosenfile)
            
            protosforfilterwindow = self.maincontroller.get_pdml_protocols()
            packetwindowcontent = self.maincontroller.get_pdml_text()
            
            self.packet_widget.set_packet_window_text(packetwindowcontent)
            #self.remove_packet_widget_from_Frame()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        self.opendialog.destroy()
        
        
    def main(self):
        Gtk.main()
        
    def destroy(self, w):
        #Gtk.main_quit()
        print("destroyed! \m/")

    def destroyComm(self, w):
        print("destroyed! \m/")
        global commOpen
        commOpen = False

    def destroyEditor(self, w):
        print("destroyed! \m/")
        global editorOpen
        editorOpen = False   

    def destroyFilter(self, w):
        print("destroyed! \m/")
        global filterOpen
        filterOpen = False 

    def destroyHook(self, w):
        print("destroyed! \m/")
        global hookOpen
        hookOpen = False 

    def destroyHist(self, w):
        print("destroyed! \m/")
        global histOpen
        histOpen = False 

    def destroyScript(self, w):
        print("destroyed! \m/")
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
        frameContainer.pack_start(frame, True, True, 6)
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
