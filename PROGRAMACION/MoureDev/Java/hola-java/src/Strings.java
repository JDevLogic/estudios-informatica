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
    System.out.println("Hola, Java".contains("ava"));

    


    }
}
