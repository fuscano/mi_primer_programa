import math



#PROPIEDADES DE LOS MATERIALES (Pa)

TENSION_FLUENCIA_COBRE = 69*10**6
MODULO_ELASTICO_COBRE = 127.6*10**9

MODULO_ELASTICO_HIERROFUNDIDO= 172.4*10**9

TENSION_FLUENCIA_TORNILLO = 345*10**6
MODULO_ELASTICO_TORNILLO = 206.8*10**9

#MEDIDAS DE MONTAJE (m)

d_interior_cilintro = 0.06
d_exterior_cilindro = 0.12

h_cilintro = 0.14
h_junta = 0.002
h_tapa_ciindro = 0.025

N_tornillos = 12
d_tornillos = 0.01

#PRESIONES DE TRABAJO (N/m2)
P_J = 250*9.8*10**4
P_CILINTRO = 70*9.8*10**4


area_junta = (math.pi/4)*(((d_exterior_cilindro**2-d_interior_cilintro**2))-(N_tornillos*d_tornillos**2))

print('El área de la junta es {} m2'.format(round(area_junta, 4)))

P = (area_junta * TENSION_FLUENCIA_COBRE / 2)

tension_tornillos = P / (N_tornillos*math.pi*(d_tornillos/2)**2)

print('La tension a la que se somete los tornillos es de {} Pa'.format(int(tension_tornillos)))
if tension_tornillos < TENSION_FLUENCIA_TORNILLO:
    print('Lor tornillos resisten esta tension')
elif tension_tornillos >= TENSION_FLUENCIA_TORNILLO:
    print('Lor tornillos NO resisten esta tension')


Q = P_CILINTRO*(math.pi*(d_interior_cilintro/2)**2)

print('La fuerza con la que tira la tapa de los tornillos Q es de {} N'.format(int(Q)))

# Calculamos Km y Kb
k1 = area_junta * MODULO_ELASTICO_HIERROFUNDIDO / h_cilintro
k2 = area_junta * MODULO_ELASTICO_COBRE / h_junta
k3 = area_junta * MODULO_ELASTICO_HIERROFUNDIDO / h_tapa_ciindro
km =1 / ((1/k1) + (1/k2) + (1/k3))
print('La elasticidad de la masa Km es de {} N/m2'.format(int(km)))

kb = (N_tornillos*MODULO_ELASTICO_TORNILLO*math.pi*(d_tornillos/2)**2)/(h_tapa_ciindro+h_junta+h_cilintro)
print('La elasticidad del tornillo Kb es de {} N/m2'.format(int(kb)))

# Calculamos fuerza S

S = Q / (1+(kb/km))

print('La fuerza que le restamos a la masa S es {} N'.format(int(S)))

p_en_junta = (P - S)/area_junta

print('La tension a la que se somete la junta es de {} Pa'.format(int(p_en_junta)))
if p_en_junta > P_J:
    print('La junta resistira estanca')
elif p_en_junta <= P_J:
    print('La junta NO resistira estanca')


# Parametros de fatiga en el bulon
F_perno_max = P + (Q - S)
F_perno_min = P
print('La fuerza maxima en el perno será de {} N y la minima de {} N'.format(int(F_perno_max), int(F_perno_min)))

F_perno_media = (F_perno_max - F_perno_min)/2
F_perno_alternativa = (F_perno_max - F_perno_min)/2
print('La fuerza media será de {} N y la alternativa de {} N'.format(int(F_perno_media), int(F_perno_alternativa)))




