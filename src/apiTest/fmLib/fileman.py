import json, base64
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
    print(f"File creation failed. Exception: \n{exception}")
    return False
  finally:
    path = directory+name+"."+extension
    f.close()
    f = None
    return path

def readF(path):
  """
  Opens an existing file and returns its contents.
  Parameters:
  path: The path to the file. This argument must be passed. This is from the scope of the library folder.
  """
  try:
    f = open(path)
    c = f.read()
  except Exception as exception:
    print(f"File opening/read failed. Exception: \n{exception}")
    return False
  finally:
    f.close()
    f = None
    return c
  
def readS(path, type="json"):
  """
  Reads specially formatted files and returns their data.
  Parameters:
  path: The path to the file. This argument must be passed.
  type: The data type to read from the file. Options: json, xml, base64. Default is json.
  """
  try:
    f = open(path)
    c = f.read()
  except Exception as exception:
    print(f"File opening/read failed. Exception: \n{exception}")
    return False
  finally:
    match type:
      case "json":
        j = json.load(f)
        f.close()
        f = None
        return j
      case "xml":
        e = ET.parse(path)
        f.close()
        f = None
        return e
      case "base64":
        b = base64.base64decode(c)
        f.close()
        f = None
        return b
      
    
