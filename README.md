# Twin Duplicity Detector

This Python program is designed to go down a directory tree
searching for duplicate files.
It does this using OS.walk(), blake2b from hashlib and argparse for command line arguments.

### Functions
I have used 3 functions (At this stage.)

##### hash_file: 
This function will be called later to hash a specific file and store that hash and file path as a key/value pair dict.

##### file_hunter:
This function will primarily be looping through the files within the directory tree and calling the hash_file function on required files.

##### main:
This function will handle argument parsing, spinning up the file_hunter function, and it will handle printing the results at the end.

### FlowChart
```mermaid
flowchart TD
    start([Program Called]) --> args(root dir)
    args --> dirLoop(Loop through all files inc;subs)
    dirLoop --> file(Add file_path and file_size to dict)
    file --> dupeSize(Add file_path with duplicate size to dict)
    dupeSize --> hash(Hash all files with duplicate files sizes)
    file -- No Dupe Size --> Discard
    
    hash --> store(dict, key = hash, value = list'filename & filepath')
    store -- continueHashing --> dirLoop
    store -- allItemsHashed --> dictLoop(Loop through dictionary)
    dictLoop --> dupHash(Store duplicate hashes in new dict)
    dupHash --> dictLoop
    dupHash --> print(print duplicates filenames and file paths)
    print --> fin([END])

    Notes -- imports --> imports(OS for os.walk, hashlib for file hashing, argparse for cli args)
```