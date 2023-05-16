class Folder:
    def __init__(self, folder_name, list_of_subfolders, list_of_filenames):
        self.name = folder_name
        self.subfolders = list_of_subfolders
        self.files = list_of_filenames
    def __str__(self):
        return self.name
    
def folder_search(folder,file):
    if file in folder.files:
        return folder
    for subfolder in folder.subfolders:
        result = folder_search(subfolder, file)
        if result is not None:
            return result
    return None

b = Folder('Folder_b', [], ['File_0', 'File_1', 'File_2'])
c = Folder('Folder_c', [], ['File_3', 'File_4'])
a = Folder('Folder_a', [b, c], [])
print(folder_search(a, 'File_3'))