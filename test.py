#list current subdirectories excluding subdirectories of current subdirectories
import os
for root, dirs, files in os.walk(".", topdown=True):
    dirs[:] = [d for d in dirs if d not in ['subdir1', 'subdir2']]
    print(root)
    for name in files:
        print(os.path.join(root, name))