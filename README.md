# Quantitative-Finance
Collection of Mathematical financial models with performance ratio


# Heath-Jarrow-Morton (HJM)

Few Key takeaways
* The Heath-Jarrow-Morton Model (HJM Model) use a differential equation that incorporates randomness to model forward interest rates.
* These rates are then modeled against an existing interest rate term structure to determine appropriate prices for interest-rate sensitive securities such as bonds or swaps.
* It is now primarily used by arbitrageurs looking for arbitrage opportunities, as well as analysts pricing derivatives.
* Formula for the HJM Model
* $df(t,T) = \alpha(t,T)dt + \sigma(t,T)dW(T)$
  * $df(t,T)$ : The stochastic differential equation shown above is assumed to satisfy the instantaneous forward interest rate of a zero-coupon bond with maturity T.
  * $\alpha, \sigma$ : Adapted
  * $W$ : Under the risk-neutral assumption, a Brownian motion (random-walk).
* More details: https://en.wikipedia.org/wiki/Heath%E2%80%93Jarrow%E2%80%93Morton_framework

# Crank–Nicolson method
Few Key Takeaways
* The Crank-Nicolson method is a finite difference method used to solve the heat equation and other partial differential equations numerically. It's a second-order method.
* The Crank-Nicolson method has also been used in those areas. The differential equation of the Black-Scholes option pricing model, in particular, can be transformed into the heat equation, and thus numerical solutions for option pricing can be obtained using the Crank-Nicolson method.
* You can find a seprate github repo for Black-Scholes pricing model (https://github.com/white07S/Black-Scholes)
* By using Crank-Nicolson method we compare the American and European option pricing with spreadhttps://github.com/white07S/Black-Scholes
* More details: https://en.wikipedia.org/wiki/Crank%E2%80%93Nicolson_method
