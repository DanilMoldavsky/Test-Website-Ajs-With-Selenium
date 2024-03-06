import json

class Utilities:
    @staticmethod
    def get_string(path):
        with open(path, 'r', encoding='utf-8') as f:
            strings = f.read().splitlines()
        return strings

    @staticmethod
    def plus_cnt(path):
        
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        cnt = data['cnt']
        cnt += 1
        trying = data['try']
        data_out = {'cnt': cnt, 'try': trying}
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data_out, f)
    
    @staticmethod
    def plus_try(path):
        
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        cnt = data['cnt']
        trying = data['try']
        trying += 1
        data_out = {'cnt': cnt, 'try': trying}
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data_out, f)
