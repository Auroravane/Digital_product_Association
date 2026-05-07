python
import json
from transformers import T5ForConditionalGeneration, T5Tokenizer

class LegalContractTemplateGenerator:
    def __init__(self, model_type, template_types):
        self.model_type = model_type
        self.template_types = template_types
        self.model = T5ForConditionalGeneration.from_pretrained('t5-base')
        self.tokenizer = T5Tokenizer.from_pretrained('t5-base')

    def generate_contract_template(self, template_type, contract_details):
        input_text = f"Generate {template_type} contract template with details: {json.dumps(contract_details)}"
        inputs = self.tokenizer(input_text, return_tensors='pt')
        outputs = self.model.generate(inputs['input_ids'], num_beams=4, no_repeat_ngram_size=2, min_length=100, max_length=500)
        contract_template = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return contract_template

    def get_template_types(self):
        return self.template_types

# Example usage:
generator = LegalContractTemplateGenerator("natural language processing", ["employment contract", "non-disclosure agreement"])
contract_details = {
    "company_name": "ABC Corporation",
    "employee_name": "John Doe",
    "job_title": "Software Engineer",
    "start_date": "2024-01-01",
    "end_date": "2024-12-31"
}
print(generator.generate_contract_template("employment contract", contract_details))