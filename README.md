# KAIT 주최 및 신한카드 주관 - 2024 빅콘테스트 생성형AI분야 
## "LLM활용 제주도 맛집 추천 대화형 AI서비스 개발" 

<br>

### 실행 결과 (서비스 웹 페이지)
https://gamgul-talk.streamlit.app/

![image](https://github.com/user-attachments/assets/9212744f-6c74-4c9f-ada6-b15dd248a070)

문제 상황: 방대한 데이터에서 유의미한 정보 추출의 어려움, 자원 소모
해결 방안: 대화형 AI 기반 서비스를 통한 정보 접근성 향상
목표: 사용자 맞춤 맛집 추천 AI 모델 구축
데이터: 신한카드 가맹점 이용 데이터, 제주 관광공사 관광 데이터, 크롤링 데이터
핵심 기능: 자연어 기반 요청 이해, 최적 맛집 추천

![image](https://github.com/user-attachments/assets/5798ed46-cef6-4d84-8133-374af2e65b8b)

메뉴 및 가격 검색 기능: 냉면, 10000원 이하 등
네이버 지도 링크 제공
착한 가격 식당 정보 제공
간편 검색 기능: 필터 기능, 주변 맛집 검색 등

![image](https://github.com/user-attachments/assets/5f199fa1-8153-4bdf-b803-15f67143b4ae)

파이프라인: 데이터 수집, 로딩, 임베딩, 저장, 검색, 생성
데이터: 제공 데이터, 크롤링 데이터
도구: JSON Loader, Document Loader, FAISS, Lang Chain 등
구성 요소: Normalize_embeddings, Quantization, Chain of Thought, Prompt 등

![image](https://github.com/user-attachments/assets/58040dda-0928-4a69-9980-0dde86372e1c)

모델 양자화: 데이터를 낮은 비트로 표현, 메모리 사용량 감소, 계산 효율성 증대
임베딩 정규화: 벡터 크기 및 분포 조정, 모델 안정성 및 정확성 향상
장점: 메모리 절약, 계산 효율성, 안정성, 정확성, 유사도 계산 정확성 향상
기대 효과: 다양한 플랫폼에서 최적 성능, 실용성 및 유연성 향상

![image](https://github.com/user-attachments/assets/6fb2699b-3aab-486e-b321-512c7f6d115c)

FAISS: 고차원 벡터 검색 라이브러리, 대규모 데이터베이스, 빠른 응답 시간
BM25: 텍스트 기반 정보 검색 알고리즘, 키워드 중심 검색, 정확한 텍스트 일치
FAISS + BM25 조합: 텍스트 및 임베딩 기반 유사도 고려, 정밀한 검색 결과 제공

![image](https://github.com/user-attachments/assets/6dcec7a4-7584-47cc-90c3-045b87927b65)

선별적 검색: 다중 FAISS 데이터베이스 구축, 질문 의도 기반 선택적 검색
효과: 효율적 데이터 검색, 시스템 자원 절약, 검색 속도 향상, 정확한 답변 제공

![image](https://github.com/user-attachments/assets/d6ce94d3-aa21-43f9-a8f4-9c5be43aaca8)

대화형 AI 시스템: 자연스러운 대화 기반 데이터 활용, 간편한 접근성
장점: 정확한 의도 파악, 맞춤형 정보 제공, 사용자 만족도 증대, 데이터 가치 극대화

![image](https://github.com/user-attachments/assets/d19f8c99-94bd-4b4e-9d67-4c56771d31e4)
