import java.util.Scanner;

public class Main {
  private static boolean askQuestion(String prompt, String[] answers, int correctAnswerNum) {
    Scanner s = new Scanner(System.in);

    int userAnswer = 0;

    System.out.println(prompt + " ");

    for (int i = 0; i < answers.length; i++) {
      System.out.println((i + 1) + ". " + answers[i]);
    }

    System.out.print("Answer: ");

    userAnswer = s.nextInt();

    if (userAnswer == correctAnswerNum) {
      System.out.println("Correct!");
    } else {
      System.out.println("Incorrect. Correct Answer: " + answers[correctAnswerNum - 1]);
    }

    return (userAnswer == correctAnswerNum);
  }

  public static void main(String[] args) {
    int correctAnswers = 0;

    String[] prompts = { "Q1. What is the capital city of Florida?",
        "Q2. What is Florida's state bird?",
        "Q3. Which grocery chain was founded in Florida?"
    };

    String[][] answers = {
        { "Jacksonville", "Tallahassee", "Miami" },
        { "Mourning dove", "Pelican", "Mockingbird" },
        { "Publix", "Target", "Aldi" }
    };

    int[] corrects = { 2, 3, 1 };

    for (int i = 0; i < 3; i++) {
      if (askQuestion(prompts[i], answers[i], corrects[i])) {
        correctAnswers++;
      }

      System.out.println("Current score: " + correctAnswers + " out of 3");
    }

    System.out.println("Thank you for playing!");
  }
}
