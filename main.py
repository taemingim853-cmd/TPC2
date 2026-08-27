import streamlit as st
import time

st.set_page_config(page_title="블링블링 투두앱 💖", page_icon="🦄", layout="centered")

st.markdown("""
    <style>
    .title-font {
        background: linear-gradient(to right, #ff9a9e, #fecfef, #a18cd1, #fbc2eb, #8fd3f4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 45px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
    }
    </style>
    <div class="title-font">✨🦄 환상의 블링블링 목표 달성기 🦄✨</div>
    <div class="subtitle">오늘도 반짝반짝 빛나는 하루를 만들어봐요! 🌟💖🎀</div>
    <br>
""", unsafe_allow_html=True)

st.sidebar.header("🎈 환영합니다! 🎈")
st.sidebar.write("오늘의 기분은 어떠신가요? 🥰")
mood = st.sidebar.radio("👇 기분 선택하기", 
                        ["행복해 😆🌸", "열정 가득 🔥🚀", "차분해 😌☕", "완전 파티 기분 🥳🎉"])

st.sidebar.write("---")
st.sidebar.write("🎵 **응원 메시지**")
st.sidebar.success("당신은 할 수 있어요! 🍀")

st.subheader("🌈 오늘의 미션을 적어주세요! ✍️")
todo = st.text_input("👇 여기에 입력하세요 🚀", placeholder="예: 코딩 1시간 하기 💻🔥")

if todo:
    st.info(f"🎯 **앗! 멋진 목표가 생겼네요:** {todo} 🤩🔥")
    
    st.write("---")
    st.write("### 🏃‍♀️ 달성 준비 완료?!")
    is_done = st.checkbox(f"✅ 쨔잔! '{todo}' 미션 클리어하셨나요? 🏆")
    
    if is_done:
        st.success("🎉 와아아아! 오늘도 완벽하게 해내셨군요! 진짜 최고예요! 💖👑💯 폼 미쳤다!! 찢었다!! 🎉")
        
        if "파티" in mood:
            st.balloons()
            time.sleep(0.5)
            st.snow()
        elif "차분해" in mood:
            st.snow()
        else:
            st.balloons()
            
        st.write("---")
        st.markdown("### 🎁 미션 완료 보상 이모지 폭탄 🎁")
        st.write("""
        🍕🍔🍟🌭🍿🥞🧇🧀🥗🥙🥪🌮🌯🍖🍗🥩🍠🥟🥠🥡🍱🍘🍙🍚🍛🍜🍣🍤🍥🥮🍢🍡🍧🍨🍦🥧🧁🍰🎂🍮🍭🍬🍫🍩🍪🍯
        🚀🛸🚁🛶⛵🚤🛥🛳⛴🚢⚓⛽🚧🚦🚥🚏🗺🗿🗽🗼🏰🏯🏟🎡🎢🎠⛲⛱🏖🏝🏜🌋⛰🏔🗻🏕⛺
        🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🦆🦅🦉🦇🐺🐗🐴🦄🐝🐛🦋🐌🐞🐜🕷🕸🐢🐍🦎🦖🦕
        """)
