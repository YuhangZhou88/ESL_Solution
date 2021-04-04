---
title: Ex. 3.15
linktitle: Ex 3.15
type: book
date: "2021-01-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 12
toc: false
---

> Verify expression (3.64), and hence show that the partial least squares directions are a compromise between the ordinary regression coefficient and the principal component directions.

## Solution 3.15

Note that

\begin{equation}
    \text{Corr}^2(\by, \bX\alpha)\text{Var}(\bX\alpha) =\frac{\text{Cov}^2(\by, \bX\alpha)}{\text{Var}(\by)\text{Var}(\bX\alpha)}\text{Var}(\bX\alpha) = \frac{\text{Cov}^2(\by, \bX\alpha)}{\text{Var}(\by)}\non
\end{equation}

We are essentially solving 

\begin{eqnarray}
    \max_\alpha &&(\by^T\bX\alpha)^2\non\\
    \text{s.t.} &&\|\alpha\|=1\non\\
                && \alpha^T\bb{S}\hat\varphi_l = 0, \  l=1,...,m-1,\non
\end{eqnarray}

where $\bb{S}=\bX^T\bX$ is the sample covariance matrix of the $\bx_j$.

We start with the case $m=1$, which immediately gives what we call the first *canonical covariance* variable (see [Ex. 3.20]) with

\begin{equation}
    \hat\alpha_1 = \bX^T\by/\|\bX^T\by\|_2.\non
\end{equation}

Note that $\hat\alpha_1 \propto \hat\varphi_1$ in Algorithm 3.3 in the text. 

The second canonical covariance variable, $\hat\alpha_2$, then has to maximize the same objective with additional constraint $\hat\alpha_2^T\bb{S}\hat\alpha_1=0$. It turns out 

\begin{equation}
\label{eq:3-15a}
    \hat\alpha_2 \propto \bX^T\by - \left(\frac{\by^T\bX \bb{S} \bX^T\by}{\by^T\bX \bb{S}^2 \bX^T\by}\right)\bb{S}\bX^T\by.
\end{equation}

To see that, we first verify that

\begin{eqnarray}
    \hat\alpha_2^T \bb{S}\hat\alpha_1 &\propto&  \by^T\bX\bb{S}\bX^T\by - \left(\frac{\by^T\bX \bb{S} \bX^T\by}{\by^T\bX \bb{S}^2 \bX^T\by}\right)\by^T\bX\bb{S}^T\bb{S}\bX^T\by\non\\
    &=&0.\non
\end{eqnarray}

Second, for $\alpha_2$ satisfying $\alpha_2^T \bb{S}\hat\alpha_1=0$, that is, $\alpha_2^T \bb{S}\bX^T\by=0$, we have the objective to maximize 

\begin{equation}
    \alpha_2^T\bX^T\by = \alpha_2^T\left(\bX^T\by - \left(\frac{\by^T\bX \bb{S} \bX^T\by}{\by^T\bX \bb{S}^2 \bX^T\by}\right)\bb{S}\bX^T\by\right).\non
\end{equation}

Therefore we see $\eqref{eq:3-15a}$ holds. Note that $\hat\alpha_2\propto \hat\varphi_2$ in the Algorithm 3.3 in the text. Continuing this, we are able to derive $\hat\varphi_m$ for $m\ge 1$. 

Now we are ready to show that partial least squares (PLS) directions are a compromise between the ordinary regression coefficient (OLS) and the principal component directions (PCR). The regressors for OLS, PCR and PLS may be referred to as *canonical correlation*, *canonical variance* and *canonical covariance* variables respectively. A generalized criterion that encompasses all three methods is

\begin{eqnarray}
    \max_\alpha &&(\by^T\bX\alpha)^2\left(\alpha^T\bX^T\bX\alpha\right)^{\frac{r}{1-r}-1}\non\\
    \text{s.t.} &&\|\alpha\|=1\non\\
                && \alpha^T\bb{S}\hat\alpha_l = 0, \  l=1,...,m-1,\non
\end{eqnarray}

where $r\in [0, 1).$ When $r =0$ we recover OLS, and when $r \ra 1$ we get PCR. The case when $r=1/2$ gives PLS. Note that this generalized regression is referred to as **continuum regression**. See \cite{stone1990continuum} for details.

