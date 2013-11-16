=================================================================
Python, Open-Source, and Numerical Solutions of Conservation Laws
=================================================================

:venue: ISGC 2014
:author: Yung-Yu Chen, Po-Hsien, and S.-T. John Yu

Abstract
========

The development of SOLVCON, a Python-based, open-source solver framework for
conservation laws, is discussed in this paper.  By utilizing a novel numerical
method, the space-time Conservation Element and Solution Element (CESE) method,
SOLVCON hosts various solvers of different physical systems for engineering
applications.  The CESE method is a general numerical method for non-linear or
linear systems that are governed by first-order, hyperbolic Partial
Differential Equations (PDEs).  To alter the physical model, SOLVCON requires
only different Jacobian matrices and boundary conditions, and the governing
equations to be simulated are changed.  SOLVCON is developed as a research
code, and currently contains a supersonic flow solver, a velocity-stress
equations solver for stress waves in solids, and a hydro acoustics solver.
Several other solvers.  The solvers are three-dimensional.  SOLVCON also helps
the solvers to be parallelized with both shared-memory and distributed-memory
techniques.  Preliminary work showed the current code can modestly scale to use
1,000 computing cores.

SOLVCON wants to provide a consistent and self-containing platform for
simulations of conservation laws.  The three pillars of continuum-based
numerical simulations by PDEs are physical models, numerical methods, and
software development.  Traditional academic publication systems can only help
discussions of the first two areas, but don’t cover the last.  This is partly
because in the past, research code and simulation results weren’t too difficult
to be reproduced.  However, in addition to complex physical models and
numerical methods, modern numerical simulations face sophisticated hardware and
software infrastructure, performance requirements that can only be met with
parallel computing, and capable result analysis demanded by applications.  The
simulation software needs to be well engineered to produce and reproduce
accountable results.  To address this challenge, SOLVCON organizes the
development of physical models, numerical methods, and software together, and
makes itself fully open-source.  The whole package, including the physical and
numerical contents, is documented by using Sphinx.  The software is organized
by Python modules, and the computing kernel is high-performance C code.  Source
code and the integrated documentation are managed by using Mercurial.
Bitbucket is used for collaboration and review.  Unit tests and functional
tests are organized and configured to be executed with every change of the
package on a test server farm.  Python is a key for SOLVCON to utilize these
modern techniques in a productive way.

To exhibit how to use SOLVCON for computational research, a recent project
about hydro acoustics is used as an example.  Further refinement of the work
flow will be discussed.
