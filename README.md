# Livesitter-MLops for a Machine Learning Project
 Implementing Simplified MLops for a Machine Learning Project
1. Version Control-
    A Deep Learning based image caption generator project using Kaggle Flickr8k dataset The objective of the project is to predict the captions for the input image. The dataset consists of 8k images and 5 captions for each image. The features are extracted from both the image and the text captions for input. The features will be concatenated to predict the next word of the caption. CNN is used for image and LSTM is used for text. BLEU Score is used as a metric to evaluate the performance of the trained model.
    ![XygNZ](https://github.com/Divyy001/Livesitter-MLops-for-a-Machine-Learning-Project/assets/80240942/a70c585c-146b-4ca8-8ae1-19e06e20bfe5)

    Here VGG16 pretrained model for feature extraction from images, a CNN model is used and for LSTM model for next word prediction, the model is trained in the following way-
   ![Untitled](https://github.com/Divyy001/Livesitter-MLops-for-a-Machine-Learning-Project/assets/80240942/f888eec3-36a5-46dc-8567-96cccaca6584)

    Saved the model as network.h5
    Created the interface using Streamlit providing the image uploading option and generating caption button.
    Here is the glimpse of the interface created.
   ![image](https://github.com/Divyy001/Livesitter-MLops-for-a-Machine-Learning-Project/assets/80240942/c2f08d38-368d-4c1d-bedc-5c63654614a6)


3. Docker Containerization-
    In the working root directory, creating a file named ‘dockerfile’ without any extensions.

    Docker Layers- 
    Firstly we define our base image where we want to build our file from, as demostrated below.

    FROM python:3.10.04-slim-bullseye

    Slim-bulleye for reducing the size of the file for image creation

    Appending the working directory of the project created

    WORKDIR / C:\Users\divyy\Desktop\github\Livesitter-MLops-for-a-Machine-Learning-Project

    Copy all the requirements into the new directory created.

    COPY requirements.txt ./requirements.txt

    Copying from the source to the destination.

    Installing all that is in the requirments.txt file.

    RUN pip install -r requiremts.txt

    Expose the port to be used to run the application.

    EXPOSE 8501

    This is the same port that our streamlit app was running on.

    Copying our app from the current directory to the working area

    COPY ./ C:\Users\divyy\Desktop\github\Livesitter-MLops-for-a-Machine-Learning-Project

    Creating an entry point to make our image executable.

    ENTRYPOINT ["streamlit", "run"]
    CMD ["interface.py"]

    Building a Docker Image-
    We build using the following command then “.” to run the current directory.

    docker build -t streamlitapp:latest .

    Output will be shown as below.

    ![image](https://github.com/Divyy001/Livesitter-MLops-for-a-Machine-Learning-Project/assets/80240942/fc31eede-d004-4101-9578-4e52fa8e12c1)


    Pushing the Docker image to a container registry(Docker Hub)-
    By using "docker images" in the same directory will give the images list.
    First login into the docker in your terminal by using "docker login", this will authenticate and login the user successfully, otherwise ask for the credentials.

    In Docker Hub, loging in and copying the repositary name.
    To push the image using the following command:

    docker push divyy001/streamlitapp:latest

    Added the repo name with the image along side the docker push command. This will push the image to the docker hub repo.

    ![image-1](https://github.com/Divyy001/Livesitter-MLops-for-a-Machine-Learning-Project/assets/80240942/7cc43249-851e-4c44-b68a-616aba41fc78)

