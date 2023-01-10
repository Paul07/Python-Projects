import sqlite3
conn = sqlite3.connect('dBdata.db')#creates the dB dBdata.db
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    col_types TEXT)')#creates table_files with 2 columns. 1 id and 1 for string values
conn.commit()


conn = sqlite3.connect('dBdata.db')
#3 list of provided items
fileList = ('information.docx', 'Hello.txt', 'myIamge.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

for x in fileList:
    if x.endswith('.txt'):#looks for items that end in .txt
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO tbl_files (col_types) VALUES (?)', (x,))
            print(x)
conn.close()


    
