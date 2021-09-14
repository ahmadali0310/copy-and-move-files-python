
import os
import shutil
import random

dict_extensions = {
    'audio_extensions': ('.mp3', '.m4a', '.wav', '.flac'),
    'vidio_extensions': ('.mp4', '.mkv' '.MKV', '.flv', '.mpeg'),
    'document_extensions': ('.docx', '.pdf', '.txt', '.html', '.png', '.css', '.jpg'),
}

folder_location = input("Enter your folder location: ")
copy_or_move = input("You want to copy or move your files: ")
copy_or_move_lower = copy_or_move.lower()
copy = False
move = False
if copy_or_move_lower == 'copy':
    copy = True
elif copy_or_move_lower == 'move':
    move = True
else:
    copy = False
    move = False


def file_finder(folder_path, file_extensions):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files


for file_name, file_extensions in dict_extensions.items():
    print("Calling...")
    # print(file_finder(folder_location, file_extensions))
    folder_name = file_name.split(
        '_')[0] + 'folder' + str(random.randint(1, 100000))
    new_folder_path = os.path.join(folder_location, folder_name)
    print(new_folder_path)
    calling_method = file_finder(folder_location, file_extensions)
    print(len(calling_method))
    if len(calling_method) > 0:
        os.mkdir(new_folder_path)
        for item in calling_method:
            item_location = os.path.join(folder_location, item)
            if copy:
                shutil.copy(item_location, new_folder_path)
            elif move:
                shutil.move(item_location, new_folder_path)
            else:
                print("Not recognizible")
    else:
        print('No '+file_name.split('_')[0]+' files')
