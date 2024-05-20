public class RandomWalkersTest {
    public static void main(String[] args) {
        // accept integer values and set values to 0
        int r = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        int x;
        int y;
        // set doubles for easy evaluation of avg
        double steps = 0;
        double avg;

        // make a for loop for the amount of trials that will be run
        for (int i = 0; i < trials; i++) {
            // zero x and y for every trial to begin at same place each time
            x = 0;
            y = 0;
            // run a while loop for the Manhattan value that will run until it is reached
            // and will increment steps and add them to the sum
            do {
                double p = Math.random();
                double p2 = Math.random();
                if (p < 0.5) {
                    x++;
                    steps++;
                }
                else {
                    x--;
                    steps++;
                }
                if (p2 < 0.5) {
                    y++;
                    steps++;
                }
                else {
                    y--;
                    steps++;
                }
                // increment steps for each time loop is run

            }
            while ((Math.abs(x) + Math.abs(y)) < r);

        }
        // compute average number of steps and print
        avg = (steps / trials);
        System.out.println("average number of steps = " + avg);
    }

}
