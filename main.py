from text_extraction import extract_text_from_pdf
import instructor
from openai import OpenAI
from pydantic import BaseModel, Field
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing import Iterable

from fields_to_extract import CreditCardStatement
from client_request import parse_lead_from_message
import csv
import sys 

def main(input_doc_path):

    
    context_markdown = extract_text_from_pdf(input_doc_path)

    print(context_markdown)
    sys.exit()

    #client = instructor.from_openai(OpenAI())

    response = parse_lead_from_message(CreditCardStatement, context_markdown, model_name="openai")

    spend_line_items = response.model_dump()['spend_line_items']

    # Step 2: Choose a filename
    filename = 'spend_line_items_v2_category_amex.csv'
    with open(filename, mode='w', newline='') as file:
        if spend_line_items:
            writer = csv.DictWriter(file, fieldnames=spend_line_items[0].keys())
            writer.writeheader()
            writer.writerows(spend_line_items)
        else:
            print("No spend_line_items found.")


if __name__ == "__main__":
    input_doc_path = "example_bill.pdf"
    main(input_doc_path)
    #print(text)
