import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int limit = sc.nextInt();

        System.out.println("Prime numbers from 2 to " + limit + " are:");

        for (int n = 2; n <= limit; n++) {

            boolean prime = true;

            for (int i = 2; i <= Math.sqrt(n); i++) {

                if (n % i == 0) {
                    prime = false;
                    break;
                }
            }

            if (prime) {
                System.out.print(n + " ");
            }
        }

        sc.close();
    }
}