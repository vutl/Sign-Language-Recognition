import os

dir_path = r'C:\Users\Vinh Tran\Desktop\DataForLife2024\MiAI_Hand_Lang\data2'
res = []
num_name = []
for i in range(1,203):
      tmp = r'C:\Users\Vinh Tran\Desktop\DataForLife2024\MiAI_Hand_Lang\data2\b_' + str(i) + '.png'
      num_name.append(tmp)

count = 0
# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
      if os.path.isfile(os.path.join(dir_path, file_path)) and file_path[0:2] == 'b_':
        # add filename to list
            full_path = dir_path + '/' + file_path
            os.rename(full_path, num_name[count])
            count += 1

for file_path in os.listdir(dir_path):
      if os.path.isfile(os.path.join(dir_path, file_path)) and file_path[0] == 'b':
            res.append(file_path) 
print(res)