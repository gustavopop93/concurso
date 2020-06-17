function calcula_fase_lunar($fecha){

#   $lunallena = mktime(hora, minuto, segundo, mes, dia , año );

    $lunallena = mktime(02, 46, 20, 01, 24, 2016);

#   24 de enero de 2016 a las 02:46:20

#   inicio de la luna llena es :

    $iniciolunallena = $lunallena - 159462;

    $fecha = strtotime($fecha);

    $year = date('Y', $fecha);

    $month = date('n', $fecha);

    $day = date('j', $fecha);

    $estanoche = mktime(23, 50, 00, $month, $day, $year);

#   calculamos la luna que de esta noche. El dia entregado a las 23:50:00

    $segundosentrelllen = $estanoche - $iniciolunallena;

#   Segundos entre luna llena y esta noche

#   resto de la division entre el tiempo de un ciclo y los segundos desde luna llena hasta ahora

    $resto = $segundosentrelllen % 2551392;

#   Si es entre      1 y 318924  - Primera fase

#   Si es entre 318924 y 637858  - Segunda fase

#   Si es entre 637858 y 956782  - Tercera fase y asi sucesivamente

    for ($fase = 0; $fase <= 8; $fase++) {

        if ($resto >= 318924) {

            $resto = $resto - 318924;

        } else {

            break;

        }

    }

#  ahora ponemos el calculo en letras (el array debe estar bien ordenado)

    $fase_array = array(

        'Luna-llena', 'Luna-gibosa-menguante', 'Cuarto-menguante', 'Luna-menguante',

        'Luna-nueva', 'Luna-nueva-visible', 'Cuarto-creciente', 'Luna-gibosa-creciente'

    );

    $fase = $fase_array[$fase];

    return $fase;

}