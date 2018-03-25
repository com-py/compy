# J Wang, Computational modeling and visualization with Python
These are common library files. They should be extracted or saved to
the Python path (e.g., C:\Python27) so they can be called from anywhere.

On Anaconda, library files may be placed in 
`"C:\Users\yourname\Anaconda3\lib"` on Windows 10 for example.
But it is tidier to put them in one folder in site-packages as
`"C:\Users\yourname\Anaconda3\lib\site-packages\compy"`. 
To do so, create a file `compy.pth` containing the folder path in quotes 
and place it and lib files in paths as folows:
<table border="0">
<tr>
   <td> C:\Users\yourname\Anaconda3\lib\site-packages\compy.pth </td>
</tr> 
<tr>
   <td> C:\Users\yourname\Anaconda3\lib\site-packages\compy\ode.py</td>
</tr> 
<tr>
   <td align="right"> . . . \xyz.py </td>
</tr> 
</table>
