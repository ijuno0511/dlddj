import streamlit as st 

# 포지션별 농구화 추천 데이터
shoe_recommendations = {
    "가드":("NIKE JA 1","경량, 민첩성, 피팅, 낮은 지상고, 우수한 트랙션"),("NIKE KOBE PROTRO 5 6","경량, 민첩성, 우수한 트랙션, 낮은 지상고, 우수한 피팅"),("ANTA KAI 1 SPEED","민첩성, 내구성, 피팅"),("NIKE SABRINA 2", "경량, 민첩성, 우수한 트랙션, 낮은 지상고, 피팅"),("Asics Gelburst,Gell hoop series","민첩성, 내구성, 피팅, 발목 지지력, 매우 낮은 지상고, 우수한 트랙션") 
    "슈팅가드": ("Anta KT 10", "균형 잡힌 쿠셔닝, 내구성, 다용도 성능"),("UNDER ARMOUR CURRY SERIES")
    "스몰포워드": ("Nike LeBron 21", "높은 발목 지지력, 푹신한 쿠셔닝, 우수한 트랙션")
    "파워포워드": ("361° AG 5", "견고한 구조, 반응성 있는 쿠셔닝, 안정성"),("Nike LeBron 21", "높은 발목 지지력, 푹신한 쿠셔닝, 우수한 트랙션")
    "센터": ("361° Joker 1", "높은 발목 지지력, 충격 흡수, 내구성 있는 아웃솔")
    "전 포지션":("LINING WAY OF WADE 10","경량, 민첩성, 탄력성, 쿠션, 우수한 트랙션, 우수한 피팅"),("LINING WAY OF WADE 808 5","경량, 민첩성, 탄력성, 쿠션, 우수한 트랙션, 우수한 피팅"),("Nike GT Cut 3", "경량, 민첩성, 쿠션, 우수한 트랙션")
}

# 앱 제목
st.title("농구 포지션별 농구화 추천")

# 사용자로부터 포지션 입력 받기
position = st.selectbox("당신의 포지션을 선택하세요:", list(shoe_recommendations.keys()))

# 선택된 포지션에 맞는 농구화 추천 정보 표시
if position:
    shoe, features = shoe_recommendations[position]
    st.subheader(f"추천 농구화: {shoe}")
    st.write(f"주요 특징: {features}")
