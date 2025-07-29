public class ConditionalsExercises {

    public static void main(String[] args) {

// 1. Establece la edad de un usuario y muestra si puede votar (mayor o igual a 18).

// 2. Declara dos números y muestra cuál es mayor, o si son iguales.

// 3. Dado un número, verifica si es positivo, negativo o cero.

// 4. Crea un programa que diga si un número es par o impar.

// 5. Verifica si un número está en el rango de 1 a 100.

// 6. Declara una variable con el día de la semana (1-7) y muestra su nombre con switch.

// 7. Simula un sistema de notas: muestra "Sobresaliente", "Aprobado" o "Suspenso" según la nota (0-100).

// 8. Escribe un programa que determine si puedes entrar al cine: debes tener al menos 15 años o ir acompañado.

// 9. Crea un programa que diga si una letra es vocal o consonante.

// 10. Usa tres variables a, b, c y muestra cuál es el mayor de las tres.




//1
    var age = 15;


    if (age >= 18){
        System.out.println("El usuario tiene derecho a votar.");
    }else{
        System.out.println("El usuario todavia no tiene derecho a votar.");
    }


//2
    var num1 = 4;
    var num2 = 4;

    if (num1 < num2){
        System.out.println("El segundo numero es mayor que el primer numero .");
    } else if (num1 > num2) {
        System.out.println("El primer numero es mayor que el segundo numero.");
    }else{
        System.out.println("Los dos numeos son iguales.");
    }



//3
    var num = -12;

    if (num < 0 ) {
        System.out.println("El numero es negativo.");
    } else if (num == 0) {
        System.out.println("El numero es igual a cero.");
    }else{
        System.out.println("El numero es positivo.");
    }



//4
    var num3 = 13;

    if(num3 % 2 == 0 ) {
        System.out.println("El numero es par");
    } else{
        System.out.println("El numero es impar.");
    }



//5
    var num4 = 101;

    if (num4 <= 100){
        System.out.println("El numero esta en el rango o es igual a 100.");
    }else{
        System.out.println("El numero esta fuera del rango.");
    }



//6
    var day = 8;

    switch (day){
        case 1:
            System.out.println("Hoy es Lunes.");
            break;

        case 2:
            System.out.println("Hoy es Martes.");
            break;

        case 3 :
            System.out.println("Hoy es Miercoles.");
            break;

        case 4:
            System.out.println("Hoy es Jueves.");
            break;

        case 5:
            System.out.println("Hoy es Viernes.");
            break;

        case 6:
            System.out.println("Hoy es Sabado.");
            break;

        case 7:
            System.out.println("Hoy es Domingo");
            break;

        default:
            System.out.println("No es ningun dia de la semana.");

    }



//7
    var nota = 4;

    if (nota >= 10 ){
        System.out.println("Sobresaliente.");
    }

     else if (nota >= 7 ){
         System.out.println("Notable.");
     }
    else if (nota >=5){
        System.out.println("Aprobado.");
        }
    else{
        System.out.println("Suspenso.");
    }



//8








    }
}
