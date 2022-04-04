import rrdtool as rd

def consultar(start, end):
	result = rd.fetch('../media/traficoTCP.rrd', 'AVERAGE', 
			'-s ' + str(start), '-e ' + str(end))
	start, end, step = result[0]
	ds = result[1]
	rows = result[2]
	#print("start: " + str(start) + "\nend: " + str(end))
	#print('\nDatasource: ' )
	#print(ds)
	return result


