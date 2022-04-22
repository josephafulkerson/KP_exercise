#Python 3.9.8

#Runtime: O(N)

#Exercise:

At K&P Remodeling we have people we call Promoters. It's their job to walk around Home Depot, approach customers and attempt to schedule appointments for the customers to meet with our designers. We want to flag Promoters who had a bad day so their managers can contact them and ask what happened.

The way we're going to do this is by comparing their total number of "Approaches" for a given day to the median number of approaches over a previous n days. If the number of approaches for that day is less than or equal to 1/2 the median of the preceding n days, we will flag that promoter.

If a promoter has worked fewer than n days, we will not flag the promoter.

Your solution must take the list of approaches and return the total number of times that promoter would have been flagged for all the days they worked.

Parameters:
approaches = a list of i integers, where 0 <= i <= 500, and the length of the list is greater than or equal to zero and less than 10,000.

days = an integer representing the number of preceding days

output = an integer representing the total number of times the Promoter would have been flagged.

Example:
A promoter works 8 days. On the first day they approach 90 customers, the second day they approach 80, then 100, 30, 110, 70, 130, and finally 35 on the last day.
If the previous days n is set to three, how many times would the promoter be flagged?

approaches = [90, 80, 100, 30, 110, 70, 130, 35]
days = 3
output = 2
The promoter would have been flagged on the fourth day and the final day.

Another example:
approaches = [60, 45, 92, 80, 75]
days = 4
output = 0

At the top of your submission please include what version of python you used as well as the big O notation for your algorithm.
