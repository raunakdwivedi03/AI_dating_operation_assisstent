import streamlit as st
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="AI Dating Operations Assistant",

    page_icon="❤️",
    layout="centered"
)

# ================= CUSTOM CSS (LIGHT PINK DATING UI) =================
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(180deg, #fff1f5 0%, #ffe4ec 100%);
    color: #2b2b2b;
}

/* Title */
.big-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    color: #d6336c;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #6b7280;
    margin-bottom: 30px;
    font-size: 16px;
}

/* Input box */
input {
    background-color: #ffffff !important;
    color: #111111 !important;
    border-radius: 12px !important;
    border: 1px solid #f3b4c8 !important;
    padding: 12px !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #ff4d6d, #ff758f);
    color: white;
    border-radius: 30px;
    padding: 10px 28px;
    font-weight: 600;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #ff758f, #ff4d6d);
}

/* Cards */
.card {
    background-color: #ffffff;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #ffd1dc;
    box-shadow: 0 8px 20px rgba(255, 105, 135, 0.15);
}

/* Final response text */
.response {
    font-size: 18px;
    line-height: 1.7;
    color: #333333;
}

/* Expanders */
.streamlit-expanderHeader {
    background-color: #fff0f6;
    border-radius: 10px;
    font-weight: 600;
    color: #c2255c;
}

/* Success box */
.stAlert-success {
    background-color: #e6fcf5;
    border-left: 6px solid #38d9a9;
}

/* Hide footer */
footer {
    visibility: hidden;
}
/* 🔧 Input label text (dark) */
label {
    color: #8a1c3a !important;
    font-weight: 600;
}

/* 🔧 Placeholder text (dark & readable) */
::placeholder {
   
    opacity: 1;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown('<div class="big-title">❤️ AI Dating Operations Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Smart AI assistant for dating bios & relationship prompts</div>',
    unsafe_allow_html=True
)
st.markdown("---")

# ================= INPUT =================
user_input = st.text_input(
    "💬 Describe yourself or your dating need",
    placeholder="25 year old confident man who likes fitness and travel"
)

# ================= BUTTON =================
run = st.button("🚀 Generate Dating Bio")

# ================= MAIN LOGIC =================
if run:
    if user_input.strip() == "":
        st.warning("Please enter something about yourself 🙂")
        st.stop()

    # -------- Planner --------
    with st.spinner("🧠 Planning your request..."):
        planner = PlannerAgent()
        plan = planner.create_plan(user_input)

    # -------- Executor --------
    with st.spinner("🤖 Writing your dating bio..."):
        executor = ExecutorAgent()
        execution_result = executor.execute(plan)

    # -------- Verifier --------
    verifier = VerifierAgent()
    final_result = verifier.verify(execution_result)

    # -------- Debug Sections --------
    with st.expander("📋 View Execution Plan"):
        st.json(plan)

    with st.expander("⚙️ View Execution Result"):
        st.json(execution_result)

    # -------- Final Output --------
    st.markdown("---")
    st.success("✨ Bio Generated Successfully!")

    st.markdown(
        f"""
        <div class="card">
            <div class="response">
                {final_result["final_response"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("Made with ❤️ for dating applications")
