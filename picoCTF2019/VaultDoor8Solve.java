import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;
class VaultDoor8 {
	public static void main(String args[]) {
		char[] expected = {
			0xf4, 0xc0, 0x97, 0xf0, 0x77, 0x97, 0xc0, 0xe4, 0xf0, 0x77, 0xa4, 0xd0, 0xc5, 0x77, 0xf4, 0x86, 0xd0, 0xa5, 0x45, 0x96, 0x27, 0xb5, 0x77, 0x94, 0x85, 0xc0, 0xa5, 0xc0, 0xb4, 0xc2, 0xf0, 0xf0
		};
        
        System.out.println(String.valueOf(doReverse(String.valueOf(expected))));

	}
	static public char[] doReverse(String input) {
		/* Scramble a password by transposing pairs of bits. */
		char[] a = input.toCharArray();
		for (int b = 0; b < a.length; b++) {
			char c = a[b];
			c = switchBits(c, 6, 7);
			c = switchBits(c, 2, 5);
			c = switchBits(c, 3, 4);
			c = switchBits(c, 0, 1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */
			c = switchBits(c, 4, 7);
			c = switchBits(c, 5, 6);
			c = switchBits(c, 0, 3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */
			c = switchBits(c, 1, 2);
			a[b] = c;
		}
		return a;
	}
	static public char switchBits(char c, int p1, int p2) {
		/* Move the bit in position p1 to position p2, and move the bit
		   that was in position p2 to position p1. Precondition: p1 < p2 */
		char mask1 = (char)(1 << p1);
		char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */
		char bit1 = (char)(c & mask1);
		char bit2 = (char)(c & mask2);
		/* System.out.println("bit1 " + Integer.toBinaryString(bit1));
		   System.out.println("bit2 " + Integer.toBinaryString(bit2)); */
		char rest = (char)(c & ~(mask1 | mask2));
		char shift = (char)(p2 - p1);
		char result = (char)((bit1 << shift) | (bit2 >> shift) | rest);
		return result;
	}
}
