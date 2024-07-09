public class Solution {
    public double AverageWaitingTime(int[][] customers) {
        int free = customers[0][0];
        double total = 0;

        for(int i = 0; i < customers.Length; i ++) {
            if(free < customers[i][0]){
                free = customers[i][0];
            }
            free = free + customers[i][1];
            total = total + (free - customers[i][0]); 
            Console.WriteLine(free);
            Console.WriteLine(total);
        }
        return (total/customers.Length);
    }
}