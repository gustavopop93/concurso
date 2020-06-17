from django.shortcuts import render

def index(request):
    return render(
        request,
        'index.html',
        {}
    )

descripcionLuna = ["nueva (Totalmente oscura)",
                   "creciente (aumentando a llena)",
                   "cuarto creciente (aumentando a llena)",
                   "menguante (aumentando a llena)",
                   "llena (totalmente iluminada)",
                   "menguante (decrementando de llena)",
                   "cuarto menguante (decrementando de llena)",
                   "creciente (decrementando de llena)"]

meses = [   "Enero", "Febrero", "Marzo", "Abril", 
            "Mayo", "Junio", "Julio", "Agosto", 
            "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def faseLunar(dia, mes, chab):
    chabS = [18, 0, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, 26, 7]
    offsets = [-1, 1, 0, 1, 2, 3, 4, 5, 7, 7, 9, 9]
    if dia == 32:
        dia = 1
    diasEnFase = ((chabS[(chab + 1) % 19] + ((dia + offsets[mes -1]) % 30) + (chab < 1900)) % 30)
    index = int((diasEnFase + 2) * 16/59.0)
    if index > 7:
        index = 7
    estado = descripcionLuna[index]

    # 
    porcentajeLuz = int(2 * diasEnFase * 100 /29)
    if porcentajeLuz > 100:
        porcentajeLuz = abs(porcentajeLuz - 200);
    #dia = "%d-%s-%d" % (dia, meses[mes-1], chab)
    dia = "%d" % (dia)

    return dia, estado, porcentajeLuz

# Funcion proximo() devuelve el numero mas proximo a otro de una lista
def proximo(final, numeros):
    def el_menor(numeros):
        menor = numeros[0]
        retorno = 0
        for x in range(len(numeros)):
            if numeros[x] < menor:
                menor = numeros[x]
                retorno = x
        return retorno

    diferencia = []
    for x in range(len(numeros)):
        diferencia.append(abs(final - numeros[x]))
    return numeros[el_menor(diferencia)]

cuartoCrecienteAux = {}
cuartoMenguanteAux = {}

cuartoCreciente = {}
lunaLlena = {}
cuartoMenguante = {}
lunaNueva = {}

aux1 = {}
aux2 = {}

contCCA = 0
contCMA = 0

contCC = 0
contLL = 0
contCM = 0
contLN = 0

for j in range( 12 ):
    #print("\n")
    # Mes = n + 1
    n = j + 1
    rango = 0
    if( n == 4 or n == 6 or n == 9 or n == 11 ) :
        rango = 30
    elif( n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12 ) :
        rango = 31
    elif( n == 2 ) :
        rango = 29

    #print( "%s - %d " % ( meses[ j ], rango ) )
    # #print(rango)

    for i in range(1, rango + 1):
        dia, estado, porcentajeLuz = faseLunar(i, n, 2020)

        if estado == descripcionLuna[0] and porcentajeLuz == 0:
            # Luna nueva
            #print("dia: %s, Fase: %s, Luz = %d%s" % (dia, estado, porcentajeLuz, '%'))
            lunaNueva[ contLN ] = (dia, estado, porcentajeLuz)
            contLN += 1
        elif estado == descripcionLuna[2] and (porcentajeLuz >= 48 and porcentajeLuz <= 55):
            # Cuarto creciente
            cuartoCrecienteAux[ contCCA ] = ( dia, estado, porcentajeLuz )
            aux1[ contCCA ]  = int( porcentajeLuz )
            contCCA += 1
        elif estado == descripcionLuna[4] and porcentajeLuz == 97:
            # Llena
            #print("dia: %s, Fase: %s, Luz = %d%s" % (dia, estado, porcentajeLuz, '%'))
            lunaLlena[ contLL ] = (dia, estado, porcentajeLuz)
            contLL += 1
        elif estado == descripcionLuna[6] and (porcentajeLuz >= 48 and porcentajeLuz <= 53):
            # Cuarto menguante
            cuartoMenguanteAux[ contCMA ]  = (dia, estado, porcentajeLuz)
            aux2[contCMA] = int(porcentajeLuz)
            contCMA += 1
    contCCA = 0
    contCMA = 0
    proCC = proximo(50, aux1)
    proCM = proximo(50, aux2)
    for c in range( cuartoCrecienteAux.__len__() ) :
        if cuartoCrecienteAux[ c ][ 1 ] == descripcionLuna[2] and cuartoCrecienteAux[ c ][ 2 ] == proCC :
            #print("dia: %s, Fase: %s, Luz = %d%s" % (cuartoCrecienteAux[ c ][ 0 ], cuartoCrecienteAux[ c ][ 1 ], cuartoCrecienteAux[ c ][ 2 ], '%'))
            cuartoCreciente[ contCC ] = (cuartoCrecienteAux[ c ][ 0 ], cuartoCrecienteAux[ c ][ 1 ], cuartoCrecienteAux[ c ][ 2 ])
            contCC += 1

    for h in range( cuartoMenguanteAux.__len__() ) :
        if cuartoMenguanteAux[ h ][ 1 ] == descripcionLuna[6] and cuartoMenguanteAux[ h ][ 2 ] == proCM :
            #print("dia: %s, Fase: %s, Luz = %d%s" % (cuartoMenguanteAux[ h ][ 0 ], cuartoMenguanteAux[ h ][ 1 ], cuartoMenguanteAux[ h ][ 2 ], '%'))
            cuartoMenguante[ contCM ] = (cuartoMenguanteAux[ h ][ 0 ], cuartoMenguanteAux[ h ][ 1 ], cuartoMenguanteAux[ h ][ 2 ])
            contCM += 1
    cuartoCrecienteAux = {}
    cuartoMenguanteAux = {}

contCCA = 0
'''
contCCA = cuartoCreciente.__len__() + cuartoMenguante.__len__() + lunaLlena.__len__() + lunaNueva.__len__()
#print('\n')
#print( cuartoCreciente.__len__() )
#print( cuartoMenguante.__len__() )
#print( lunaLlena.__len__() )
#print( lunaNueva.__len__() )
#print( contCCA )
#print( '\n' )
'''
fechasMes = {}
contCMA = -1
for x in range(15):
    try:
        contCMA += 1
        fechasMes[ contCMA ] = cuartoCreciente[ x ][ 0 ]
        if contCMA == contCCA:
            pass
    except:
        pass
    try:
        contCMA += 1
        fechasMes[ contCMA ] = lunaLlena[ x ][ 0 ]
        if contCMA == contCCA:
            pass
    except:
        pass
    try:
        contCMA += 1
        fechasMes[ contCMA ] = cuartoMenguante[ x ][ 0 ]
        if contCMA == contCCA:
            pass
    except:
        pass
    try:
        contCMA += 1
        fechasMes[ contCMA ] = lunaNueva[ x ][ 0 ]
        if contCMA == contCCA:
            pass
    except:
        pass
    #print("x: %d"%x)

'''
for x in range( fechasMes.__len__() ):
    print( fechasMes[ x ] )
'''
def calendario(request):
    """
    """
    return render(
        request,
        'calendario.html',
        { 'meses': meses, 'dias': fechasMes }
    )

def calendariov2(request):
    """
    """
    
    return render(
        request,
        'calendariov2.html',
        {  }
    )