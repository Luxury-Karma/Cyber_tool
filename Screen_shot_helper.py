
import os
import time
import keyboard
import pyautogui
import Functions

"""
    Screen Shot helper do : 
        Creat a folder in picture windows default folder to put the screen shot AND Comments later
        Take inpute of keyboard to take screen shot of the whole screen
        at the end make all the picture and comments taken in a PDF and compress it

"""



# get all the user input end send them back to put them in the correct variables
def screen_shot_helper_settings(regex_full_date, date_hour_separator, regex_partial_date, stop_key, date):
    '''
    :param regex_full_date: split the date
    :param date_hour_separator: The separation between the date and the hours side of the DATE
    :param regex_partial_date: spilt the date to get partial
    :param stop_key: key to stop the program
    :return: Setting (in order) Screen shot Button, Name Of Final PDF, If we modify PNG name, if we want to comment the
    pictures, path for the pictures
    '''

    personal_name = False
    comments = False
    setting = []

    print("This script will take screenshots and save them in the scripts Dir")
    print(f'To stop taking screenshots press {stop_key}')
    print(f'The day is formatted Year, month, Day. The date is '
          f'{date}')
    screenShotButton = input("Please enter the key youd like to use to take a screenshot: ")
    setting.append(screenShotButton)
    pdf_img_name = input('name for the final pdf: ')
    setting.append(pdf_img_name)
    choice = input('do you want to personalise the name of the pictures ? y/n')
    if choice.lower() == 'y':
        personal_name = True
    choice = input('Do you want to comment the pictures ? y/n: ')
    if choice.lower() == 'y':
        comments = True
    setting.append(personal_name)
    setting.append(comments)
    # ask where to put the image
    path = input('Please enter the name of the folder you want to download')
    path = f'C:\\Users\\PC\\Pictures\\{path}'  # possible to change the path
    setting.append(path)
    return setting


# Try to creat the folder to keep the files
def screen_shot_helper_make_directory(path, date):
    try:
        os.makedirs(path)
        print("Main Screenshot folder has been created!")

    except:
        print("New folder either already exist or was unable to be created for the Main Screenshot folder")

    Functions.creat_folder(path, date)


# return name of the files
def screen_shot_helper_name_handler(personal_name, number_of_pictures):
    '''
    :param personal_name: Do we ask for a name
    :return: the name of the file
    :number_of_pictures:The number of key pressed
    '''
    file_name = ''
    if not personal_name:
        file_name = int(number_of_pictures)
    else:
        file_name = input('What is the name of the screen shot ? : ')
    return file_name


# listen key to take picture
def screen_shot_helper_listener(picture_key, path, comments, personal_name, stop_key,regex_full_date:str,regex_partial_date:str,date_hour_separator:str):
    '''
    :param picture_key: The key to press to take screen shot
    :param path: Directory to put all files
    :param comments:
    :param personal_name:
    :param stop_key:
    :return: list of all the names in the file to compile (png,txt)
    '''
    # Key lisnter that will take a screenshot when a key is pressed
    names = []
    text_names = []

    press_time = 0
    while True:
        try:
            if keyboard.is_pressed(picture_key):  # listens for the key press
                time.sleep(.5)
                press_time = press_time + 1
                try:  # trys to take a screenshot and save it
                    name = screen_shot_helper_name_handler(personal_name, press_time)
                    name = str(name)
                    myScreenshot = pyautogui.screenshot()
                    myScreenshot.save(f'{path}\screenshot_{name}.png')
                    names.append(f'screenshot_{name}.png')
                    print(f'A screenshot {name} was taken')
                    # APPLY COMMENTARY SETTING
                    if comments:
                        Functions.comments_helper(f'Text_{name}.txt',path)
                        text_names.append(f'Text_{name}')

                except:  # Lets user know the screenshot was unnable to be taken
                    print("A screenshot was unable to  be taken")
            if keyboard.is_pressed(stop_key):  # listen for the ` to be pressed signaling the session

                print(f"you have pressed {stop_key}. Breaking loop now\nsave path {path}")
                break


        except:  # Doesnt really work
            print('error')
    return [names, text_names]


# save all the files
def screen_shot_helper_save(path, date, names, pdf_img_name, text_names, comments):
    try:
        try:
            os.mkdir(f'{path}\\{date}')
        except:
            print('folder allready exist')
        for e in names:  # goes through the 'names[]' list and adds each screenshot to the pdf that was created
            print(f"{e} was added to the PDF")
        Functions.save_file(f'{path}\\{date}', Functions.creat_new_img(names, path), pdf_img_name, 'PDF')
        if comments:
            Functions.fusion_comments(path, text_names, f'{path}\\{date}')
            print('PDF saved\nA full commentary have been created')
            Functions.compress_files(Functions.get_all_folder_files(f'{path}\\{date}'), f'Compress_{pdf_img_name}',
                                     f'{path}\\{date}')


    except:  # if the screenshots cant be added to the word doc
        print("was unable to add screenshots to file...")
        input("session over")


# Set up the screenshot manager
def screen_shot_helper(regex_full_date,regex_partial_date,date_hour_separator):

    # variables
    stop_key = ']'
    date = Functions.get_date(Functions.get_date_model(regex_full_date, date_hour_separator), regex_partial_date,
                              date_hour_separator)
    picture_key,\
        pdf_img_name,\
        personal_name,\
        comments,\
        path= screen_shot_helper_settings(regex_full_date,date_hour_separator,regex_partial_date,stop_key,date)

    screen_shot_helper_make_directory(path,date)
    #add names of the files to correct list
    names,text_names = screen_shot_helper_listener(picture_key,path,comments,personal_name,stop_key,regex_full_date,regex_partial_date,date_hour_separator)

    # Creates a pdf doc and adds the screenshots
    screen_shot_helper_save(path,date,names,pdf_img_name,text_names,comments)
