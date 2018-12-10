import datetime

year = int(input('Introduce un año: '))
month = int(input('Introduce un mes: '))
day = int(input('Introduce un dia: '))


user_date = datetime.datetime(year=year, month=month, day=day)

time_remaining = user_date - datetime.datetime.now()

print('Faltan {} dias y {} horas para esa fecha'.format(time_remaining.days, int(time_remaining.seconds / 60/60)))

print('Mañana es dia: \n{}'.format(datetime.datetime.now() + datetime.timedelta(days=1)))

'''
Crea un programa que te diga la fecha de hace 5 días respecto a hoy, y el día de la semana.
'''
dias_atras = 5
fecha_calculada = (datetime.datetime.now()-datetime.timedelta(days=dias_atras))
dicdias = {'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles','THURSDAY':'Jueves', \
'FRIDAY':'Viernes','SATURDAY':'Sabado','SUNDAY':'Domingo'}
print('Hace {} dias la fecha era {} {}'.format(dias_atras, dicdias[fecha_calculada.strftime('%A').upper()], fecha_calculada.strftime('dia %d del %m de %Y')))



'''
Crea un programa que te diga cuando falta para tu cumpleaños y que día de la semana será.
'''

dia_cumpleanos = datetime.datetime(year=2019, month=10, day=3)
dias_restantes = dia_cumpleanos - datetime.datetime.now()

print('Para tu cumpleaños faltan {} dias y sera un {}'.format(int(dias_restantes.total_seconds()/3600/24), dia_cumpleanos.strftime('%A')))


'''
Crea un programa que te diga, introduciendo cualquier fecha, cuantas horas han pasado desde ese momento.
'''
fecha_transcurrida = datetime.datetime.now() - user_date
print('Han pasado {} horas'.format(int(fecha_transcurrida.total_seconds()/3600)))