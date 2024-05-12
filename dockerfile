# Use the official Python 3.9 image as the base
FROM python:3.9-slim

#FROM nvidia/cuda:12.2.0-base-ubuntu20.04

#FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-runtime

# Set the environment variable
#ENV DEBIAN_FRONTEND=noninteractive

# Install the necessary libraries
# RUN apt-get update && apt-get install -y \
#     libx11-6 \
#     libgl1-mesa-glx \
#     libxrender1 \
#     python3.9 \
#     python3-pip

# Set the working directory inside the container
WORKDIR /app

# Copy your Streamlit app files into the container
COPY . .
# Copy streamlit config
COPY config.toml /root/.streamlit/config.toml

# Install dependencies from requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8501

# Specify the entry point for your Streamlit app
#ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
CMD ["streamlit", "run", "app.py"]