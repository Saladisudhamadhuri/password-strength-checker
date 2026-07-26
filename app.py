import streamlit as st
import re
import random
import string

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# ----------------------------
# Common Passwords
# ----------------------------
common_passwords = [
    "123456",
    "password",
    "123456789",
    "qwerty",
    "admin",
    "welcome",
    "abc123",
    "password123"
]

# ----------------------------
# Crack Time
# ----------------------------


def estimate_crack_time(score):
    if score == 5:
        return "Hundreds of years"
    elif score == 4:
        return "Several years"
    elif score == 3:
        return "Few months"
    elif score == 2:
        return "Few days"
    else:
        return "Few seconds"

# ----------------------------
# Password Generator
# ----------------------------


def generate_password(length=12):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )
    return ''.join(random.choice(characters) for _ in range(length))


# ----------------------------
# UI
# ----------------------------
st.title("🔐 Password Strength Checker")
st.write("Check the strength of your password instantly.")

password = st.text_input(
    "Enter your password",
    type="password"
)

if st.button("Analyze Password"):

    if password == "":
        st.warning("Please enter a password.")

    elif password.lower() in common_passwords:
        st.error("🚨 Extremely Common Password!")
        st.write("This password is very easy to crack.")

    else:

        strength = 0

        feedback = []

        if len(password) >= 8:
            strength += 1
        else:
            feedback.append("Minimum 8 characters")

        if re.search(r"[A-Z]", password):
            strength += 1
        else:
            feedback.append("Add an uppercase letter")

        if re.search(r"[a-z]", password):
            strength += 1
        else:
            feedback.append("Add a lowercase letter")

        if re.search(r"[0-9]", password):
            strength += 1
        else:
            feedback.append("Add a number")

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            strength += 1
        else:
            feedback.append("Add a special character")

        st.subheader(f"Password Score: {strength}/5")

        st.progress(strength / 5)

        if strength == 5:
            st.success("✅ Strong Password")

        elif strength >= 3:
            st.warning("⚠️ Medium Password")

        else:
            st.error("❌ Weak Password")

        st.info(f"Estimated Crack Time: {estimate_crack_time(strength)}")

        if feedback:
            st.subheader("Suggestions")
            for item in feedback:
                st.write("•", item)

        st.subheader("Suggested Strong Password")
        st.code(generate_password())
