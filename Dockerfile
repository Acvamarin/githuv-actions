FROM python:3.12-alpine
RUN pip install --upgrade pip
RUN pip install --no-cache-dir numpy
RUN pip install --no-cache-dir tqdm
ENV PYTHONUNBUFFERED=1
WORKDIR /python-app
COPY . .
CMD ["python", "python.py"]