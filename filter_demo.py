from json import *

def filter(line):
    data = loads(line)
    ans = {'created_at':data.pop('created_at'), 'id_str':data.pop('id_str'), 'text':data.pop('text')}
    return ans

if __name__ == "__main__":


    with open('python.txt') as file:
        lines = file.readlines()
        length = len(lines)

        for i in range(length):
            if lines[i] is '\n':
                continue
            temp = filter(lines[i])
            print(temp)




