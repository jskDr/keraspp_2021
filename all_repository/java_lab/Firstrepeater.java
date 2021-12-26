import java.util.*;

public class Firstrepeater {
    public void run() {
        String Str = "Firstrepeater";
        char[] str = Str.toCharArray();
        for (char ch: str)
            System.out.print(ch);
        System.out.println();
        FirstRepeatedChar(str);
    }
    public char FirstRepeatedChar(char[] str) {
        int[] count = new int[256];
        int i;
        for (i=0; i < count.length; i++){
            count[i] = 0;
        }
        for (i=0; i < str.length; i++){
            if(count[str[i]] == 1) {
                System.out.println("Repeated char: " + str[i]);
                break;
            }
            else {
                count[str[i]]++;
            }
        }
        if (i==str.length)
            System.out.println("No repeated character.");
        return 0;
    }
}