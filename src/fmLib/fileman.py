import json
import xml.etree.ElementTree as ET
def newF(name, directory="../", extension="txt"):
  """
  Creates a new file and returns its file path.
  Parameters:
  name: The new file's name. This argument must be passed.
  directory: The directory to hold the new file. Default is the directory the library resides in. If the directory does not exist, it will be created.
  extension: The file extension the file will use. Default is txt.
  """
  try:
    f = open(f"{directory}{name}.{extension}", "x") # makes the new file
  except Exception as exception:
    # if some error happens, handle it
    print(f"File opening failed. Exception: \n{exception}")
  finally:
    path = directory+name+"."+extension
    return path
  return
def readF(path, write=False):
  """
  Opens an existing file and returns its contents.
  Parameters:
  path: The path to the file. This argument must be passed.
  write: If True, sets the file up for writing. This will still return the contents of the file.
  """

def readS(path, type="json"):
  """
  Reads specially formatted files.
  Parameters:
  path: The path to the file. This argument must be passed.
  type: The data type to read from the file. Options: json, xml, base64. Default is json.
  """

