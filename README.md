# ProtocolFormatter

-UTEP Spring 2017 Computer Science Senior Capstone Project

-Created by Team5

-The ProtocolFormatter is a system that enables a user to open/edit PDML capture files

-PDML (Packet Description Markup Language) "conforms to the XML standard and contains details about the packet dissection" -wikiwireshark

-Aside from just open/editing PDML, The ProtocolFormatter system filters/sorts/converts and applies formatters to PDML's

-Formatters are defined actions that are applied to PDML's

# Development Environment:

-Kali 2016.v2

-Gtk 3.0

-Python 3+
 
# System Breakdown

# FileSub

-These classes help load capture files, create/edit scripts and communicate with tshark 

-tshark converts other captures into pdml before loading them into the system

# FormatterSub

-In here you'll find all the classes that create and edit Formatters 

-Formatters are made of Rules 

-Rules apply actions (renaming, annotating, hiding, and hooking(an external script to a field)

-Rules apply these actions according to the Berkeley Packet Filter created

# PDMLSub

-This system parses the pdml file into a data structure 

-In here you'll also find the HistoricalCopy class that compares your current edit with the original pdml

# RestofSystem

-This folder contains the controller class that acts as the jelly between the subsystems 

-The controller class creates it's own thread in case you need to run any background operations after launching the Gtk GUI

-The tracker class will keep track of changes as they happen an offer an undo or redo function 

# images

-Pretty sure I don't need to say anything here... 

# windows

-These are all the components to create the Gtk GUI

-Widgets are dynamically created and loaded by the WindowController 

-WindowController talks to the controller when it needs access to information for the other subsystems 
 
# Launching

-To launch the system, ProtocolFormatter/windows/python WindowController.py
 
