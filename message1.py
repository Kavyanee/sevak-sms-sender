import streamlit as st
from twilio.rest import Client

# Streamlit UI
st.title("Sevak SMS Sender 📩")

# Input fields
to_number = st.text_input("Recipient's Phone Number", value="+919603551345")
message_body = st.text_area("Message", value="Welcome to Sevak. For your registration send return message as 1.")

# Twilio credentials (Replace with secure environment variables)
account_sid = 'ACfc50e37304bc2dd1a20183358bf24205'
auth_token = '92f1e4779d2734a30afb3be098434b2c'
from_number = '+18312823486'  # Your Twilio phone number

# Twilio Client
client = Client(account_sid, auth_token)

# Button to send SMS
if st.button("Send SMS 📲"):
    message = client.messages.create(
        from_=from_number,
        body=message_body,
        to=to_number
    )

    if message.sid:
        st.success(f"✅ Message sent successfully! SID: {message.sid}")

        # Clear only the message input field (not the phone number)
        st.session_state["message_body"] = ""

