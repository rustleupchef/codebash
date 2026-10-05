import java.util.*;

public class Main {
    private static String[] getLines() {
        Scanner scanner = new Scanner(System.in);
        int size = Integer.parseInt(scanner.nextLine());
        String[] lines = new String[size];
        for (int i = 0; i < size; i++) 
            lines[i] = scanner.nextLine();
        scanner.close();
        return lines;
    }

    private  static String[][] getGroups() {
        Scanner scanner = new Scanner(System.in);
        int size = Integer.parseInt(scanner.nextLine());
        String[][] groups = new String[size][];
        for (int i = 0; i < size; i++) {
            int length = Integer.parseInt(scanner.nextLine());
            groups[i] = new String[length];
            for (int j = 0; j < length; j++) {
                groups[i][j] = scanner.nextLine();
            }
        }
        scanner.close();
        return groups;
    }

    public static void main(String[] args) {
        
    }
}