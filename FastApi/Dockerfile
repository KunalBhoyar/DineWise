FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY . .

EXPOSE 8000

ENV open_api_key=""
ENV bucket_name = ""
ENV host = "" 
ENV user = ""
ENV password = ""
ENV db = ""
ENV JWT_SECRET=""
ENV Embedding_Model = ""
ENV pinecone_api_key=""
ENV pinecone_environment=""
ENV pinecone_index_name = ""

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]