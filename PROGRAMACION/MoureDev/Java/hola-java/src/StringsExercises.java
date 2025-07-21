public class StringsExercises {
    public static void main(String[] args) {

// 1. Concatena dos cadenas de texto.

// 2. Muestra la longitud de una cadena de texto.

// 3. Muestra el primer y último carácter de un string.

// 4. Convierte a mayúsculas y minúsculas un string.

// 5. Comprueba si una cadena de texto contiene una palabra concreta.

// 6. Formatea un string con un entero.

// 7. Elimina los espacios en blanco al principio y final de un string.

// 8. Sustituye todos los espacios en blanco de un string por un guión (-).

// 9. Comprueba si dos strings son iguales.

// 10. Comprueba si dos strings tienen la misma longitud.





//1
        var fruta1 = "manzana";
        var fruta2 = "banana";


        System.out.println(fruta1+ " " +fruta2);


//2
        System.out.println(fruta1.length());



//3
        System.out.println(fruta1.charAt(0));
        System.out.println(fruta1.charAt(fruta1.length()-1));



//4
        var name = "JONATHAN";

        System.out.println(name.toLowerCase());



//5
        System.out.print(fruta1.contains("zana"));



//6
        var age = 2;
        System.out.println(String.format("La %s tiene sin comerse %d años",fruta1,age));



//7
        var presentation = " Hola me llamo Jonathan ";

        System.out.println(presentation.trim());



//8
        System.out.println(presentation.replace(" ","-"));



//9
        var fruta3 = "naranjas";

        var fruta4 = "naranjas";

        System.out.println(fruta3.equals(fruta4) );



//10
        var fruta5 = "naranja";

        System.out.println(fruta3.length() == fruta4.length());
        System.out.println(fruta5.length() == fruta4.length());
    }
}
