# coding=utf-8
"""Extract messenger messages."""

import json

if __name__ == '__main__':
    mess = json.loads(open('mess.json').read(), encoding='latin1')
    messages = [m['content'].encode('latin_1').decode('utf-8').lower() for m in mess['messages'] if 'content' in m]
    mess2 = json.loads(open('mess2.json').read(), encoding='latin1')
    messages2 = [m['content'].encode('latin_1').decode('utf-8').lower() for m in mess['messages'] if 'content' in m]
    with open('out_ko.txt', 'w', encoding='utf-32') as out_file:
        for m in messages:
            out_file.write(m + '\n')
        for m in messages2:
            out_file.write(m + '\n')
