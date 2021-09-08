# LucIA

## Docker

Build:
```
docker build -t lux_playground:dev .
```

Open Jupyter on a Docker container:
```
docker run -v $(pwd):/root -p 8888:8888 -it --rm lux_playground:dev
```
