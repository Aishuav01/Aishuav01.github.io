#include<stdio.h>
#include<string.h>
main()
{
int j,i;
char c ,s3[100], s2[70],s1[100];
printf("Enter the string ");
gets(s3);
i=0;
if(s3[i]!= '\0')
{
  s1[i] = s3[i];
  i++;
}
 
 j = strlen(s1);
 
 i=0;
if(s3[j-2]!= '\0')
{ 
 s2[i]=s3[j];
 i++;
 j++;

}
c = s3[0];
printf("Ripping the lower case %c from his shirt , Letterman changes %s back to %s " , c , s1 , s2 );
printf("%d" , &j);
}
 
