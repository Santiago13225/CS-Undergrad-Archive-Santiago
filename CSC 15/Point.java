public class Point
{
    private double x;
    private double y;
    
    //cretae constrcutor, no static , no return vale, the name is exact same as the class
    public Point(double x, double y)
    {
       this.x = x;
       this.y = y;
    }
    public Point()
    { 
      this.x = 1; 
      this.y = 1;
    }
    public Point(int x, int y)
    {
       this.x = x;
       this.y = y;
    }
    //mutator, allows you to change the values for the attributes
    public void setX(double newX)
    {
       this.x = newX;
    }
    public void setY(double newY)
    {
       this.y = newY;
    }
    //getter methods
    public double getX()
    {
       return x;
    }
    public double getY()
    {
       return y;
    }

    

    
    //cretae a string representing my object
    public String toString()
    {
      String s = "";
      s = "( " + this.x  + "," + this.y + " )";
      return s;
    }

    
    
}