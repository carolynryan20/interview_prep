import org.junit.Test;

import java.util.Arrays;
import java.util.List;

import static junit.framework.Assert.assertEquals;
import static junit.framework.Assert.assertFalse;
import static junit.framework.Assert.assertTrue;

/**
 * UnitTestYahtzee.java
 * A class to run unit tests on YahtzeeScorer
 * Author: Carolyn Ryan
 * Date:  1/14/16
 */
public class UnitTestYahtzee {
    // Variables used in multiple tests
    private List<Integer> dieList;
    private Boolean alreadyScored;

    @Test
    // Test for instantiation of the YatzeeScorer Class
    public void testYahtzeeClass() {
        YahtzeeScorer myScore = new YahtzeeScorer();
    }

    @Test
    // Test for Normal Play
    // Unscored Category; Correct Die Values
    public void testNormalPlay() {
        YahtzeeScorer myScore = new YahtzeeScorer();
        // Test scoring for straight
        dieList = Arrays.asList(2,3,1,5,4);
        Boolean straightSuccess = myScore.score("straight", dieList);
        assertTrue(straightSuccess);

        // Test scoring for Yahtzee
        dieList = Arrays.asList(1,1,1,1,1);
        Boolean yahtzeeSuccess = myScore.score("yahtzee", dieList);
        assertTrue(yahtzeeSuccess);

        // Test scoring for three of a kind
        dieList = Arrays.asList(4,5,4,4,2);
        Boolean threeOfASuccess = myScore.score("3ofA", dieList);
        assertTrue(threeOfASuccess);

        // Test scoring for full house
        dieList = Arrays.asList(2,1,2,2,1);
        Boolean fullHouseSuccess = myScore.score("fullHouse", dieList);
        assertTrue(fullHouseSuccess);
    }

    @Test
    // Test for Insufficient die in Straight
    // Unscored Category; Incorrect Die Values
    public void testInsufficientDiceStraight() {
        YahtzeeScorer myScore = new YahtzeeScorer();
        Boolean straightFailure;

        // Test different die combinations that should not allow for scoring straight
        dieList = Arrays.asList(1, 2, 3, 4, 6);
        straightFailure = myScore.score("straight", dieList);
        assertFalse(straightFailure);

        dieList = Arrays.asList(1, 2, 2, 3, 4);
        straightFailure = myScore.score("straight", dieList);
        assertFalse(straightFailure);

        dieList = Arrays.asList(2, 3, 4, 4, 4);
        straightFailure = myScore.score("straight", dieList);
        assertFalse(straightFailure);
    }

    @Test
    // Test for Insufficient die in Yahtzee
    // Unscored Category; Incorrect Die Values
    public void testInsufficientDiceYahtzee() {
        YahtzeeScorer myScore = new YahtzeeScorer();
        Boolean yahtzeeFailure;

        // Test different die combinations that should not allow for scoring yahtzee
        dieList = Arrays.asList(1, 2, 3, 4, 6);
        yahtzeeFailure = myScore.score("yahtzee", dieList);
        assertFalse(yahtzeeFailure);

        dieList = Arrays.asList(1, 2, 2, 3, 2);
        yahtzeeFailure = myScore.score("yahtzee", dieList);
        assertFalse(yahtzeeFailure);

        dieList = Arrays.asList(1, 1, 1, 1, 4);
        yahtzeeFailure = myScore.score("yahtzee", dieList);
        assertFalse(yahtzeeFailure);
    }

    @Test
    // Test for Insufficient die in Three of a Kind
    // Unscored Category; Incorrect Die Values
    public void testINsufficientDice3ofA() {
        YahtzeeScorer myScore = new YahtzeeScorer();
        Boolean threeOfAFailure;

        // Test different die combinations that should not allow for scoring 3 of a kinds
        dieList = Arrays.asList(1,1,2,3,4);
        threeOfAFailure = myScore.score("3ofA", dieList);
        assertFalse(threeOfAFailure);

        dieList = Arrays.asList(1,2,3,4,5);
        threeOfAFailure = myScore.score("3ofA", dieList);
        assertFalse(threeOfAFailure);
    }

    @Test
    // Test for Insufficient die in Full House
    // Unscored Category; Incorrect Die Values
    public void testInsufficientDiceFullHouse() {
        YahtzeeScorer myScore = new YahtzeeScorer();
        Boolean fullHouseFailure;

        // Test different die combinations that should not allow for scoring full house
        dieList = Arrays.asList(1, 1, 1, 1, 3);
        fullHouseFailure = myScore.score("fullHouse", dieList);
        assertFalse(fullHouseFailure);

        dieList = Arrays.asList(1, 1, 2, 2, 3);
        fullHouseFailure = myScore.score("fullHouse", dieList);
        assertFalse(fullHouseFailure);

        dieList = Arrays.asList(1, 1, 1, 1, 1);
        fullHouseFailure = myScore.score("fullHouse", dieList);
        assertFalse(fullHouseFailure);
    }

    @Test
    // Test for Already Scored Straight
    // Select category has already been scored
    public void testAlreadyScoredStraight() {
        YahtzeeScorer myScore = new YahtzeeScorer();

        // Score Straight
        dieList = Arrays.asList(1, 2, 3, 4, 5);
        myScore.score("straight", dieList);

        // Test that scoring straight again will fail
        alreadyScored = myScore.score("straight", dieList);
        assertFalse(alreadyScored);
    }

    @Test
    // Test for Already Scored Yahtzee
    // Select category has already been scored
    public void testAlreadyScoredYahtzee() {
        YahtzeeScorer myScore = new YahtzeeScorer();

        // Score Yahtzee
        dieList = Arrays.asList(1, 1, 1, 1, 1);
        myScore.score("yahtzee", dieList);
        // Test that scoring yahtzee again will fail
        alreadyScored = myScore.score("yahtzee", dieList);
        assertFalse(alreadyScored);
    }

    @Test
    // Test for Already Scored Three of A Kind
    // Select category has already been scored
    public void testAlreadyScored3ofA() {
        YahtzeeScorer myScore = new YahtzeeScorer();

        // Score Three of A Kind
        dieList = Arrays.asList(1, 1, 1, 2, 4);
        myScore.score("3ofA", dieList);

        // Test that scoring 3ofA again will fail
        alreadyScored = myScore.score("3ofA", dieList);
        assertFalse(alreadyScored);
    }

    @Test
    // Test for Already Scored Full House
    // Select category has already been scored
    public void testAlreadyScoredFullHouse() {
        YahtzeeScorer myScore = new YahtzeeScorer();

        // Score Full House
        dieList = Arrays.asList(1,1,4,1,4);
        myScore.score("fullHouse", dieList);

        // Test that scoring Full House again will fail
        alreadyScored = myScore.score("fullHouse", dieList);
        assertFalse(alreadyScored);
    }

    @Test
    // Test for Correct Score
    // When prompted the correct current score for the game is returned
    public void testCorrectScore(){
        YahtzeeScorer myScore = new YahtzeeScorer();
        dieList = Arrays.asList(2,2,2,2,2);
        myScore.score("yahtzee", dieList);      // A Yahtzee should add 50 to scoreTotal
        assertEquals(50, myScore.getScore());

        dieList = Arrays.asList(1,2,3,4,5);
        myScore.score("straight", dieList);     // A Straight should add 40 to scoreTotal
        assertEquals(90, myScore.getScore());

        dieList = Arrays.asList(1,1,1,2,3);
        myScore.score("3ofA", dieList);         // A 3 of a kind should add every die to the scoreTotal
        assertEquals(98, myScore.getScore());

        dieList = Arrays.asList(3,3,3,4,4);
        myScore.score("fullHouse", dieList);    // A full house should add 25 to the scoreTotal
        assertEquals(123, myScore.getScore());
    }
}
