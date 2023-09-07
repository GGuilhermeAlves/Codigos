import java.util.Scanner;

public class Converter_idade {
public static void main(String []args){   
    Scanner sc = new Scanner(System.in);
        System.out.print("Ano: ");
        int anos = sc.nextInt();
        System.out.print("Mes: ");
        int meses = sc.nextInt();
        System.out.print("Dia: ");
        int dias = sc.nextInt();
        int anos_dias=(anos*365);
        int meses_dias=(meses*30);
        int dias_total=(anos_dias+meses_dias+dias);
        System.out.println(anos+" Anos,"+meses+" Meses,"+"e "+dias+" dias = "+dias_total+" dias");
        sc.close();
    }
} 