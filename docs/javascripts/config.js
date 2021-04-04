window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true,
      tags: 'ams',
      macros: {
        bb: ["{\\textbf #1}", 1],
        bX: "\\textbf{X}",
        bx: "\\textbf{x}",
        bY: "\\textbf{Y}",
        by: "\\textbf{y}",
        non: "\\nonumber",
        ra: "\\rightarrow"
      }
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };