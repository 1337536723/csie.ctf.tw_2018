
import java.util.Arrays;

public class Main {
   public static void main(String[] var0) {
      byte[] var1 = new byte[]{37, 5, 118, 90, -112, -13, -34, 7, 106, 102, -115, -20, -51, 0, 80, 84, -115, -3, -34, 2, 121, 84, -87, -8};
      byte[] var3 = new byte[]{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
      for(int var2 = 0; var2 < var1.length; ++var2) {
         var3[var2] = (byte)(var1[var2] ^ (var2 * 42 + 1 ^ 66));
      }
      String s1 = new String(var3);
      System.out.println(s1);
   }
}