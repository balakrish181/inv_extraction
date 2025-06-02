from pydantic import BaseModel


def parse_lead_from_message(client, pydantic_model: BaseModel, user_message: str):
    
    
    return client.chat.completions.create(
        model="gpt-4.1-mini-2025-04-14",
        response_model=pydantic_model,
        messages=[
            {
                "role": "system",
                "content": "You are an intelligent assistant that extracts structured information from "
                "credit card statements/ invoices based only on the information provided. Your ability "
                "to extract and summarize this information accurately is essential. Do not use "
                "outside knowledge. Only rely on the context passed by the user",
            },
            {
                "role": "user",
                "content": f"Extract the user's CreditCardStatement information from this statement: {user_message}",
            },
        ],
    )