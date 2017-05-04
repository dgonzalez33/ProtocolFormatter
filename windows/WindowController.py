import sys
from gi.overrides.Gtk import Window
sys.path.insert(0, '../')
import gi
from numpy import empty
from threading import Thread
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango, GObject, Gdk
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
from FileSub.Capture import Capture
from FormatterSub.Filter import Filter
from subprocess import call

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
        self.capture = Capture()
        
        #Dialog Window
        self.chosenfile = ""
        self.previousfile = ""
#         self.opendialog = Gtk.FileChooserDialog("Please choose a file", None,
#                 Gtk.FileChooserAction.OPEN,
#                 (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
#                  Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        
        #containers
        self.second_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.third_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.fourth_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

        #Widgets
        #self.icon_widget = iconBar()
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
        self.icon_box = self.create_icon_bar()
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
        self.window_main = Gtk.Window()
        self.create_default_window()


    
    """
    This function creates the default window
    by combining 5 widget in 4 containers 
    """
    def create_default_window(self):


        #create main window
        self.title = "Protocol Formatter System"
        self.window_main.set_title(self.title)
        self.window_main.set_size_request( -1, -1)
        self.window_main.connect("destroy", self.destroy)
        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        self.menu_bar = Gtk.MenuBar()

        #create file drop down menu
        self.file_menu = Gtk.Menu()
           
        #begin creating items for the drop down menu 
        self.open_item = Gtk.MenuItem("Open")
        self.open_item.connect_object("activate",self.on_Open_clicked, "open")

        self.save_item = Gtk.MenuItem("Save")
        self.save_item.connect_object("activate",self.on_Save_clicked, "save")

        self.close_item = Gtk.MenuItem("Close")
        self.close_item.connect_object("activate",self.on_Close_clicked, "close")
        
        #insert items into the drop down menu
        self.file_menu.append(self.open_item)
        self.file_menu.append(self.save_item)
        self.file_menu.append(self.close_item)
        
        self.save_item.set_sensitive(False)
        
        self.open_item.show()
        self.save_item.show()
        self.close_item.show()
        
        #create edit drop down menu
        self.edit_menu = Gtk.Menu()
            
        #begin creating items for the drop down menu
        self.undo_item = Gtk.MenuItem("Undo")
        self.undo_item.connect_object("activate",self.on_Undo_clicked, "undo")

        self.redo_item = Gtk.MenuItem("Redo")
        self.redo_item.connect_object("activate",self.on_Redo_clicked, "redo")

        self.copy_item = Gtk.MenuItem("Copy")
        self.copy_item.connect_object("activate",self.on_Copy_clicked, "copy")

        self.cut_item = Gtk.MenuItem("Cut")
        self.cut_item.connect_object("activate",self.on_Cut_clicked, "cut")

        self.paste_item = Gtk.MenuItem("Paste")
        self.paste_item.connect_object("activate",self.on_Paste_clicked, "paste")

        self.restore_item = Gtk.MenuItem("Restore")
        self.restore_item.connect_object("activate",self.on_Restore_clicked, "restore")
        
        #insert items into the drop down menu
        self.edit_menu.append(self.undo_item)
        self.edit_menu.append(self.redo_item)
        self.edit_menu.append(self.copy_item)
        self.edit_menu.append(self.cut_item)
        self.edit_menu.append(self.paste_item)
        self.edit_menu.append(self.restore_item)
        
        self.undo_item.show()
        self.redo_item.show()
        self.copy_item.show()
        self.cut_item.show()
        self.paste_item.show()
        self.restore_item.show()
        
        # create window drop down menu
        self.window_menu = Gtk.Menu()

        #begin creating items for the drop down menu            
        self.filter_item = Gtk.MenuItem("Filter")
        self.filter_item.connect("activate",self.create_filter_window)

        self.editor_item = Gtk.MenuItem("Editor")
        self.editor_item.connect("activate",self.create_editor_window)

        self.script_item = Gtk.MenuItem("Script")
        self.script_item.connect("activate",self.create_script_window)

        self.hook_item = Gtk.MenuItem("Hook")
        self.hook_item.connect("activate",self.create_hook_window)

        self.commandline_item = Gtk.MenuItem("CommandLine")
        self.commandline_item.connect("activate",self.create_commandline_window)

        self.historical_item = Gtk.MenuItem("Historical")
        self.historical_item.connect("activate", self.create_historical_window)
        
        self.editor_item.set_sensitive(False)
        self.historical_item.set_sensitive(False)
        
        
        #insert items into the drop down menu        
        self.window_menu.append(self.filter_item)
        self.window_menu.append(self.editor_item)
        self.window_menu.append(self.script_item)
        self.window_menu.append(self.hook_item)
        self.window_menu.append(self.commandline_item)
        self.window_menu.append(self.historical_item)
        
        self.filter_item.show()
        self.editor_item.show()
        self.script_item.show()
        self.hook_item.show()
        self.commandline_item.show()
        self.historical_item.show()
        
        # insert drop down menus into the menu bar
        self.file_root = Gtk.MenuItem("File")
        self.edit_root = Gtk.MenuItem("Edit")
        self.window_root = Gtk.MenuItem("Window")
        self.help_root = Gtk.MenuItem("Help")
        self.help_root.connect("activate", self.on_Help_clicked)
        
        self.file_root.show()
        self.edit_root.show()
        self.window_root.show()
        self.help_root.show()
        
        self.file_root.set_submenu(self.file_menu)
        self.edit_root.set_submenu(self.edit_menu)
        self.window_root.set_submenu(self.window_menu)
        
        self.window_main.add(self.mainbox)
        self.mainbox.show()
        
        self.menu_bar = Gtk.MenuBar()
        self.mainbox.pack_start(self.menu_bar, False, False, 2)
        
        self.menu_bar.show()
        
        self.menu_bar.append(self.file_root)
        self.menu_bar.append(self.edit_root)
        self.menu_bar.append(self.window_root)
        self.menu_bar.append(self.help_root)
        
        

        #Create icon bar  
        self.insert_widget_to_Frame_Contracted("<Mode of Operation>", self.icon_box,
                                    self.second_container, self.mainbox)
          
        self.filterbar_widget.p_widget = self.packet_widget
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
    
    
    """
    create stand alone widget windows 
    by declaring a function like these 
    """
    def create_editor_window(self, widget):
        global editorOpen
        if(not editorOpen):
            self.editor_window = Gtk.Window()
            self.editor_window.set_size_request(500, 500)
            self.packet_widget.set_editor_widget(self.editor_widget)
            self.packet_widget.editorisopen = 1
            self.editorbox = self.editor_widget.create_widget()
            self.insert_widget_to_window("Editor Window", self.editorbox, self.editor_window)
            editorOpen = True
            
    def create_script_window(self, widget):
        global scriptOpen
        if(not scriptOpen):
            self.script_window = Gtk.Window()
            self.script_window.set_size_request(500, 500)
            self.scriptbox = self.script_widget.create_widget()
            self.insert_widget_to_window("Script Window", self.scriptbox, self.script_window)
            scriptOpen = True
        
    def create_filter_window(self, widget):
        global filterOpen
        if(not filterOpen):
            self.filter_window = Gtk.Window()
            self.filter_window.set_size_request(500, 550)
            self.filterbox = self.filter_widget.create_widget()
            self.insert_widget_to_window("Filter Window", self.filterbox, self.filter_window)
            filterOpen = True

    def create_hook_window(self, widget):
        global hookOpen
        if(not hookOpen):
            self.hook_window = Gtk.Window()
            self.hook_window.set_size_request(500, 300)
            self.hookbox = self.hook_widget.create_widget()
            self.insert_widget_to_window("Hook Window", self.hookbox, self.hook_window)
            hookOpen = True

    def create_commandline_window(self,widget):
        global commOpen
        if(not commOpen):
            self.command_window = Gtk.Window()
            self.command_window.set_size_request(500, 100)
            self.commandbox = self.command_widget.create_widget()
            self.insert_widget_to_window("Command Line Window", self.commandbox, self.command_window)
            commOpen = True

    def create_historical_window(self,widget):
        global histOpen
        if(not histOpen):
            self.history_window = Gtk.Window()
            self.history_window.set_size_request(500, 500)
            self.historybox = self.history_widget.create_widget()
            val = self.chosenfile+ "  VS  "+ self.previousfile
            self.history_widget.update_label(val)
            self.history_widget.create_historical_copy(self.chosenfile, self.previousfile)
#             self.history_widget.check_line_colors()
            self.insert_widget_to_window("Historical Copy Window", self.historybox, self.history_window)
            histOpen = True
    
    
    
    def create_icon_bar(self):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        #fullContainer is a container for the whole  widget
        fullContainer = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        #buttonContainer contains the buttons
        buttonContainer = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        #pack_start says fullContainer is now a child of vbox
        vbox.pack_start(fullContainer,True,True,0)
        
        #==================================================================================================================
        o_imagebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        o_imagebox.set_border_width(2)
        o_image = Gtk.Image()
        o_label = Gtk.Label("Open")
        o_label.modify_font(Pango.FontDescription("sans 8"))
        o_image.set_from_file("../images/open.png")
        o_imagebox.pack_start(o_image, False, False, 0)
        o_imagebox.pack_start(o_label, False, False, 0)
        o_image.show()
        o_label.show()
        openButton = Gtk.Button()
        openButton.set_alignment(xalign=0.0, yalign=1)
        openButton.connect("clicked",self.on_Open_clicked)
        openButton.add(o_imagebox)
        buttonContainer.pack_start(openButton,False,False,2)
        
        s_imagebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        s_imagebox.set_border_width(2)
        s_image = Gtk.Image()
        s_label = Gtk.Label("Save")
        s_label.modify_font(Pango.FontDescription("sans 8"))
        s_image.set_from_file("../images/save.png")
        s_imagebox.pack_start(s_image, False, False, 0)
        s_imagebox.pack_start(s_label, False, False, 0)
        s_image.show()
        s_label.show()
        self.saveButton = Gtk.Button()
        self.saveButton.set_alignment(xalign=0.0, yalign=1)
        self.saveButton.connect("clicked",self.on_Save_clicked)
        self.saveButton.add(s_imagebox)
        buttonContainer.pack_start(self.saveButton,False,False,2)
        self.saveButton.set_sensitive(False)
        
        f_imagebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        f_imagebox.set_border_width(2)
        f_image = Gtk.Image()
        f_label = Gtk.Label("Filter")
        f_label.modify_font(Pango.FontDescription("sans 8"))
        f_image.set_from_file("../images/filter.png")
        f_imagebox.pack_start(f_image, False, False, 0)
        f_imagebox.pack_start(f_label, False, False, 0)
        f_image.show()
        f_label.show()
        filterButton = Gtk.Button()
        filterButton.set_alignment(xalign=0.0, yalign=1)
        filterButton.connect("clicked",self.on_Filter_clicked)
        filterButton.add(f_imagebox)
        buttonContainer.pack_start(filterButton,False,False,2)
        
        u_imagebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        u_imagebox.set_border_width(2)
        u_image = Gtk.Image()
        u_label = Gtk.Label("Undo")
        u_label.modify_font(Pango.FontDescription("sans 8"))
        u_image.set_from_file("../images/undo.png")
        u_imagebox.pack_start(u_image, False, False, 0)
        u_imagebox.pack_start(u_label, False, False, 0)
        u_image.show()
        u_label.show()
        undoButton = Gtk.Button()
        undoButton.set_alignment(xalign=0.0, yalign=1)
        undoButton.connect("clicked",self.on_Undo_clicked)
        undoButton.add(u_imagebox)
        buttonContainer.pack_start(undoButton,False,False,2)

        r_imagebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        r_imagebox.set_border_width(2)
        r_image = Gtk.Image()
        r_label = Gtk.Label("Redo")
        r_label.modify_font(Pango.FontDescription("sans 8"))
        r_image.set_from_file("../images/redo.png")
        r_imagebox.pack_start(r_image, False, False, 0)
        r_imagebox.pack_start(r_label, False, False, 0)
        r_image.show()
        r_label.show()
        redoButton = Gtk.Button()
        redoButton.set_alignment(xalign=0.0, yalign=1)
        redoButton.connect("clicked",self.on_Redo_clicked)
        redoButton.add(r_imagebox)
        buttonContainer.pack_start(redoButton,False,False,2)

        fullContainer.pack_start(buttonContainer,False,False,4)
        return vbox
    
    
    
    def on_Help_clicked(self, widget):
        print("help was clicked")
    
    def on_Undo_clicked(self, widget):
        print("undo was clicked")
        
    def on_Redo_clicked(self, widget):
        print("redo was clicked")
        
    def on_Filter_clicked(self, widget):
        print("filter was clicked")
        
    def on_Save_clicked(self, widget):
        print("save was clicked")
        w = Gtk.Window(Gtk.WindowType.POPUP)
        self.savedialog = Gtk.FileChooserDialog("Save PDML", w,
            Gtk.FileChooserAction.SAVE,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_SAVE_AS, Gtk.ResponseType.OK))
        self.savedialog.set_transient_for(w)
        w.add(self.savedialog)
        
        response = self.savedialog.run()
        if response == Gtk.ResponseType.OK:
            print("Save clicked")
            if(self.previousfile != self.chosenfile):
                self.previousfile = self.chosenfile
            self.chosenfile = self.savedialog.get_filename()
            print("filename chosen",self.chosenfile)
            self.createFilePath(self.chosenfile)
            
            if(self.capture.isCapture(self.chosenfile)):
                
                if(self.capture.isPDML(self.chosenfile)):
                    
                    self.capture.set_man(self.maincontroller.get_pdml_man())
                    self.capture.save_pdml(self.chosenfile)
                    self.update_pdml_contents()
                    self.historical_item.set_sensitive(True)
                    
                else:
                    print("need to convert")
                    self.make_convert_window()
            else:
                print("launch error window")
                self.make_error_window("this is not a capture bruh")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        self.savedialog.destroy()
        w.destroy()
    
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
        Gtk.main_quit()
        

    def createFilePath(self, filepath):
        print("touch",filepath)
        call(["touch", filepath])
        
    def on_Open_clicked(self, widget):
        self.temp = ""
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
            if(self.capture.isCapture(self.chosenfile)):
                
                if(self.capture.isPDML(self.chosenfile)):
#                     self.capture.createFilePath(self.chosenfile)
#                     self.capture.set_man(self.chosenfile)
#                     self.capture.save_pdml(self.maincontroller.get_pdml_man().get_pdml(), self.chosenfile)
                    self.update_pdml_contents() 
                    self.save_item.set_sensitive(True)
                    self.saveButton.set_sensitive(True)
                    self.editor_item.set_sensitive(True)
                    
                else:
                    print("need to convert")
                    self.make_convert_window()
            else:
                print("launch error window")
                self.make_error_window("this is not a capture bruh")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        self.opendialog.destroy()
        w.destroy()
    
    def update_pdml_contents(self):
        self.maincontroller.set_pdml_file(self.chosenfile)
        
        self.history_widget.clear_list()
        self.packet_widget.clear_list()
        packets = self.maincontroller.get_all_packets()
        self.editor_widget.set_pdml_man(self.maincontroller.get_pdml_man())
        x = 0
        while(x < len(packets)):
            self.rowvalue = []
            self.p_name = ""
            if(x < 10):
                self.p_name = "0"+str(packets[x].get_packet_id())
            else:
                self.p_name =""+str(packets[x].get_packet_id())
                
            self.rowvalue.append(self.p_name)
                
            proto = packets[x].get_proto_element()
            y = 0
            while(y < len(proto)):
                self.rowvalue.append(proto[y].proto_attributes_values[0])
                
                if(proto[y].proto_attributes_values[0] == "geninfo"):
                    self.rowvalue.append(proto[y].proto_attributes_values[2])
                elif(len(proto[y].proto_attributes_values) > 1):
                    self.rowvalue.append(proto[y].proto_attributes_values[1])
                else:
                    self.rowvalue.append("")

                if(proto[y].proto_attributes_values[0] == "geninfo"):
                    self.field = proto[y].get_field_element_at_index(3)
                    self.date = self.field.field_attributes_values[2]
                    self.rowvalue.append(self.date)
                else:
                    self.rowvalue.append(self.date)
                    
                if(len(self.rowvalue) != 4):
                    print(self.owvalue)
                    self.rowvalue.clear()
                    self.rowvalue.append(self.p_name)
                else:  
                    self.packet_widget.add_to_list(self.rowvalue)
                    self.rowvalue.clear()
                    self.rowvalue.append(self.p_name)
                y+=1
            self.rowvalue.clear()
                
            x+=1  
        
    def make_error_window(self, message):
        ww = Gtk.Window()
        ww.set_size_request(150, 75)
        ww.set_keep_above(True)
        ww.connect("destroy", self.destroy)
        button = Gtk.Button(message)
        button.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("red") )
        #colorb = Gtk.ColorButton(button, Gdk.Color(1,0,0))
        #button.modify_bg(Gtk.StateType.PRELIGHT, color)
   
        
        self.insert_widget_to_window("Error", button, ww)
        
    def make_convert_window(self):
        self.convertwindow = Gtk.Window()
        self.convertwindow.set_size_request(150, 75)
        self.convertwindow.set_keep_above(True)
        self.convertwindow.connect("destroy", self.destroy)
        button = Gtk.Button("Click to convert to pdml")
        button.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("yellow") )
        button.connect("clicked", self.convert_file)
        self.insert_widget_to_window("Convert?", button, self.convertwindow)
        
        
    def main(self):
        Gtk.main()
        
    def convert_file(self, widget):
        self.chosenfile = self.capture.createCapture(self.chosenfile)
        self.convertwindow.destroy()
        if(self.capture.isPDML(self.chosenfile)):
            self.update_pdml_contents()
            self.save_item.set_sensitive(True)
            self.saveButton.set_sensitive(True)
        else:
            self.make_error_window("convert failed")
            
        
    def destroy(self, w):
        print("main destroyed! \m/")

    def destroyComm(self, w):
        print("comm destroyed! \m/")
        global commOpen
        commOpen = False

    def destroyEditor(self, w):
        print("editor destroyed! \m/")
        self.packet_widget.editorisopen = 0
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
        #window.set_size_request( -1, -1)
        if(title == "Command Line Window"):
            window.connect("destroy", self.destroyComm)
            window.set_keep_above(True)
        elif(title == "Editor Window"):
            window.connect("destroy", self.destroyEditor)
            window.set_keep_above(True)
        elif(title == "Filter Window"):
            window.connect("destroy", self.destroyFilter)
            window.set_keep_above(True)
        elif(title == "Hook Window"):
            window.connect("destroy", self.destroyHook)
            window.set_keep_above(True)
        elif(title == "Historical Copy Window"):
            window.connect("destroy", self.destroyHist)
            window.set_keep_above(True)
        elif(title == "Script Window"):
            window.connect("destroy", self.destroyScript)
            window.set_keep_above(True)
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
