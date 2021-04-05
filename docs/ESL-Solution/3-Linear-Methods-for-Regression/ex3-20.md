---
title: Ex. 3.20
linktitle: Ex 3.20
type: book
date: "2021-01-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 12
toc: false
---

> 	Consider the canonical-correlation problem (3.67). Show that the leading pair of canonical variates $u_1$ and $v_1$ solve the problem
>
>\begin{equation}
>    \max_{\substack{u^T(\bb{Y}^T\bb{Y})u=1\\ v^T(\bb{X}^T\bb{X})v=1}} u^T(\bb{Y}^T\bb{X})v,\non
>\end{equation}
>
> a generalized SVD problem. Show that the solution is given by $u_1=(\bb{Y}^T\bb{Y})^{-\frac{1}{2}}u_1^\ast$, and $v_1=(\bb{X}^T\bb{X})^{-\frac{1}{2}}v_1^\ast$, where $u_1^\ast$ and $v_1^\ast$ are the leading left and right singular vectors in 
> 
>\begin{equation}
>\label{eq:3-20a}
>    (\bb{Y}^T\bb{Y})^{-\frac{1}{2}}(\bb{Y}^T\bb{X})(\bb{X}^T\bb{X})^{-\frac{1}{2}}=\bb{U}^\ast\bb{D}^\ast\bb{V}^{\ast T}.
>\end{equation}
>
>Show that the entire sequence $u_m, v_m, m=1,...,\min(K,p)$ is also given by (3.87) ($\eqref{eq:3-20a}$ above).

First, the correlation (3.67) in the text, for each $m$, is given by

\begin{eqnarray}
    \text{Corr}(\bY u_m, \bX v_m) &=& \frac{\text{Cov}(\bY u_m, \bX v_m)}{\sqrt{\text{Var}(\bY u_m)\text{Var}(\bX v_m)}}\non\\
    &=&\frac{u_m^T(\bY^T \bX)v_m}{\sqrt{\text{Var}(\bY u_m)\text{Var}(\bX v_m)}}.\non 
\end{eqnarray}

Therefore we know $u_1$ and $v_1$ solve the problem

\begin{equation}
    \max_{\substack{u^T(\bb{Y}^T\bb{Y})u=1\\ v^T(\bb{X}^T\bb{X})v=1}} u^T(\bb{Y}^T\bb{X})v.\non
\end{equation}

To find its solution, we write out the Lagrangian function 

\begin{equation}
    L(u, v, \lambda_1, \lambda_2) = u^T(\bb{Y}^T\bb{X})v - \frac{\lambda_1}{2}(u^T(\bb{Y}^T\bb{Y})u-1)-\frac{\lambda_2}{2}(v^T(\bb{X}^T\bb{X})v-1).\non
\end{equation}

Taking derivatives and setting them to zero yield

\begin{eqnarray}
    \frac{\partial L(u, v, \lambda_1, \lambda_2)}{\partial u} &=& \bY^T\bX v - \lambda_1 \bY^T\bY u = 0\non\\
    \frac{\partial L(u, v, \lambda_1, \lambda_2)}{\partial v} &=& \bX^T\bY u - \lambda_2 \bX^T\bX v = 0.\label{eq:3-20b}
\end{eqnarray}

Multiplying the first equation by $u^T$ and the second by $v^T$, and noting the constraints (e.g., $u^T(\bb{Y}^T\bb{Y})u=1$), we obtain

\begin{eqnarray}
    u^T\bY^T\bX v &=& \lambda_1\non\\
    v^T\bX^T\bY u &=& \lambda_2.\label{eq:3-20c}
\end{eqnarray}

We see that $\lambda_1 = \lambda_2 = u^T\bY^T\bX v$, and we denote $\lambda := \lambda_1 = \lambda_2$.

Denote $\bb{M} = (\bb{Y}^T\bb{Y})^{-\frac{1}{2}}(\bb{Y}^T\bb{X})(\bb{X}^T\bb{X})^{-\frac{1}{2}}$, we need to find the relation between $\bb{M}$ and the pair $u$ and $v$. Recall the definition of $u_1^\ast$ and $v_1^\ast$, it's easy to verify that $\eqref{eq:3-20b}$ can be rewritten as 

\begin{eqnarray}
    Mv_1^\ast &=& \lambda u_1^\ast,\non\\
    M^Tu_1^\ast &=& \lambda v_1^\ast.\non
\end{eqnarray}

Therefore we know $u_1=(\bb{Y}^T\bb{Y})^{-\frac{1}{2}}u_1^\ast$ and $v_1=(\bb{X}^T\bb{X})^{-\frac{1}{2}}v_1^\ast$ solve the optimization problem.

For the entire sequence $u_m, v_m, m=1,...,\min(K,p)$, we have already solved the case $m=1$. Consider $1 < k \le \min(K, p)$ and assume $u_j, v_j$ for $1\le j < k$ have been solved as above. Then the problem becomes 

\begin{equation}
    \max_{\substack{u^T(\bb{Y}^T\bb{Y})u=1\\ v^T(\bb{X}^T\bb{X})v=1 \\ u^Tu_j = 0\  \forall j < k\\ v^Tv_j = 0\  \forall j < k}} u^T(\bb{Y}^T\bb{X})v.\non
\end{equation}

The Lagrangian becomes

\begin{eqnarray}
    L &=& u^T(\bb{Y}^T\bb{X})v - \frac{\lambda_1}{2}(u^T(\bb{Y}^T\bb{Y})u-1)-\frac{\lambda_2}{2}(v^T(\bb{X}^T\bb{X})v-1)\non\\
    &&-\sum_{j<k}\alpha_ju^Tu_j - \sum_{j<k}\beta_jv^Tv_j.\non
\end{eqnarray}

Similar to $\eqref{eq:3-20b}$, we have

\begin{eqnarray}
    \frac{\partial L}{\partial u} &=& \bY^T\bX v - \lambda_1 \bY^T\bY u -\sum_{j<k}\alpha_ju_j= 0\non\\
    \frac{\partial L}{\partial v} &=& \bX^T\bY u - \lambda_2 \bX^T\bX v -\sum_{j<k}\beta_jv_j= 0.\non
\end{eqnarray}

We multiply the first equation by $u^T$ and the second by $v^T$, and note the constraints here, in addition to $u^T(\bb{Y}^T\bb{Y})u=1$ we have $u^Tu_j=0$ for $j < k$, we obtain the same set of equations as $\eqref{eq:3-20c}$. Then the rest follows the same arguments.
