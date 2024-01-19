## Prompt:
In a new post-apocalyptic world, the world queen is desperately concerned about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or else they face massive fines. If all families abide by this policy -- that is, they continue to have children until they have one girl, at which point they immediately stop -- what will the gender ratio of the new generation be? (Assume that the odds of someone having a boy or a girl on any given pregnancy is equal.) Solve this out logically and then write a computer simulation of it.

## Answer:
Use expected value of the number of boys that each family has:
```
    Expected Value = Sum of (Probability of achieving number of boys * Number of boys)
```

Consider a population:
- 1/2 will have 1 girl on first try: G                      => Probability of sequence: 1/2
- 1/2 of the rest will have 1 girl on second try: BG        => Probability of sequence: 1/4
- 1/2 of the rest will have 1 girl on third try: BBG        => Probability of sequence: 1/8
- ...

Therefore, we have the sum of probabilities:
```
    (0 * 1/2) + (1 * 1/4) + (2 * 1/8) + (3 * 1/16) + ...
```
Try converting these to a large common denominator (e.g. 128) and add them. The possibility is quite close to 1, meaning each family will have 1 boy (and 1 girl).


Simulation is straight-forward to write.