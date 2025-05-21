# problem set 01 : extensions.py

# Prompt the user to input a file name, remove surrounding whitespace, and convert to lowercase
file_name = input("File name: ").strip().lower()

# Check if there's a dot in the file name to identify an extension
if "." in file_name:
    # Split the filename from the right side only once to get the extension
    extension = file_name.rsplit(".", 1)[-1]
else:
    # If there's no dot, treat it as having no extension
    extension = ""

# Match the extension to known MIME types
if extension == "gif":
    print("image/gif")

elif extension == "jpg" or extension == "jpeg":
    # Both .jpg and .jpeg map to the same MIME type
    print("image/jpeg")

elif extension == "png":
    print("image/png")

elif extension == "pdf":
    print("application/pdf")

elif extension == "txt":
    print("text/plain")

elif extension == "zip":
    print("application/zip")

else:
    # If the extension is unknown or missing, use the default MIME type
    print("application/octet-stream")
