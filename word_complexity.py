import xml.etree.ElementTree as ET
import glob
import os

# Directory containing the XML files
directory_path = "/Users/reynir/Documents/nlp/FINAL/repo/E2R-Tool/giga/IGC-News1-22.10.ana"

# Define the TEI namespace (you may need to adjust this if the URI differs in your files)
TEI_NAMESPACE = {"tei": "http://www.tei-c.org/ns/1.0"}

# List to hold extracted text
extracted_text = []

# Loop through all XML files in the directory
for filename in glob.glob(os.path.join(directory_path, "*.xml")):
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Extract text by specifying the namespace (replace "YourTargetTag" with the correct tag in TEI)
    for element in root.findall(".//tei:YourTargetTag", namespaces=TEI_NAMESPACE):
        text = element.text
        if text:
            extracted_text.append(text.strip())

# Combine or save the extracted text as needed
with open("extracted_text.txt", "w", encoding="utf-8") as output_file:
    output_file.write("\n".join(extracted_text))

print("Text extraction completed.")
