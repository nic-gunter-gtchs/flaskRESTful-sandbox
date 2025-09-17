def newF(name, directory="../", extension="txt"):
  """
  Creates a new file and returns its file path.
  Parameters:
  name: The new file's name. This argument must be passed.
  directory: The directory to hold the new file. Default is the directory the library resides in. If the directory does not exist, it will be created.
  extension: The file extension the file will use. Default is txt.
  """

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

