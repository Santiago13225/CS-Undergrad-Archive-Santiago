/* https://www.man7.org/linux/man-pages/man3/readdir.3.html */
#include <dirent.h>
#include <stdio.h>
#include <string.h>

int printFileNamesRecursively( char *name )
{

  DIR           *myDir;
  struct dirent *dir;
  char dirName[1024] ;


  myDir = opendir(name); // OPEN THE DIR OF FILES
  if  ( myDir )
  {
      while ( (dir = readdir(myDir)) != NULL )
        {
           if (dir->d_type & DT_DIR )
             {
                if ( (strcmp (dir->d_name, ".") == 0) ||
                   (strcmp (dir->d_name, "..") == 0 ) )
                      continue;
                else
                {
                  strcpy(dirName, name);
                  strcat (dirName, "/");
                  printf(" Dir name %s \n", dir->d_name);
                  strcat (dirName, dir->d_name) ;
                  printf(" Dir path %s \n", dirName);
                  printFileNamesRecursively(dirName );
                }
             }
              else
                if (dir->d_type & DT_REG)
                   printf(" File name %s \n", dir->d_name);
        }
    closedir ( myDir);
  }


}


int main ( )
{

printFileNamesRecursively(".") ;

}


