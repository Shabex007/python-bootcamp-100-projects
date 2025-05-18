# word_list.py
logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
'''
# Hangman states
states = [
    '''
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 ____|____
 ''' , '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|____
 ''' , '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|____
 ''' , '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 ____|____
 ''' , '''
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
 ____|____
 ''' , '''
      _______
     |/      |
     |      (_)
     |      \
     |      
     |      
     |
 ____|____
 ''' , '''
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 ____|____
 ''' , '''
      _______
     |/      |
     |      
     |      
     |       
     |     
     |
 ____|____
 ''']

# Word categories
words = {
    "countries": ["india", "germany", "brazil", "canada", "france", "japan", "china", "italy", "mexico", "russia", "spain", "turkey", "egypt", "greece", "australia"],
    "animals": ["elephant", "giraffe", "kangaroo", "dolphin", "penguin", "cheetah", "crocodile", "squirrel", "hippopotamus", "rhinoceros", "wolf", "fox", "parrot", "eagle", "tiger"],
    "fruits_veggies": ["apple", "banana", "carrot", "tomato", "grape", "watermelon", "potato", "orange", "cucumber", "strawberry", "blueberry", "onion", "pineapple", "avocado", "broccoli"],
    "foods": ["pizza", "burger", "pasta", "sushi", "tacos", "sandwich", "noodles", "salad", "biryani", "pancake", "fries", "steak", "curry", "dumplings", "lasagna"]
}