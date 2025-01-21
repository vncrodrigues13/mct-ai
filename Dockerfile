# Step 1: Use an official Python runtime as a parent image
FROM python:3.8

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt into the container at /app
COPY requirements.txt .

# Step 4: Install the dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Step 5: Copy the rest of the application files into the container
COPY . /app

# Step 6: Expose any necessary ports (for example, if running Flask)
EXPOSE 5000
