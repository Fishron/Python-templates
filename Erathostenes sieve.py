        notprimes=set() #eratosthenes sieve
        for i in range(2,21):
            if i not in notprimes:
                j=i
                while j<400:
                    j+=i
                    notprimes.add(j)
        primes={*range(2,400)}-notprimes
        primes=sorted(primes)
