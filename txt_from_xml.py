import xml.etree.ElementTree as ET
import pathlib
import os

'''
For pulling all the CONTENT element contents from Concordiensis XML files.
Run this from  $path parent directory. 
Remove dot files (rm .*) before running. 
'''

path = input("Path to parent dir")
subDirs = pathlib.Path(path).iterdir()
for subDir in subDirs:
    allPagesList = []
    for file in sorted(os.listdir(subDir)):
        if file.endswith(".xml"):
            fullname = os.path.join(subDir, file)
            tree = ET.parse(fullname)
            root = tree.getroot()

            page = list()
            for child in root:
                word = child.attrib['CONTENT'].strip()
                page.append(word)

            pageString = " ".join(page)
            allPagesList.append(pageString)
            allPagesString = "\n\n".join(allPagesList)

    allPagesFile = open(f"{subDir}.txt",'w')
    allPagesFile.write(allPagesString)
    allPagesFile.close()