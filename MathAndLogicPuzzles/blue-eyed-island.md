## Prompt:
A bunch of people are living on an island when a visitor comes with a strange order: all blue-eyed people must leave the island as soon as possible. There will be a flight out at 8:00pm every evening. Each person can see everyone else's eye color, but they do not know their own (nor is anyone allowed to tell them). Additionally, they do not know many people have blue eyes, although they do know that at least one person does. How many days will it take the blue-eyed people to leave.

## Solution:
Note: It's important to recognize that the blue-eyed people are the ones making the decision (since it'd just be terribly easy for an outsider to accomplish this). We are just thinking of a scheme for them.

Let c (c > 0) be the number of people with blue eyes:
- If c = 1: The person with blue eyes see that no one else has blue eyes, and deduces that he must be the one. He leaves on the first night
- If c = 2: Each of the blue-eyed people see that there is 1 other blue-eyed person, however they are not sure whether he himself has blue eyes. If he does not, then it is case `c = 1`, and that person will have left by the next day. Therefore, both people wait until the next day. If they both are still there, they leave together.
- If c > 2: Recursive. Waits until day `c`.

