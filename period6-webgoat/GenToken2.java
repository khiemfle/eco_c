/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

public class Main
{
    public static void main(String[] args) {
        // if (args == null || args.length != 2) {
        //     System.out.println("Need a username and key");
        //     System.exit(1);
        // }
        String username = "admin";
        String key = "w";
        System.out.println("Generation password reset link for " + username);
        
        for (int i = 0; i < 1000; i++) {
            if (i >= 20) {
                System.out.println("Length = " + i);
                System.out.println(new PasswordResetLink().createPasswordReset(username, key));    
            }
            key = key + "w";
        }
        
    }
}
