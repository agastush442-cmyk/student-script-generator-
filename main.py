import streamlit as st

# App ka chehra
st.title("🔥 Student Script Generator")
st.write("अपनी समस्या चुनो और कड़क स्क्रिप्ट ले जाओ!")

# Problems aur Scripts
data = {
    "Padhai mein mann nahi lagta": "ओए! रील छोड़ और किताब उठा, वरना कल पछताएगा!",
    "Sab bhool jata hoon": "रट्टा मत मार, लिख के देख। हाथ चलेगा तो दिमाग खुलेगा!",
    "Exam ka dar": "डर तैयारी की कमी है। अभी पढ़ना शुरू कर, डर अपने आप भाग जाएगा!"
}

option = st.selectbox('Apni problem chuno:', list(data.keys()))

if st.button('Script Generate Karo'):
    st.subheader("Teri Kadhak Script:")
    st.write(f"👉 {data[option]}")
