## Prompt:
You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips which can be used to detect poison. A single drop of poison will turn the test strip positive permanently. You can put any number of drops on a test strip at once, and you can reuse a test strip as many times as you'd like (as long as the results are negative). However, you can only run tests once per day and it takes seven days to return a result. How would you figure out the poisoned bottle in as few days as possible.

## Answer:
### Initial Observations:
- Running tests once per day means that we would like to make use of as many of the test strips in one day as possible.
- Divide an conquer seems like the way to go, but we should probably divide by the number of test strips instead of 2 or sth.

### Naive Solution:
- While we have not found the poison:
    + Divide the remaining n bottles across 10 test strips
    + Wait 7 days
    + Get rid of all bottles whose test strips are negative

The time taken can be measured by the number of bottles remaining at each iteration:
- Iter 0: 1000 bottles
- Iter 1: 100 bottles
- Iter 2: 10 bottles
- Iter 3: 1 bottle
=> We take 21 days to solve this

In this solution, we should be aware that the 7-day wait seems suspicious. There must be an optimization that makes use of that time.



### Clever Solution:
Recognize that we can do tests on the strips that still has tests running on it. Since there is always a 7-day interval for results to turn up, if we know when we placed a set of tests, we know 7 days later is the day on which the results for those tests turn up.

Think about the naive solution and how bottles might be divided.

1000 -> 000-099, 100-199, ..., 900-999
100 -> a00-a09, a10-a19, ..., a90-a99
10 -> ab0, ab1, ... ab9

Here, we notice that a clever division of the bottles actually "reveals" each digit of the bottle index.
What if we can test these 3 digits separately? Indeed, we can:
- Test for first digit on day 0->7
- Test for second digit on day 1->8
- Test for third digit on day 2->9

On day 7, 8, and 9, there might be few of these scenarios:
- If a strip turns from negative to positive, we know the corresponding digit of the poison bottle.
- If no strip changes:
    + On day 8: Then digit 1 and digit 2 are equal
    + On day 9: Then digit 3 is the same as either digit 1 or digit 2 (provided they are different)
Therefore, we need to do an additional test (on day 3->10, just in case) for the last digit. To avoid it from repeating the result of day 2->9, we just shift (increment/decrement) the digits by 1 so that a change is guaranteed to occur.