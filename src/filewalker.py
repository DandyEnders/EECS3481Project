import os
import sys
import subprocess

def walk_files_and_apply_func (walk_directory, func):
    new_folder_name = f"{walk_directory}_result"
    os.system(f"rm -rf {new_folder_name}")
    os.system(f"cp -rf {walk_directory} {new_folder_name}")
    for root, _subdirs, files in os.walk(new_folder_name):
        for file in files:
            full_dir = os.path.join(root, file)
            with open(full_dir, "rb") as f:
                # print(f"Reading file {full_dir}")
                res = func(f.read())

            with open(full_dir, "wb") as f:
                # print(f"Writing file {full_dir}")
                f.write(res)

def walk_files_compare_file_hash (dir1, dir2):
    
    def walk_collect_file_hashes (dir):
        dir_file_hashes = []
        for root, _, files in os.walk(dir):
            for file in files:
                full_dir = os.path.join(root, file)
                std_result = subprocess.check_output(["sha1sum", f"{full_dir}"])
                std_result = std_result.decode("utf-8")
                std_result = std_result.split(" ")[0]
                dir_file_hashes.append((file, std_result))
        return dir_file_hashes
    
    dir1_file_hashes = walk_collect_file_hashes(dir1)
    dir2_file_hashes = walk_collect_file_hashes(dir2)
    
    print("isSameHash?", "Filename", "file1 hash", "file2 hash", sep="\t")
    for pair in zip(dir1_file_hashes, dir2_file_hashes):
        print(pair[0][1] == pair[1][1], pair[0][0], pair[0][1], pair[1][1], sep="\t")
        
    return dir1_file_hashes == dir2_file_hashes
            

# walk_dir = sys.argv[1]

# print('walk_dir = ' + walk_dir)

# # If your current working directory may change during script execution, it's recommended to
# # immediately convert program arguments to an absolute path. Then the variable root below will
# # be an absolute path as well. Example:
# # walk_dir = os.path.abspath(walk_dir)
# print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

# for root, subdirs, files in os.walk(walk_dir):
#     print('--\nroot = ' + root)
#     list_file_path = os.path.join(root, 'my-directory-list.txt')
#     print('list_file_path = ' + list_file_path)

#     with open(list_file_path, 'wb') as list_file:
#         for subdir in subdirs:
#             print('\t- subdirectory ' + subdir)

#         for filename in files:
#             file_path = os.path.join(root, filename)

#             print('\t- file %s (full path: %s)' % (filename, file_path))

#             with open(file_path, 'rb') as f:
#                 f_content = f.read()
#                 list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
#                 list_file.write(f_content)
#                 list_file.write(b'\n')