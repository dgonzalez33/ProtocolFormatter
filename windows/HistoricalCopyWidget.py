#Command line widget
#python 3.5
import gi
import difflib
import sys
#from difflib_data import *
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class HistoricalCopyWidget:


    def create_widget(self):
        #vbox is the top_level parent
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    
        #fullContainer is a container for the whole  widget
        fullContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        #buttonContainer contains the buttons
        buttonContainer = Gtk.Box(spacing=6)
        
        #pack_start says fullContainer is now a child of vbox
        vbox.pack_start(fullContainer,True,True,0)
        
        #create a scrollable container (ScrolledWindow is not really a 'window')
        scrollContainer = Gtk.ScrolledWindow()
        
        #create a container for the packet 
        packetContainer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        
        packetBuffer = Gtk.TextBuffer()
        infile = open("../Scripts/cubic.pdml", "r")
        file2 = open("../Scripts/cubic2.pdml", "r")
        file3 = open("../Scripts/testcubic.txt", "w")
        diff = difflib.ndiff(infile.readlines(), file2.readlines())
        sys.stdout=file3
        print ("\n".join(diff),"\n")

       # diff = difflib.ndiff(infile.readlines(), file2.readlines())
        #print ("\n".join(diff),)

#read line in for loop
        print ("hey" )
        file3 = open("../Scripts/testcubic (copy).txt", "r")
       # print (file3.readlines())

        filetext = "\n\n\n\n            <Historical Packet Contents compare>\n\n\n\n" + '\n'.join(file3.readlines()) + "\n"


        packetBuffer.set_text(filetext)
        
        #create a Textviewer
        packetView = Gtk.TextView()
        packetView.set_buffer(packetBuffer)
        
        #packetviewer is now a child of packet container 
        packetContainer.pack_start(packetView, False, False, 0)

        restorebutton = Gtk.Button.new_with_label("Restore")
        packetContainer.pack_start(restorebutton, False, False, 0)


        
        #add the packetview to the scroll window 
        scrollContainer.add(packetContainer)
        
        #scroll window is now a child of the full container
        fullContainer.pack_start(scrollContainer,True,True,0)
        
        return vbox
    
    def create_historical_copy(self):


        infile = open("../Scripts/cubic.pdml" , "r")
        file2 = open("../Scripts/cubic2.pdml" , "r")
       # differ = difflib.HtmlDiff()
       # hi=differ.make_table(infile,file2)
      #  print("table created")
      #  print (hi)
        diff =difflib.ndiff(infile.readlines(),file2.readlines())

        #print( ''.join(diff),)
        #


    #def compare(self):

