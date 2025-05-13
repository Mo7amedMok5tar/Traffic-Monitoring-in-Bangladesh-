def xml_to_yolo_bbox(bbox, width, height):
    """Convert the XML bounding box coordinates into YOLO format.

    Input:  bbox    The bounding box, defined as [xmin, ymin, xmax, ymax],
                    measured in pixels.
            width   The image width in pixels.
            height  The image height in pixels.

    Output: [x_center, y_center, bb_width, bb_height], where the bounding
            box is centered at (x_center, y_center) and is of size
            bb_width x bb_height.  All values are measured as a fraction
            of the image size."""

    xmin, ymin, xmax, ymax = bbox
    
    x_center = (xmax+xmin)/2/width
    y_center =  (ymax+ymin)/2/height
    
    bb_width = (xmax-xmin)/width
    bb_height = (ymax-ymin)/height
    
    return [x_center, y_center, bb_width, bb_height]