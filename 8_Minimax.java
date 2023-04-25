import java.util.Scanner;
public class Minimax 
{

   	public static int min(int a[][],int n,int setIndex) 
   	{
        	int smallest = a[setIndex][0];
	        for(int i=1; i<n; i++) 
		{
	        	if(smallest > a[setIndex][i])
        	        smallest = a[setIndex][i];
        	}
        	return smallest;
    	}

	public static int max(int a[][],int n,int setIndex) 
	{
        	int greatest = a[setIndex][0];
	        for(int i=1; i<n; i++) 
		{
        		if(greatest < a[setIndex][i])
	                greatest = a[setIndex][i];
        	}
	        return greatest;
    	}

	public static void main(String[] args) 
	{
       		Scanner s = new Scanner(System.in);
	        System.out.println("Enter the no. of nodes in each subtree");
        	int n = s.nextInt();
	        int set[][] = new int[n][n];
        	System.out.println("Enter the utility values: ");
	        for(int i=0; i<n; i++) 
		{
	            	for(int j=0; j<n; j++) 
			{
                		set[i][j] = s.nextInt();
            		}
        	}
	
	        int max[][] = new int[1][n];
        	System.out.print("The min values retured are: ");
	        for(int i=0; i<n; i++) 
		{
	            max[0][i] = min(set, n, i);
        	    System.out.print(" " +max[0][i]);
        	}

	        System.out.println("");
        	int maxValue = max(max, n, 0);
	        System.out.println("The Max Value is " + maxValue);
    	}
}