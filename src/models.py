from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from langchain.callbacks import StreamingStdOutCallbackHandler
from .config import GOOGLE_API_KEY
from typing import Optional
from functools import wraps
import streamlit as st


# LLM 호출 횟수 제한을 위한 데코레이터
def limit_llm_calls(func):
    call_count = 0
    max_calls = 3

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count
        if call_count >= max_calls:
            raise MaxLLMCallsExceeded("최대 LLM 호출 횟수(3회)를 초과했습니다.")
        call_count += 1
        return func(*args, **kwargs)

    return wrapper


def initialize_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        top_p=0.85,
        frequency_penalty=0.1,
        presence_penalty=0.1,
        google_api_key=GOOGLE_API_KEY,
        max_output_tokens=1000,
        streaming=True,
        max_tokens=5000,
    )


# LLM 체인 생성 함수
@limit_llm_calls
def create_chain(llm, prompt_template, memory: Optional[dict] = None):
    if "keywords" not in st.session_state:
        st.session_state["keywords"] = "일반"
    if "locations" not in st.session_state:
        st.session_state["locations"] = "제주시내"
    if "score" not in st.session_state:
        st.session_state["score"] = 4.5
    if "user_input" not in st.session_state:
        st.session_state["user_input"] = ""
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    if "search_results" not in st.session_state:
        st.session_state["search_results"] = []

    # 'input_text'를 'user_input'으로 변경
    input_text = st.session_state["user_input"]

    prompt = prompt_template.template.format(
        keyword=st.session_state["keywords"],
        location=st.session_state["locations"],
        min_score=st.session_state["score"],
        user_input=input_text,
        chat_history=st.session_state["chat_history"],
        search_results=st.session_state["search_results"],
    )

    return LLMChain(
        prompt=prompt_template,
        llm=llm,
        memory=memory,
        output_parser=StrOutputParser(),
        verbose=True,
        callbacks=[StreamingStdOutCallbackHandler()],
    )
