import re
import torch
import warnings
from peft import PeftModel
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    pipeline,
)

warnings.filterwarnings("ignore", category=UserWarning)

# set base model
base_model = "NousResearch/Llama-2-7b-chat-hf"

# load tokenizer
tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# define quantization config
compute_dtype = getattr(torch, "float16")
quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=compute_dtype,
    bnb_4bit_use_double_quant=False,
)

# load base model
base_model = AutoModelForCausalLM.from_pretrained(
    base_model,
    quantization_config=quant_config,
    device_map="auto"
)
base_model.config.use_cache = False
base_model.config.pretraining_tp = 1

# set adapter model
adapter_model = "models/model_240411_0952"

# load merged model
model = PeftModel.from_pretrained(
    model=base_model,
    model_id=adapter_model
)
model = model.merge_and_unload()

# build pipeline
qna_pipeline = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=1024,
)

# format prompt
def get_question_prompt(question):
    system_msg = "<<SYS>>\n" \
        + "You are a helpful and honest psychologist." \
        + "Respond to the following question from the user." \
        + "Your answers should not include any critical, dangerous or illegal content." \
        + "Your answers should be unbiased and encouraging.\n" \
        + "<</SYS>>\n\n"
    prompt = f"<s>[INST] {system_msg}###User: {question}###You: [/INST]"
    return prompt

print("\nHello, this Menthy. Is there anything I can help you with?\n")
while True:
    prompt = get_question_prompt(input(""))
    result = qna_pipeline(prompt)
    answer = re.split(r"\[\/INST\]\s*", result[0]["generated_text"], maxsplit=1)[1]
    print("\n" + answer)
    command = input("\nDo you have another question? (Y/N)")
    if command.lower() in ["n", "no"]:
        print("\nThanks for using Menthy. See you next time!\n")
        break
    else:
        print("\nPlease let me know your other concerns!\n")
