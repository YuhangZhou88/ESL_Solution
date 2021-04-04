---
title: Ex. 3.19
linktitle: Ex 3.19
type: book
date: "2021-01-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 12
toc: false
---

> Show that $\|\hat\beta^{\text{ridge}}\|$ increases as its tuning parameter $\lambda\ra 0$. Does the same property hold for the lasso and partial least squares estimates? For the latter, consider the *tuning parameter* to be the successive steps in the algorithm.

## Solution 3.19

Recall the SVD decomposition of $\bX=\bb{U}\bb{D}\bb{V}^T$. Here $\bb{U}$ and $\bb{V}$ are $N\times p$ and $p\times p$ orthogonal matrices, and $\bb{D}$ is a $p\times p$ diagonal matrix. So we have

\begin{eqnarray}
    \beta^{\text{ridge}} &=& (\bX^T\bX + \lambda\bI)^{-1}\bX^T\by\non\\
    &=&\left(\bb{V}\bb{D}^2\bb{V}^T + \lambda\bI\right)^{-1}\bb{V}\bb{D}\bb{U}^T\by\non\\
    &=&\left(\bb{V}(\bb{D}^2 + \lambda\bI\right)\bb{V}^T)^{-1}\bb{V}\bb{D}\bb{U}^T\by\non\\
    &=&\bb{V}^T(\bb{D}^2 + \lambda\bI)^{-1}\bb{D}\bb{U}^T\by.\non
\end{eqnarray}

Therefore,

\begin{eqnarray}
    \|\beta^{\text{ridge}}\|_2^2 &=& \by^T\bb{U}\bb{D}(\bb{D}^2+\lambda\bI)^{-1}(\bb{D}^2+\lambda\bI)^{-1}\bb{D}\bb{U}^T\by\non\\
    &=&(\bb{U}^T\by)^T[\bb{D}(\bb{D}^2+\lambda\bI)^{-2}\bb{D}](\bb{U}^T\by)\non\\
    &=&\sum_{j=1}^p\frac{d_j^2(\bb{U}^T\by)_j^2}{(d_j^2 + \lambda)^2}.\non
\end{eqnarray}

where $\bb{D}(\bb{D}^2+\lambda\bI)^{-2}\bb{D}$ represents a diagonal matrix with elements $\frac{d_j^2}{(d_j^2 + \lambda)^2}$. Therefore we see that $\|\hat\beta^{\text{ridge}}\|$ increases as its tuning parameter $\lambda\ra 0$.

For Lasso, there is no explicit solution as Ridge, however, we can start with the orthogonal case, where the formula is given in [Ex. 3.16](ex3dot16.md). It's easy to see that $\|\hat\beta^{\text{lasso}}\|_1$ increases as $\lambda\ra 0$. For the general case, recall the dual form of Lasso defined in (3.51) and (3.52) in the text. It's easy to see that $t$ in (3.51) and $\lambda$ in (3.52) have an inverse relationship, therefore, as $\lambda\ra 0$, $t$ increases and so does the norm of optimal solutions (see Figure 3.11 for an intuitive illustration in $\mathbb{R}^2$).
