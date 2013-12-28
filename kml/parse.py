import xml.etree.ElementTree as ET
import sys

schema = '{http://www.opengis.net/kml/2.2}'

planning_tree = ET.parse(sys.argv[1])

ET.register_namespace('', 'http://www.opengis.net/kml/2.2')
ET.register_namespace('atom', 'http://www.w3.org/2005/Atom')
ET.register_namespace('gx', 'http://www.google.com/kml/ext/2.2')

planning_root = planning_tree.getroot()

kml = planning_root[0]
folder = kml.find(schema + 'Folder')
places = folder.findall(schema+'Placemark')

for place in places:
  p_data = place.find(schema+'ExtendedData').find(schema+'SchemaData').findall(schema+'SimpleData');
  found = False
  for e in p_data:
    if 'Location' in e.attrib.values():
      location = e.text
      if 'Sutton' in location:
        found = True
        print 'Sutton is in', e.text
      else:
        print 'Sutton is not in', e.text
  if not found:
    print 'deleting', location
    folder.remove(place)

planning_tree.write('new.kml', xml_declaration = True,method = 'xml')

