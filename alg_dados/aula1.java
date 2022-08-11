package alg_dados;

import java.util.Scanner;

public class aula1 {

	public static void main(String[] args) {
		
		
		int a, b, sum, sub, mult, div;
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Digite a primeira variável");
		a = sc.nextInt();
		
		System.out.println("Digite a segunda variável");
		b = sc.nextInt();
		
		
		sum = a + b;
		sub = a - b;
		mult = a * b;
		div = a / b;
		
		System.out.println("A soma deles é = " +sum);
		System.out.println("A subtração deles é = " +sub);
		System.out.println("A multiplicação deles é = " +mult);
		System.out.println("A divisão deles é = " +div);

	}

}

