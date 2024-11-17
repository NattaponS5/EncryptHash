import os

# read every file in plant_house_logs_400 folder

folder_path = '/home/nattapons5/vscode/EncryptHash/plant_house_logs_400'

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
        
        # Remove the first line (Timestamp line)
        if content and content[0].startswith('Timestamp:'):
            content = content[1:]
        
        # Write the original content back to the file
        with open(file_path, 'w') as file:
            file.writelines(content)

