import sqlite3

diphthong=["zh","ch","sh"]#双声母
all_initials=['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's', 'y', 'w']
k=0

conn=sqlite3.connect("target.db")
c=conn.cursor()
c.execute('''CREATE TABLE 拆分表(
       ID INT PRIMARY KEY     NOT NULL,
       汉字           TEXT    NOT NULL,
       声母            TEXT     NOT NULL,
       韵母        TEXT NOT NULL );''')
#此段用于初始化SQLite表格
    
OriginalData=open("material.txt",encoding="UTF-8")
while 1:
    f=OriginalData.readline()
    f_split=f.split(" ")
    character=initial=vowel=""
    if f == "":
        break
    if "Z">=f>="A" or f=="\n":
        continue
    for i in range(0,len(f_split)):
        character=f_split[i][0]
        if not f_split[i][2:3] in all_initials:
            initial=""
            for m in f_split[i][2::]:
                if m==")":
                    break
                vowel+=str(m)
        elif f_split[i][2:4] in diphthong:
            initial=str(f_split[i][2:4])
            for m in f_split[i][4::]:
                if m==")":
                    break
                vowel+=str(m)
        else:
            initial=f_split[i][2:3]
            for m in f_split[i][3::]:
                if m==")":
                    break
                vowel+=m
        c.execute("INSERT INTO 拆分表 (ID,汉字,声母,韵母) VALUES (?,?,?,?)",(k,character,initial,vowel))
        character=initial=vowel=""
        k+=1
        print(k)
OriginalData.close()
conn.commit()
conn.close()