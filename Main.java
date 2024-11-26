import java.util.Arrays;
import java.util.List;

class SonarIssueCreation {
    private List<String> badGrades = null;

    public String testSplitArray() {
        badGrades = Arrays.asList("C", "D", "E");

        List<String> myGrades = Arrays.asList("A,B,A", "A,C,A", "A,D,E");
        String test = "Hello World!";
        return test + " LLM World!";
    }

    // CodeQL issue: Potential NullPointerException due to lack of null check before accessing badGrades
    public void processGrades() {
        //if (badGrades != null) {
            for (String grade : badGrades) {
                System.out.println("Bad grade: " + grade);
           //}
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // 创建 SonarIssueCreation 对象
        SonarIssueCreation sonarIssueCreation = new SonarIssueCreation();
        
        // 调用 processGrades 方法
        sonarIssueCreation.processGrades();
    }
}
