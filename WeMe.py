import streamlit as st
import base64
import os

# --- Page Configuration ---
# st.set_page_config(page_title="WeMe", page_icon="", layout="wide")
st.set_page_config(
    page_title="WeMe",
    page_icon="https://github.com/Abdullah5590/WeMe_Streamlit/blob/main/1.png",  # Path to your logo file
    layout="wide"
)

# --- Custom CSS for Rolls-Royce Theme ---
st.markdown("""
    <style>
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background:#000000;
            backdrop-filter: blur(6px);
            padding-top: 0 !important;
        }
        /* Logo container */
        .sidebar-logo {
            display: flex;
            align-items: center;
            justify-content: flex-start;
            border-bottom: 1px solid rgba(255,255,255,0.2);
            padding: 10px 0;
        }
        /* Logo image */
        .sidebar-logo img {
            width: 80px;
            border-radius: 50%;
            border: 2px solid #2bafe0;
            box-shadow: #2bafe0;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .sidebar-logo img:hover {
            transform: scale(1.1) rotate(3deg);
            box-shadow: 0px 0px 20px #2bafe0;
        }
        /* Sidebar text styles */
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span {
            color: white !important;
            # font-family: 'Trebuchet MS', sans-serif;
            font-weight: 800;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.6);
            letter-spacing: 1px;
        }
        /* Radio button container spacing */
        .stRadio > div[role="radiogroup"] > label {
            margin-bottom: 12px;
            padding: 6px 0;
            color:#2bafe0;
        }
        /* Gold arrow radio button */
        .stRadio input[type="radio"] {
            appearance: none;
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background-color: #D4AF37;
            background-image: url("data:image/svg+xml;utf8,<svg fill='white' height='14' width='14' viewBox='0 0 24 24'><path d='M8.59 16.59 13.17 12 8.59 7.41 10 6l6 6-6 6z'/></svg>");
            background-repeat: no-repeat;
            background-position: center;
            background-size: 12px;
            cursor: pointer;
            border: 2px solid #D4AF37;
            color:#2bafe0;
        }
        .stRadio input[type="radio"]:checked {
       color:#2bafe0;
            background-color: #FFD700;
            border: 2px solid #FFD700;
        }
        /* Main content background */
        [data-testid="stAppViewContainer"] {
            background-color: #000000;
        }
        /* Global text color */
        body, h1, h2, h3, h4, h5, h6, p, div, span, label {
            color: white !important;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
        }
        /* Project cards */
        .scroll-container {
            display: flex;
            overflow-x: auto;
            padding: 10px;
            gap: 20px;
            scroll-behavior: smooth;
        }
        .project-card {
            flex: 0 0 auto;
            width: 300px;
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            padding: 10px;
            text-align: center;
            transition: transform 0.2s ease;
            text-decoration: none;
            color: inherit;
        }
        .project-card:hover {
            transform: scale(1.05);
        }
        .project-img {
            width: 100%;
            border-radius: 10px;
        }
        .project-title {
            font-size: 18px;
            font-weight: bold;
            margin-top: 8px;
            color: #333;
        }
        .project-desc {
            font-size: 14px;
            color: #666;
            margin-top: 5px;
        }
        .scroll-container::-webkit-scrollbar {
            display: none;
        }
        .scroll-container {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
        .project-card {
    flex: 0 0 auto;
    width: 300px;
    background-color: #adadad; /* changed from white to yellow/gold */
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    padding: 10px;
    text-align: center;
    transition: transform 0.2s ease;
    text-decoration: none !important;
    color: inherit;

}

    </style>
""", unsafe_allow_html=True)

# --- Helper: Convert Image to Base64 ---
def image_to_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f"data:image/{path.split('.')[-1]};base64,{base64.b64encode(f.read()).decode()}"
    return path  # If it's already a URL

# --- Sidebar Logo ---
logo_path = "https://github.com/Abdullah5590/WeMe_Streamlit/blob/main/1.png"
logo_base64 = image_to_base64(logo_path)
st.sidebar.markdown(
    f"""
    <div class="sidebar-logo">
        <img src="{logo_base64}" alt="Logo">
    </div>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Navigation ---
menu = st.sidebar.radio("", ("Home", "Research","About US","Contact US"))
# st.sidebar.markdown("👤 [Portfolio](https://ashburn.webariansoftwares.com/)")
st.sidebar.markdown(
    """
    <style>
    .bottom-link {
        position: absolute;
        bottom: -280px;
        width: 100%;
        color: white;
        font-size: 25px;
    }
    .bottom-link a {
        color: white;
        text-decoration: none;
    }
    </style>
   <div class="bottom-link">
  <span style="color:#2bafe0;">🧑‍💻</span> <a href="https://abd14k.my.canva.site/portfolio" target="_blank">Portfolio</a>
</div>
    """,
    unsafe_allow_html=True
)

# --- Page Content Logic ---
if menu == "Home":
    st.header("Model1, Model2")
    st.write("✨ Coming Soon........")

elif menu == "About US":
    st.header("ℹ About Me")
    st.write(
        "Energetic and innovative Generative AI Engineer with a strong background in AI, "
        "specializing in vector databases, frameworks, and cloud deployments. "
        "Passionate about applying technical expertise and creativity to develop "
        "cutting-edge AI solutions within a dynamic team environment."
    )

    cards_html = """
    <style>
    .card {
        background-color: #000;  /* bright red */
        color: white;
        padding: 15px 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow:0 1px 4px #00baff;
        transition: transform 0.2s ease;
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        cursor: pointer;
    }
    </style>

    <div class="card">
      <h3>💻 Programming Languages</h3>
      <p>C++, PHP, Python 🐍</p>
    </div>

    <div class="card">
      <h3>🧰 Frameworks & Tools</h3>
      <p>TensorFlow, PyTorch, LangChain, Streamlit, Flask, Laravel, Docker 🐳</p>
    </div>

    <div class="card">
      <h3>🤖 Generative AI Tech</h3>
      <p>LLaMA 2, Mistral, OpenAI</p>
    </div>

    <div class="card">
      <h3>🗃️ Vector Databases</h3>
      <p>ChromaDB, Pinecone</p>
    </div>

    <div class="card">
      <h3>🛢️ DBMS</h3>
      <p>MySQL, Cassandra</p>
    </div>

    <div class="card">
      <h3>☁️ Deployment Platforms</h3>
      <p>AWS, Azure, Hugging Face</p>
    </div>

    <div class="card">
      <h3>🧠 AI/ML Techniques</h3>
      <p>Fine-tuning, vector embeddings, NLP</p>
    </div>

    <div class="card">
      <h3>💡 Soft Skills</h3>
      <p>Analytical thinking, Problem-solving, Communication, Agile methodology</p>
    </div>
    """

    st.markdown(cards_html, unsafe_allow_html=True)


elif menu == "Research":
    st.header("📄 Research Papers")
    st.write("Stay tuned for my upcoming research publications.")

# elif menu == "Contact US":
#     st.header("📄 Contact US")
#     st.write("Stay tuned for my upcoming research publications.")

elif menu == "Contact US":
    # Custom CSS for background + hover effects
    st.markdown("""
        <style>
        /* Contact Section Background */
        .contact-section {
            padding: 20px;
            border-radius: 10px;
        }
        /* Buttons */
        .contact-btn {
            display: inline-block;
            padding: 10px 20px;
            border-radius: 6px;
            font-size: 21px;
            cursor: pointer;
            text-decoration: none !important; /* remove underline */
            border: none;
            transition: all 0.3s ease;
            color: white !important; /* text white */
        }
        .call-btn, .email-btn {
            background-color: #000000;
        }
        /* Hover effects for buttons */
        .call-btn:hover, .email-btn:hover {
            background-color: #2bafe0;
            transform: scale(1.05);
        }
        /* Form fields */
        .stTextInput>div>div>input,
        .stTextArea>div>textarea {
            border-radius: 6px;
            border: 2px solid #ccc;
            transition: all 0.3s ease;
        }
        /* Hover & focus effects for form fields */
        .stTextInput>div>div>input:hover,
        .stTextArea>div>textarea:hover {
            border-color: #adadad;
        }
        .stTextInput>div>div>input:focus,
        .stTextArea>div>textarea:focus {
            border-color: #adadad;
            outline: none;
        }
        /* Submit button style */
        div.stFormSubmitButton>button {
            background-color:#adadad !important; /* yellow */
            color: black !important;
            border-radius: 6px;
            padding: 8px 21px;
            border: none;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        div.stFormSubmitButton>button:hover {
            transform: scale(1.05);
              background-color: #2bafe0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Section start
    st.markdown('<div class="contact-section">', unsafe_allow_html=True)

    st.header("📄 Contact US")
    st.write("Feel free to reach out to me through any of the following methods:")

    # Contact Buttons
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<a href="tel:+918175806100" class="contact-btn call-btn">📞 Call Me</a>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<a href="mailto:5590azmi@gmail.com" class="contact-btn email-btn">📮 Email Me</a>',
            unsafe_allow_html=True
        )

    st.markdown("<hr>", unsafe_allow_html=True)

    # Contact Form
    st.subheader("Or send me a message here:")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Send Message 📤")
        if submitted:
            if not name or not email or not message:
                st.error("Please fill in all fields.")
            else:
                st.success("✅ Thank you for reaching out! I will get back to you soon.")

    st.markdown("</div>", unsafe_allow_html=True)













