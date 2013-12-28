import xml.etree.ElementTree as ET

schema = '{http://www.opengis.net/kml/2.2}'
planning_tree = ET.parse('./Planning_Applications_Archive.kml')
planning_root = planning_tree.getroot()

kml = planning_root[0]
folder = kml.find(schema + 'Folder')
places = folder.findall(schema+'Placemark')

for place in places:
  print place.tag, place.attrib

