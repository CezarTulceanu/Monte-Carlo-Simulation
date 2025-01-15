import numpy as np
def simulate_infections(n, initial_cases, infection_prob, healing_prob, days):
    # 1 e bolnav, 0 e curat
    status=np.zeros(n, dtype=int)
    for i in range(initial_cases):
        status[i]=1
    count_cases=initial_cases
    for day in range(days):
        for i in range(n):
            for j in range(n):
                if(status[i]==1 and status[j]==0):
                   apollo=np.random.random()
                   if(apollo<infection_prob):
                       status[j]=1
                       count_cases+=1
        for i in range(n):
            health_status=np.random.random()
            if(health_status<healing_prob and status[i]==1):
               status[i]=0
               count_cases-=1
    return count_cases
tests=300 #sau cate zice CLT ca trebuie puse ca sa convearga
sum=0
for i in range(tests):
    sum+=simulate_infections(100, 30, 0.6, 0.2, 11)
print(sum/tests)
