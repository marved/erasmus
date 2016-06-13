 #!/bin/sh
#Crear antes el directorio backupsDatabase con la ruta correspondiente:
# mkdir /tfg/tfg/backupsDatabase
# necesario editar el fichero /etc/crontab añadiendo la siguiente línea:
#0 3 * * * /home/usuario/scripts/mysqlrespaldo.sh
#El archivo de crontab tiene la siguiente estructura de izquierda a derecha:
#-Minutos (rango de 0-59)
#-Horas (0-23)
#-Día del mes (1-31)
#-Mes (1-12)
#-Día de la semana (0-6 siendo 0=Domingo)
#-Path completo al script o programa que queramos ejecutar

 mysqldump -uroot -ppwd --opt /tfg/tfg/db.sqlite3 > /tfg/tfg/backupsDatabase/db.sqlite3
 cd /tfg/tfg/backupsDatabase/
 tar -zcvf database_$(date +%d%m%y-%H%M%S).tgz db.sqlite3
 find -name '*.tgz' -type f -mtime +7 -exec rm -f {} ;
