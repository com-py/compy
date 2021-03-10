<img src="https://jwang.sites.umassd.edu/files/2021/03/cover1.jpg" width="300px" align="left" border="0" alt="book cover">

# Computational modeling and visualization with Python
# GitHub project page. J Wang
#
## The latest source programs, library and data files for the book are deposited here and at http://www.faculty.umassd.edu/j.wang/
- ## Sep. 2017: Jupyter vpython notebooks (.ipynb) are added next to the standard programs (.py), in addition to the archive containing all  notebooks (Jupyter_vpython/VPython_Programs_ipynb.zip)
- ## Sep. 2017: Updated input() function compatibility between Python 2.xx and 3.xx to affected programs (Original versions can be found in `v1.0` folder). To summarize, all codes (.py and .ipynb) should run under Python 2.7x and 3.xx as follows: 
  - ### .py codes not using VPython: will run in Jupyter (via `load prog_name`) and in a terminal
  - ### .py codes using classic VPython (`visual` installed): will run in Jupyter and in a terminal
  - ### .ipynb codes using Jupyter vpython: will run in Jupyter only 
- ## March 2018: Complete update of all .py programs to Jupyter notebook versions.
  - ### This includes all non-VPython programs and revisons to some Jupyter VPython program, so all programs can be run in dual mode: standard mode (`python program.py`) or in Jupyter notebook.
  - ### Programs using `matplotlib` now utilize the `notebook` backend, enabling users to interactively manipulate plots such as zoom and save in nearly the same way as the standard .py versions run from a terminal. In addition, programs using `matplotlib` animation (Programs 8.1, 10.2, and 11.4) work correctly in Jupyter notebook.
- ## Sep. 2018: Updated Program_12.2_qmscatt.py and Program_12.2_qmscatt.ipynb.
  - ### This update fixes the compatibility in spherical Bessel functions between `SciPy` versions 0.x.x and 1.x.x. In version 1.x.x, the name is changed from `sph_jn/yn` to `spherical_jn/yn`, its signature is also different. With this fix, the program automatically detects the `SciPy` version and should work under either version.
- ## March 2021: VPython advisory.
  - ### .py codes using classic VPython (`visual`) will generally not run in either Jupyter or in a terminal because of changes in latest vpython versions. While one could slightly modify the .py programs to run from a terminal, the easiest way is to run the corresponding .ipynb programs instead. If you have  to run from a terminal, refer to  the .ipynb counterpart on necessary modifications (mostly related to vectors and canvas) to make it work.
- ## Computational modeling forum:  https://groups.google.com/forum/#!forum/comphys  
