import streamlit as st

# 심리 상태 리스트
emotion_list = {
    "불안 😰": {
        "msg": "마음이 불안할 땐 깊은 숨을 들이쉬고 천천히 내쉬어 보세요 🧘‍♀️",
        "music": "https://www.youtube.com/watch?v=2OEL4P1Rz04",  # 잔잔한 명상음악
        "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb"  # 자연 이미지
    },
    "우울 😔": {
        "msg": "괜찮아요. 당신의 감정은 소중해요. 🌈 혼자가 아니에요.",
        "music": "https://www.youtube.com/watch?v=G0IBqtvZKvk",  # 따뜻한 음악
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
    },
    "분노 😡": {
        "msg": "화를 참기보단, 조용한 공간에서 감정을 흘려보내 보세요 🌬️",
        "music": "https://www.youtube.com/watch?v=IQ3G5QH9zek",
        "image": "https://images.unsplash.com/photo-1483794344563-d27a8d18014e"
    },
    "지루함 😑": {
        "msg": "새로운 취미에 도전해보는 건 어때요? 🎨 혹은 산책도 좋아요!",
        "music": "https://www.youtube.com/watch?v=5qap5aO4i9A",  # Lo-fi
        "image": "https://images.unsplash.com/photo-1508780709619-79562169bc64"
    },
    "외로움 😢": {
        "msg": "세상 어딘가엔 당신을 기다리는 사람이 있어요 💌",
        "music": "https://www.youtube.com/watch?v=1ZYbU82GVz4",
        "image": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e"
    },
    # 👇 여기에 나머지 11가지 감정도 유사하게 추가할 수 있어요
}

# Streamlit 페이지 설정
st.set_page_config(page_title="감정 힐링 가이드 🌿", page_icon="🧠", layout="centered")

# 타이틀 영역
st.markdown("""
    <h1 style='text-al

