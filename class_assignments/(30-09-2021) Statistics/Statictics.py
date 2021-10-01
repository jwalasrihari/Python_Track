import numpy as np

class stat:
    sum=0
    def dsmean(self, data, frequency):
            res_list=[]
            data=np.array(data,dtype=int)
            frequency=np.array(frequency,dtype=int)
            if isinstance(data,np.ndarray)==True and isinstance(data[-1], np.int32):
                if(len(data))==len(frequency):
                    for i in range(0, len(data)):
                        res_list.append(data[i] * frequency[i])
                        print(res_list)
                    return (sum(res_list)/sum(frequency))
                else:
                    return("Error 1")
            else:
                return("error 2")
# median of the dataset
    def median(self, data):
        data.sort()
        #even number data
        if(len(data)%2 ==0):
            self.number = (len(data)+1)/2
            return (data[int(self.number)-1])
        #odd number dataset
        elif(len(data)%2!=0):
            self.number=(len(data)+1)/2
            return(data[int(self.number-1)])
        else:
            return("error")

# mode method in statistics(can be implemented on non numerical enities also)
    def mode(self, data):
        count = 0
        num = data[0]
        for i in data:
            mode = data.count(i)
            if(mode > count):
                count = mode
                num = i
        return (num)
    def geometric_mean(self,data):
        prod=1
        for i in data:
            prod*=i
        return prod**(1/len(data))

    def harmonic_mean(self,data):
        temp=0
        for i in data:
            temp+=(1/i)
        return len(data)/temp

s=stat()
data=[4, 10, 16, 24]
#freq=[4,3,2,1]
print(s.geometric_mean(data))

print(s.harmonic_mean(data))