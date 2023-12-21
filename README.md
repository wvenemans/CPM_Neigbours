# Neighbours Law in the Cellular Potts Model

This repository contains the code used to generate the results in the paper "Neighbours Law in the Cellular Potts Model", written by Willem Venemans and Nina Henninger.

## Requirements
- The Tissue Simulator Toolkit, developed by J.T. Daub and M.H. Merks, available at [sourceforge](https://sourceforge.net/projects/tst/).
- Up-to-date versions of the following python packages: numpy, matplotlib.

## Usage
The TST code is written using c++. To compile the code, follow the procedure to install the TST as usual (manual avalaible [here](https://sourceforge.net/projects/tst/files/)) and then copy the files in the 'TST' folder to the 'src' folder of the TST. Then, compile the code using the command `make` in the 'src' folder. Lastly, run the code using the command `./sorting sorting.par' in the 'src' folder with a .par file of your choice. The results will be saved in a text file called 'NeighboursLaw.txt'.

The python code is used to generate the figures in the paper. The code is written in python 3. To generate the figures, run the code using the command `python3 NeighboursLaw.py` in the 'NeighboursLaw' folder. You can add the path to the generated 'NeighboursLaw.txt' file as an argument to the command to use the file. The figures will be saved in the 'Figures' folder.

## License
This code is licensed under the GNU General Public License v3.0. See the LICENSE file for details.