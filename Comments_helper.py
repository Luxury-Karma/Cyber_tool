'''
On the Press of a bouton put out a file with date and time to write
'''
import Functions
import os


def comment_helper_write(regex_full_date,regex_partial_date,date_hour_separator):
    path = 'C:\\Users\\PC\\Documents'
    name = f'quick_comment_{Functions.get_date(Functions.get_date_model(regex_full_date,date_hour_separator),regex_part, date_hour_separator)}.txt'
    Functions.text_from_user(name, path)

#https://stackoverflow.com/questions/11615455/python-start-new-command-prompt-on-windows-and-wait-for-it-finish-exit
'NEED TO OPPEN NEW CMD FOR THE TXT FILE AND POP IT TO USER' 
def comment_heleper_open_cmd():
    os.system('cmd')

def comments_helper(regex_full_date,regex_partial_date,date_hour_separator):
    comment_helper_write(regex_full_date,regex_partial_date,date_hour_separator)


