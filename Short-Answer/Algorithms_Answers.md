#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)

b) O(n^2)

c) O(Log n)

## Exercise II

Best way to do it would be to start at the middle of the floors rounding up to the next highest floor if an odd number.
if the egg doesnt not break at nth floor
increase floor

    if the egg does break go down a floor
        decrease floor
        return floor_number
    return floor_number

you would also need to set a variable to track what floor you are on
aswell as setup somthing that says if you break an egg and go down a floor set the optimal floor to that number and return it. I think that there could be a few ways to do this but It would take me sitting down with a whiteboard to get some real code.
