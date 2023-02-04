'''
Control the Thread of all apps.
'''
# IMPORTS
import Screen_shot_helper
import Functions


def main():
    regex_full_date = '(^[^.]*.)'
    regex_partial_date = '(^[^H]*.)'
    date_hour_separator = 'H'
    Screen_shot_helper.screen_shot_helper(regex_full_date,regex_partial_date,date_hour_separator)


if __name__ == '__main__':
    main()

