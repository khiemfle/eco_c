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
        
        for (int i = 0; i < 6000; i++) {
            if (i >= 3000) {
                System.out.println("//Length = " + i);
                System.out.println("getContent(\"" + new PasswordResetLink().createPasswordReset(username, key) + "\");");    
            }
            key = key + "w";
        }
        
    }
}
