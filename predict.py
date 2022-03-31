from simpletransformers.classification import ClassificationModel, ClassificationArgs
import torch
from transformers import RobertaTokenizer

from transformers import RobertaTokenizer

MODEL_PATH = "./outputs"


def prediction(sms):
    model_args = ClassificationArgs(num_train_epochs=1, use_multiprocessing=False,
                                    use_multiprocessing_for_evaluation=False, process_count=1)
    model = ClassificationModel(
        "roberta", "./outputs",
        args=model_args, use_cuda=False)
    tokenizer = RobertaTokenizer.from_pretrained(
        "./outputs")

    model_args = ClassificationArgs(num_train_epochs=1)
    #
    # # Create a ClassificationModel
    cuda_available = torch.cuda.is_available()
    # cuda_available = False

    # Create a ClassificationModel
    # this loads the models from the output directory
    print("starting to load model")
    model = ClassificationModel(
        "roberta", MODEL_PATH, args=model_args,
        use_cuda=cuda_available
    )
    print("performing prediction")
    # predictions, raw_outputs = model.predict([sms])
    print("returning prediction")

    inputs = tokenizer(sms, return_tensors="pt")
    outputs = model.model(**inputs)

    if outputs[0][0][0].item() > outputs[0][0][1].item():
        return "Non-Spam"
    else:
        return "Spam"
