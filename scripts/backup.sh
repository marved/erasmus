 #!/bin/sh
#Crear antes el directorio backupsDatabase con la ruta correspondiente:
# mkdir /tfg/tfg/backupsDatabase
 mysqldump -uroot -ppwd --opt /tfg/tfg/db.sqlite3 > /tfg/tfg/backupsDatabase/db.sqlite3
 cd /tfg/tfg/backupsDatabase/
 tar -zcvf database_$(date +%d%m%y-%H%M%S).tgz db.sqlite3
 find -name '*.tgz' -type f -mtime +7 -exec rm -f {} ;
