from xml.dom import minidom

chatFile = minidom.parse("chat.xml");
messages = chatFile.getElementsByTagName("msg");
output = open("chatOutPut.txt", "w");
for i in messages:
    output.write("nick = %s time = %s %s \n" % (i.attributes["nick"].value, i.attributes["time"].value, i.firstChild.nodeValue));

output.close();
