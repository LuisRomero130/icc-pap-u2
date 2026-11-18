import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class App {
    public static void main(String[] args) {
        //runEjemplo1();
        //runEjemplo2();
        runEjemplo3();
        
    }
    private static void runEjemplo3() {
        String texto= "Sensores: T001 reporta 23.5 C ; O001 reporta 12 PERSONAS; T002 reporta -2 C.";
        Pattern patron= Pattern.compile("[TO][0-9]{3}");
        Matcher matcher= patron.matcher(texto);
        while (matcher.find()) {
            System.out.printf("Encontrado: %s, posición: %d%n", matcher.group(),matcher.start());
            
        }
    }
        
        

      
    
    private static void runEjemplo2() {
        String regex= "[TO][0-9]{3}";
        // del 0 al nueve y tienen que aver 3 digitos
        String [] list= new String[]{"T001","O120","T01","X001","T0001"};
        for(String codigo: list){
            System.out.printf("%s => %s%n,", codigo, codigo.matches(regex));
        }
        
    }
    public static void runEjemplo1(){
        String patron= "ab*";
        String[] palabras= new String []{"a","ab","abbb","abab","b",""};
        for(String p: palabras){
            System.out.println(p+ "-> "+ p.matches(patron));
        
        }
    }
    
}
