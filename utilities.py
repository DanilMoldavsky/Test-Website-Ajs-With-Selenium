
class Utilities:
    @staticmethod
    def get_string(path):
        with open(path, 'r', encoding='utf-8') as f:
            strings = f.read().splitlines()
        return strings
