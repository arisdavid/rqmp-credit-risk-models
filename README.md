## Credit Models

### Introduction
Sample models to execute on the platform


### Build a docker image

```
docker build -t credit-models:latest .
```

### Test
```
docker run -it credit-models:latest python3 main.py 1000000 900000 500000 0.18 0.12
```