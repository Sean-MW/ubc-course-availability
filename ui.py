import sys
import threading
import queue

from availability import availability
from config import SEARCH_DELAY_MINS


alerts = []


def search_for_course_availability():
    if not alerts:
        print('Nothing to search for.',
              'Please set up an alert before searching for availability.')
        return
    print('Searching for course availability...')
    availability(alerts)
    print(f'Waiting {SEARCH_DELAY_MINS} minutes to try again.',
          'Press ENTER to cancel.')
    if input_with_timeout(60 * SEARCH_DELAY_MINS):
        return  # user interrupt
    search_for_course_availability()


def select_menu_option():
    options = {
        '1': add_new_course_alert,
        '2': remove_course_alert,
        '3': display_current_alerts,
        '4': search_for_course_availability,
        '5': quit_program,
    }
    print('Please select an option:')
    print('[1] Add new course alert')
    print('[2] Remove course alert')
    print('[3] View current alerts')
    print('[4] Search for course availability')
    print('[5] Quit')
    option = input()
    if option not in options:
        invalid_selection(select_menu_option)
    else:
        options[option]()
    select_menu_option()


def add_new_course_alert():
    alert = {}
    print('Department (e.g. CPSC, STAT):')
    alert['department'] = input().upper()
    print('Course Number (e.g. 101, 200):')
    alert['course_num'] = input()
    print('Term (e.g. 1, 2):')
    alert['term'] = input()
    print('Sections (You may enter multiple sections separated by spaces,',
          'e.g. 2A3 L1H):')
    alert['sections'] = input().upper().split()
    alerts.append(alert)
    print('Successfully added alert:', alert)


def display_current_alerts():
    if len(alerts) == 0:
        print('You have no alerts set up.')
        return
    for idx in range(len(alerts)):
        print(f'[{idx + 1}] {alerts[idx]}')


def remove_course_alert():
    print('Select a course to remove:')
    display_current_alerts()
    selection = input()
    if not selection.isdigit() or 0 <= int(selection) > len(alerts):
        invalid_selection(remove_course_alert)
    else:
        del alerts[int(selection) - 1]


def quit_program():
    print('Exiting...')
    sys.exit()


def invalid_selection(retry_func):
    print('Invalid selection. Please try again.')
    retry_func()


# Adapted from r0dn0r's waitForInput.py:
# https://gist.github.com/r0dn0r/d75b22a45f064b24e42585c4cc3a30a0
def input_with_timeout(timeout):
    channel = queue.Queue()
    thread = threading.Thread(target=user_interupt, args=(channel,))
    # by setting this as a daemon thread, python won't wait for it to complete
    thread.daemon = True
    thread.start()
    try:
        _ = channel.get(True, timeout)
        return True
    except queue.Empty:
        return False


def user_interupt(channel):
    res = input()
    channel.put(res)

