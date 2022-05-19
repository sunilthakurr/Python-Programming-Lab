with open('words_count.txt','r') as f:
    data = f.read()
    words = data.split()
    print(words)
    print(len(words))
    f.close()
