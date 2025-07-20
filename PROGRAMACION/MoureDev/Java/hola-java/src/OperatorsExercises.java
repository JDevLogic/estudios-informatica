public class OperatorsExercises {

    public static void main(String[] args) {

// 1. Crea una variable con el resultado de cada operación aritmética.

// 2. Crea una variable para cada tipo de operación de asignación.

// 3. Imprime 3 comparaciones verdaderas con diferentes operadores de comparación.

// 4. Imprime 3 comparaciones falsas con diferentes operadores de comparación.

// 5. Utiliza el operador lógico and.

// 6. Utiliza el operador lógico or.

// 7. Combina ambos operadores lógicos.

// 8. Añade alguna negación.

// 9. Imprime 3 ejemplos de uso de operadores unarios.

// 10. Combina operadores aritméticos, de comparación y lógicos.



//1.
        var num1 = 9;
        var num2 = 1;

        System.out.println(num1 + num2);
        System.out.println(num1 - num2);
        System.out.println(num1 * num2);
        System.out.println(num1 / num2);
        System.out.println(num1 % num2);



//2
        var a = 5;
        a += 2;
        System.out.println(a);

        var b = 3;
        b -= 3;
        System.out.println(b);

        var c = 10;
        c *= 8;
        System.out.println(c);

        var d = 49;
        d /= 7;
        System.out.println(d);

        var e = 25;
        e %= 5;
        System.out.println(e);


//3
        System.out.println(a == d);

        System.out.println(c >= b);

        System.out.println(e <= a);



//4
        System.out.println(!(a == d));

        System.out.println(e >= c);

        System.out.println(b != e);



//5
        System.out.println(a == d && b == e);



//6
        System.out.println(e <= a ||b != e );



//7
        System.out.println((e <= c && a == d) && (b != e || c >= b));



//8
        System.out.println(!(e == a));



//9

        System.out.println(a--);

        System.out.println(a);

        System.out.println(--c);

        System.out.println(c++);

        System.out.println(c);



//10
        System.out.println((1+1 == 3- 1) && (5*2 >= 2));

    }
}
