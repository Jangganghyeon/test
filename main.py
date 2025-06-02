import streamlit as st

st.title('나의 첫 streamlit 프로젝트!')
st.write('Hello streamlit')

import streamlit as st
import random

# MBTI별 직업 추천 데이터 (생략하지 않고 유지)
mbti_jobs = {
    # [기존 코드 유지 - 생략]
}

# 제목 꾸미기
st.markdown("""
    <h1 style='text-align: center; color: #FF69B4;'>🌟 MBTI로 알아보는 ✨<br>나에게 어울리는 직업은? 💼</h1>
""", unsafe_allow_html=True)

# 사이드바 설정
st.sidebar.title("📌 사용 방법")
st.sidebar.info("아래 간단한 테스트로 MBTI를 알아보거나, 알고 있다면 직접 선택하세요!")

# 간단한 MBTI 테스트
st.markdown("### ✨ 초간단 MBTI 테스트 ✨")
col1, col2 = st.columns(2)

with col1:
    e_i = st.radio("🧠 사람들과 함께 있을 때, 나는:", ["E: 에너지를 얻는다", "I: 지친다"])
    s_n = st.radio("🔍 정보를 처리할 때 나는:", ["S: 사실을 중시한다", "N: 직관을 신뢰한다"])
with col2:
    t_f = st.radio("❤️ 결정을 내릴 때 나는:", ["T: 이성을 따른다", "F: 감정을 따른다"])
    j_p = st.radio("📅 일정을 관리할 때 나는:", ["J: 계획을 세운다", "P: 즉흥적으로 한다"])

# 결과 조합
mbti_result = (e_i[0] + s_n[0] + t_f[0] + j_p[0]).upper()
st.markdown(f"### 👉 당신의 추정 MBTI는 **`{mbti_result}`** 입니다!")

# 직접 선택
selected_mbti = st.selectbox("💖 또는 MBTI를 직접 선택해보세요!", sorted(mbti_jobs.keys()), index=sorted(mbti_jobs.keys()).index(mbti_result) if mbti_result in mbti_jobs else 0)

# 결과 출력
if selected_mbti:
    st.markdown(f"## 🎯 {selected_mbti}에게 어울리는 직업 추천! 💼")
    recommended_jobs = mbti_jobs[selected_mbti]
    for job, desc in recommended_jobs:
        st.markdown(f"### {job}\n🔎 {desc}")

    # 랜덤 추가 추천
    st.markdown("---")
    st.markdown("### 🌈 특별 보너스 추천 🎁")
    bonus = random.choice(recommended_jobs)
    st.success(f"{bonus[0]} 는 당신에게 찰떡궁합 직업이에요! ✨\n➡️ {bonus[1]}")

# 하단 장식
st.markdown("""
    <hr>
    <p style='text-align: center;'>
        💡 이 앱은 재미와 흥미를 위한 진로 탐색 도우미입니다 🎈<br>
        by <b>진로쌤 AI</b> 🤖<br>
        🌟 모든 MBTI 유형을 위한 직업 추천 서비스 🌟
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
    .stMarkdown h3 {
        color: #FF1493;
    }
    .stSuccess {
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)
