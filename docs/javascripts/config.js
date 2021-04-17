window.MathJax = {
    loader: {load: ['[tex]/boldsymbol']},
    tex: {
      packages: {'[+]': ['boldsymbol']},
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true,
      tags: 'ams',
      macros: {
        bb: ["{\\textbf #1}", 1],
        bA: "\\textbf{A}",
        bX: "\\textbf{X}",
        bx: "\\textbf{x}",
        bY: "\\textbf{Y}",
        by: "\\textbf{y}",
        non: "\\nonumber",
        ra: "\\rightarrow",
        bI: "\\textbf{I}",
        bB: "\\textbf{B}",
        bW: "\\textbf{W}",
        bR: "\\textbf{R}",
        bV: "\\textbf{V}",
        bU: "\\textbf{U}",
        bD: "\\textbf{D}",
        bM: "\\textbf{M}",
        rl: "\\rangle",
        bm: ["\\boldsymbol #1", 1]
      }
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };