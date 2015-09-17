# PUI2015_cprince
## Setting up the variable and alias

My `.bashrc` file was already pre-populated with some interesting-looking commands, so I added the new commands in a separate section that will be easy to identify and, if necessary, remove at a later date.

The command to add the variable is:

    export PUI2015="/home/cmp/GX5003/PUI2015"

and the alias to simply change to this directory from the bash prompt is:

    alias pui2015="cd $PUI2015"

We could have also set the variable equal to `$HOME/GX5003/PUI2015` or `~/GX5003/PUI2015`, either of which would be portable for other users, but there's not really a need for portability in this case.

The edited file is shown below:
![Screenshot showing my .bashrc file edited as described above](/img/pui2015-bashrc-cmprince.png)

## Printing and setting the directory

Here we test the alias from the prompt and display the results using `pwd` and `pui2015`:
![Screenshot of the command executed at the prompt](/img/pui2015-cd-cmprince.png)

So it works!
