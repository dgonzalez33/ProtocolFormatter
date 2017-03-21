import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from scriptWidget import ScriptWidget
from filterWidget import FilterWidget
from editorWidget import EditorWidget

class DefaultGui:
    def __init__(self):
        self.create_default_window()
        self.create_script_window()
        self.create_filter_window()
    
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
        
        third_widget = EditorWidget().create_widget()
        third_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.insert_widget_to_Frame("Filter Bar",third_widget,
                                    third_container, self.mainbox)
        
        fourth_widget = ScriptWidget().create_widget()
        fourth_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.insert_widget_to_Frame("Packet Window", fourth_widget, 
                                    fourth_container, self.mainbox)
        
        fifth_widget = FilterWidget().create_widget()
        self.insert_widget_to_Frame("Formatter Window",fifth_widget,
                                    fourth_container, self.mainbox)
        
        self.window_main.show_all()
        
    def create_script_window(self):
        self.window_script= Gtk.Window()
        title = "Script Window"
        self.window_script.set_title(title)
        self.window_script.set_size_request( -1, -1)
        self.window_script.connect("destroy", self.destroy)
        self.scriptbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.window_script.add(self.scriptbox)
        first_widget = ScriptWidget().create_widget()
        first_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.insert_widget_to_Frame("Script Widget", first_widget, 
                                    first_container, self.scriptbox)
        self.window_script.show_all()
        
    def create_filter_window(self):
        self.window_filter= Gtk.Window()
        title = "Filter Window"
        self.window_filter.set_title(title)
        self.window_filter.set_size_request( -1, -1)
        self.window_filter.connect("destroy", self.destroy)
        self.filterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.window_filter.add(self.filterbox)
        first_widget = FilterWidget().create_widget()
        first_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.insert_widget_to_Frame("Filter Widget", first_widget, 
                                    first_container, self.filterbox)
        self.window_filter.show_all()
        
    def main(self):
        Gtk.main()
        
    def destroy(self, w):
        #Gtk.main_quit()
        print("destroyed! \m/")
        
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
    d = DefaultGui()
    d.main()

