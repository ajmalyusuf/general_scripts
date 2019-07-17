import sys, getopt
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

def printprop(filename, root):
        list_props = []
        for prop in root.getchildren():
                prop_name = prop.find('name')
                if prop_name is not None:
                        element = str(prop_name.text) + "=|" + str(prop.find('value').text) + "|"
                        list_props.append(element)
        if len(list_props) > 0:
                list_props.sort()
                for item in list_props:
                        print item

file_name = ''
file_list = ''

try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print 'test.py -i <file_name> -o <file_list>'
    sys.exit(2)

for opt, arg in opts:
	if opt == '-h':
		print 'test.py -i <file_name> -o <file_list>'
		sys.exit()
	elif opt in ("-i", "--ifile"):
		file_name = arg
	elif opt in ("-o", "--ofile"):
		file_list = arg

print 'Input file is "', file_name
print 'Output file is "', file_list



if len(sys.argv) < 2:
        print "Usage: python " + sys.argv[0] + " <xml file name>"
        exit(1)

file_name = sys.argv[1]

xml_list_file = open(file_name)
for line in xml_list_file:
        xml_file = line[:-1]
        print "Printing properties in " + xml_file
        print "==================================="

        conf = ElementTree.parse(xml_file).getroot()
        printprop(xml_file, root = conf)

#new_file = "core-site.new.xml";
#conf_file = open(new_file,'w')
#conf_file.write(ElementTree.tostring(conf))
#conf_file.close()

#format by calling xmllint in bash script - future
#xmllint --format "$new_file" > "$new_file".pp && mv "$new_file".pp "$new_file"
