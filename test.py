import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# API 키 입력 받기
api_key = st.text_input("Google API Key를 입력하세요", type="password")

if api_key:
    # 작문 내용 입력 받기
    st.subheader("작문을 위한 내용을 입력해주세요")
    topic = st.text_input("주제")
    content = st.text_area("세부 내용")

    # 생성 버튼
    if st.button("작문 생성하기"):
        try:
            # Gemini 모델 초기화
            llm = ChatGoogleGenerativeAI(
                model="gemini-1.5-pro-latest",
                google_api_key=api_key,
                temperature=0.7
            )

            # 프롬프트 템플릿 생성
            template = """
            다음 내용을 바탕으로 자연스러운 작문을 작성해주세요:
            주제: {topic}
            세부 내용: {content}
            """

            prompt = PromptTemplate(
                input_variables=["topic", "content"],
                template=template
            )

            # 최종 프롬프트 생성
            final_prompt = prompt.format(
                topic=topic,
                content=content
            )

            # 결과 생성
            response = llm.invoke(final_prompt)
            
            # 결과 출력
            st.subheader("생성된 작문")
            st.write(response.content)

        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")
else:
    st.warning("API 키를 입력해주세요.")

