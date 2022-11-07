print('Buenvenido, este programa te ayudara a saber en que cuadrante se encuentra el punto con las coordenadas ingresadas a continuacion.')

resp = 1

while resp == 1:
    x = float(input("Ingresa X:"))
    y = float(input("Ingresa Y:"))

    if x==0 and y==0:
        print (f'Tu punto (',x,',',y,') se encuentra en el origen')
    elif x==0:
        print (f'Tu punto (',x,',',y,') se encuentra sobre el eje Y')
    elif y==0:
        print (f'Tu punto (',x,',',y,') se encuentra sobre el eje X')
    elif x>0 and y>0:
        print (f'Tu punto (',x,',',y,') se encuentra en el Cuadrante I')
    elif x<0 and y>0:
        print (f'Tu punto (',x,',',y,') en el Cuadrante II')
    elif x<0 and y<0:
        print (f'Tu punto (',x,',',y,') se encuentra en el Cuadrante III')
    elif x>0 and y<0:
        print (f'Tu punto (',x,',',y,') se encuentra en el Cuadrante IV')
    resp = int(input('Ingresa 1 si quieres encontrar otro punto, o 0 si queres salir del programra: '))
    if resp == 0:
        print('--------------------------FIN DEL PROGRAMA--------------------------')

