from bs4 import BeautifulSoup
from requests_html import HTMLSession
from Course import Course


table_columns = ['status', 'section', 'activity', 'term', 'delivery', 'interval', 'days', 'start',
                 'end', 'comments', 'in_person']
url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&'
session = HTMLSession()


def scrape_classes(department, course):
    classes = []
    response = session.get(url + f'dept={department}&course={course}')
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class':'table table-striped section-summary'})
    if not table:
        return classes
    for row in table.findAll('tr')[1:]:
        col = row.findAll('td')
        values = []
        for val in col:
            values.append(val.getText())
        class_info_dict = dict(zip(table_columns, values))
        class_info_dict['department'] = department
        class_info_dict['course'] = course
        classes.append(Course(class_info_dict))
    return classes


def get_available_classes(classes, term):
    available_classes = []
    for ubc_class in classes:
        if ubc_class.term == term and ubc_class.available():
            available_classes.append(ubc_class)
    return available_classes
