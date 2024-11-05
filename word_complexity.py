import xml.etree.ElementTree as ET
import os

# Path to the root XML file
root_xml_path = "giga/IGC-News1-22.10.ana/IGC-News1-22.10.ana.xml"

# Define the XInclude namespace
NAMESPACES = {"xi": "http://www.w3.org/2001/XInclude"}

# List to hold paths to linked XML files
linked_files = []

# Parse the root XML file
tree = ET.parse(root_xml_path)
root = tree.getroot()

# Find all <xi:include> elements and get the 'href' attribute
for element in root.findall(".//xi:include", namespaces=NAMESPACES):
    linked_file = element.get("href")
    if linked_file:
        # Resolve the relative path
        linked_file_path = os.path.join(os.path.dirname(root_xml_path), linked_file.strip())
        linked_files.append(linked_file_path)

# List to hold paths to the actual content XML files
content_files = []

# Parse each subfolder XML file to find links to content files
for subfolder_xml in linked_files:  # 'linked_files' is the list of subfolder XML files from the previous step
    tree = ET.parse(subfolder_xml)
    root = tree.getroot()

    # Find all <xi:include> elements in each subfolder XML to get the content file links
    for element in root.findall(".//xi:include", namespaces=NAMESPACES):
        content_file = element.get("href")
        if content_file:
            # Resolve the relative path based on the subfolder XML location
            content_file_path = os.path.join(os.path.dirname(subfolder_xml), content_file.strip())
            content_files.append(content_file_path)

# List to hold extracted text content
extracted_text = []

# Extract text content from each content XML file
for content_xml in content_files:
    tree = ET.parse(content_xml)
    root = tree.getroot()
    if content_files.index(content_xml) % 100000 == 0:
        print(content_files.index(content_xml))
    # Extract text within <w> tags
    for element in root.findall(".//w", namespaces=NAMESPACES):  # Target <w> tag specifically
        text = element.text
        if text:
            extracted_text.append(text.strip())
            

# Combine or save the extracted text as needed
with open("extracted_text.txt", "w", encoding="utf-8") as output_file:
    output_file.write(" ".join(extracted_text))  # Join with spaces to form readable text

print("Text extraction from <w> tags completed.")


