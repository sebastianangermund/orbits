# orbits
## Prerequisites
You will need a ffmpeg writer. For Linux:
```bash
apt-get install ffmpeg
```

## play
`playground.py` is a dashbord where you can play with different initial condition for a "protoplanetary disk", a.k.a. early solarsystem.  
In `chaos.py` you can get a nice effect of chaos. Make a small change to any initial value and the outcome will differ dramatically.

## Modules
`three_bodies.py` contain the model for initiating a particle array and updating it. Don't touch.
`plot.py` contain a function you import to write a mpeg-plot. Can take a really long time for long simulations.

## Legacy
`matlab/` is legacy.
