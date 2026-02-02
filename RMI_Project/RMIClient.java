import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIClient {

    public static void main(String[] args) {

        try {
            String serverIP = "20.188.114.10";
            int port = 1099;

            Registry registry = LocateRegistry.getRegistry(serverIP, port);
            Calculator calc = (Calculator) registry.lookup("CalcService");

            int addResult = calc.add(20, 10);
            int subResult = calc.subtract(20, 10);

            System.out.println("Addition: " + addResult);
            System.out.println("Subtraction: " + subResult);

        } catch (Exception e) {
            System.out.println("RMI Client Error:");
            e.printStackTrace();
        }
    }
}

