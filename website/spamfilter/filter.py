import re
import os


class SpamFilter:

    def __init__(self):
        banned_names = self._parse_file('banned_names')
        banned_emails = self._parse_file('banned_emails')
        banned_messages = self._parse_file('banned_messages')

        self.RE_BANNED_NAMES = re.compile('Sender name: (%s)\n' % '|'
                                          .join(banned_names))
        self.RE_BANNED_EMAILS = re.compile('Sender mail: (%s)\n' % '|'
                                           .join(banned_emails))
        self.RE_MSG = re.compile('Message: (%s)' % '|'
                                 .join(banned_messages), flags=re.DOTALL)

    def hit(self, msg):
        return (self.RE_BANNED_NAMES.search(msg) or
                self.RE_BANNED_EMAILS.search(msg) or
                self.RE_MSG.search(msg))

    def _parse_file(self, name):
        path = os.path.join(os.path.dirname(__file__), name)
        with open(path) as f:
            return list(filter(len, f.read().split('\n')))


if __name__ == '__main__':
    s = SpamFilter()
    print(s.RE_BANNED_NAMES)
