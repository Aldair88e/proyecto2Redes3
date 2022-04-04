from fetch import consultar
from getSNMP import consultaSNMP
from getSNMP2 import consultaStringSNMP
import rrdtool as rdt
import datetime
import os

lastup = rdt.lastupdate('../media/traficoTCP.rrd')
lastDate = lastup['date']
host = '192.168.0.174'

print('Introduce la fecha inicial de consulta siguiendo el siguiente formato aaaa-mm-dd-hh-mm-ss la fecha debe ser anterior a ' + str(lastDate))
fechaString = input()
#fechaString = '2022-04-02-14-24-00'
comp = fechaString.split('-')
dateStart = datetime.datetime(int(comp[0]), int(comp[1]), int(comp[2]), int(comp[3]), int(comp[4]), int(comp[5]))



print('Introduce la fecha final de consulta siguiendo el siguiente formato aaaa-mm-dd-hh-mm-ss la fecha debe ser anterior a ' + str(lastDate) + ' y superior a ' + str(dateStart))
fechaString = input()
#fechaString = '2022-04-02-14-29-00'
comp = fechaString.split('-')
dateEnd = datetime.datetime(int(comp[0]), int(comp[1]), int(comp[2]), int(comp[3]), int(comp[4]), int(comp[5]))

print(dateStart.timestamp())
print(dateEnd.timestamp())
res = consultar(int(dateStart.timestamp()), int(dateEnd.timestamp()))

#print(res)

os.system('clear')
reporte = '\ndevice: '
device = consultaSNMP('comunidadASR', host, '1.3.6.1.2.1.1.5.0')

reporte = reporte + device + '\n'
descripcion = consultaStringSNMP('comunidadASR', host, '1.3.6.1.2.1.1.1.0')

reporte = reporte + 'description: ' + descripcion + '\n'

email = consultaSNMP('comunidadASR', host, '1.3.6.1.2.1.1.4.0')
reporte = reporte + 'email: ' + email + '\ndate: ' + str(datetime.datetime.now()) + '\n'

reporte = reporte + 'defaultProtocol: radius\n'


dateEpoch = res[0][0]
step = res [0][2]

for row in res[2]:
	if row[0]!= None:
		reporte = reporte + '\nrdate: ' + str(datetime.datetime.fromtimestamp(dateEpoch)) + '\n'
		reporte = reporte + '#Acct-Input-Packets\n47: ' + '{:.2f}'.format(row[0]) + '\n'
		reporte = reporte + '#Acct-Output-Packets\n48: ' +  '{:.2f}'.format(row[1]) + '\n'
		reporte = reporte + '#Acct-Input-Octets\n42: ' +  '{:.2f}'.format(row[2]) + '\n'
		reporte = reporte + '#Acct-Output-Octets\n43: ' +  '{:.2f}'.format(row[3]) + '\n'
	dateEpoch = dateEpoch + step


print(reporte)
archivo = open('../media/reporte.txt', 'w')
archivo.write(reporte)
archivo.close()


