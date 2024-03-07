from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

# video_url = "https://www.youtube.com/watch?v=lG7Uxts9SXs&t=1241s&ab_channel=freeCodeCamp.org"
video_url ="https://www.youtube.com/watch?v=pRGtPd89MRA"

def create_vector_db_from_youtube_url( video_url: str ) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url, language="zh-Hans")
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)

    return docs

print(create_vector_db_from_youtube_url(video_url))


