import pymysql

parametros = {'user':'root',
              'host':'localhost',
              'passwd':'',
              'database':'casa'}
Banco = pymysql.connect(**parametros)

c = con.cursor()
for i in xrange(5):
    c.execute("INSERT INTO teste VALUES (%s, 'teste%s')"%(i, i))
    
c.execute('SELECT * FROM teste')
c.fetchall()

c.execute('SELECT * FROM teste WHERE id=%d'%3)
c.fetchone()

c.execute('SELECT * FROM teste WHERE nome=%s',('teste%d'%2,))
c.fetchone()

c.execute('SELECT nome FROM teste WHERE id=%s',[1])
c.fetchone()

itens = [(10, 'banana'),
         (11, 'coco'),
         (12, 'carambola')]

c.executemany('insert into teste values (%s, %s)', itens)
con.commit()

c.execute('select * from teste order by nome')
c.fetchall()

