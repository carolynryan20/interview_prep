import java.util.Collections;
import java.util.List;

/**
 * YahtzeeScorer.java
 * A class score the die game Yahtzee
 * Author: Carolyn Ryan
 * Date:  1/14/16
 */
public class YahtzeeScorer {
    private Boolean straightScored;
    private Boolean yahtzeeScored;
    private Boolean ofAScored;
    private Boolean fullHouseScored;
    private int scoreTotal;

    public YahtzeeScorer() {
        // Define variables upon instantiation of class
        straightScored = false;
        yahtzeeScored = false;
        ofAScored = false;
        fullHouseScored = false;
        scoreTotal = 0;
    }

    // Method for general scoring
    public boolean score(String type, List<Integer> dieList) {
        // Check to ensure that the dieList is the correct size, if not then scoring fails
        if (!(dieList.size() == 5)) {
            return false;
        }

        // Sort the dieList for easier scoring
        Collections.sort(dieList);

        // A series of if statements to check the type and if that category has already been scored
        // If the statement is true then a call to the corresponding scoring method is made
        if ((type.equals("straight")) && !(straightScored)){
            return scoreStraight(dieList);
        }

        if ((type.equals("yahtzee")) && !(yahtzeeScored)){
            return scoreYahtzee(dieList);
        }

        if ((type.equals("3ofA")) && !(ofAScored)){
            return scoreThreeOfA(dieList);
        }

        if ((type.equals("fullHouse")) && !(fullHouseScored)) {
            return scoreFullHouse(dieList);
        }
        // If none of the statements were triggered, then the type is not recognized
        // Return false for un-recognized type
        return false;
    }

    // Method for scoring full house
    private boolean scoreFullHouse(List<Integer> dieList) {
        // A series of if statements that will ensure the die indeed show a full house
        if ((dieList.get(0) == dieList.get(1)) && (dieList.get(3) == dieList.get(4))){
            if ((dieList.get(1) == dieList.get(2)) || (dieList.get(2) == dieList.get(3))) {
                if (! (dieList.get(1) == dieList.get(4))) {
                    scoreTotal += 25;           // Add 25 to the total score for having a full house!
                    fullHouseScored = true;     // Set to true after check for correct die to ensure category actually gets scored
                    return true;
                }
            }
        }
        return false;
    }

    // Method for scoring three of a kind
    private boolean scoreThreeOfA(List<Integer> dieList) {
        if((dieList.get(0) == dieList.get(1)) && (dieList.get(1) == dieList.get(2))){
            scoreTotal += ((dieList.get(0)*3) + dieList.get(3) + dieList.get(4));  // All die added together = score for 3ofA
            ofAScored = true;
            return true;
        }
        if((dieList.get(1) == dieList.get(2)) && (dieList.get(2) == dieList.get(3))){
            scoreTotal += ((dieList.get(1)*3) + dieList.get(0) + dieList.get(4));
            ofAScored = true;
            return true;
        }
        if((dieList.get(2) == dieList.get(3)) && (dieList.get(3) == dieList.get(4))){
            scoreTotal += ((dieList.get(2)*3) + dieList.get(0) + dieList.get(1));
            ofAScored = true;
            return true;
        }
        return false;
    }

    // Method for scoring yahtzee
    private boolean scoreYahtzee(List<Integer> dieList) {
        // For loop checks for die that don't match
        // False returned when unmatching die found
        for (int i=0; i<= 3; i++) {
            int die = dieList.get(i);
            int nextDie = dieList.get(i+1);
            if (!(die == nextDie)) {
                return false;
            }
        }
        yahtzeeScored = true;
        scoreTotal += 50;   // A yahtzee is worth 50 points!
        return true;
    }

    // Method for scoring straight
    private boolean scoreStraight(List<Integer> dieList) {
        // For loop checks to see if there is a break in the straight
        // If a break occurs, return false
        for (int i=0; i<= 3; i++) {
            int die = dieList.get(i);
            int nextDie = dieList.get(i+1);
            if (!(die+1 == nextDie)){
                return false;
            }
        }
        straightScored = true;
        scoreTotal += 40;   // A straight is worth 40 points.  Add that to the total.
        return true;
    }

    // A method to return the scoreTotal
    public int getScore(){
        return scoreTotal;
    }
}
