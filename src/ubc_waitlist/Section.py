import pyshorteners


class Section:
    url = 'https://courses.students.ubc.ca/cs/courseschedule' \
          + '?pname=subjarea&tname=subj-section'
    unavailable_statuses = ['Blocked', 'Restricted', 'Full', 'STT']

    def __init__(self, department, course_number, section_number, status, term,
                 activity):
        self.department = department
        self.course_number = course_number
        self.section_number = section_number
        self.status = status
        self.term = term
        self.activity = activity
        self.section_url = self.url
        self.section_url += f'&dept={self.department}' \
                            f'&course={self.course_number}' \
                            f'&section={self.section_number}'

    def available(self):
        if self.status not in self.unavailable_statuses:
            return True
        return False

    def url_shorten(self):
        shortener = pyshorteners.Shortener()
        return shortener.tinyurl.short(self.section_url).split('//')[1]

    def __str__(self):
        return f'{self.department} ' \
               + f'{self.course_number} ' \
               + f'{self.activity} ' \
               + f'{self.section_number} ' \
               + f'[term: {self.term}]\n' \
               + f'{self.url_shorten()}'
