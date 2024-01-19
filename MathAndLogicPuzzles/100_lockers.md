## Prompt:
There are 100 closed lockers in a hallway. A man begins by opening all 100 lockers. Next, he closes every second locker. Then on his third pass, he toggles every third locker. This process continues for 100 passes, such that on each pass i, the toggles every ith locker. After his 100th pass in the hallway, in which he toggles only locker 100th, how many lockers are open?

## Answer
### Initial Observations:
- For any ith iteration, i - 1 lockers before it will be fixed. Therefore, for the ith locker, we only need to take
into account the previous iterations.
- In those previous iterations, only in the iterations k where `i mod k = 0` is the ith locker toggled.

### Naive Solution:
For each locker i we can count the number of the denominators of i that we have encountered so far. If the number of denominators (toggles) is odd (the 1 iteration is opening), we know that the locker is open.

### Clever Solution:
For each factor, we know that there is a counterpart that multiplies to that number. We want an odd number of factors, and this only occurs when there is a pair of identical factors (e.g. 6 * 6 = 36). Therefore, only lockers at perfect-square positions will be left open.

There are 10 such perfect squares from 1 to 100: `1*1` through `10*10`.