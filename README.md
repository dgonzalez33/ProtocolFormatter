# ProtocolFormatter
For software 2!

# Getting Started
Installatio Details
Development Environment:
Kali 2016.v2
LiClipse
 
Workspace setup
Create a new branch on gitHub based off the Master branch
Start a new python project on LiClipse and call it "ProtocolFormatter"
copy the contents of the clone into your python project 
 
# Creating a widget 
Create a new python file in the windows folder called [widgetname]Widget.py
A widget should have a function called create_widget(self)
create_widget(self) will return a Gtk.Box object, for consistency we'll call this
object vbox. 
vbox should be the top-parent object of your widget
your widget should be visual and functionally complete inside your widget class 
before passing to the WindowController
 
# Displaying your widget
The WindowController class can add single or multiple widgets to a window 
by adding your widget to a frame first 