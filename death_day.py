
import datetime

AVERAGE_LIFESPAN = 80

SMOKER_PENALIZATION = 10
DRINKER_PENALIZATION = 10
SEDENTARY_PENALIZATION = 20

def print_with_underscores(message):
    print(message)
    print(len(message)*'-')

def ask_yes_or_not(message):
    response = None
    while response != 'S' and response != 'N':
        response = input(message + '[S/N]')
    return response == 'S'

print_with_underscores('¡AVERIGUA CUANDO TE QUEDA DE VIDA!')
print('Completa esta encuesta para saber cuantos años de vida te quedan')

birth_date = input('¿Cual es tu fecha de nacimiento? [dd/mm/yyyy]')

birth_date = datetime.datetime.strptime(birth_date, '%d/%m/%Y')
year_lost = 0

if ask_yes_or_not('¿Fumas?'):
    year_lost += SMOKER_PENALIZATION

if ask_yes_or_not('¿Bebes?'):
    year_lost += DRINKER_PENALIZATION

if not ask_yes_or_not('¿Haces deporte?'):
    year_lost += SEDENTARY_PENALIZATION

lefespan = AVERAGE_LIFESPAN - year_lost
death_day = birth_date + datetime.timedelta(days=lefespan*365)
days_to_death = death_day - datetime.datetime.now()

print('Tu fecha de fallecimiento es {}, te quedan {} para morir'.format(death_day.strftime('%d/%m/%Y'), days_to_death.days))

