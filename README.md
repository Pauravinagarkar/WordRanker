# Top K Words in a Document using Kafka

This repository contains an implementation to determine the top K most frequently occurring words in a document using Kafka and Spark.

## Project Overview

### Goals
1. Implement Spark code to determine the top 100 most frequently occurring words and the top 100 most frequently occurring words having more than 6 characters in a 16GB dataset.
2. Gain proficiency in log analytics and implement log analytics techniques.
3. Develop a data processing and analysis pipeline using Kafka (producer and consumer), Spark Streaming, Parquet files, and HDFS.

### Problem Statement
1. **Top K Words**: Develop Spark code to determine the top 100 most frequently occurring words and the top 100 most frequently occurring words with more than 6 characters.
2. **Log Analytics**: 
   - Identify the endpoint with the highest number of invocations on a specific day of the week.
   - Find the top 10 years with the least occurrences of 404 status codes.
3. **Data Processing Pipeline**: Implement a pipeline starting with a Kafka producer, followed by a Kafka consumer performing transformations using Spark, and storing the transformed data in Parquet format in HDFS.

### How to Run the Code

#### Jupyter Notebooks
- `.ipynb` files can be executed directly using Jupyter notebook.

#### Producer
To run `producer.py`:
```bash
python producer.py

#### Consumer
To run `consumer.py`:
```bash
python consumer.py



