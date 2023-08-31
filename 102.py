import os
import shutil
'''

'''

path = 'tree'

isExist = os.path.exists(path)
print(isExist)

print("Before copying all files:")
print(os.listdir(path))
source = "feather.jfif"
destination = "tree/copyfeather.jfif"

dest = shutil.copy(source,destination)
print("After copying files")
print(os.listdir(path))