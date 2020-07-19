1)login to weblogic docker container

2)navigate to wlst path
Ex:/u01/oracle/oracle_common/common/bin

3)Place the files dsn_dburl_modify.py and server.properties on path accessible from docker.

4)Modify the properties file as per the new server details

4)Invoke the python script from wlst with the server.properties location as input
./wlst.sh /share/datasource_password/dsn_dburl_modify.py /share/datasource_password/server.properties

5)Restart the managed server to reflect the changes.