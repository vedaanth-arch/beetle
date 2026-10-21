class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        unique_integers = set() #set used for handling the different count 
        current_num = ""
        
        for char in word:
            if char.isdigit():
                # Step 3: Assign/accumulate into the temporary variable
                current_num += char
            else:
                # Step 4: The number has ended (we hit a letter)
                if current_num:
                    unique_integers.add(int(current_num))
                    current_num = "" # Reset for the next number
                    
        # Catch the last number if the word ends with digits
        if current_num:
            unique_integers.add(int(current_num))
            
        # The final count of unique integers is the size of our set
        return len(unique_integers)