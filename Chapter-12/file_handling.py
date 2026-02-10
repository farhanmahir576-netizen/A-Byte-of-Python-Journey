# টেক্সট ফাইল তৈরি ও পড়া
poem = '''\
Programming is fun
When the work is done
use Python!'''

with open('test.txt', 'w') as f:
    f.write(poem)

with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')
