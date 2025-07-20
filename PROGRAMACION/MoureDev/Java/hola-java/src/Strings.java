public class Strings    {

    public static void main(String[] args) {


    //Cadenas de texto

    String name = "Jonathan";
    var surname  = new String("Ruales");

    // Operaciones basicas

    // Concatenacion
    System.out.println(name + " " + surname);

    // Longitud
    System.out.println(name.length());

    // Obtener caracter
    System.out.println(name.charAt(name.length()-1));

    // Subcadena (Un trozito de la cadena)
    System.out.println(name.substring(2));
    System.out.println(name.substring(1,3));

    // Mayuscualas y minusculas
    System.out.println(name.toLowerCase());
    System.out.println(name.toUpperCase());

    System.out.println(name);

    // Comprobar si contiene
    System.out.println("Hola, Java".contains("Jonathan"));
    System.out.println("Hola, Java".toUpperCase().contains("AVA"));  //.toUpperCase para poner la frase en MAYUSCULAS

    // Comparacion
    System.out.println(name.equals("Jonathan"));        // Para comparar en vez de == se usa equals
    System.out.println(name.equals("jonathan"));        // No es lo mismo en minusculas que en mayusculas
    System.out.println(name.equalsIgnoreCase("jonathan"));      // Para que ignore las minusculas y mayusculas se pone equalsIgnoreCase

    // == vs .equals

    var a = "Jonathan";

    var b = "Jonathan";

    var c = new String("Jonathan");


    System.out.println(a == b);
    System.out.println(a == c);         //Al ser un objeto distinto, aunque tenga el mismo valor, no es el mismo objeto en memoria por eso da false

    System.out.println(a.equals(c));    // En este caso el equals compara contenido, por eso da true

    }
}
