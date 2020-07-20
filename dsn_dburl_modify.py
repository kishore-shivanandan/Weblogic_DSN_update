import sys
#read properties file

if len(sys.argv) != 2:
    print "Invalid Arguments"
    exit()
try:
    print "Load properties file"
    properties=sys.argv[1]
    print 'property file location : ',properties
    file=open(properties,'r')
    print "Read properties file"
    exec file
    print "Execute properties file"
    file.close

except:
    print "exception file read"
    exit()  

dsnnames = DATASOURCES.split(',') 
connect(USER,PASSWORD,ADMIN_URL)

edit()
server='AdminServer'
        
for dsn in dsnnames:
        
        startEdit()
        print "came for datasource",dsn
        cd("/JDBCSystemResources/"+dsn)
        targets = get('Targets')
        
        cd("JDBCResource/"+dsn+"/JDBCDriverParams/"+dsn)
        set("Url", JDBC_URL)             
        save()
        activate()
        
        startEdit()
        cd("/JDBCSystemResources/"+dsn)
        set('Targets', targets)
        save()
        activate()
