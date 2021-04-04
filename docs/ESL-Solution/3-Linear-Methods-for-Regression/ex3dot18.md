---
title: Ex. 3.18
linktitle: Ex 3.18
type: book
date: "2021-01-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 12
toc: false
---

> Read about conjugate gradient algorithms (Murray et al., 1981, for example)\cite{gill2019practical}, and establish a connection between these algorithms and partial least squares.

We briefly review the conjugate gradient algorithm described in Murray et al., 1981. The conjugate-gradient method described in Section 4.8.3.1 in \cite{gill2019practical} can be applied to minimize the quadratic function $c^T + \frac{1}{2}x^TGx$, where $G$ is symmetric and positive definite, it computes the solution of the system

\begin{equation}
    Gx = -c.\non
\end{equation}

When describing the linear conjugate-gradient method, it's customary to use the notation $r_j$ (for residual) for the gradient vector $c+Gx_j$. To initiate the iterations, we adopt the convention that $\beta_{-1}=0, p_{-1}=0$. Given $x_0$ and $r_0=c+ Gx_0$, each iteration includes the following steps for $k=0,1,...$:

\begin{eqnarray}
    p_k &=&-r_k + \beta_{k-1}p_{k-1}\non\\
    \alpha_k &=& \frac{\|r_k\|_2^2}{p_k^TGp_k}\non\\
    x_{k+1} &=& x_k + \alpha_kp_k\non\\
    r_{k+1} &=& r_k + \alpha_kGp_k\non\\
    \beta_k &=& \frac{\|r_{k+1}\|_2^2}{\|r_k\|_2^2}\non 
\end{eqnarray}

In theory, the algorithm will compute the exact solution within a fixed number of iterations. In particular, the method has the property that, if exact arithmetic is used, convergence will occur in $m\le n$ iterations, where $m$ is the number of distinct eigenvalues of $G$.

The connection between this algorithm (iteratively getting $\hat\beta^{m}$) and PLS (iteratively getting $\hat \by^m$) is $\hat \by^m = \bX\hat\beta^m$. 
