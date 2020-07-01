# whatsapp-gifting-simulator

A simulation I wrote to prove that this "whatsapp gifting" crap is really a pyramid scheme.

To run it you will need python 3.

By default it will simulate for about 1000 days with a "population" of 100 000 people(assuming the entire population is even willing to join which is extremely unlikely, so this is being optimistic), and with a single group of 5 people starting out(who didn't pay any joining fee obviously), and the joining fee set to 1000 units of money(rands in South Africa).

The results from running with the above settings:

```
Running simulation with initial group of 5 people
Population size: 100000
Starting cash per person: 1000
Joining fee: 1000
Results after 1000 days:
Count of people who lost all their money: 81920
Count of people who broke even: 1697
Count of people who gained: 16383
Total groups formed in the end: 16384
```

This means that if 100 000 people are willing to participate, and assuming uniform distribution of new recruits to groups, after 1000 days (maybe even less than that) there would've been 81920 people who did not
receive any payment whatsoever before willing people ran out. About 82% of the population lost out completely. Only about 16% of the population who joined in early
actually made a profit. While about 1.7% of the population managed to get paid back what they put in.


If we set it to a population of 100 people we get a similar result

```
Running simulation with initial group of 5 people
Population size: 100
Starting cash per person: 1000
Joining fee: 1000
Results after 1000 days:
Count of people who lost all their money: 80
Count of people who broke even: 5
Count of people who gained: 15
Total groups formed in the end: 16
```


With 100 willing people, 80 of them lose out completely, 5 break even, and 15 actually make a profit.


This is a typical pyramid scheme and it should be illegal.


