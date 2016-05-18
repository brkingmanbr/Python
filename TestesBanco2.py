import pymysql

parametros = {'user':'root',
              'host':'localhost',
              'passwd':'',
              'database':'casa'}

db = pymysql.connect(**parametros)

c = db.cursor()
#for i in xrange(5): c.execute("INSERT INTO teste VALUES (%s, 'teste%s')"%(i, i))
    
c.execute('SELECT * FROM teste')
x = c.fetchone()
for y in x:
	print(x)

db.close()
