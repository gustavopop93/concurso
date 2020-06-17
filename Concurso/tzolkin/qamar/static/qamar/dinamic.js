$(function () {
  'use strict'
  $('[data-toggle="offcanvas"]').on('click', function () {
    $('.offcanvas-collapse').toggleClass('open')
  })
})

function crear(){
    var col = 12;
    var filas = 30;
    var tabla="<table align=\"center\" cellpadding=\"0\" cellspacing=\"0\" class=\"table\" border=\"white\" id=\"tblCampoDeJuego\">";

    for(i=0;i<filas;i++){
    	tabla+="<tr>";
    	if( i == 0 ){
    		for( c=0; c<4; c++ ){
                tabla += "<td colspan=\"6\">Head 1</td>";
    		}
            tabla += "</tr>";
    	}else if( i==1 ){
    		for( c=0; c<col; c++ ){
    			tabla += "<td colspan=\"2\">i</td>";
    		}
    		tabla += "</tr>";
    	}/*else{
    		for( c=0; c<16; c++ ){
    			tabla+="<td class=\"auto-style5\" onclick=\"celdaClick(this)\" ondblclick=\"celdaDobleClick(this)\">i</td>";
    		}
    	}*/
        tabla+="</tr>";
    }
    tabla+="</table>";
    document.getElementById("calendario").innerHTML=tabla;
}

window.onload = crear;

function celdaClick(celda) {
    if (celda.bgColor == "#0a851f" || celda.bgColor == "#4d917b") {
        celda.bgColor = "#FFFFFF";
    } else {
        celda.bgColor = "#0a851f";
    }
    
}
function celdaDobleClick(celda) {
    if (celda.bgColor == "#0a851f" || celda.bgColor == "#4d917b") {
        celda.bgColor = "#FFFFFF";
    } else {
        celda.bgColor = "#4d917b";
    }
}





//------------------------------------------------------------//
function MakeArray (n) {
    this.length= n
    for (var j = 0; j < n; j++) {
      this [j] = 0
    }
    return this
    }
function compute(form) {
    Mes=eval(form.mes.value)
    any=eval(form.any.value)
    with (Math) {

  JDM=new MakeArray (4);
  DDM=new MakeArray (4);
  MMM=new MakeArray (4);
  ANM=new MakeArray (4);
  HHM=new MakeArray (4);
  MIM=new MakeArray (4);
  SEM=new MakeArray (4);
  
for (var s=0; s<=3; s++) {
    k=floor((any+(Mes-1)/12-1900)*12.3685+0.5);
    k=k+0.25*s;
    T=(k/1236.85);
    T2=T*T;
    T3=T2*T;
    RAD=57.29577951
    <!-- Tiempo para las fases medias -->
JD=2415020.75933+29.53058868*k+0.0001178*T2-0.000000155*T3+0.00033*sin((166.56+132.87*T-0.009173*T2)/RAD);
    <!-- Anomalias mediasde Sol y Luna y arg. latitud -->
    M=359.2242+29.10535608*k-0.0000333*T2-0.00000347*T3;
    M1=306.0253+385.81691806*k+0.0107306*T2+0.00001236*T3;
    F=21.2964+390.67050646*k-0.0016528*T2-0.00000239*T3
    M=M/RAD;
    M1=M1/RAD;
    F=F/RAD;
    <!-- Correción para Luna Nueva y Llena -->
    AJ=(0.1734-0.000393*T)*sin(M)+0.0021*sin(2*M)-0.4068*sin(M1)+0.0161*sin(2*M1);
    AJ=AJ-0.0004*sin(3*M1)+0.0104*sin(2*F)-0.0051*sin(M+M1)-0.0074*sin(M-M1);
    AJ=AJ+0.0004*sin(2*F+M)-0.0004*sin(2*F-M)-0.0006*sin(2*F+M1)+0.0010*sin(2*F-M1);
    AJ=AJ+0.0005*sin(M+2*M1);
    <!-- Correción para Cuarto creciente y menguante -->
    BJ=(0.1721-0.0004*T)*sin(M)+0.0021*sin(2*M)-0.6280*sin(M1)+0.0089*sin(2*M1);
    BJ=BJ-0.0004*sin(3*M1)+0.0079*sin(2*F)-0.0119*sin(M+M1)-0.0047*sin(M-M1);
    BJ=BJ+0.0003*sin(2*F+M)-0.0004*sin(2*F-M)-0.0006*sin(2*F+M1)+0.0021*sin(2*F-M1);
    BJ=BJ+0.0003*sin(M+2*M1)+0.0004*sin(M-2*M1)-0.0003*sin(2*M+M1);
    CJ=0.0028-0.0004*cos(M)+0.0003*cos(M1);
    if (s==0) {JD=JD+AJ};
    if (s==1) {JD=JD+BJ+CJ};
    if (s==2) {JD=JD+AJ};
    if (s==3) {JD=JD+BJ-CJ};
    J=JD;
     <!-- fecha juliana a calendario -->
        if (J>=2299160.5) {
        G=1;
        } else {
        G=0;
        }
    F= J-floor(J);
    J=floor(J);
    F=F +0.5;
    if (F>=1) {
        F= F - 1;
        J= J + 1;
        }
    if (G==0) {
        A=J;
        } else {
            A1=floor((J/36524.25)-51.12264);
            A=J + 1 + A1 - floor(A1 / 4);
            }
    B = A + 1524;
    C = floor((B / 365.25) - 0.3343);
    D = floor(365.25 * C);
    E1 = floor((B - D) / 30.61);
    D = B - D - floor(30.61 * E1) + F;
    M = E1 - 1;
    Y = C - 4716;
    if (E1>13.5) {
        M=M-12;
        }
    if (M<2.5) {
        Y = Y + 1;
        }
    H = (D - floor(D)) * 24;
    H1 = (H - floor(H)) * 60;
    H2 = (H1 - floor(H1)) * 60;
    
    D=floor(D);
    H=floor(H);
    H1=floor(H1);
    H2=floor(H2+0.5);
<!-- asignacion valores a las matrices resultado-->
    JDM[s]=JD;
    DDM[s]=D;
    MMM[s]=M;
    ANM[s]=Y;
    HHM[s]=H;
    MIM[s]=H1
    SEM[s]=H2;
    }
 }
    form.jd0.value=JDM[0];
    form.d0.value =DDM[0];
    form.m0.value =MMM[0];
    form.a0.value =ANM[0];
    form.h0.value =HHM[0];
    form.mi0.value =MIM[0];
    form.s0.value =SEM[0];
    form.jd1.value=JDM[1];
    form.d1.value =DDM[1];
    form.m1.value =MMM[1];
    form.a1.value =ANM[1];
    form.h1.value =HHM[1];
    form.mi1.value =MIM[1];
    form.s1.value =SEM[1];
    form.jd2.value=JDM[2];
    form.d2.value =DDM[2];
    form.m2.value =MMM[2];
    form.a2.value =ANM[2];
    form.h2.value =HHM[2];
    form.mi2.value =MIM[2];
    form.s2.value =SEM[2];
    form.jd3.value=JDM[3];
    form.d3.value =DDM[3];
    form.m3.value =MMM[3];
    form.a3.value =ANM[3];
    form.h3.value =HHM[3];
    form.mi3.value =MIM[3];
    form.s3.value =SEM[3];
    
}