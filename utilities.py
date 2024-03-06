
class Utilities:
    def __init__(self):
        self.strings = []
    
    def get_string(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            self.strings = f.read().splitlines()
        return self.strings

    