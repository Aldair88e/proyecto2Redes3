import time
import rrdtool
from getSNMP import consultaSNMP
total_input_TCP = 0
total_output_TCP = 0
total_input_octets = 0
total_output_octets = 0
while 1:
    total_input_TCP = int(
        consultaSNMP('comunidadASR','192.168.0.174',
                     '1.3.6.1.2.1.6.10.0'))
    total_output_TCP = int(
        consultaSNMP('comunidadASR','192.168.0.174',
                     '1.3.6.1.2.1.6.11.0'))
    total_input_octets = int(
        consultaSNMP('comunidadASR','192.168.0.174',
                     '1.3.6.1.2.1.2.2.1.10.2'))
    total_output_octets = int(
        consultaSNMP('comunidadASR','192.168.0.174',
                     '1.3.6.1.2.1.2.2.1.16.2'))


    valor = "N:" + str(total_input_TCP) + ':' + str(total_output_TCP) + ':' + str(total_input_octets) + ':' + str(total_output_octets)
    print (valor)
    rrdtool.update('../media/traficoTCP.rrd', valor)
   # rrdtool.dump('traficoRED.rrd','traficoRED.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)
