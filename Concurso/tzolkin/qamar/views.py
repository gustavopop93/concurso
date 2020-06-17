from django.shortcuts import render
import pandas as pd

from .models import Actividad, LunaMes, Mes, LunaActividad, Chab, Fase, LogosPieDePagina

def index(request):
    menu_items = Chab.objects.order_by('chab')
    return render(
        request,
        'index.html',
        {'menu_items': menu_items,}
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
def editarCalendario(request):
    """
    """
    menu_items = Chab.objects.order_by('chab')
    meses = Mes.objects.order_by('pk')
    return render(
        request,
        'editarCalendario.html',
        { 'meses': meses, 'dias': fechasMes, 'menu_items': menu_items }
    )

def calendario(request, pk):
    actividades = Actividad.objects.order_by('pk')
    meses = Mes.objects.order_by('pk')
    cantidadDias = LunaMes.objects.filter(idChab=pk).count()
    lunaActividad = LunaActividad.objects.order_by('pk')
    menu_items = Chab.objects.order_by('chab')
    dias = LunaMes.objects.filter(idChab=pk)
    chab = Chab.objects.filter(pk=pk)
    fases = Fase.objects.order_by('pk')
    logos = LogosPieDePagina.objects.order_by('pk')

    cP = 0
    cS = 0
    cT = 0
    
    tS = 0
    tL = 0
    tSS = 0

    cSDM = 0 #Diciembre-Marzo
    cSMJ = 0 #Marzo-Junio
    cSJS = 0 #Junio-Septiembre
    cSSD = 0 #Septiembre-Diciembre

    cEF = 0 #Frío
    cEC = 0 #Calor
    cEH = 0 #Húmedo
    cEV = 0 #Viento
    cEFF = 0 #Frío

    cMJ = 0 #
    cMF = 0 #
    cMM = 0 #
    cMA = 0 #
    cMMY = 0 #
    cMJN = 0 #
    cMJL = 0 #
    cMAU = 0 #
    cMS = 0 #
    cMO = 0 #
    cMV = 0 #
    cMD = 0 #

    for la in dias.values():
        for m in meses.values():
            if la['idMes_id'] == m['id']:
                if m['nombreMes'] == 'ENERO':
                    cMJ += 1
                if m['nombreMes'] == 'FEBRERO':
                    cMF += 1
                if m['nombreMes'] == 'MARZO':
                    cMM += 1
                if m['nombreMes'] == 'ABRIL':
                    cMA += 1
                if m['nombreMes'] == 'MAYO':
                    cMMY += 1
                if m['nombreMes'] == 'JUNIO':
                    cMJN += 1
                if m['nombreMes'] == 'JULIO':
                    cMJL += 1
                if m['nombreMes'] == 'AGOSTO':
                    cMAU += 1
                if m['nombreMes'] == 'SEPTIEMBRE':
                    cMS += 1
                if m['nombreMes'] == 'OCTUBRE':
                    cMO += 1
                if m['nombreMes'] == 'NOVIEMBRE':
                    cMV += 1
                if m['nombreMes'] == 'DICIEMBRE':
                    cMD += 1

    for la in dias.values():
        for m in meses.values():
            if la['idMes_id'] == m['id']:
                if m['nombreMes'] == 'ENERO' or m['nombreMes'] == 'FEBRERO':
                    cEF += 1
                if m['nombreMes'] == 'MARZO' or m['nombreMes'] == 'ABRIL':
                    cEC += 1
                if m['nombreMes'] == 'MAYO' or m['nombreMes'] == 'JUNIO' or m['nombreMes'] == 'JULIO' or m['nombreMes'] == 'AGOSTO' or m['nombreMes'] == 'SEPTIEMBRE' or m['nombreMes'] == 'OCTUBRE':
                    cEH += 1
                if m['nombreMes'] == 'NOVIEMBRE':
                    cEV += 1
                if m['nombreMes'] == 'DICIEMBRE':
                    cEFF += 1

    for la in dias.values():
        #print(la['fecha']) #la['idMes_id']
        for m in meses.values():
            if la['idMes_id'] == m['id']:
                if m['nombreMes'] == 'ENERO' or m['nombreMes'] == 'FEBRERO':
                    cSDM += 1
                    #print(la['fecha'])
                if m['nombreMes'] == 'MARZO' and la['fecha'] < 21:
                    #print(la['fecha'])
                    cSDM += 1
                if m['nombreMes'] == 'MARZO' and la['fecha'] >= 21:
                    #print(la['fecha'])
                    cSMJ += 1
                if m['nombreMes'] == 'ABRIL' or m['nombreMes'] == 'MAYO':
                    #print(la['fecha'])
                    cSMJ += 1
                if m['nombreMes'] == 'JUNIO' and la['fecha'] < 21:
                    #print(la['fecha'])
                    cSMJ += 1
                if m['nombreMes'] == 'JUNIO' and la['fecha'] >= 21:
                    #print(la['fecha'])
                    cSJS += 1
                if m['nombreMes'] == 'JULIO' or m['nombreMes'] == 'AGOSTO':
                    cSJS += 1
                    #print(la['fecha'])
                if m['nombreMes'] == 'SEPTIEMBRE' and la['fecha'] < 21:
                    #print(la['fecha'])
                    cSJS += 1
                if m['nombreMes'] == 'SEPTIEMBRE' and la['fecha'] >= 21:
                    #print(la['fecha'])
                    cSSD += 1
                if m['nombreMes'] == 'OCTUBRE' or m['nombreMes'] == 'NOVIEMBRE':
                    cSSD += 1
                    #print(la['fecha'])
                if m['nombreMes'] == 'DICIEMBRE' and la['fecha'] < 21:
                    #print(la['fecha'])
                    cSSD += 1

    for la in dias.values():
        for m in meses.values():
            if la['idMes_id'] == m['id']:
                if m['idCuatrimestre_id'] == 1:
                    cP += 1
                elif m['idCuatrimestre_id'] == 2:
                    cS += 1
                elif m['idCuatrimestre_id'] == 3:
                    cT += 1

                if m['idTiempo_id'] == 1:
                    if m['nombreMes'] == 'ENERO' or m['nombreMes'] == 'FEBRERO' or m['nombreMes'] == 'MARZO' or m['nombreMes'] == 'ABRIL':
                        tS += 1
                    elif m['nombreMes'] == 'NOVIEMBRE' or m['nombreMes'] == 'DICIEMBRE':
                        tSS += 1
                elif m['idTiempo_id'] == 2:
                    tL += 1

    #Posiciones cuatrimestres
    nums = [cP, cS, cT]
    #Posiciones tiempos
    temps = [tS, tL, tSS]
    #Cantidad divs sols
    sols = [cSDM, cSMJ, cSJS, cSSD]
    #Cantidad divs épocas
    cEpocas = [cEF, cEC, cEH, cEV, cEFF]
    #Cantidad divs meses
    #cMeses = {'1': cMJ, '2': cMF, '3': cMM, '4': cMA, '5': cMMY, '6': cMJN, '7': cMJL, '8': cMAU, '9': cMS, '10': cMO, '11': cMV, '12': cMD}
    cMeses = [cMJ, cMF, cMM, cMA, cMMY, cMJN, cMJL, cMAU, cMS, cMO, cMV, cMD]

    cuentaAc = 0
    cuentaDi = 0

    n = actividades.__len__()
    m = dias.__len__() + 1

    data = [[0] * m for i in range(n)]

    for act in actividades.values():
        for fecha in dias.values():
            for la in lunaActividad.values():
                data[cuentaAc][0] = act['nombreActividad']
                if fecha['id'] == la['idFecha_id'] and act['id'] == la['idActividad_id']:
                    data[cuentaAc][cuentaDi+1] = 1
                    break
            cuentaDi += 1
        cuentaAc += 1
        cuentaDi = 0

    return render(
        request,
        'calendario.html',
        { 'data': data, 'actividades': actividades, 'fases': fases, 'logos':logos, 'meses': meses, 'dias': dias, 'cantidadDias': range(cantidadDias), 
        'lunaActividad': lunaActividad, 'menu_items': menu_items, 'chab': chab, 'nums': nums, 'temps': temps, 'sols': sols, 'cEpocas': cEpocas,
        'cMeses': cMeses }
    )

def detalle_actividad(request, pk):

    menu_items = Chab.objects.order_by('chab')
    try:
        actividad = Actividad.objects.get(pk=pk)
        cuatrimestre = LunaActividad.objects.filter(idActividad_id=pk)

        nAc = Actividad.getTipoActividad(actividad)
        #print(nAc)
        ct = cuatrimestre.values();
        cuat = []
        tiem = []
        epo = []
        po = []
        fas = []

        for ci in ct.values():
            #print(ci['idFecha_id'])
            fechaL = LunaMes.objects.get(pk=ci['idFecha_id'])
            fFase = LunaMes.getFase(fechaL)
            fMes = LunaMes.getMes(fechaL)
            fC = Mes.objects.get(nombreMes=fMes)
            fCuatrimestre = Mes.getCuatrimestre(fC)
            fTiempo = Mes.getTiempo(fC)
            fEpoca = Mes.getEpoca(fC)

            if fCuatrimestre not in cuat:
                cuat.append(fCuatrimestre)
            if fTiempo not in tiem:
                tiem.append(fTiempo)
            if fEpoca not in epo:
                epo.append(fEpoca)
            if fMes not in po:
                po.append(fMes)
            if fFase not in fas:
                fas.append(fFase)

            #print(fCuatrimestre)
            #print(fTiempo)
            #print(fEpoca)
            #print(fMes)
            #print(fFase)

    except Actividad.DoesNotExist:
        raise Http404("No existe actividad")
    return render(request, 'detalle_actividad.html', {'actividad': actividad, 'cuatrimestre': cuatrimestre, 'menu_items': menu_items,
        'cuat': cuat, 'tiem':tiem, 'epo':epo, 'po':po, 'fas':fas, 'cantidadDias': range(5)})