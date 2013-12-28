#!/usr/bin/python2.7

import xml.etree.ElementTree as ET
import sys


def CDATA(text=None):
    element = ET.Element('![CDATA[')
    element.text = text
    return element

ET._original_serialize_xml = ET._serialize_xml
def _serialize_xml(write, elem, encoding, qnames, namespaces):
    if elem.tag == '![CDATA[':
        write("\n<%s%s]]>\n" % (
                elem.tag, elem.text))
        return
    return ET._original_serialize_xml(
        write, elem, encoding, qnames, namespaces)
ET._serialize_xml = ET._serialize['xml'] = _serialize_xml




schema = '{http://www.opengis.net/kml/2.2}'

planning_tree = ET.parse(sys.argv[1])

ET.register_namespace('', 'http://www.opengis.net/kml/2.2')
planning_root = planning_tree.getroot()
kml = planning_root[0]
folder = kml.find(schema + 'Folder')
places = folder.findall(schema+'Placemark')

suttonians = 0
others = 0

for place in places:
  extended_data = place.find(schema+'ExtendedData')
  p_data = place.find(schema+'ExtendedData').find(schema+'SchemaData').findall(schema+'SimpleData');

  found = False
  url = None
  for e in p_data:
    if 'Location' in e.attrib.values():
      location = e.text
      if 'Sutton' in location:
        found = True
        suttonians += 1
      else:
        others += 1
    if 'More_Information' in e.attrib.values():
      url = e.text

  if not found:
    folder.remove(place)
  else:
    description = ET.SubElement(place, 'description')
    tag = '<a href="' + url + '">' + location + '</a>'
    cdata = CDATA(tag)
    description.append(cdata)


print "Found", suttonians, "in sutton and ignoring ", others, "others"
planning_tree.write('new.kml', xml_declaration = True, method = 'xml')
print "Finished writing records"

