from sys import argv
from json import loads, dumps
from datetime import datetime

time_stamp = datetime.now().isoformat()
def update(content):
    if not(type(content) == list or type(content) == tuple or type(content) == dict):
        return content
    
    if type(content) == list or type(content) == tuple:
        for key,item in enumerate(content):
            content[key] = update(item)
    if type(content) == dict:
        for key,value in content.items():
            if key == "updated":
                content[key] = time_stamp
            else:
                content[key] = update(value)
    
    return content


def main():
    path = argv[1]
    with open(path,'r') as file:
        content = loads(file.read())
        content = update(content)
    print(content)
    with open(path,'w') as file:
        file.write(dumps(content))

if __name__ == "__main__":
    main()
