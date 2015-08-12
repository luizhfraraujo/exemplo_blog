import pypyodbc

class main():
  __dbname = ""
  __destinationpath = ""
  __driver = ""
  __server = ""
  __database = ""
  __user = ""
  __passwd = ""
  __connectionString = 'Driver=%s;Server=%s;Database=%s;uid=%s;pwd=%s' % (__driver,__server,__database,__user,__passwd)
  __connection = pypyodbc.connect(__connectionString,autocommit=True)
  __cursor = __connection.cursor()
  __cursor.execute("BACKUP DATABASE ? TO DISK=? WITH NOFORMAT, INIT, NOUNLOAD, NAME ='? Backup', NOSKIP, STATS = 10", [__dbname, __destinationpath + __dbname + '.bak'], __dbname)
  while __cursor.nextset():
    pass

if __name__ == '__main__':
  main()
