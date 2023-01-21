import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.util.InputMismatchException;
import java.util.Scanner;


class Algorithm {
    public void solution(BigInteger n){
        BigDecimal Decimal_n = new BigDecimal(n);
        BigDecimal sum = Decimal_n.add(BigDecimal.ONE).sqrt(new MathContext(100));

        System.out.println("numeric sum: "+sum);
        System.out.println("symbolic sum: sqrt("+n.add(BigInteger.ONE)+")");
    }
}

public class Main {
    public static void main(String[] args) {
        BigInteger n;
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Enter n:");
            n = scanner.nextBigInteger();

            if (n.compareTo(BigInteger.ONE) < 0) {
                throw new Exception("n must be greater than 0");
            }
        }catch (InputMismatchException e) {
            System.out.println("n must be a number");
            return;
        }catch (Exception e) {
            System.out.println(e.getMessage());
            return;
        }

        Algorithm calculate = new Algorithm();
        calculate.solution(n);
    }
}

