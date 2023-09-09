FROM apache/airflow:2.6.3-python3.9

# Switch to the root user to perform installations
USER root

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libffi-dev \
    libssl-dev \
    build-essential \
    cmake \
    git \
    g++

# Install Arrow
RUN git clone https://github.com/apache/arrow.git && \
    cd arrow/cpp && \
    mkdir build && \
    cd build && \
    cmake .. -DCMAKE_BUILD_TYPE=Release && \
    make -j$(nproc) && \
    make install

# Set the working directory
WORKDIR /opt/airflow

# Switch to the airflow user to perform pip installations
USER airflow

# Copy requirements.txt and install Python dependencies
COPY ./docker/airflow/requirements.txt ./
RUN pip install -r requirements.txt

ENV PYTHONPATH=/opt/airflow/etl:/opt/airflow/data:/opt/airflow/src:/opt/airflow/config:$PYTHONPATH
