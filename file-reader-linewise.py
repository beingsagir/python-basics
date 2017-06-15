with open('sample_text_file.txt', 'r') as infile:
    data = infile.read()
my_list = data.splitlines()

print (my_list)