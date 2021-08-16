import os
print(os.getcwd())

# change directory
os.chdir('C:\\Users\\Niraj\\test')
print(os.listdir())
print(os.getcwd())

#  make directory
os.mkdir('nishant')

os.rename('nishant', 'laaka')
# remane directory

# removing file and dir
os.remove('test.txt.txt')
os.rmdir('laaka')

os.chdir('C:\\Users\\Niraj')