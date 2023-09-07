import java.util.Scanner;


public class Treino {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double[] temperaturas = new double[365];

        for (int i = 0; i < temperaturas.length; i++) {
            temperaturas[i] = input.nextDouble();
            
            System.out.print("Array atual: [");
            for (int j = 0; j <= i; j++) {
                System.out.print(temperaturas[j]);

                if (j < i) {
                    System.out.print(", ");
                }
            }
            System.out.println("]");

        }

        input.close();
    }
}
