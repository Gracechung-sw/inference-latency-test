# inference-latency-test

Code from https://github.com/https-deeplearning-ai/machine-learning-engineering-for-production-public/tree/main/course4/week2-ungraded-labs/C4_W2_Lab_3_Latency_Test_Compose

1. pull locust image

```bash
docker pull locustio/locust
```

2. build the image

```bash
cd online-inference
docker build -t mlepc4w2-ugl:no-batch .
```

```bash
cd batch-inference
docker build -t mlepc4w2-ugl:with-batch .
```

3. run multi-container application usign docker compose

```bash
docker-compose up
```
