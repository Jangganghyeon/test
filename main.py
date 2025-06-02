import streamlit as st

st.title('나의 첫 streamlit 프로젝트!')
st.write('Hello streamlit')

import streamlit as st
import random

# MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["🧠 데이터 과학자", "📈 전략 컨설턴트", "🔬 연구 과학자"],
    "INFP": ["🎨 일러스트레이터", "📚 소설가", "🌿 환경운동가"],
    "ESFP": ["🎤 가수", "🎬 배우", "🎡 이벤트 플래너"],
    "ENTP": ["🧑‍💼 창업가", "🎙️ 방송인", "💡 혁신 컨설턴트"],
    # 더 많은 MBTI 추가 가능
}

# 제목 꾸미기
st.markdown("""
    <h1 style='text-align: center; color: #FF69B4;'>🌟 MBTI로 알아보는 ✨<br>나에게 어울리는 직업은? 💼</h1>
""", unsafe_allow_html=True)

# 사이드바 설정
st.sidebar.title("📌 사용 방법")
st.sidebar.info("왼쪽에서 자신의 MBTI를 선택해보세요!")

# MBTI 선택
selected_mbti = st.selectbox("💖 당신의 MBTI는 무엇인가요?", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.markdown(f"## 🎯 {selected_mbti}에게 어울리는 직업 추천! 💼")
    recommended_jobs = mbti_jobs[selected_mbti]
    for job in recommended_jobs:
        st.markdown(f"- {job}")

    # 랜덤 추가 추천
    st.markdown("---")
    st.markdown("### 🌈 특별 보너스 추천 🎁")
    st.success(f"{random.choice(recommended_jobs)} 는 당신에게 찰떡궁합 직업이에요! ✨")

# 하단 장식
st.markdown("""
    <hr>
    <p style='text-align: center;'>
        💡 이 앱은 재미와 흥미를 위한 진로 탐색 도우미입니다 🎈<br>
        by <b>진로쌤 AI</b> 🤖
    </p>
""", unsafe_allow_html=True)

# 배경 설정 (커스텀 CSS)
st.markdown("""
    <style>
    body {
        background-color: #FFF0F5;
        background-image: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
    }
    .stSelectbox > div {
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)
