public class Operators {

    public static void main(String[] args) {

        // Operadores

        // Aritmeticos

        var a = 5;
        var b = 3;

        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a * b);
        System.out.println(a / b);
        System.out.println(a % b);


        // Asignacion

        a = b;
        System.out.println(a);

        a = b * 2;
        System.out.println(a);

        a += 1;     // a = a + 1   | Es una asignacion directa
        System.out.println(a);

        a -= 1;
        System.out.println(a);

        a *= 2;
        System.out.println(a);

        a /= 2;
        System.out.println(a);

        a %= 2;
        System.out.println(a);


        // Comparacion (Relacionales)

        System.out.println(a == b);
        System.out.println(a == 0);

        System.out.println(a != 0);
        System.out.println(a > 0);
        System.out.println(a >= 0);
        System.out.println(a < 0);
        System.out.println(a <= 0);

        // Logicos

        // Y (AND)

        System.out.println(true && true);
        System.out.println(true && false);
        System.out.println(false && true);
        System.out.println(false && false);

        System.out.println(3 > 2 && 5 == 2);


        // O (OR)

        System.out.println(true || true);
        System.out.println(true || false);
        System.out.println(false || true);
        System.out.println(false || false);

        System.out.println(3 > 2 || 5 == 2);


        // NO (NOT)

        System.out.println(!true);
        System.out.println(!false);
        System.out.println(!(3 > 2) || 5 == 2);

        // Unarios

        System.out.println(+b);
        System.out.println(-b);
        System.out.println(++b);   //
        System.out.println(b++);   /* Sirve para usarlo en bucles por indice ,
                                      por ejemplo porque primero imprime el valor y luego lo incrementa */
        System.out.println(b);
        System.out.println(--b);
        System.out.println(b--);
        System.out.println(b);

        b++;
        System.out.println(b);



    }
}
