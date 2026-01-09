# MACHINE-LEARNING-MODEL-IMPLEMENTATION

*COMPANY NAME*: CODTECH IT SOLUTIONS PRIVATE LIMITED

*NAME*: KANIGA K

*INTERN ID*: CTIS0301

*DOMAIN*: PYTHON PROGRAMINNG

*DURATION*: 4 WEEKS

*MENTOR NAME*: NEELA SANTHOSH

**MACHINE LEARNING MODEL IMPLEMENTATION(SPAM/NOT SPAM):

This task is about building an SMS Spam Detection system using Machine Learning. The main aim of this project is to automatically identify whether a text message is spam or not spam (ham). Spam messages usually contain advertisements, fake offers, or fraud-related content, while ham messages are normal personal or informational messages. This project helps in understanding how machine learning can be applied to real-life problems such as filtering unwanted messages.

For this task, the SMS Spam Collection Dataset is used. This dataset contains a large number of SMS messages, and each message is already labeled as either “spam” or “ham”. Using this dataset makes it easier to train the machine learning model because the correct output is already known. The dataset is stored in CSV format and is loaded into the project using the pandas library.

The project is implemented using Python in Jupyter Notebook. Several important libraries are used, such as pandas and numpy for data handling, scikit-learn for machine learning algorithms, and joblib for saving the trained model. Jupyter Notebook is used because it allows step-by-step execution of code and easy visualization of outputs, which is helpful for learning and debugging.

After loading the dataset, data preprocessing is performed. This includes cleaning the data, removing unwanted columns, and converting text labels into numerical form. The text messages are then converted into numerical vectors using the TF-IDF Vectorizer. This step is very important because machine learning models cannot understand text directly; they only work with numbers.

Once the data is prepared, it is split into training and testing sets. The training data is used to train the machine learning model, while the testing data is used to evaluate its performance. In this project, a classification algorithm is used to learn the pattern of spam and ham messages. After training, the model achieves very good accuracy, showing that it can correctly classify messages.

After successful training and testing, the model and vectorizer are saved using the joblib library. These saved files can later be used in a backend application without retraining the model again. Finally, the model is tested with a custom message, and it correctly predicts whether the message is spam or ham.

Overall, this task demonstrates the complete workflow of a machine learning project, including data collection, preprocessing, model training, evaluation, and deployment preparation.

*OUTPUT*:

<img width="661" height="367" alt="Image" src="https://github.com/user-attachments/assets/0d3cf8a6-38dd-4ced-b47e-e3021fc8f357" />

<img width="747" height="365" alt="Image" src="https://github.com/user-attachments/assets/f820ad3a-5a36-492b-8d2f-636fbfb563ea" />


