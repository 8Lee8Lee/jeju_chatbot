import streamlit as st
import os
import faiss
from langchain.schema import Document
from src.chatbot import get_chatbot_response
from src.ui import initialize_streamlit_ui
from src.models import initialize_llm, create_chain
from src.config import INDEX_PATHS, PKL_PATHS, PKL_PATHS
from langchain_community.embeddings import HuggingFaceEmbeddings


# 임베딩 모델 초기화
def initialize_embeddings(model_name="jhgan/ko-sroberta-multitask"):
    embedding = HuggingFaceEmbeddings(model_name=model_name)
    return embedding


# 문서 생성
def create_documents(data):
    return {
        "mct_docs": [
            Document(page_content=item.get("가게명", ""), metadata=item)
            for item in data["mct"]
        ],
        "month_docs": [
            Document(page_content=item.get("관광지명", ""), metadata=item)
            for item in data["month"]
        ],
        "wkday_docs": [
            Document(page_content=item.get("관광지명", ""), metadata=item)
            for item in data["wkday"]
        ],
        "mop_docs": [
            Document(page_content=item.get("관광지명", ""), metadata=item)
            for item in data["mop_sentiment"]
        ],
        "menu_docs": [
            Document(page_content=item.get("가게명", ""), metadata=item)
            for item in data["menu"]
        ],
        "visit_docs": [
            Document(page_content=item.get("관광지명", ""), metadata=item)
            for item in data["visit_jeju"]
        ],
        "kakaomap_reviews_docs": [
            Document(page_content=item.get("관광지명", ""), metadata=item)
            for item in data["kakaomap_reviews"]
        ],
    }


# Streamlit 세션 상태 초기화
if "chain" not in st.session_state:
    st.session_state.chain = None  # 또는 적절한 초기값으로 설정


# FAISS 인덱스를 로드하고 초기화하는 함수
def load_faiss_indexes_with_retriever(INDEX_PATHS, data, embedding_function):
    retrievers = {}
    for key, path in INDEX_PATHS.items():
        # 경로 확인
        abs_path = os.path.abspath(path)
        print(f"Loading index from: {abs_path}")

        # 파일이 존재하는지 확인
        if os.path.exists(abs_path):
            try:
                # FAISS 인덱스를 로드
                index = faiss.read_index(abs_path)

                # 문서 생성
                documents = create_documents(data)[f"{key}_docs"]

                # FAISS VectorStore 객체 생성
                retriever = FAISS.from_documents(
                    documents,
                    embedding_function,
                    index=index,  # 로드된 FAISS 인덱스 사용
                )

                retrievers[key] = retriever
            except Exception as e:  # 구체적인 오류 메시지 추가
                print(f"Error loading index '{key}': {e}")
        else:
            print(f"Index file '{abs_path}' not found.")
    return retrievers


data = {}  # 실제 데이터 로딩 필요
embedding_function = initialize_embeddings()

retrievers = load_faiss_indexes_with_retriever(INDEX_PATHS, data, embedding_function)
