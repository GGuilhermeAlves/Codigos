
//Teste Zenoth

import java.util.Random;
import java.util.Scanner;

class Main{ 
  public static void main(String[] args) {
    System.out.println("-----------------------------------");
    System.out.println("  Bem-vindo ao jogo de advinhação");
    System.out.println("-----------------------------------");
    Jogo jogo = new Jogo();
    jogo.jogar();
  }
}

class Jogo {
  static int numAl;
  static int numDig;

  public void jogar() {
    Scanner input = new Scanner(System.in);
    Random genarator = new Random();
    int life = 3;
    int numAl = genarator.nextInt(11);
    String playagain;
    
    //ENTRAR NO LOOP DO JOGO
    while(true) {
      //VERIFICAR SE O VALOR DIGITADO ESTÁ ENTRE 0 E 10 (INCLUSIVE)
      while(true) {
        System.out.print("Digite um número: ");
        numDig = input.nextInt();
        
        if(numDig >= 0 && numDig <= 10) {
          break;
        } else {
          System.out.println("Digite novamente, número passou do limite!");
        }
      }
      
      //VERIFICAR SE O JOGADOR ACERTOU O NÚMERO     
      if(numDig == numAl) {
        System.out.println("Parabéns você venceu!");
        System.out.println("Número encontrado: " + numAl);
        break;
      } else {
        if(life > 1) {
          life--;
          if(numDig > numAl) {
            System.out.println("Tente um número menor, " + life + " tentativas");
          } else {
            System.out.println("Tente um número maior, " + life + " tentativas");
          }
        } else {
          System.out.println("Você perdeu!");
          System.out.println("O número procurado era " + numAl);
          break;
        }
      }
    } 

    //VERFICAR SE ELE QUER JOGAR NOVAMENTE
    System.out.print("Deseja jogar novamente? S/N: ");
    playagain = input.next();
    System.out.println();
        
    if(playagain.toUpperCase().equals("S")) {
    //RECURSIVIDADE
      Jogo jogo = new Jogo();
      jogo.jogar();
    } else {
      System.out.println("Obrigado por jogar!");
      input.close();
    }   
  }
}
