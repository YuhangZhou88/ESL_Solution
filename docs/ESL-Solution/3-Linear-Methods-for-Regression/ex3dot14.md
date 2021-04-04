---
title: Ex. 3.14
linktitle: Ex 3.14
type: book
date: "2021-01-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 12
toc: false
---

> Show that in the orthogonal case, PLS stops after $m=1$ steps, because subsequent $\hat\varphi_{mj}$ in Step 2 in Algorithm 3.3 are zero.

## Solution 3.14

Observe that in Algorithm 3.3 on partial least squares (PLS) if $\hat\varphi_{mj}=0$ for all $j$ on any given step $m$ then the algorithm will stop.

We start with $m=1$. We have

(a) 

\begin{equation}
    \bb{z}_1 = \sum_{j=1}^p\hat\varphi_{1j}\bx^{(0)}_j \text{ with } \hat\varphi_{1j} = \langle \bx^{(0)}_j, \by \rangle. \non
\end{equation}

(b) For $\hat\theta_1$, we have

\begin{eqnarray}
    \hat\theta_1 = \langle \bb{z}_1, \by \rangle/\langle \bb{z}_1, \bb{z}_1 \rangle\non 
\end{eqnarray}
    
where

\begin{eqnarray}
    \langle \bb{z}_1, \bb{z}_1 \rangle &=& \left\langle \sum_{j=1}^p\hat\varphi_{1j}\bx^{(0)}_j, \sum_{j=1}^p\hat\varphi_{1j}\bx_{j}^{(0)}\right\rangle\non\\
    &=& \sum_{i=1}^p\sum_{j=1}^p\hat\varphi_{1i}\hat\varphi_{1j}\langle \bx^{(0)}_j, \bx^{(0)}_{j'} \rangle\non\\
    &=& \sum_{i=1}^p\sum_{j=1}^p\hat\varphi_{1i}\hat\varphi_{1j}\delta_{ij}\non\\
    &=&\sum_{i=1}^p\hat\varphi_{1i}^2\non
\end{eqnarray}

since $\bx_i^{(0)}$ are orthogonal. On the other hand, we have
    
\begin{equation}
    \langle \bb{z}_1, \by \rangle = \sum_{i=1}^p \hat\varphi_{1i}\langle \bx^{(0)}_j, \by\rangle = \sum_{i=1}^p \hat\varphi_{1i}^2\non
\end{equation}
    
so we have $\hat\theta_1 =1$.

(c) We have
    
\begin{equation}
    \hat\by^{(1)} = \hat\by^{(0)} + \bb{z}_1 = \hat\by^{(0)} + \sum_{i=1}^p\hat\varphi_{1i}\bx_{i}^{(0)}.\non
\end{equation}
    
(d) For each $j=1,...,p$,

\begin{eqnarray}
    \bx_j^{(1)} &=& \bx_j^{(0)} - \frac{\langle \bb{z}_1, \bx_{j}^{(0)} \rangle}{\langle \bb{z}_1, \bb{z}_1 \rangle}\cdot \bb{z}_1\non\\
    &=&\bx_j^{(0)} - \frac{\hat\varphi_{1j}}{\sum_{i=1}^p\varphi_{1i}^2}\bb{z}_1\non\\
    &=&\bx_j^{(0)} - \left(\frac{\hat\varphi_{1j}}{\sum_{i=1}^p\hat\varphi_{1i}^2}\right)\sum_{i=1}^p\hat\varphi_{1i}\bx^{(0)}_i.\non
\end{eqnarray}	
    

Now we move to $m=2$.

It's easy to see that for any $j=1,...,p$ we have

\begin{eqnarray}
    \hat\varphi_{2j} &=& \langle \bx^{(1)}_j, \by \rangle \non\\
    &=&\langle \bx_j^{(0)}, \by \rangle - \left(\frac{\hat\varphi_{1j}}{\sum_{i=1}^p\hat\varphi_{1i}^2}\right)\sum_{i=1}^p\hat\varphi^2_{1i}\non\\
    &=&\hat\varphi_{1j} - \hat\varphi_{1j}=0.\non
\end{eqnarray}

Therefore we see the algorithm stops in Step 2.
