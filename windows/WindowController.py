import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from scriptWidget import ScriptWidget
from filterWidget import FilterWidget
from hookWidget import HookWidget
from editorWidget import EditorWidget

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
        self.create_script_window()
        self.create_filter_window()
        self.create_editor_window()
    
    """
    This function creates the default window
    by combining 5 widget in 4 containers 
    """
    def create_default_window(self):
        self.window_main = Gtk.Window()
        self.title = "Protocol Formatter System"
        self.window_main.set_title(self.title)
        self.window_main.set_size_request( -1, -1)
        self.window_main.connect("destroy", self.destroy)
        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.window_main.add(self.mainbox)
        
        first_widget = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        first_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.insert_widget_to_Frame("Menu Bar", first_widget,
                                    first_container, self.mainbox)
        
        second_widget = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        second_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.insert_widget_to_Frame("Icon Bar", second_widget,
                                    second_container, self.mainbox)
        
        third_widget = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        third_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.insert_widget_to_Frame("Filter Bar",third_widget,
                                    third_container, self.mainbox)
        
        fourth_widget = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        fourth_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.insert_widget_to_Frame("Packet Window", fourth_widget, 
                                    fourth_container, self.mainbox)
        
        fifth_widget = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.insert_widget_to_Frame("Formatter Window",fifth_widget,
                                    fourth_container, self.mainbox)
        
        self.window_main.show_all()
    
    """
    create stand alone widget windows 
    by declaring a function like these 
    """
    def create_editor_window(self):
        self.editorbox = EditorWidget().create_widget()
        self.insert_widget_to_window("Editor Window", self.editorbox)
            
    def create_script_window(self):
        self.scriptbox = ScriptWidget().create_widget()
        self.insert_widget_to_window("Script Window", self.scriptbox)
        
    def create_filter_window(self):
        self.filterbox = FilterWidget().create_widget()
        self.insert_widget_to_window("Filter Window", self.filterbox)

    def create_hook_window(self):
        self.hookbox = HookWidget().create_widget()
        self.isert_widget_to_window("Fileter Window", self.hookbox)
        
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
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        window= Gtk.Window()
        title = windowtitle
        window.set_title(title)
        window.set_size_request( -1, -1)
        window.connect("destroy", self.destroy)
        window.add(vbox)
        first_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
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
    
if(__name__ == "__main__"):
    d = WindowController()
    d.main()

