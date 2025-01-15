import numpy as np
import math
import scipy


n=100 #nr total de oameni
initial_cases=3
infection_prob=0.23
healing_prob=0.10
days=10
#infection_chance[i]=sansa unui sanatos sa devina bolnav daca avem i infectati
infection_chance=np.zeros((n+1),dtype=float)
infection_chance[0]=0
for i in range(1,n+1):
        infection_chance[i]=1-(1-infection_prob)**i
#print(infection_chance)
inf=np.zeros((n+1,n+1),dtype=float)
#inf[i][j] probabilitatea ca de la i infectati sa ajungem la j infectati dupa dimineata
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<i:
            inf[i,j]=0
        else:
            inf[i,j]=scipy.special.comb(n-i, j-i)*(infection_chance[i]**(j-i))*((1-infection_chance[i])**(n-j))
heal=np.zeros((n+1,n+1),dtype=float)
#heal[i][j] probabilitatea ca de la i infectati sa ajungem la i infectati dupa seara
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<j:
            heal[i,j]=0
        else:
            heal[i,j]=scipy.special.comb(i, i-j)*(healing_prob**(i-j))*((1-healing_prob)**j)
#dp[i][j] probabilitatea ca de la i infectati sa ajungem la j infectati dupa o zi
dp=np.matmul(inf,heal)

#final[i][j] va fi egal cu probabilitatea ca de la i infectati sa ajungem la j infectati dupa d zile
final=np.identity(n+1,dtype=float)
for i in range(1,days+1):
    final=np.matmul(final,dp)

ans=0.0
for i in range(0,n+1):
    ans+=i*final[initial_cases][i]
print(ans)# returneaza expected value-ul

expected_value=ans
expected_value_of_square=0.0

for i in range(0,n+1):
    expected_value_of_square+=i*i*final[initial_cases][i]

variation=expected_value_of_square-(expected_value*expected_value)


accuracy_percentage=95

epsilon=0.25

sim_number=((variation/(epsilon*epsilon))/(1-accuracy_percentage/100))+1
sim_number=int(sim_number)

print(sim_number)

            
