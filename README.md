## Debugging 
Python use call by sharing. You are essentially always passing the object itself, and the object's 
mutability determines whether or not it can be modified. Lists and Dicts are mutable objects. 
Numbers, Strings, and Tuples are not. 

In this case, the dictionary is passed to the function, not a copy. So, when you modify dict, you 
are also modifying the original copy. The solution is deepcope & changes or new dict creation. 
Whereas we are updating the entire dictionary, it is more profitable to create a new empty object 
and fill it.

### Testing
```
    $ python -m unittest debugging.py
```

## The largest loss

In my opinion, The best solution has O(n) time complexity. Going throw the list of prices we calculate
a potential loss as difference between current price and the largest price before. Update the largest 
loss in case potential loss is higher. Also, update the largest price if the current price is higher.

### Testing
**Comment**: an additional library is used to check the runtime and prevents the logic of function 
from being replaced with a slower algorithm.
```
    $ pip install -r requirements.txt
    $ python -m unittest largest_loss.py
```