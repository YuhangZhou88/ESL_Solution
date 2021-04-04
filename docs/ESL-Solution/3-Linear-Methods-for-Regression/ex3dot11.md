---
title: Ex. 3.11
linktitle: Ex 3.11
type: book
date: "2021-01-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 11
toc: false
---

> Show that the solution to the multivariate linear regression problem (3.40) is given by (3.39). What happens if the covariance matrices $\boldsymbol{\Sigma}_i$ are different for each observation?

## Solution 3.11
Like (3.38), we write (3.40) in matrix form

\begin{equation}
    \text{RSS}(\textbf{B};\boldsymbol{\Sigma}) = \text{tr}[(\textbf{Y}-\textbf{X}\textbf{B})^T\boldsymbol{\Sigma}^{-1}(\textbf{Y}-\textbf{X}\textbf{B})].\nonumber
\end{equation}

By properties of trace operator, we have

\begin{eqnarray}
    &&\text{RSS}(\textbf{B};\boldsymbol{\Sigma})\nonumber\\
     &=& \text{tr}[(\textbf{Y}^T\boldsymbol{\Sigma}^{-1}-\textbf{B}^T\textbf{X}^T\boldsymbol{\Sigma}^{-1})(\textbf{Y}-\textbf{X}\textbf{B})]\nonumber\\
    &=&\text{tr}(\textbf{Y}^T\boldsymbol{\Sigma}^{-1}\textbf{Y}-\textbf{Y}^T\boldsymbol{\Sigma}^{-1}\textbf{X}\textbf{B} - \textbf{B}^T\textbf{X}^T\boldsymbol{\Sigma}^{-1}\textbf{Y} + \textbf{B}^T\textbf{X}^T\boldsymbol{\Sigma}^{-1}\textbf{X}\textbf{B}).\nonumber
\end{eqnarray}

Taking derivative and setting it to be zero, we get

\begin{eqnarray}
    &&\frac{\partial \text{RSS}(\textbf{B};\boldsymbol{\Sigma})}{\partial \textbf{B}}\nonumber\\
     &=& \textbf{X}^T(\boldsymbol{\Sigma}^{-1}+(\boldsymbol{\Sigma}^{-1})^{T})\textbf{X}\textbf{B} - \textbf{X}^T(\boldsymbol{\Sigma}^{-1}+(\boldsymbol{\Sigma}^{-1})^{T})\textbf{Y}\nonumber\\
    &=&\textbf{0}. \label{eq:3-11a} 
\end{eqnarray}

Note that $\boldsymbol{\Sigma}$ is a positive definite symmetric matrix, there exists $\textbf{S}$ such that $\boldsymbol{\Sigma}^{-1}=\textbf{S}\textbf{S}^T$. Therefore we obtain

\begin{eqnarray}
    \hat{\textbf{B}} &=& (\textbf{X}^T\textbf{S}\textbf{S}^T\textbf{X})^{-1}\textbf{X}^T\textbf{S}\textbf{S}^T\textbf{Y}\nonumber\\
    &=&(\textbf{X}^T\textbf{S}\textbf{S}^T\textbf{X})^{-1}\textbf{X}^T\textbf{S}\textbf{S}^T\textbf{X}\textbf{X}^T(\textbf{X}\textbf{X}^T)^{-1}\textbf{Y}\nonumber\\
    &=&\textbf{X}^T(\textbf{X}\textbf{X}^T)^{-1}\textbf{Y}\nonumber\\
    &=&(\textbf{X}^T\textbf{X})^{-1}\textbf{X}^T\textbf{X}\textbf{X}^T(\textbf{X}\textbf{X}^T)^{-1}\textbf{Y}\nonumber\\
    &=&(\textbf{X}^T\textbf{X})^{-1}\textbf{X}^T\textbf{Y},\nonumber
\end{eqnarray}

which is (3.39) in the text.

When $\boldsymbol{\Sigma}_i$ are different, the simple solution for $\textbf{B}$ above does not hold. Instead, we have to deal with equations like $\eqref{eq:3-11a}$ with different $\boldsymbol{\Sigma}_i$. Numerical solutions are available though, as the problem is essentially in quadratic form of $\textbf{B}$.