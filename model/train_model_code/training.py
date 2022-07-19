from sklearn.model_selection import train_test_split
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
import torch

if __name__ == '__main__':
    #  Transformers has a centralized logging system, so that you can setup the verbosity of the library easily.
    logging.basicConfig(level=logging.INFO)
    transformers_logger = logging.getLogger("transformers")
    transformers_logger.setLevel(logging.WARNING)

    # Organize Data Frame
    df = pd.read_csv("spam.csv", index_col=False, header=None, encoding='latin-1')

    # change label of headers

    df = df.iloc[:, [1, 0]]
    df[0] = df[0].map({'ham': 1, 'spam': 0})

    # remove null data
    df = df[df[0].notna()]

    # split data to train and test
    train, test = train_test_split(df, test_size=0.2)

    # checks if GPU is available
    cuda_available = torch.cuda.is_available()

    # Optional model configuration
    model_args = ClassificationArgs(num_train_epochs=1)

    # Create a ClassificationModel
    model = ClassificationModel(
        "roberta", "roberta-base", args=model_args, use_cuda=cuda_available
    )
    df[0] = df[0].astype(int)
    print(train)
    # Train the model
    model.train_model(train)

    # Evaluate the model
    result, model_outputs, wrong_predictions = model.eval_model(test)
