---
title: Ex. 3.13
linktitle: Ex 3.13
type: book
date: "2021-01-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 12
toc: false
---

> Derive the expression (3.62), and show that $\hat\beta^{\text{pcr}}(p) = \hat\beta^{\text{ls}}$.

## Solution 3.13

Since $\bb{z}_m=\bb{X}v_m$, from (3.61) in the text we have

\begin{eqnarray}
    \hat{\by}^{\text{pcr}}_{(M)} &=& \bar y\bb{1} + \bX\sum_{m=1}^M\hat\theta_mv_m\nonumber\\
    &=&\begin{pmatrix}
        \bb{1} & \bX
    \end{pmatrix}
    \begin{pmatrix}
        \bar y\\
        \sum_{m=1}^M\hat\theta_mv_m
    \end{pmatrix}.\nonumber
\end{eqnarray}

Therefore, we can represent 

\begin{equation}
    \hat\beta^{\text{pcr}}(M) = \sum_{m=1}^M\hat\theta_mv_m,\nonumber
\end{equation}

which is (3.62) in the text.

Recall the SVD decomposition of $\bX=\bb{U}\bb{D}\bb{V}^T$. Here $\bb{U}$ and $\bb{V}$ are $N\times p$ and $p\times p$ orthogonal matrices, and $\bb{D}$ is a $p\times p$ diagonal matrix. We have $\bX\bb{V} = \bb{U}\bb{D}$ since $\bb{V}$ is orthogonal, so that

\begin{equation}
    \bb{z}_m = \bX v_m = d_mu_m,\nonumber
\end{equation}

where $d_m\in\mathbb{R}$ is the $m$-th diagonal element in $\bb{D}$ and $u_m$ is $m$-th column in $\bb{U}$.  By definition of $\hat\theta_m=\langle \bb{z}_m, \by\rangle/\langle \bb{z}_m, \bb{z}_m \rangle$, we have $\hat\theta_m = \langle u_m, \by\rangle/d_m$ so that

\begin{equation}
    \hat\beta^{\text{pcr}}(p) = \sum_{m=1}^M\hat\theta_mv_m =\bb{V}\begin{pmatrix}
        \hat\theta_1\\\hat\theta_2\\\vdots\\\hat\theta_p
    \end{pmatrix} = \bb{V}\bb{D}^{-1}\bb{U}^T\by.\nonumber
\end{equation}

On the other hand, recall $\bX=\bb{U}\bb{D}\bb{V}^T$, by simple algebra we have

\begin{eqnarray}
    \hat\beta^{ls} &=&(\bX^T\bX)^{-1}\bX^T\by\nonumber\\
    %&=&(\bb{V}\bb{D}^2\bb{V}^T)^{-1}\bb{U}\bb{D}\bb{V}^T\by\nonumber\\
    &=&\bb{V}\bb{D}^{-1}\bb{U}^T\by.\nonumber
\end{eqnarray}

Therefore we have

\begin{equation}
    \hat\beta^{\text{pcr}}(p)=\hat\beta^{ls}.\nonumber
\end{equation}
