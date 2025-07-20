public class HelloWordlExercises {

    public static void main(String[] args) {


// 1. Imprime un mensaje que diga tu nombre en lugar de "¡Hola Mundo!".

// 2. Imprime dos líneas: "Hola" y luego "Mundo" con un solo println.

// 3. Añade un comentario sobre lo que hace cada línea del programa.

// 4. Crea un comentario en varias líneas.

// 5. Imprime tu edad, tu color favorito y tu ciudad.

// 6. Explora los diferentes System.XXX.println(); más allá del "out".

// 7. Utiliza varios println para imprimir una frase.

// 8. Imprime un diseño ASCII (por ejemplo, una cara feliz usando símbolos).

// 9. Intenta ejecutar el programa sin el metodo main y observa el error.

// 10. Intenta cambiar el nombre del archivo a uno diferente del de la clase y compílalo. ¿Qué pasa?




// 1.
        System.out.println("Hola mundo");


//2
        System.out.println("Hola \nMundo");


//3
        // El primer ejercicio muestra un mensaje basico que dice "Hola mundo".



//4
        /* El segundo ejercico lo que hace es lo mismo que el primero
        pero lo que tiene de diferente es que cada palabra tiene un salto de linea.
         */


//5
        System.out.println("\nTengo 21 años \nMi color favorito es el azul \nVivo en Bilbao");


//6
        System.out.println(System.getProperty("user.name"));    // Sirve para imprimir el valor de una propiedad del sistema en Java,
                                                                // como la versión de Java, el nombre del usuario, el sistema operativo,


//7
        System.out.println("Hola,buenos dias,");
        System.out.println("Por la mañana");


//8
        System.out.println(" O.O ");
        System.out.println(" ^_^ ");


//9
        /* Sin el metodo main no me deja ni ejecutar el programa
         porque no sabe que se debe de ejecutar (es el punto de entrada de cualquier aplicacion Java)
        */

//10
        // Si cambio el nombre y no es igual a la clase no funciona
        // porque la clase debe llamarse igual el archivo y daria un error de compilacion

    }


}

