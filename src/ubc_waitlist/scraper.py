from bs4 import BeautifulSoup
from requests_html import HTMLSession
from ubc_waitlist.Section import Section


table_columns = ['status', 'section', 'activity', 'term', 'delivery', 'interval', 'days', 'start',
                 'end', 'comments', 'in_person']
url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&'

session = HTMLSession()


def scrape_sections(department, course_number):
    response = session.get(url + f'dept={department}&course={course_number}')
    soup = BeautifulSoup(response.content, 'html.parser')
    section_table = soup.find('table', {'class':'table table-striped section-summary'})
    if not section_table:
        return []
    return parse_sections(section_table, department, course_number)


def parse_sections(sections_table, department, course_number):
    sections = []
    for row in sections_table.findAll('tr')[1:]:
        col = row.findAll('td')
        values = []
        for val in col:
            values.append(val.getText())
        section_info = dict(zip(table_columns, values))
        section = Section(department,
                          course_number,
                          section_info['section'].split(' ')[-1],
                          section_info['status'],
                          section_info['term'],
                          section_info['activity'])
        sections.append(section)
    return sections


def get_available_sections(sections, term):
    available_sections = []
    for section in sections:
        if section.term == term and section.available():
            available_sections.append(section)
    return available_sections
