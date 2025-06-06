import streamlit as st

st.title('나의 첫 streamlit 프로젝트!')
st.write('Hello streamlit')

import streamlit as st
import random

# MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": [
        ("🧠 데이터 과학자", "빅데이터를 분석해 인사이트를 도출하는 전문가입니다. 논리적 사고에 강한 INTJ에게 딱 맞아요!"),
        ("📈 전략 컨설턴트", "기업의 방향성을 설계하고 문제를 해결하는 고난이도 직업입니다."),
        ("🔬 연구 과학자", "새로운 이론과 기술을 탐구하며 지적 만족을 느낄 수 있어요.")
    ],
    "INTP": [
        ("👨‍💻 소프트웨어 엔지니어", "복잡한 문제를 구조적으로 해결하는 데 강한 INTP에게 어울리는 직업입니다."),
        ("🔍 데이터 분석가", "숫자와 논리를 활용해 통찰을 제공하는 직업입니다."),
        ("🧪 실험 연구원", "호기심이 많고 탐구적인 성향을 살릴 수 있어요.")
    ],
    "ENTJ": [
        ("🧑‍💼 CEO", "비전을 제시하고 팀을 이끄는 강력한 리더십 직업입니다."),
        ("⚖️ 경영 컨설턴트", "문제를 진단하고 해결책을 제시하는 지적인 도전이 있는 직업이에요."),
        ("🏛️ 기획 관리자", "조직 전체의 전략을 수립하고 운영하는 중추 역할을 합니다.")
    ],
    "ENTP": [
        ("🎙️ 방송인", "말솜씨와 센스로 사람을 사로잡는 직업입니다."),
        ("💡 혁신 컨설턴트", "새로운 아이디어와 창의력을 요구하는 직업이에요."),
        ("🧑‍💻 IT 창업가", "새로운 기술을 이용해 세상을 바꾸는 데 도전해보세요.")
    ],
    "INFJ": [
        ("🧑‍🏫 상담사", "타인의 감정을 이해하고 치유할 수 있는 직업입니다."),
        ("📖 작가", "깊은 통찰과 감성을 글로 풀어낼 수 있어요."),
        ("🎨 예술가", "자신만의 세계를 예술로 표현할 수 있어요.")
    ],
    "INFP": [
        ("🎨 일러스트레이터", "감성적이고 창의적인 표현을 할 수 있는 직업입니다."),
        ("📚 시인/소설가", "감정을 섬세하게 표현하고 싶은 INFP에게 잘 맞아요."),
        ("🌿 환경운동가", "자신의 신념을 따라 사회를 변화시키는 직업입니다.")
    ],
    "ENFJ": [
        ("🎓 교육자", "학생을 이끌고 성장시키는 데 기쁨을 느낄 수 있는 직업이에요."),
        ("🎤 연설가", "사람들의 마음을 움직이는 말솜씨로 세상을 바꿔보세요."),
        ("🫶 NGO 활동가", "사회를 더 나은 방향으로 이끄는 데 힘이 되는 직업입니다.")
    ],
    "ENFP": [
        ("🎬 영화 감독", "자유로운 상상력을 영상으로 표현할 수 있어요."),
        ("📣 마케팅 기획자", "사람들의 관심을 끌고 아이디어를 실현할 수 있는 직업입니다."),
        ("🌎 여행 가이드", "사람들과 함께 즐겁고 역동적인 삶을 살아보세요.")
    ],
    "ISTJ": [
        ("📊 회계사", "정확성과 신뢰가 중요한 직업입니다."),
        ("⚖️ 법무사", "질서와 체계를 중시하는 성격에 잘 맞는 직업입니다."),
        ("🏢 공무원", "규칙과 체계를 기반으로 일하는 데 적합해요.")
    ],
    "ISFJ": [
        ("👩‍⚕️ 간호사", "타인을 돌보는 따뜻한 직업입니다."),
        ("🏫 초등 교사", "아이들의 성장을 돕는 데 보람을 느낄 수 있어요."),
        ("💼 인사 관리자", "조직 내 구성원들의 삶의 질을 챙기는 직업이에요.")
    ],
    "ESTJ": [
        ("🏦 은행원", "책임감 있고 체계적인 성격을 살릴 수 있어요."),
        ("🚔 경찰관", "질서를 유지하고 사회를 지키는 직업입니다."),
        ("🏛️ 관리자", "조직을 효율적으로 이끄는 데 능력이 발휘돼요.")
    ],
    "ESFJ": [
        ("👩‍🏫 학원 강사", "사람들과 가까이에서 소통하고 도움을 주는 직업이에요."),
        ("👨‍🍳 요리사", "맛과 감정을 나눌 수 있는 직업이에요."),
        ("👨‍👩‍👧‍👦 복지사", "사람들의 삶을 따뜻하게 만들어주는 역할입니다.")
    ],
    "ISTP": [
        ("🔧 자동차 정비사", "기계와 손을 다루는 데 능한 사람에게 딱이에요."),
        ("🧗‍♂️ 탐험가", "새로운 것을 직접 체험하고 싶은 성향을 만족시킬 수 있어요."),
        ("👨‍🔬 기술 엔지니어", "논리적 사고로 구조와 시스템을 파악하는 데 적합해요.")
    ],
    "ISFP": [
        ("🎼 음악가", "감성과 창의성을 음악으로 표현할 수 있어요."),
        ("🎨 패션 디자이너", "아름다움을 창조하고 표현할 수 있는 직업이에요."),
        ("🧁 제과제빵사", "손재주와 섬세함을 살릴 수 있는 직업입니다.")
    ],
    "ESTP": [
        ("🚀 스타트업 창업자", "모험과 도전을 즐기는 성향에 맞는 직업입니다."),
        ("💼 세일즈 매니저", "사람과 빠르게 소통하며 성과를 내는 데 뛰어난 능력을 발휘할 수 있어요."),
        ("📦 물류 관리자", "효율적이고 실용적인 성격에 잘 어울리는 직업이에요.")
    ],
    "ESFP": [
        ("🎤 가수", "사람 앞에서 빛나는 에너지를 발산할 수 있어요."),
        ("🎬 배우", "감정과 표현을 무대 위에서 자유롭게 펼칠 수 있는 직업입니다."),
        ("🎡 이벤트 플래너", "사람들과 함께 즐거운 추억을 만드는 일을 해보세요.")
    ]
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
