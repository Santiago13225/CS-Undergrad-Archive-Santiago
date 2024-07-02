import java.io.FileNotFoundException;
import java.util.*;
class DirectoryMain{
  public static void main(String[] args) throws FileNotFoundException{
    Directory phoneDirectory = new Directory("names.txt"); //create the directory
    DirectoryHelper.interpretChoice(phoneDirectory); // run the menu and interpret choices
}