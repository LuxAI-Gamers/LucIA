# LucIA

## Docker

Build:
```
docker build -t lux_playground:dev .
```

Run a container and open a bash terminal:
```
docker run -v $(pwd):/root -p 8888:8888 -it --rm lux_playground:dev
```
