function imprime(){
    let nombre = prompt("¿Cual es tu nombre?: ");
    alert("Tu nombre es"+nombre);
}
function suma(){
    let x=parseFloat(prompt("Ingresa un numero flotante: "));
    let y=parseFloat(prompt("Ingresa otro numero flotante: "));
    alert("El resultado de sumarlos es"+(x+y));
}

function logicaInverso(){
    let x=Boolean(prompt("Ingresa True o False (1 = True/ 0 = False): "));
    alert("El inverso del valor ingresado es"+(!x));
}
function logicaBinaria(){
    let x=Boolean(input("Ingresa True o False (1 = True/ 0 = False): "));
    let y=Boolean(input("Ingresa True o False (1 = True/ 0 = False): "));
    let z=prompt("Ingresa una operacion logica binaria (and / or / xor): ");
    let toRes="El resultado de"+x+" "+z+" "+y+"es "
    alert(toRes+operaLog(x,y,z));
}

function operaLog(x, y,  z){
    if(z==="and") {return x && y}
    if (z==="or") {return x || y}
    if (z==="xor") {return (x && y)  ((!x) && (!y))}
    }

function secNum(){
    let cuenta
    for(let i=0; i++;i<11) {
        cuenta += String(i)+"!\n";
    }
    alert("!Contemos!\n"+cuenta);
}

function adivinaInador(){//adivina el numero del 1 al 10
    let x=parseInt(Math.random()*10)
    let respuesta;
    while(respuesta!==x){
        respuesta=parseInt(prompt("¿En que numero del 1 al 10 estoy pensando?: "))
        if(x<respuesta){alert("te pasaste intenta otra vez")}
        if(x>respuesta){alert("muy bajo intenta otra vez")}
        }
    alert("Correcto :)")
}