// Do check this one and letme know if there is/are any problems.
// Appology for sharing here but other repositories are blank. kindly delete after reviewing.

import java.util.*;

public class CommonInFactorialOfTwoNumbers {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        // taking input from user
        System.out.println("Enter First Value :");
       int scanFirst = scan.nextInt();
        System.out.println("Enter Second value :");
       int scanSecond = scan.nextInt();

       // Calling Method
        calculateFactorial(scanFirst,scanSecond);
    }

    public static void calculateFactorial(int first, int second) {
        //initialisation
        ArrayList<Integer> list = new ArrayList<Integer>();
        ArrayList<Integer> list2 = new ArrayList<Integer>();
        int factorialFirst = 1, factorialSecond = 1;
        int CommonValue;
        // loop for first Factorial
        for (int i = first; i > 0; i--) {
            factorialFirst *= i;
            list.add(i);
        }
        // loop for second factorial
        for (int j = second; j > 0; j--) {
            factorialSecond *= j;
            list2.add(j);
        }
        // finding the common of both
        CommonValue = Math.min(first, second);
        // output
        System.out.println("factorial of "+ first + " is = " + factorialFirst);
        System.out.println("Elements :" + list );
        System.out.println("factorial of "+ second + " is = " + factorialSecond);
        System.out.println("Elements :" + list2);
        System.out.println("*****************************");
        System.out.println("Highest Common element = " + CommonValue);
        if(CommonValue == first){
            System.out.println("Elements :" + list);
        }else
            System.out.println("Elements :" + list2);


    }
}
