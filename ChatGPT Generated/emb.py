from tiktoken import TokenBatcher
from transformers import AutoModel, AutoTokenizer
import torch

def generate_embeddings(tokens):
    model_name = "your_model_name"  # Specify the name of the pre-trained model you want to use
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    batcher = TokenBatcher(tokenizer, model)

    input_ids = batcher(tokens)
    input_ids = torch.tensor(input_ids).unsqueeze(0)

    with torch.no_grad():
        outputs = model(input_ids)

    embeddings = outputs.last_hidden_state.squeeze(0)

    # Return the embeddings
    return embeddings
