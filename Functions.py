import os
import re
import zipfile

from PIL import Image
import datetime


# Find all the PNG file in a specific folder and return all the image open
def get_picture(img_path):
    files = []
    regex = r'\.png$'
    for path in os.listdir(img_path):
        # check if we are in folder or if it is a file
        if os.path.isfile(os.path.join(img_path,path)):
            files.append(path) # get every file in the folder, ignore all others folder
    lst_img = [img_path+'\\'+e for e in files if re.search(regex,e.lower())]
    return lst_img


# Creat One Big PNG top to bottom with all the PNG it receive
def creat_new_img(file_open, path):
    # creat a new image with the correct size
    length = 0
    img = []
    img_size = []
    for e in file_open:
        print(e)
        f = Image.open(f'{path}\\{e}')
        img.append(f)
        img_size.append(f.size)
        length = length + f.size[1]
    new_img = Image.new('RGB', (img_size[0][0], length),(250,250,250))

    emplacement_x= 0
    emplacement_y= 0
    # place the file where they should be to be past
    for e in range(len(img)):
        new_img.paste(img[e],(emplacement_y, emplacement_x))
        emplacement_x = emplacement_x + img_size[e][1]
    return new_img


# save files
def save_file(path, file,name,type):
    file_save = f'{path}\\{name}.{type}'
    file.save(file_save)

def creat_folder(path,name):
    try:
        newFolder = f'{path}\\{name}'
        os.makedirs(newFolder)
        print(f'New folder Created for screenshots!'
              f'path: {newFolder}')
    except:
        print("New folder either already exist or was unable to be created for screenshots")


# allow the user to write text
def text_from_user(name_of_the_file,path,name):
    user_text = []
    new_text = ''
    print(f'Comments for the file {name_of_the_file}, enter :qwa to quite the comments mode')
    print(f'enter ":wa" to quit: \n')
    while new_text != ':wa':
        new_text = input()
        if new_text != ':wa':
            user_text.append(new_text)
        else:
            print(f'Comments Over command {new_text} ')
    try:
        file_name = f'{path}\\{name}.txt'
        text_file = open(f'{file_name}','w')
        for e in user_text:
            text_file.write(f'{e}\n')
        file_name.close()
    except:
        print('file allready existed')
    return user_text


#send only the day date
def get_date(date,regex,separator):
    return re.search(regex,date).group(1).replace(separator,'')


#send back the date and hours
def get_date_model(regex,date_hour_separator):
    return re.search(regex, str(datetime.datetime.now())).group(1).replace(' ',date_hour_separator).replace('.','')


def fusion_comments(path,files_names,path_to_save):
    final_file = open(f'{path_to_save}\\all_comments.txt', 'w')
    for e in files_names :
        print(e)
        text_file = open(f'{path}\\{e}.txt','r') #break here
        final_file.write(f'\n text : {e} \n{text_file.read()}')
        text_file.close()
    final_file.close()


#compress in one file all files receive
def compress_files(files,zip_name,zip_path):
    regex_get_name = '/(\\(?:.(?!\\))+$)'
    try:
        print(f'{zip_path}\\{zip_name}.zip')
        zf = zipfile.ZipFile(f'{zip_path}\\{zip_name}.zip', 'w')

        for file_to_write in files:
            #insure to not zip the zip
            if str(file_to_write).lower() != f'{zip_path}\\{zip_name}.zip'.lower():
                print(f' *** Processing file {file_to_write}')
                # spliting to get name
                file_name_unfound = True
                compteur = len(file_to_write)
                file_name = ''

                #get file name without path with extentions
                while file_name_unfound:
                    char = str(file_to_write[compteur-1])
                    if char != '\\':
                        file_name = file_name + char
                    else:
                        file_name_unfound = False
                        print(f'**** Name In Folder : {str(file_name[::-1])}')
                        break
                    compteur = compteur - 1
                zf.write(file_to_write,str(file_name[::-1]), zipfile.ZIP_DEFLATED)

        zf.close()

    except:
        print('Error in compression')



#get all files in the folders with the path in string
def get_all_folder_files(folder_path):
    files = []
    for path in os.listdir(folder_path):
        # check if we are in folder or if it is a file
        if os.path.isfile(os.path.join(folder_path, path)):
            files.append(f'{folder_path}\\{path}')  # get every file in the folder, ignore all others folder
    return files


