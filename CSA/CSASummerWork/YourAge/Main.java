import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    System.out.println("What's your name? ");
    String name = s.nextLine();

    System.out.println("Ok, " + name + ", How old are you? ");
    int age = s.nextInt();

    if (age < 16) {
      System.out.println("You can't drive.");
    }
    if (age < 18) {
      System.out.println("You can't vote.");
    }
    if (age < 25) {
      System.out.println("You can't rent a car.");
    }
    if (age >= 25) {
      System.out.println("You can do anything that's legal.");
    }
  }
}