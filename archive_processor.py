'''
module for archive processor (it required patool tool)
- unpack_targz, is unpacking one .tar.gz archive
- unpack_gz, is unpacking one .gz archive
- unpack_all, is unpacking all .zip and .gz archives in folder
'''

import os
import tarfile


def unpack_targz():
    '''
    function for unpacking .tar.gz archive
    '''
    print("Enter the path, in that format:",
              '\n',
              'C:\\test.../file.tar.gz')
    path_to_file = input()
    tar = tarfile.open(path_to_file, "r")
    tar.extractall()
    tar.close()

def unpack_gz():
    '''
    unpacking one .gz archive
    '''
    import patoolib
    print("Enter the path, in that format:",
          '\n',
          'C:\\test.../file.gz')
    path_to_file = input()
    print("Enter the path, in that format:",
          '\n',
          'C:\\test...\\folder_for_unpacked_files')
    path_to_unpack_folder =input()
    if os.path.exists(path_to_unpack_folder):
        pass
        # skip if folder exist
    else:
        os.makedirs(path_to_unpack_folder)
    patoolib.extract_archive(path_to_file, outdir=path_to_unpack_folder)

def unpack_all():
    '''
    function for unpacking .zip; .gz; archives
    '''
    import patoolib
    extensions = ['zip', 'gz']
    print("Enter the path, in that format:",
          '\n',
          'C:\\test...\\archive-folder')
    path_to_file = input()
    # getting the path to archives folder
    for i in os.walk(path_to_file):
        # getting info about said folder
        for n in i[2]:
            # round for archives
            file = n.split('.')
            # getting info about archive
            if len(file) >= 2:
                # if file have extension
                fileExtension = file[-1].lower()
                # get file extension
                filefoldername = ''.join(file[:-1])
                # create folder-name for archive stuff
                # (it is name of the archive without extension)
                if fileExtension in extensions:
                    # if extension in allowable
                    if os.path.exists(path_to_file +'\\'+ str(filefoldername)):
                        continue
                        # skip if folder exist
                    else:
                        os.makedirs(path_to_file +'\\'+ str(filefoldername))
                        # making directory for files
                        path_to_unpack_folder = path_to_file +'\\'+ str(filefoldername)
                        # string variable for way to unpacking folder
                        uaf = path_to_file +'\\'+ str(n)
                        # string variable for full path to unpacking file
                        patoolib.extract_archive(uaf, outdir=path_to_unpack_folder)
                        # unpacking file to directory
                else:
                    print("Extension not supported - ",  n)
            else:
                print("File-type is empty")

if __name__ == '__main__':
    uda = unpack_gz()