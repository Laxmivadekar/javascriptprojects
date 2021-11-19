n = int(raw_input())
arr = map(int, raw_input().split())
def func(list):
nums = sorted(list, reverse=True)
for x in nums[1:]:
if x == nums[0]:
continue
else:
print x
break
func(arr) 