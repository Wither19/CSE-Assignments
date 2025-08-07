import java.util.GregorianCalendar;

public class Main {
  public static String weekdayName(int weekday) {
    String result = "";

    if (weekday == 1) {
      result = "Sunday";
    } else if (weekday == 2) {
      result = "Monday";
    } else if (weekday == 3) {
      result = "Tuesday";
    } else if (weekday == 4) {
      result = "Wednesday";
    } else if (weekday == 5) {
      result = "Thursday";
    } else if (weekday == 6) {
      result = "Friday";
    } else if (weekday == 7) {
      result = "Saturday";
    } else {
      result = "error";
    }

    return result;
  }

  public static void main(String[] args) {
    System.out.println("Weekday 1: " + weekdayName(1));
    System.out.println("Weekday 2: " + weekdayName(2));
    System.out.println("Weekday 3: " + weekdayName(3));
    System.out.println("Weekday 4: " + weekdayName(4));
    System.out.println("Weekday 5: " + weekdayName(5));
    System.out.println("Weekday 6: " + weekdayName(6));
    System.out.println("Weekday 7: " + weekdayName(7));
    System.out.println("Weekday 0: " + weekdayName(0));
    System.out.println();
    System.out.println("Weekday 43: " + weekdayName(43));
    System.out.println("Weekday 17: " + weekdayName(17));
    System.out.println("Weekday -1: " + weekdayName(-1));

    GregorianCalendar cal = new GregorianCalendar();
    int dow = cal.get(GregorianCalendar.DAY_OF_WEEK);

    System.out.println("\nToday is a " + weekdayName(dow) + "!");
  }
}