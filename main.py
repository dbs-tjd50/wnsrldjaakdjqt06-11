import streamlit as st

# 👉 MBTI별 직업 추천 딕셔너리
mbti_jobs = {
    "INTJ 🧠": ["🔬 데이터 과학자", "📊 전략 컨설턴트", "🧪 연구원"],
    "INFP 🌸": ["📝 작가", "🎨 예술가", "🧘‍♀️ 심리 상담사"],
    "ENTP ⚡": ["💡 창업가", "🎤 마케터", "📣 방송인"],
    "ISFJ 🛡️": ["👩‍🏫 교사", "👩‍⚕️ 간호사", "🧑‍💼 사무직"],
    "ESFP 🎉": ["🎭 배우", "🎧 DJ", "🧑‍🍳 요리사"],
    "ESTJ 🏆": ["🏛️ 공무원", "🗂️ 관리자", "⚖️ 법조인"],
    # 더 많은 유형은 원하시면 확장 가능
}

# 🎨 Streamlit 설정
st.set_page_config(page_title="MBTI 진로 추천기 💼", page_icon="🌟", layout="centered")

# 💖 타이틀 & 설명
st.markdown("""
    <h1 style='text-align: center; color: #FF69B4;'>✨ MBTI 진로 추천기 💼</h1>
    <h3 style='text-align: center; color: #9370DB;'>당신의 성격에 딱 맞는 직업을 찾아보세요!</h3>
    <p style='text-align: center;'>🌈 MBTI 유형을 선택하면 어울리는 직업을 추천해드릴게요. 인생은 너무 짧아요! 자신에게 맞는 길을 찾아 떠나보세요! 🌟</p>
    """, unsafe_allow_html=True)

# 🎯 사용자 MBTI 선택
mbti_types = list(mbti_jobs.keys())
selected_mbti = st.selectbox("📌 MBTI 유형을 선택하세요:", mbti_types)

# 📌 결과 출력
if selected_mbti:
    st.markdown("---")
    st.markdown(f"<h2 style='color:#00BFFF;'>💡 {selected_mbti} 유형에게 어울리는 직업</h2>", unsafe_allow_html=True)
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"<h4 style='color:#FFD700;'>👉 {job}</h4>", unsafe_allow_html=True)

    st.markdown("""
    <br>
    <div style='text-align: center; font-size: 18px;'>
        🎯 <b>자신의 성격을 이해하는 것</b>은 멋진 진로를 여는 첫걸음이에요!<br>
        🌟 지금부터 당신만의 길을 찾아보세요!
    </div>
    """, unsafe_allow_html=True)

# 🌟 푸터
st.markdown("""
    <br><br>
    <hr>
    <p style='text-align: center; font-size: 14px;'>Made with ❤️ by 미래교육랩</p>
    """, unsafe_allow_html=True)
