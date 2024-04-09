import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def _generate_token_with_past(model, inputs):
    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    last_logits = logits[0, -1, :]
    next_token_id = last_logits.argmax()
    return next_token_id, outputs.past_key_values


def generate(
    model: AutoModelForCausalLM, tokenizer: AutoTokenizer, prompt: str, max_tokens: int
) -> str:
    generated_tokens = []
    inputs = tokenizer(prompt, return_tensors="pt")
    next_inputs = inputs
    for _ in range(max_tokens):
        next_token_id, past_key_values = _generate_token_with_past(model, next_inputs)
        next_inputs = {
            "input_ids": next_token_id.reshape((1, 1)),
            "attention_mask": torch.cat(
                [next_inputs["attention_mask"], torch.tensor([[1]])], dim=1
            ),
            "past_key_values": past_key_values,
        }

        next_token = tokenizer.decode(next_token_id)
        generated_tokens.append(next_token)
    return "".join(generated_tokens)
