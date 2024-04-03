package youlAlgorithm.java.zip.string;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 늑대와_올바른_단어 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] word = br.readLine().toCharArray();

        int index = 0;
        while(index < word.length) {
            // wolf 순서대로 확인
            int w_count = 0;
            while(index < word.length && word[index] == 'w') {
                w_count += 1;
                index += 1;
            }

            int o_count = 0;
            while(index < word.length && word[index] == 'o') {
                o_count += 1;
                index += 1;
            }

            int l_count = 0;
            while(index < word.length && word[index] == 'l') {
                l_count += 1;
                index += 1;
            }

            int f_count = 0;
            while(index < word.length && word[index] == 'f') {
                f_count += 1;
                index += 1;
            }


            if (w_count != o_count || l_count != f_count || w_count != l_count) {
                System.out.print("0");
                return;
            }
        }

        if (index >= word.length) {
            System.out.println("1");
        }
    }
    
}
