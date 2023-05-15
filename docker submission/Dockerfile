## Pull from existing image
FROM nvcr.io/nvidia/pytorch:21.05-py3


## Copy requirements
COPY ./requirements.txt .

## Install Python packages in Docker image
RUN pip3 install -r requirements.txt

## Copy all files
COPY ./ ./

## Execute the inference command 
CMD ["./predict_task1.py"]
ENTRYPOINT ["python3"]