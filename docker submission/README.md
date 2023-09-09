# Instructions for the submission of AIIB2023

## Instructions for Validation Phase submission
During the validation phase, competitors are required to submit mask predictions (*.nii.gz) for task 1 and the mortality rate predictions (*.csv) for task 2. We require zipped submissions for both tasks to the submission page.

For task 1, the zipped file should be arranged as follows:

── teamname_ValPhase.zip

   ├── AIIB_001.nii.gz
   
   └── AIIB_002.nii.gz
   
   ├── ...
   
   └── AIIB_110.nii.gz

For task 2, the CSV file should contain two columns, one named 'ID' with the ID of all patients; and the other named 'prediction'. The zipped file for submission should be arranged as follows:

── teamname_ValPhase.zip

   └── mortality_prediction.csv
   
 

## Instructions for Test Phase submission

The AIIB2023 challenge will be held as a Type II challenge that will not release the test set to its competitors. For the test phase submission, we will require the competitors to submit their containerized docker images. We encourage the challengers to publicize their codes on GitHub, and provide the URL for their GitHub projects in their submitted documents. However, we do not require open-source publication of codes. 

### Step 1. Organize an inference script

We require a script file that automatically performs inference on the test set, i.e., outputting the predicted segmentation masks or mortality rates on the test set. We did not require the competitors to participate in both tasks, so for different tasks, the inference script can vary.

For task 1, we require that the input folder be mounted into *input* and the output folder be *output*. In addition, the output files should have the same file name as the input, e.g. the input file input/AIIB_001.nii.gz must have a matched output prediction named output/AIIB_001.nii.gz. An example of the inference script can be found [here](./predict_task1.py).

For task 2, the mortality predictions on all test files should be summarized in one single CSV file, named as output/mortality.csv. The input should be the CT volumes mounted at *input_image*. An example of the inference script can be found [here](./predict_task1_and_2.py).




### Step 2. Containerize the application using Docker

We require the competitors to use [Docker] to containerize their applications. Docker images can be created using Dockerfiles, which contain all commands that help to run applications. An example of Dockerfile can be found [here](./Dockerfile). Four basic components are required to be included in the Docker file:

1. Pulling a pre-existing image with an operating system and, if needed, CUDA (FROM instruction).
2. Installing additional dependencies (RUN instructions).
3. Transferring local files into your Docker image (COPY instructions).
4. Executing your algorithm (CMD  and ENTRYPOINT instructions).

After finishing the Dockerfile, you can build your docker image with:
docker build -f Dockerfile -t [teamname] .


### Step 3. Docker running commands
Your container will be run with the following command:
```
docker run --rm -v [input directory]:/input -v [output directory]:/output -it [teamname]
```

[input directory] will be the absolute path of our directory containing the test set, [output directory] will be the absolute path of the prediction directory.

### Step 4. Docker container submission
The name of the submission should be named as "Teamname_TaskNO.", e.g. "ImperialCollegeLondon_Task2", and send to ![aiib23.miccai@gmail.com](mailto:aiib23.miccai@gmail.com).


## References
This tutorial and examples containd are based on [CrossModa](https://crossmoda.grand-challenge.org/submission/).
