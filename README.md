# Chatbot-to-compare-multiple-PDF-documents-with-RAG-Chat-GPT-and-LlamaIndex
This chatbot is different to others in that is built to avoid the poor performance of chatbots that have the embeddings of multiple PDF and other documents all embedded together in one large dataset.

Instead it uses Retrieval Augmented Generation (RAG) and LlamaIndex to not only create a separate embeddings dataset for each PDF but it uses QueryEngineTool and SubQuestionQueryEngine to break down a complex query (like compare and contrast) into multiple sub questions and sends them to their specific targetted dataset.

All responses are then gathered and sent to response synthesiser to produce the final response to your question.

# Instructions

## Step 1

First, install the required packages:

```
pip install -r requirements.txt
```

## Step 2

Copy and paste your Open AI API key in both the embed.py and chat.py files here

```python
openai.api_key = "copy-and-paste-your-openai-api-key-here"
```

## Step 3 

Run embed.py 

```python
python embed.py 
```

You will probably get 2 warnings but no errors. You can ignore the 2 warnings.

This will create 2 new sub directories containing embeddings created from the 2 PDF files which will be called alice_docs.DB and glass_docs.DB

alice_docs.DB are the emebeddings created from the text of the PDF of Alice In Wonderland and glass_docs.DB are the emebeddings created from the text of the PDF of the sequel Through The Looking Glass

## Step 4

Talk to the chatbot :

```python
python chat.py
```

Any question you ask will result in two things : 

1) It will be broken down into multiple sub questions and then sent to both datasets.
2) All responses are then gathered and sent to response synthesiser to produce the final response to your question.
 
The multiple sub questions in step one will all be colour coded so you can see what questions are being directed to what dataset and also what their response was.

The final response from step 2 (which is not colour coded) will then be displayed.

For example try asking "which book is more surreal and why?"

Or perhaps ... "In which book does alice learn the most things and what are they?"



