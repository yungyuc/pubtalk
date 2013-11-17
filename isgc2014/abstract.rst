=================================================================
Python, Open-Source, and Numerical Solutions of Conservation Laws
=================================================================

:Venue: ISGC 2014
:author: Yung-Yu Chen, Po-Hsien Lin, and S.-T. John Yu

Abstract
========

This paper demonstrates a modern work flow for numerical simulations, by using
an open-source solver framework for conservation laws.  The software, SOLVCON,
utilizes a novel numerical method, the space-time Conservation Element and
Solution Element (CESE) method, to host various solvers of different physical
systems for engineering applications.  The CESE method is a general numerical
method for non-linear or linear systems that are governed by first-order,
hyperbolic Partial Differential Equations (PDEs).  We need only different
Jacobian matrices and boundary conditions to change the governing equations.
SOLVCON is developed as a research code, and currently contains (i) a
supersonic flow solver, (ii) a velocity-stress equations solver for stress
waves in solids, and (iii) a hydro acoustics solver.  The framework also helps
the two-/three-dimensional solvers to simultaneously use shared-memory and
distributed-memory parallel computing.  Preliminary work showed that it can
modestly scale to use 1,000 computing cores.

By making the software, we want to provide a consistent and self-containing
platform for numerical simulations of conservation laws.  The three pillars of
continuum-based numerical simulations by PDEs are physical models, numerical
methods, and software development.  Traditional academic publication systems
only facilitate discussions about the first two.  However, modern simulation
codes are complex and need professional review to ensure the correctness.  The
simulations face sophisticated hardware and software infrastructure,
performance requirements that can only be met with parallel computing, and
capable result analysis demanded by applications.  The software itself should
be available in a form that can be executed to produce and reproduce the
simulation results with reasonable efforts, and thus enable meaningful review.
To respond to the need, we made SOLVCON open-source and tried to explore a new
work flow for the research activities.  We organized the development of
physical models, numerical methods, and software altogether.  The whole
package, including the physical and numerical contents, is documented by using
Sphinx.  The software is structured by Python modules, and uses C in computing
kernels for high performance.  Source code and the integrated documentation are
managed by using Mercurial.  Bitbucket is used for collaboration and review.
Unit tests and functional tests are developed and configured to be executed
with every change of the package on a test server farm.  Python is a key to the
utilization of these modern techniques in a productive way.

To exhibit how research is done with the new work flow, a recent project about
hydro acoustics is used as an example.  Further refinement of the work flow
will be discussed.
