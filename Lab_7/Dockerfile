FROM python:3.12

WORKDIR /app

COPY Product.py .
COPY Inventory.py .
COPY CanBeShipped.py .
COPY PhysicalProduct.py .
COPY DigitalProduct.py .
COPY main.py .
COPY inventory.json .

CMD ["python", "main.py"]