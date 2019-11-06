import java.util.Random;

// 
// Decompiled by Procyon v0.5.36
// 

public class PasswordResetLink
{
    public String createPasswordReset(final String s, final String s2) {
        final Random random = new Random();
        if (s.equalsIgnoreCase("admin")) {
            random.setSeed(s2.length());
        }
        return scramble(random, scramble(random, scramble(random, MD5.getHashString(s))));
    }
    
    public static String scramble(final Random random, final String s) {
        final char[] charArray = s.toCharArray();
        for (int i = 0; i < charArray.length; ++i) {
            final int nextInt = random.nextInt(charArray.length);
            final char c = charArray[i];
            charArray[i] = charArray[nextInt];
            charArray[nextInt] = c;
        }
        return new String(charArray);
    }
    
    public static void main(final String[] array) {
        if (array == null || array.length != 2) {
            System.out.println("Need a username and key");
            System.exit(1);
        }
        final String str = array[0];
        final String s = array[1];
        System.out.println("Generation password reset link for " + str);
        System.out.println("Created password reset link: " + new PasswordResetLink().createPasswordReset(str, s));
    }
}