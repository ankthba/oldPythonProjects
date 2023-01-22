import java.lang.Math;
import java.util.List;
import java.util.ArrayList;

public class PrimeNumbers {
    private static final int maxNumber = 100;

    public static void main(String[] args){
        List<Integer> primeNumberList = new ArrayList<Integer>();
        primeNumberList.add(2);

        for(int nextNum = 3; nextNum <= maxNumber; nextNum++){
            double root = Math.sqrt(nextNum);
            boolean isNextNumPrime = true;
            for(int primeNum: primeNumberList){
                if(primeNum > root) break;

                if(nextNum % primeNum == 0){
                    isNextNumPrime = false;
                    break;
                }
            }

            if(isNextNumPrime){ // same as isNextNumPrime == true
                primeNumberList.add(nextNum);
            }
        }

        for(int primeNum: primeNumberList) {
            System.out.println(primeNum);
        }
    }
    
}

