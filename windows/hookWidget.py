import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows.hookList import HookList
from windows.filterRow import FilterRow
from windows.scriptWidget import ScriptWidget
import os.path as osp
class HookWidget:
            
        def create_widget(self):
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            
            fieldContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(fieldContainer,True,True,0)

            fieldLabel = Gtk.Label()
            fieldLabel.set_markup("<b>Field(s) Selector</b>")
            fieldLabel.set_alignment(xalign=0, yalign=1) 
            fieldContainer.pack_start(fieldLabel,True,True,0)

            self.expLists = HookList()
            hoodAdd = Gtk.Box(spacing = 6)
            fieldContainer.pack_start(hoodAdd,True,True,0)
            hoodAdd.pack_start(self.expLists.getList(),True,True,0)

            addField = Gtk.Button("->")
            # addFilter.set_image(image)
            addField.connect("clicked",self.on_addField_clicked)
            hoodAdd.pack_start(addField,False,False,1)

            self.listbox = Gtk.ListBox()
            self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
            hoodAdd.pack_start(self.listbox,True,True,0)

            self.context = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            vbox.pack_start(self.context,False,False,0)
            contextLabel = Gtk.Label()
            contextLabel.set_markup("<b>Script Selector</b>")
            contextLabel.set_alignment(xalign=0, yalign=1) 
            self.context.pack_start(contextLabel,False,False,0)
            self.scriptWrapper = Gtk.Box(spacing=6)
            self.context.pack_start(self.scriptWrapper,False,False,0)
            self.createBut = Gtk.Button(label="Create Script")
            self.createBut.connect("clicked", self.create_script_clicked)
            self.scriptWrapper.pack_start(self.createBut,False,False,0)
            self.scriptPathEntry = Gtk.Entry()
            self.scriptPathEntry.set_text("<File Path>")
            self.scriptWrapper.pack_start(self.scriptPathEntry,True,True,0)
            self.addHook = Gtk.Button(label="Add Script")
            self.addHook.connect("clicked", self.add_script_clicked)
            self.scriptWrapper.pack_start(self.addHook,False,False,0)
            self.box = Gtk.Box(spacing=6)
            vbox.pack_start(self.box,False,False,0)
            customLabel = Gtk.Label("Custom Name: ")
            self.box.pack_start(customLabel,False,False,0)
            self.customName = Gtk.Entry()
            self.customName.set_text("<Name of Hook>")
            self.box.pack_start(self.customName, False, False, 0)
            self.butCreate = Gtk.Button(label="Create Hook")
            self.butCreate.connect("clicked", self.on_butCreate_clicked)
            self.box.pack_start(self.butCreate,False,False,0)
            self.butCancel = Gtk.Button(label="Cancel")
            self.box.pack_start(self.butCancel,False,False,0)
            
            return vbox
            
        def add_script_clicked(self, widget):
            w = Gtk.Window(Gtk.WindowType.POPUP)
            self.opendialog = Gtk.FileChooserDialog("Please choose a file", w,
                Gtk.FileChooserAction.OPEN,
                (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                 Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
            self.opendialog.set_current_folder(osp.abspath('../Scripts'))
            self.opendialog.set_transient_for(w)
            w.add(self.opendialog)
            response = self.opendialog.run()
            if response == Gtk.ResponseType.OK:
                self.chosenfile = self.opendialog.get_filename()
                self.scriptPathEntry.set_text(self.chosenfile)
            elif response == Gtk.ResponseType.CANCEL:
                print("Cancel clicked")
            self.opendialog.destroy()
            w.destroy()
        def set_applied_hooks(self):
            print("eventua;;y")
        def set_fields(self,fields):
            print("eventually")
        def on_butCreate_clicked(self, widget):
            print("eventually")
        def on_butReset_clicked(self, widget):
            print("Resetting FIlter!")
        def create_script_clicked(self, widget):
            self.script_window = Gtk.Window()
            self.script_window.set_size_request(500, 500)
            self.script_widget = ScriptWidget()
            self.scriptbox = self.script_widget.create_widget()
            self.script_window.set_keep_above(True)
            self.script_window.add(self.scriptbox)
            self.script_window.show_all()
            
        def on_excludeBut_clicked(self, widget):
            print("Including!") 
        def on_addField_clicked(self, widget):
            selected = self.expLists.getSelected()
            print(selected[0])
            row = FilterRow(self.listbox,selected[0],selected[1],list())
            self.listbox.add(row.getRow())
            self.listbox.show_all()    

