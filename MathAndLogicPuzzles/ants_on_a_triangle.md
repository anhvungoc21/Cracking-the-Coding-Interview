## Prompt:
There are three ants on different vertices of a triangle. What is the probability of collision (between any two or all of them) if they start walking on the sides of the triangle? Assume that each ant randomly picks a direction, with either direction being equally likely to be chosen, and that they walk at the same speed.

Similarly, find the probability of collision with n ants on an n-vertex polygon. 

## Answer:
First, in order for a collision to happen, there must be at least 1 ant going in the opposite direction of other ants.
So, we can think in terms of when a collision DEFINITELY does NOT happen, that is when all ants go in the same direction.

I like to visualize this as a bit flipping problem. We have n 0 bits, basically the question is asking what is the probability of at least 1 bit flipping. That is the same as 1 minus the probability of all bits flipping and all bits staying:
```
    1 - ((1/2)^n + (1/2)^n)
  = 1 - 2 * (1/2)^n
  = 1 - (1/2)^(n-1)
```

In the triangle example, the probability is `1 - (1/2)^2 = 3/4`

