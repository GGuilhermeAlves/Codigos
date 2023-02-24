import java.util.Scanner;

class Nodo {
  public int chave;
  public Nodo esquerda;
  public Nodo direita;

  public Nodo(int chave) {
    this.chave = chave;
  }

  public Nodo inserir(Nodo aux, int num) {
    if (aux == null) {
      aux = new Nodo(num);
 
    } else if (num < aux.chave) {
      aux.esquerda = inserir(aux.esquerda, num);
    } else {
      aux.direita = inserir(aux.direita, num);
    }
    return aux;
  }

  public boolean localizar(Nodo aux, int num) {
    boolean loc = false;

    if (aux != null) {
      if (aux.chave == num) {
        loc = true;
      } else if (num < aux.chave) {
        loc = localizar(aux.esquerda, num);
      } else {
        loc = localizar(aux.direita, num);
      }
    }
     
    return loc;
  }

  public Nodo excluir(Nodo aux, int num) {
    Nodo p, p2, r = null;
    if (aux.chave == num) {
        if (aux.esquerda == aux.direita) {
          return null;
        } else if (aux.esquerda == null) {
          return aux.direita;
        } else if (aux.direita == null) {
          return aux.esquerda;
        } else {
          p2 = aux.direita;
          p = aux.direita;
          while (p.esquerda != null) {
            r = p;
            p = p.esquerda;
          }
          aux.chave = p.chave;
          p = null;
          r.esquerda = null;
          return aux;
        }
    } else if (aux.chave < num) {
      aux.direita = excluir(aux.direita, num);
    } else {
      aux.esquerda = excluir(aux.esquerda, num);
    }
      return aux;
  }

   public void emordem(Nodo no) {
    if(no != null){
      emordem(no.esquerda);
      System.out.print(no.chave + " ");
      emordem(no.direita);
    }
  }
}

class Main {
  public static void main(String[] args) {
    Nodo tree = new Nodo(12);
    Scanner input = new Scanner(System.in);

    tree.inserir(tree, 5);
    tree.inserir(tree, 6);
    tree.inserir(tree, 4);
    tree.inserir(tree, 1);
    tree.inserir(tree, 10);
    tree.inserir(tree, 21);
    tree.inserir(tree, 15);

    
    tree.excluir(tree, 1);
    tree.excluir(tree, 12);
    
    System.out.print("Digite um número: ");
    int n = input.nextInt();

    boolean search = tree.localizar(tree, n);

    if(search == true) {
      System.out.println("Número encontrado!");
    } else {
      System.out.println("Número não encontrado!");
    }

    tree.emordem(tree);


    input.close();
  }
}