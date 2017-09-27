# Anti-Duplicator

This script detects duplicate files in specified folder and prints list of them. The following information about each set of doublicates is printed to console:
1) MD5 hash, which can be used afterwards in another programms
2) Full path to each dublicate

# Quickstart

Place duplicates.py somewhere. Then run command line, go to folder in which you moved script and execute it with one parameter containing path to folder with duplicates.

Example of script launch on Linux, Python 3.5:

```#!bash

$ python duplicates.py <path to folder>

```

Output data example:

```#!bash

1) 2 files with 76e6ad8e57f2a89b602e0cebd2ea4f14 MD5 hash were found:
    1. C:\TEST_FOLDER\TEST_SUBDOLER\Новый текстовый документ.txt
    2. C:\TEST_FOLDER\TEST_SUBDOLER\TEST_SUBFOLER_2\ООО.txt
2) 2 files with e3aeaa1bdffc84b1040e6a7be44e6132 MD5 hash were found:
    1. C:\TEST_FOLDER\TEST_SUBDOLER\TEST_SUBFOLER_2\ksmdfsdf.txt
    2. C:\TEST_FOLDER\TEST_SUBDOLER\TEST_SUBFOLER_2\TEST_SUBFOLER_3_1\kssdasd.txt
3) 2 files with 3f9e29fe88c9322ce8095fe5ee8624b6 MD5 hash were found:
    1. C:\TEST_FOLDER\___thumbnails.bat
    2. C:\TEST_FOLDER\TEST_SUBDOLER\TEST_SUBFOLER_2\TEST_SUBFOLER_3_1\___thumbnails.bat
......

```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

