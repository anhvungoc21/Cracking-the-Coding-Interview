## Prompt:

You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight 1.1 grams. Given a scale that provides an exact measurement, how would you find the heavy bottle? You can only use the scale once.

## Answer:

### Initial Logic:
- We can only measure once. There must be a way to include all 20 bottles in one weighing that DISTINGUISHES THEM

### Solution:
- To distinguish bottles, we can use a different number of pills for each bottle.
- Say we put i pills in for the i-th bottle, we will always have:
```
    (1 * 1.0) + (2 * 1.0) + ... + (20 * 1.0) + (k * 0.1)
 =  210 + 0.1k
```
where k is the bottle which has 1.1-gram pills.
- Given that we remember the position of the bottle, we can identify that bottle based the surplus over 210

For example:
Bottle 14 has 1.1-gram pills. We have the total to be `211.4`. We take

```
    (211.4 - 210) / 0.1 = 14
```