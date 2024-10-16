import csv
from functools import reduce

def count(predicate, iterable):
  count_filter = filter(predicate, iterable)
  count_reduce = reduce(lambda x,y: x + 1, count_filter, 0)
  return count_reduce   

def average(itr):
  # If itr is not iterable, this will generate an iterator.  
  iterable = iter(itr) 
  return avg_helper(0, iterable, 0)

def avg_helper(curr_count, itr, curr_sum):
  next_num = next(itr, 'null')
    #Base Case
  if next_num == 'null':
    return curr_sum / curr_count
    #Computation
  curr_sum += next_num
  curr_count += 1
    #Recursive Call
  return avg_helper(curr_count, itr, curr_sum)


with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  belgiums = count(lambda x: x[1] == 'Belgium', reader)
  print(belgiums)
  csvfile.seek(0)
  avg_portugal = average(map(lambda x: float(x[13]), filter(lambda x: x[1] == 'Portugal', reader)))
  print(avg_portugal)
