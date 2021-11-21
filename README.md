# inference-latency-test

Code from https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/tree/main/course4/week2-ungraded-labs/C4_W2_Lab_3_Latency_Test_Compose

## Quick Start

### 1. pull locust image

```bash
docker pull locustio/locust
```

### 2. build the image

```bash
cd online-inference
docker build -t mlepc4w2-ugl:no-batch .
```

```bash
cd batch-inference
docker build -t mlepc4w2-ugl:with-batch .
```

### 3. run multi-container application usign docker compose

```bash
docker-compose up
```

### 4. Load Testing the servers

go http://localhost:8089/
Start with low values because the more users you add more memory will be required and you risk crashing the application. A good start point is 10 Number of users and 10 Spawn rate.

### 5. stopping the application

`ctrl + c`

```bash
docker-compose down
```
