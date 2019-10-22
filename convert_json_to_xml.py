import json
with open("C:\\Users\\gnane\\Downloads\\coco_annotations.json") as json_file:
    data = json.load(json_file)
    image=[]
    image_name=[]
    annotation =[]
    b_b=[]
    for i in data['images']:
        image.append(i)
    print (image[0]['file_name'])
    for j in image:
        image_name.append(j['file_name'])
    print (image_name)
    for k in data['annotations']:
        annotation.append(k)
    for i in annotation:
        b_b.append(i['bbox'])
    print (b_b)
    #function to convert  xml
    import xml.etree.ElementTree as ET
    def create_xml(filename, xmin, ymin, xmax, ymax):
        tree = ET.parse('scene00621.xml')
        root = tree.getroot()
        path = 'C:\\Users\\gnane\\PycharmProjects\\object_detection\\images\\' + filename
        # changing a field text
        for elem in root.iter('path'):
            elem.text = str(path)
        for elem in root.iter('filename'):
            elem.text = str(filename)
        for elem in root.iter('width'):
            elem.text = str(512)
        for elem in root.iter('height'):
            elem.text = str(512)

        for elem in root.iter('xmin'):
            elem.text = str(xmin)
        for elem in root.iter('ymin'):
            elem.text = str(ymin)
        for elem in root.iter('xmax'):
            elem.text = str(xmax)
        for elem in root.iter('ymax'):
            elem.text = str(ymax)
        for elem in root.iter('name'):
            elem.text = 'cig_butt'
        filename = filename[:-4]
        tree.write(str(filename + '.xml'))
    for i,b in zip(image_name,b_b):
        filename=i
        xmin=b[0]
        ymin=b[1]
        xmax=b[2]+b[0]
        ymax=b[3]+b[1]
        create_xml(filename, xmin, ymin, xmax, ymax)















