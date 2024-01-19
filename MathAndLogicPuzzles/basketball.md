## Prompt
You have a basketball hoop and someone says that you can play one of two games.
- Game 1: You get to make the hoop
- Game 2: You get three shots, and you have to make two of three shots

If `p` is the probability of making a particular shot, for which values of `p` should you pick one game or the other?

## Answer

### Initial Logic:
Examine each game:
- Game 1: Probability of winning is `p`
- Game 2: Probability of winning is:
    + Making two shots:
        * Making the second and third. Missing the first: `(1 - p) * p * p`
        * Making the first and second. Missing the third: `p * p * (1 - p)`
        * Making the first and third. Missing the second: `p * (1 - p) * p`
    + Making three shots: `p * p * p`
The probability for game 2 is:
```
    3p^2 - 2p^3
```

So, we want to find out when each odds are superior:
```
    3p^2 - 2p^3 > p
<=> 3p^2 - (2p^3 + p) > 0
<=> 3p^2 - p(2p^2 + 1) > 0
<=> 3p - 2p^2 - 1 > 0
<=> 2p - 2p^2 + p - 1 > 0
<=> 2p(1 - p) - (1 - p) > 0
<=> (2p - 1)(1 - p) > 0
```

To choose game 2, both terms must be either both positive or both negative. Since `p < 1`, `(1 - p)` is always positive.
Therefore, both terms must be positive:
```
    2p - 1 > 0
    1 - p > 0

=>  p > 1/2
    p < 1

=> 1/2 < p < 1
```

So, we should:
- Play Game 2 if `1/2 < p < 1`
- Play Game 1 if `0 < p < 1/2`

If `p` is one of the roots of the equation above, that is `0.5` or `1`, 
it doesn't matter which game we play because the probabilities are equal.
Also, we did a division by 0. An odds of 0 also makes no difference in
each game is chosen.