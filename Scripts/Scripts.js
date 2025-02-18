function calcularArea(){

const pi=3.1416;

let radio = prompt("Ingresa el radio");

var area = pi * radio * radio;
window.alert("El area del circulo es de: " + area);  
}

function calcularRectan(){
    let ancho = prompt("Ingresa un ancho");
    let largo = prompt("Ingresa el largo");

    var Rectan = ancho * largo;
    window.alert("El area es de: " + Rectan); 
}

function calcularTrian(){
    let base = prompt("Ingresa una base");
    let altura = prompt("Ingresa una altura");

    var Trian = base * altura / 2;
    window.alert("El area es de: " + Trian);

}

function calcularHexa(){
    let perimetro = prompt("Ingresa un perimetro");
    let apotema = prompt("Ingresa un apotema");

    var Hexa = perimetro * apotema / 2;
    window.alert("El area es de: " + Hexa); 

}

    



