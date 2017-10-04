import os
import sys
import hashlib
import argparse


def hashfile(path, blocksize=65536):
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
    for dir_name, subdir_list, file_list in os.walk(filepath):
        for filename in file_list:
            path = os.path.join(dir_name, filename)
            file_hash = hashfile(path)
            if file_hash in unique_hashes:
                if file_hash not in duplicate_files:
                    # More than 2 duplicate files with same hash can exist,
                    # so list of filepaths is created.
                    duplicate_files[file_hash] = []
                    duplicate_files[file_hash].append(unique_hashes[file_hash])
                duplicate_files[file_hash].append(path)
            else:
                unique_hashes[file_hash] = path
    return duplicate_files


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="duplicates detector")
    parser.add_argument("path_to_folder",
                        help="path to folder containig duplicates")
    args = parser.parse_args()
    path = args.path_to_folder
    duplicates = make_duplicate_list(path)
    for idx, (key, value) in enumerate(duplicates.items(), 1):
        print("{}) {} files with {} MD5 hash were " +
              "found:".format(idx, len(value), key))
        for idx, folder in enumerate(value, 1):
            print("    {}. {}".format(idx, folder))
    sys.exit()
