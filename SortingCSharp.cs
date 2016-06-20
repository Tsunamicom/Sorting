using System;

namespace SortingCSharp
{
    class Sorting_Algorithms
    {
        static void Main()
        {
            //Instantiate a New Array
            int[] testArray = new int[] {5, 4, 6, 3, 2, 6, 2, 6, 99, 10, 1, 5};

            //Iterate and print each element in original array
            for (int num = 0; num < testArray.Length; num++)
            {
                Console.Write(String.Format("{0} ", testArray[num]));
            }
            Console.WriteLine();

            //Perform Insertion Sort on Array
            insertion(testArray);

            //Iterate and print each element in sorted array
            for (int num = 0; num < testArray.Length; num++)
            {
                Console.Write(String.Format("{0} ", testArray[num]));
            }
            Console.WriteLine();
        }

        // Insertion Sort on an array of integers
        static int[] insertion (int[] testArray) {
            for (int i=1; i<testArray.Length; i++)
            {
                int j = i;
                while ((j > 0) && (testArray[j-1] > testArray[j])){
                    int temp = testArray[j-1];
                    testArray[j-1] = testArray[j];
                    testArray[j] = temp;
                    j--;
                }
            }
            
            return testArray;
        }
    }
}
