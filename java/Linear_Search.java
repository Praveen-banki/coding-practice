import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = {10,20,30,40,50};
        int x = sc.nextInt();

        int index = -1;

        for(int i=0;i<arr.length;i++){
            if(arr[i]==x){
                index=i;
                break;
            }
        }

        System.out.println(index);
    }
}