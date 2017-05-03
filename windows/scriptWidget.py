import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os.path as osp
"""
Script Widget is a type of widget for our
protocol formatter window that allows
the user to open/edit/create a script
Widgets do not need windows and should
return a top_level Gtk.Box with all the 
contents of the widget as children 
"""
class ScriptWidget:
             
        def create_widget(self):
            
            #vbox is the top_level parent
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
            #fullContainer is a container for the whole  widget
            fullContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            #buttonContainer contains the buttons
            buttonContainer = Gtk.Box(spacing=6)
            self.chosenfile = ""
            #pack_start says fullContainer is now a child of vbox
            vbox.pack_start(fullContainer,True,True,0)
            
            #create an Open button 
            openButton = Gtk.Button("Open")
            
            #connect the button to a function 'on_Open_clicked'
            openButton.connect("clicked",self.on_Open_clicked)
            openButton.set_alignment(xalign=0, yalign=1) 
            
            #open button is now a child of the buttoncontainer 
            buttonContainer.pack_start(openButton,False,False,0)
            
            #create a New button
            newButton = Gtk.Button("New")
            
            #connect the button to a function 'on_New_clicked'
            newButton.connect("clicked",self.on_New_clicked)
            newButton.set_alignment(xalign=0, yalign=1) 
            
            #new button is now a child of the buttoncontainer
            buttonContainer.pack_start(newButton,False,False,0)
            #create a New button
            saveButton = Gtk.Button("Save")
            
            #connect the button to a function 'on_New_clicked'
            saveButton.connect("clicked",self.on_save_clicked)
            saveButton.set_alignment(xalign=0, yalign=1) 
            
            #new button is now a child of the buttoncontainer
            buttonContainer.pack_start(saveButton,False,False,0)
            #buttoncontainer is not a child of the fullcontainer
            fullContainer.pack_start(buttonContainer,False,False,0)
            
            #create a scrollable container (ScrolledWindow is not really a 'window')
            scrollContainer = Gtk.ScrolledWindow()
            
            #create a container for the script 
            scriptContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
            
            self.scriptBuffer = Gtk.TextBuffer()
            self.scriptBuffer.set_text("")
            
            #create a Textviewer
            scriptView = Gtk.TextView()
            scriptView.set_buffer(self.scriptBuffer)
            
            #scriptviewer is now a child of script container 
            scriptContainer.pack_start(scriptView, False, False, 0)
            
            #add the scriptview to the scroll window 
            scrollContainer.add(scriptContainer)
            
            #scroll window is now a child of the full container
            fullContainer.pack_start(scrollContainer,True,True,0)
            
            return vbox
                
        def on_Open_clicked(self, widget):
            w = Gtk.Window(Gtk.WindowType.POPUP)
            self.opendialog = Gtk.FileChooserDialog("Please choose a file", w,
                Gtk.FileChooserAction.OPEN,
                (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                 Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
            # print("./"+os.getcwd()+"/Scripts")
            # self.opendialog.set_current_folder("./"+os.getcwd()+"/Scripts")
            self.opendialog.set_current_folder(osp.abspath('../Scripts'))
            self.opendialog.set_transient_for(w)
            w.add(self.opendialog)
            response = self.opendialog.run()
            if response == Gtk.ResponseType.OK:
                print("Open clicked")
                self.chosenfile = self.opendialog.get_filename()
                print("filename chosen",self.chosenfile)
                self.scriptBuffer.set_text(self.read_file(self.chosenfile))

            elif response == Gtk.ResponseType.CANCEL:
                print("Cancel clicked")
            self.opendialog.destroy()
            w.destroy()

        def on_New_clicked(self, widget):
            self.scriptBuffer.set_text("")
            self.chosenfile = ""
        def on_save_clicked(self, widget):
            w = Gtk.Window(Gtk.WindowType.POPUP)
            self.savedialog = Gtk.FileChooserDialog("Save Script", w,
                Gtk.FileChooserAction.SAVE,
                (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                 Gtk.STOCK_SAVE_AS, Gtk.ResponseType.OK))
            self.savedialog.set_transient_for(w)
            self.opendialog.set_current_folder(osp.abspath('../Scripts'))
            w.add(self.savedialog)
            response = self.savedialog.run()
            if response == Gtk.ResponseType.OK:
                self.chosenfile = self.savedialog.get_filename()
                with open(self.chosenfile , 'w') as file:
                    file.write( self.scriptBuffer.get_text(self.scriptBuffer.get_bounds()[0],self.scriptBuffer.get_bounds()[1], True))
            elif response == Gtk.ResponseType.CANCEL:
                print("Cancel clicked")
            self.savedialog.destroy()
            w.destroy()
           
        def read_file(self, filename):
            with open(filename, 'r') as myfile:
                data = myfile.read()
            return data


