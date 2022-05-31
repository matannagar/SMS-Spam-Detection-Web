from simpletransformers.classification import ClassificationModel, ClassificationArgs
import torch


from transformers import RobertaTokenizer

MODEL_PATH = "./outputs"


def prediction(sms):
    tokenizer = RobertaTokenizer.from_pretrained(
        "./outputs")

    # checks if GPU is available
    cuda_available = torch.cuda.is_available()

    print("starting to load model")
    # model args for creation
    model_args = ClassificationArgs(num_train_epochs=1)

    # this loads the models from the output directory
    model = ClassificationModel(
        "roberta", MODEL_PATH, args=model_args,
        use_cuda=cuda_available
    )
    print("performing prediction")
    inputs = tokenizer(sms, return_tensors="pt")

    outputs = model.model(**inputs)
    print("returning prediction")

    # make pretty
    if outputs[0][0][0].item() > outputs[0][0][1].item():
        return "Non-Spam"
    else:
        return "Spam"
