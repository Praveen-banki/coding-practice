import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Read the complete sentence
        System.out.print("Enter a sentence: ");
        String str = sc.nextLine();

        // Split the sentence into words
        String[] words = str.split(" ");

        // Print words in reverse order
        System.out.print("Reversed Sentence: ");
        for (int i = words.length - 1; i >= 0; i--) {
            System.out.print(words[i] + " ");
        }

        sc.close();
    }
}