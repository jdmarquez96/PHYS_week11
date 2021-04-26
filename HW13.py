import numpy as np
import matplotlib.pyplot as plt


l = 25  #lambda for poisson
sig = 5 #sigma for gaussian
mean = 25   #mean for gaussian
size = 1000000   #size of the array
size2 = 1000

x = np.linspace(0, 25, size)


#randomly generated gaussian and poisson equations
H1 = np.random.normal(mean, sig, size)
H0 = np.random.poisson(l, size)


H02 = np.random.poisson(l, size2)
H12 = np.random.normal(mean, sig, size2)

H03 = np.random.poisson(l, 100)
H13 = np.random.normal(mean, sig, 100)


#plotting histogram over each other
plt.figure()
plt.hist(H03, 50, density=True,label="Poisson, $\lambda$ = 25",alpha=0.5, color="blue")
plt.hist(H13, 50, density=True, label="gaussian, $\sigma$ = 5 mean=25",color="orange",alpha = 0.5)
plt.legend()
plt.title("Gaussian vs Poisson Function with 100 Data Points")
plt.xlabel("Data Points")
plt.ylabel("Probability")
plt.grid(True)
plt.savefig("gaussvspoisson100points.png")

plt.show()

plt.figure()
plt.hist(H02, 50, density=True,label="Poisson, $\lambda$ = 25",alpha=0.5, color="blue")
plt.hist(H12, 50, density=True, label="gaussian, $\sigma$ = 5 mean=25",color="orange",alpha = 0.5)
plt.legend()
plt.title("Gaussian vs Poisson Function with 1000 Data Points")
plt.xlabel("Data Points")
plt.ylabel("Probability")
plt.grid(True)
plt.savefig("gaussvspoisson1000points.png")

plt.show()


plt.figure()
plt.hist(H0, 50, density=True,label="Poisson, $\lambda$ = 25",alpha=0.5, color="blue")
plt.hist(H1, 50, density=True, label="gaussian, $\sigma$ = 5 mean=25",color="orange",alpha = 0.5)
plt.legend()
plt.title("Gaussian vs Poisson Function with 1000 Data Points")
plt.xlabel("Data Points")
plt.ylabel("Probability")
plt.grid(True)
plt.savefig("gaussvspoisson1000000points.png")

plt.show()


