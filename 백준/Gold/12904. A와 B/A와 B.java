
import java.io.*;
import java.util.*;


public class Main {


    public static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String S = br.readLine();
        String T = br.readLine();


        ;

        while(true){

            if(S.length() == T.length()){
                if(S.equals(T)){
                    answer = 1;
                }
                break;
            }

            if(T.charAt(T.length()-1)=='A'){
                T = T.substring(0,T.length()-1);
            }else{
                T = T.substring(0,T.length()-1);
                StringBuffer sb = new StringBuffer(T);
                T = sb.reverse().toString();
            }
        }

        System.out.println(answer);
    }


}