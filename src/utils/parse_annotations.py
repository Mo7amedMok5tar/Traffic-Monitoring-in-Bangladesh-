import sys
import xml.etree.ElementTree as ET
sys.path.append("../src")
from utils.xml_to_yolo_bbox import xml_to_yolo_bbox

classes = [
    "ambulance",
    "army vehicle",
    "auto rickshaw",
    "bicycle",
    "bus",
    "car",
    "garbagevan",
    "human hauler",
    "minibus",
    "minivan",
    "motorbike",
    "pickup",
    "policecar",
    "rickshaw",
    "scooter",
    "suv",
    "taxi",
    "three wheelers (CNG)",
    "truck",
    "van",
    "wheelbarrow",
]

class_mapping = {name :idx for idx ,name in enumerate(classes)}


def parse_annotations(f):
    """Parse all of the objects in a given XML file to YOLO format.

    Input:  f      The path of the file to parse.

    Output: A list of objects in YOLO format.
            Each object is a list [index, x_center, y_center, width, height]."""
    
    objects =[]

    tree = ET.parse(f)
    root = tree.getroot()

    width= int (root.find("size").find("width").text)
    height= int (root.find("size").find("height").text)

    for obj in root.findall("object"):
        label= obj.find("name").text
        class_id = class_mapping[label]
        bbox= obj.find("bndbox")
        xmin=int(bbox.find("xmin").text)
        ymin=int(bbox.find("ymin").text)
        xmax=int(bbox.find("xmax").text)
        ymax=int(bbox.find("ymax").text)

        yolo_bbox = xml_to_yolo_bbox([xmin, ymin, xmax, ymax], width, height)

        objects.append([class_id]+yolo_bbox)

    return objects

