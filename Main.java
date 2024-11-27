import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;


public class Main {
    
    public static void main(String[] args) throws FileNotFoundException {
        String str = null;
        // 试图调用 null 引用的方法
        System.out.println(str.length());

        int[] numbers = {1, 2, 3};
        // 访问越界索引
        System.out.println(numbers[3]);

        Object obj = "Hello";
        // 错误地尝试将 String 转换为 Integer
        Integer number = (Integer) obj;
        System.out.println(number);

        BufferedReader reader = new BufferedReader(new FileReader("test.txt"));
        try {
            System.out.println(reader.readLine());
        } catch (IOException ex) {
        }
    }
    
}