package factorymethod;

import java.io.*;


public class Driver
{

    /**
     * The entry-point of the application
     *
     * @param args    The command-line arguments
     */
    public static void main(String[] args) throws Exception
    {
       BufferedReader                 in;
       DirectoryListing               dir;
       DirectoryListingFactory        factory;
       String                         path;

       factory = new DirectoryListingFactory();

       in = new BufferedReader(new InputStreamReader(System.in));
       System.out.print("Enter a path: ");
       while ((path = in.readLine()) != null) 
       {
          dir = factory.createDirectoryListing(path);
          print(dir);
          System.out.print("Enter a path: ");
       }
    }


    /**
     * Print a DirectoryListing
     *
     * @param dir    The DirectoryListing to print
     */
    public static void print(DirectoryListing dir)
    {
       File[]         files;
       int            i;

       files = dir.getContents();

       for (i=0; i < files.length; i++) 
       {
          System.out.println(files[i].getName());
       }
       System.out.println("\n\n");
    }
}