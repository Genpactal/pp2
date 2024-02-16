class MyNums:
    def __iter__(self):
        self.a = 12
        return self

    def __next__(self):
        x = self.a
        self.a += 12
        return x
    
mynums = MyNums()
N=int(input())
myiter = iter(mynums)
nums=[]
for i in range(0,N//12):
    nums.append(str(next(myiter)))
print(", ".join(nums))