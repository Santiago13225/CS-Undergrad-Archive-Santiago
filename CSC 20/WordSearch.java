/** Author: Alec Resha
*   Date: Feb 10, 2020
*   Project: Lab 3: Word Search
*   Purpose: Read list of words to find into an array, search in another array for them
 */

import java.io.*;
import java.util.*;

public class WordSearch {

	public static void main(String[] args) {
		Scanner input = null;
		try {                                     //Checks if file can be found, stops program if not.
			File f = new File("wordpuzzle.dat");
	      input = new Scanner(f);
		}
		catch(FileNotFoundException ex) {
			System.out.println("File not found");
         return;
		}
      
      String[] needles = new String[6]; //Makes needles array, items to search for
      fillArray(input, needles);        //Fills array to length
      System.out.println();            
      String[] haystack = new String[20];//Makes haystack array
      fillArray(input, haystack);       //Fills haystack array
      
      
      //Arrays.sort(needles); //Sorts needles
        
      int col = -1;                    //Initializes col
      boolean found = false;           //used to catch words that are not found
      
      for(int i = 0; i < needles.length; i++){  //Increment needles (Search for one word fully at a time)
         found = false;
         for(int j = 0; j < haystack.length; j++){ //Increment haystack, checking each line for needles word
            if(haystack[j].indexOf(needles[i]) > -1){
             System.out.println(needles[i] + " found at row " + (j + 1) + " column " + (haystack[j].indexOf(needles[i]) + 1)); //Outputs when word is found
             found = true; //Mark word as found
            }
         }
         if(found == false)
            System.out.println(needles[i] + " not found."); //If word not found in all of haystack, say word not found
      }
    }//End of main
   
   public static void fillArray(Scanner input, String[] array){ //Used to read into files based on array size
      for(int i = 0; i < array.length; i++){
         if(input.hasNextLine()){
           String line = input.nextLine();
          array[i] = line;
          if(line.equals("***")){                               //Excludes asterisk bar from being in beginning of second array
            line = input.nextLine();
          }
         }
         else{
            array[i] = " ";                                   //fills empty spaces
         }
      }
   }

}//End of class
