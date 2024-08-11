#   мод a - запись и помещение новых данных в конец файла
#   мод w - запись новых данных, с удалением старых данных
#   мод r - чтение данных из файла

# var = input("Write some text, please ")
# fw = open('doc/file.txt', 'a')
# fw.write(var)
# fw.close()

# fw = open('doc/file2.txt', 'w')
# fw.write("Hello !")
# fw.close()

fr = open('doc/file.txt', 'r')
text = fr.read()
fr.close()

print(text)