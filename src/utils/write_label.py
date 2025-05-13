def write_label(objects, filename):
    """Write the annotations to a file in the YOLO text format.

    Input:  objects   A list of YOLO objects, each a list of numbers.
            filename  The path to write the text file."""
    

    with open( filename , "w")as f:
        for obj in objects :
            line = " ".join(str(x) for x in obj)
            f.write(line+"\n")