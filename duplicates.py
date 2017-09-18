import os
import sys
import hashlib


def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def make_duplicate_list(filepath):
    unique_hashes = {}
    duplicate_files = {}
    for dirName, subdirList, fileList in os.walk(filepath):
        for fname in fileList:
            path = os.path.join(dirName, fname)
            file_hash = hashfile(path)
            if file_hash in unique_hashes:
                if file_hash not in duplicate_files:
                    #more than 2 dublicates with same has can exist, so list 
                    #of filepaths is created
                    duplicate_files[file_hash] = []
                    duplicate_files[file_hash].append(unique_hashes[file_hash])
                duplicate_files[file_hash].append(path)
            else:
                unique_hashes[file_hash] = path
    return duplicate_files


if __name__ == '__main__':
    for idx, (key, value) in enumerate(make_duplicate_list(sys.argv[1]).items(), 1):
        print("{}) {} files with {} MD5 hash were found:".format(idx, len(value), key))
        for idx, folder in enumerate(value, 1):
            print("    {}. {}".format(idx, folder))
    sys.exit()
