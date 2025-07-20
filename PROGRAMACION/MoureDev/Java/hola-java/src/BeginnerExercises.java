public class BeginnerExercises {

    public static void main(String[] args) {

// 1. Declara una variable de tipo String y asignale tu nombre.

// 2. Crea una variable de tipo int y asignale tu edad.

// 3. Crea una variable double con tu altura en metros.

// 4. Declara una variable de tipo boolean que indique si te gusta programar.

// 5. Declara una constante con tu email.

// 6. Crea una variable de tipo char y guardale tu inicial.

// 7. Declara una variable de tipo String con tu localidad, y a continuacion cambia su valor y vuelve a imprimirla.

// 8. Crea una variable int llamada a, otra b, e imprime la suma de ambas.

// 9. Imprime el tipo de dos variables creadas anteriormente.

// 10. Intenta declarar una variable sin inicializarla y luego asignale un valor antes de imprimirla.



//1
        String name = "Jonathan";
        System.out.println("Mi nombre es: " + name);

//2
        int age = 21;
        System.out.println("Mi edad es: " + age);

//3
        double height = 1.74;
        System.out.println("Mi altura es: " + height);

//4
        boolean programmer = true;
        System.out.println("¿Me gusta la programacion? "+ programmer);

//5
        final String EMAIL = "jdevlogic@gmail.com";
        System.out.println(EMAIL);


//6
        char inicial ='J';
        System.out.println("Mi inical es : " +inicial);


//7
       String location = "Bilbao";
       System.out.println("Vivo en: " +location);
       location = "España";
       System.out.println("El pais es: " +location);


//8
       int num1 = 1;
       int num2 = 4;
       System.out.println(num1 + num2);


//9
       System.out.println(((Object)num1).getClass().getSimpleName());
       System.out.println(((Object)inicial).getClass().getSimpleName());


//10
       int num;
       num = 123456;
       System.out.println(num);


    }
}
