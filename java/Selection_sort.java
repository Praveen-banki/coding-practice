public class Main {

    public static void main(String[] args) {

        int[] arr = {64, 25, 12, 22, 11};

        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {

            int min = i;

            for (int j = i + 1; j < n; j++) {

                if (arr[j] < arr[min]) {
                    min = j;
                }

            }

            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }

        System.out.println("Sorted Array:");

        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}