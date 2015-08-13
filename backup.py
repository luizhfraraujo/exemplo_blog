import pypyodbc

#Função backup
def backup():
  #Nome do banco que vai ser realizado o Backup
  __dbname = "MeuBanco"

  #Pasta de destino
  __destinationpath = "C:\Teste\\"

  #Driver de conexão (No caso SQL Server)
  __driver = "{SQL Server}"

  #Servidor a ser acessado
  __server = "."

  #Database para aceesar (deixar default: master)
  __database = "master"

  #Usuário do banco
  __user = "sa"

  #Senha do banco
  __passwd = "sa"

  #Aqui será criada a connection string, de acordo com os dados passados
  __connectionString = 'Driver=%s;Server=%s;Database=%s;uid=%s;pwd=%s' % (__driver,__server,__database,__user,__passwd)

  #Conexão sera aberta
  __connection = pypyodbc.connect(__connectionString,autocommit=True)

  #Criando o cursor
  __cursor = __connection.cursor()

  #Exibe na tela uma mensagem informando que sera realizado um backup, e executa o cursor logo em seguida
  print("Criando Backup de %s em %s" % (__dbname, __destinationpath))
  __cursor.execute("BACKUP DATABASE ? TO DISK=? WITH NOFORMAT, INIT, NOUNLOAD, NAME ='? Backup', NOSKIP, STATS = 10", [__dbname, __destinationpath + __dbname + '.bak'], __dbname)
  while __cursor.nextset():
    pass

#Inicia o código
if __name__ == '__main__':
  #chama função backup
  backup()