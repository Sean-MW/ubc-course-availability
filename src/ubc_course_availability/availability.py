from scraper import scrape_classes, get_available_classes
from alert import email_alert
import os
from dotenv import load_dotenv


load_dotenv()

PHONE_NUM_EMAIL = os.environ['PHONE_NUM_EMAIL']


def availability(alerts):
    for alert in alerts:
        classes = scrape_classes(alert['department'], alert['course_num'])
        available_classes = get_available_classes(classes, alert['term'])
        available_classes = [c for c in available_classes if c.section in alert['sections']]
        if len(available_classes) == 0:
            print('No classes currently available.')
            return
        print('Available Classes:')
        available_classes_str = ''
        for idx, ubc_class in enumerate(available_classes):
            available_classes_str += str(ubc_class)
            if idx < len(available_classes) - 1:
                available_classes_str += '\n'
        print(available_classes_str)
        email_alert('Found available classes!', available_classes_str, PHONE_NUM_EMAIL)

