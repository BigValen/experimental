import xml.etree.ElementTree as ET

planning_tree = ET.parse('./Planning_Applications_Archive.kml')
test_tree = ET.parse('./test.xml')
planning_root = planning_tree.getroot()
test_root = test_tree.getroot()

print test_root.findall('country')
print planning_root.findall('Document')
print planning_root.findall('Folder')
print planning_root.findall('name')

