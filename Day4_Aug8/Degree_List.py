from collections import Counter

def  Degree_List(nums):
     num_dict = Counter(nums)
     max_num = max(list(num_dict.values()))
     start_end = dict()

     for index, x in enumerate(nums):
            if x not in start_end:
              start_end[x] = [index, index]
            else:
              start_index = start_end[x][0]
              start_end[x] = [start_index, index]
                
     degree = len(nums)
        
     for num, occ in num_dict.items():
            if occ == max_num:
                
              end_index = start_end[num][1]
              start_index = start_end[num][0]                
              degree = min(degree, end_index - start_index + 1)
                
     return degree

print(Degree_List([1, 2, 2, 3, 1]))