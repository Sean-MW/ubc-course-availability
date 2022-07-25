import pyshorteners


class Course:
    def __init__(self, class_info):
        self.department = class_info['department']
        self.course = class_info['course']
        self.section = class_info['section'].split(' ')[-1]
        self.status = class_info['status']
        self.term = class_info['term']
        self.activity = class_info['activity']
        self.url = f'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept={self.department}&course={self.course}&section={self.section}'

    def available(self):
        if self.status not in ['Blocked', 'Restricted', 'Full', 'STT']:
            return True
        return False

    def url_shorten(self):
        shortener = pyshorteners.Shortener()
        return shortener.tinyurl.short(self.url).split('//')[1]

    def __str__(self):
        return f'{self.department} {self.course} {self.activity} {self.section} [term: {self.term}]\n{self.url_shorten()}\n'
