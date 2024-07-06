package strategy;

import java.awt.*;
import java.awt.image.*;
import java.io.*;
import javax.imageio.*;
import javax.swing.*;

//import math.*;



public class PosterizerDriver
{
    /**
     * The entry point of the application
     *
     * @param args   The command-line arguments
     */
    public static void main(String[] args) throws Exception
    {
       BufferedImage  image;
       
       ImageIcon   icon;       
       JFrame      window;
       JLabel      label;       
       JPanel      contentPane;       
       Posterizer  posterizer;
       


       window = new JFrame();
       contentPane = (JPanel)window.getContentPane();
       contentPane.setLayout(new BorderLayout());
       //use absolute path to the picture file, with "/" instead of "\"
       //use bmp file only
       image = ImageIO.read(new File("D:/house.bmp"));

       posterizer = new Posterizer();
       //use any of line 40, 41, 42 to setMetric
       //posterizer.setMetric(new EuclideanMetric());
       posterizer.setMetric(new RectilinearMetric());
       //posterizer.setMetric(new SupremumMetric());
       posterizer.toBlackAndWhite(image);
       

       icon  = new ImageIcon(image);       

       label = new JLabel(icon);
       contentPane.add(label, BorderLayout.CENTER);
       
       window.setSize(800,800);
       window.setVisible(true);       
       
    }
    
    
}