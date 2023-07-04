import os
import pandas as pd
import hashlib
import magic
import mimetypes

# specify the directory path where the files are located
dir_path = 'C:\\Users\\Mario\\Downloads\\Lab2_download_1'

# create an empty list to store the file names
file_names = []
# create an empty list to store the extensions
extensions = []
# create an empty list to store MD5
md5s = []
# create an empty list to store SHA1
sha1s = []
# create an empty list to store SHA256
sha256s = []
# create an empty list to store magic numbers
magic_numbers = []
# create a magic object
magic_object = magic.Magic(mime=True)
# create an empty list to check if extensions match
extension_matches = []

# iterate through all files in the directory
for file in os.listdir(dir_path):
    # check if the file is a regular file (i.e., not a directory)
    if os.path.isfile(os.path.join(dir_path, file)):
        # if so, add the file name to the list
        (file_name, extension) = os.path.splitext(file)
        file_names.append(file_name)
        extensions.append(extension)

        with open(file, 'rb') as f:
            data = f.read()

            md5 = hashlib.md5(data).hexdigest()
            md5s.append(md5)

            sha1 = hashlib.sha1(data).hexdigest()
            sha1s.append(sha1)

            sha256 = hashlib.sha256(data).hexdigest()
            sha256s.append(sha256)

            magic_number = magic_object.from_file(os.path.join(dir_path, file))
            magic_numbers.append(magic_number)

            # check if the magic number contains the file extension
            if extension.lower() == '':
                 extension_matches.append(False)
            elif mimetypes.guess_type('test'+extension.lower())[0] in magic_number.lower():
                 extension_matches.append(True)
            else:
                extension_matches.append(False)

# create a Pandas dataframe with the file names
df = pd.DataFrame({'file_name': file_names, 'extension': extensions, 'md5': md5s, 'sha1': sha1s, 'sha256': sha256s, 'magic_number': magic_numbers})

# print the dataframe
print(df)
