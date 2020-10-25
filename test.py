from src import filewalker

print("TEST1: encryption, Every hash must be different.")
filewalker.walk_files_compare_file_hash("data", "data_result")
print("TEST2: decryption, Every hash must be same.")
filewalker.walk_files_compare_file_hash("data", "data_result_result")