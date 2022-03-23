from simpletransformers.classification import ClassificationModel, ClassificationArgs
import torch
import logging

def performPrediction(sms):
    # logging.basicConfig(level=logging.INFO)
    # transformers_logger = logging.getLogger("transformers")
    # transformers_logger.setLevel(logging.WARNING)
    #
    # # Optional model configuration
    model_args = ClassificationArgs(num_train_epochs=1)
    #
    # # Create a ClassificationModel
    cuda_available = torch.cuda.is_available()
    # cuda_available = False

    # Create a ClassificationModel
    # this loads the models from the output directory
    print("starting to load model")
    model = ClassificationModel(
        "roberta", "C:/Users/matan/My PC (DESKTOP-RLTMVS3)/Desktop/simpletransformers_project/outputs", args=model_args, use_cuda=cuda_available
    )
    print("performing prediction")
    predictions, raw_outputs = model.predict([sms])
    print("returning prediction")
    return predictions[0]

if __name__ == '__main__':
    print(performPrediction("You have just won the lottery! Click here to claim your reward!"))