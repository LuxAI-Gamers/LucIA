# LucIA

## Docker

Build:
```
<<<<<<< HEAD
docker build -t lucia:dev .
=======
docker build -t lux_playground:dev .
>>>>>>> ff77c9e1e90499b4098ce117aea3240c5329141d
```

Run a container and open a bash terminal:
```
<<<<<<< HEAD
docker run -p 8888:8888 -it --rm lux_ai:dev bash
```

Once your inside the container, you can run jupyter this way:
```
jupyter notebook --port=8888 --no-browser --ip=0.0.0.0 --allow-root
```

=======
docker run -v $(pwd):/root -p 8888:8888 -it --rm lux_playground:dev
```
>>>>>>> ff77c9e1e90499b4098ce117aea3240c5329141d
