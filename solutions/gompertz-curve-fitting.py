def gompertz(t, N0, K, r, T):
    return K * np.exp(-T * np.exp(-r * t))

popt, cov = curve_fit(gompertz, t, N, (N.min(), N.max(), 1, 2))
N0, K, r, T = popt
Nhat = gompertz(t, N0, K, r, T)
print('N0={0:.3f}, K={1:.3f}, r={2:.6f}, T={3:.4f}'.format(N0, K, r, T))
print("MSE:", ((N - Nhat)**2).mean())

plt.scatter(t, N)
plt.plot(t, logistic(t, N0, K, r), label='Logistic')
plt.plot(t, Nhat, label='Gompertz')
plt.xlabel('Time')
plt.ylabel('OD')
plt.legend(loc='upper left')
sns.despine();