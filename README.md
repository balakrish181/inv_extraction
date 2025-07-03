# PDF Information Extractor

This project extracts structured information from PDF documents like invoices and credit card statements. It uses a combination of OCR, table recognition, and large language models (LLMs) to parse the data and save it in a structured format (CSV).

## Features

- Extracts text and tables from PDF documents using OCR.
- Parses unstructured text into a structured format using LLMs (OpenAI or Ollama).
- Defines a clear data schema for the extracted information using Pydantic.
- Saves the extracted line items into a CSV file.
- Modular design for easy extension and maintenance.

## How it Works

1.  **Text Extraction (`text_extraction.py`):** The process starts by taking a PDF file as input. The `docling` library is used to perform OCR and extract all the text content, including tables, into a markdown format.
2.  **Data Structuring (`fields_to_extract.py`):** Pydantic models define the desired structure of the final data (e.g., `CreditCardStatement`, `SpendItem`, `CustomerAddress`, `PaymentInfo`). This ensures that the data extracted by the LLM is well-formed and validated.
3.  **AI-Powered Parsing (`client_request.py`):** The extracted markdown text is sent to an LLM (either OpenAI's GPT or a local Ollama model). A system prompt instructs the model to act as an information extractor and populate the Pydantic models based on the provided text. The `instructor` library is used to get structured output from the LLM.
4.  **Execution and Output (`main.py`):** The main script orchestrates the workflow. It calls the text extraction module, then the parsing module, and finally saves the extracted `spend_line_items` into a CSV file named `spend_line_items_v2_category_amex.csv`.

## Project Structure

```
.
├── client_request.py       # Handles requests to the LLM (OpenAI/Ollama) for parsing.
├── fields_to_extract.py    # Defines the Pydantic models for the data structure.
├── main.py                 # The main script to run the extraction process.
├── sample_invoices/        # Directory for sample PDF invoices.
├── text_extraction.py      # Extracts text from PDFs using docling.
├── .gitignore              # Git ignore file.
└── README.md               # This file.
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd invoice_extraction
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Install the dependencies from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    If you are using OpenAI, you need to set your API key as an environment variable:
    ```bash
    export OPENAI_API_KEY='your-api-key'
    ```

## Usage

1.  Run the main script, providing the path to the PDF file as a command-line argument:
    ```bash
    python main.py path/to/your/invoice.pdf
    ```
2.  The script will generate a `transactions.csv` file in the project's root directory with the extracted transaction data.