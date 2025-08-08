import java.util.Scanner;

class Main {

  private static int areaRectangle(int length, int width) {
    return length * width;
  }

  private static int areaSquare(int side) {
    return side * side;
  }

  private static double areaTriangle(int base, int height) {
    return 0.5 * base * height;
  }

  private static double areaCircle(int radius) {
    return Math.PI * Math.pow(radius, 2);
  }

  public static void main(String[] args) {
    int option = 0;

    Scanner s = new Scanner(System.in);

    while (option != 5) {
      System.out.println("-----------------------");
      System.out.println("1. Triangle");
      System.out.println("2. Rectangle");
      System.out.println("3. Square");
      System.out.println("4. Circle");
      System.out.println("5. Quit\n");
      System.out.print("Which shape: ");

      option = s.nextInt();

      if (option == 1) {
        System.out.print("Base: ");
        int b = s.nextInt();

        System.out.print("Height: ");
        int h = s.nextInt();

        System.out.println("The area is " + areaTriangle(b, h));
      } else if (option == 2) {
        System.out.print("Length: ");
        int l = s.nextInt();

        System.out.print("Width: ");
        int w = s.nextInt();

        System.out.println("The area is " + areaRectangle(l, w));
      } else if (option == 3) {
        System.out.print("Side length: ");
        int side = s.nextInt();

        System.out.println("The area is " + areaSquare(side));
      } else if (option == 4) {
        System.out.print("Radius: ");
        int r = s.nextInt();

        System.out.println("The area is " + areaCircle(r));
      }
    }

  }
}