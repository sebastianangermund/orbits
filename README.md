# orbits
## Prerequisites
You will need a ffmpeg writer. For Linux:
```bash
apt-get install ffmpeg
```

## play
Edit `playground.py` to generate a simulation.  
In `simulations` there are a few template simulations for inspiration.

## Modules
`model.py` contains the model for initiating a particle array and updating it. Don't touch the code.  
`plot.py` contains an ugly function you import to write a mpeg-plot. Can take a really long time for long simulations.

## Legacy
`matlab/` is legacy.
