public class PointDriver
{
  public static void main(String[] args)
  {
    Point p = new Point(3,4);
    Point p1 = new Point();
    System.out.println(p);
    System.out.println(p1);
    //calling the mutator methods
    p.setX(10);
    p.setY(20);
    //getter methods
    System.out.println(p.x);
    
    System.out.println(p);
    
  }
}