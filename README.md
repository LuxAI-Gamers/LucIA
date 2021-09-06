# LucIA

## Docker

Build:
```
docker build -t lucia:dev .
```

Run a container and open a bash terminal:
```
docker run -p 8888:8888 -it --rm lux_ai:dev bash
```

Once your inside the container, you can run jupyter this way:
```
jupyter notebook --port=8888 --no-browser --ip=0.0.0.0 --allow-root
```

