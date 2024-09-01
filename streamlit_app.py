# streamlit_app.py
import streamlit as st
from pdf_creator import generate_pdf
from io import BytesIO

st.title("PDF Generator")

if 'participants' not in st.session_state:
    st.session_state.participants = []

with st.form(key='pdf_form'):
    to_line_1 = st.text_input("To Line 1")
    to_line_2 = st.text_input("To Line 2")
    subject = st.text_input("Subject")
    respected = st.text_input("Respected")
    start_time = st.text_input("Start Time")
    end_time = st.text_input("End Time")
    sincerely = st.text_input("Sincerely")
    sincerely_post = st.text_input("Sincerely (Post)")
    event_name = st.text_input("Event Name")
    event_date = st.date_input("Event Date")

    submit_button = st.form_submit_button("Generate PDF")

with st.form(key='participant_form', clear_on_submit=True):
    st.write("Participants")
    name = st.text_input("Name")
    branch = st.text_input("Branch")
    roll_number = st.text_input("Roll Number")
    add_participant_button = st.form_submit_button("Add Participant")
    
    if add_participant_button and name and branch and roll_number:
        st.session_state.participants.append({
            'name': name,
            'branch': branch,
            'roll_number': roll_number
        })
        st.success("Participant added successfully!")

st.write("Current Participants:")
for participant in st.session_state.participants:
    st.write(f"Name: {participant['name']}, Branch: {participant['branch']}, Roll Number: {participant['roll_number']}")

if submit_button:
    data = {
        'to_line_1': to_line_1,
        'to_line_2': to_line_2,
        'subject': subject,
        'respected': respected,
        'start_time': start_time,
        'end_time': end_time,
        'sincerely': sincerely,
        'sincerely_post': sincerely_post,
        'event_name': event_name,
        'event_date': event_date.strftime('%Y-%m-%d'),
        'participants': st.session_state.participants
    }
    pdf_output = generate_pdf(data)
    st.success("PDF generated successfully!")
    st.download_button(
        label="Download PDF",
        data=pdf_output,
        file_name="generated_document.pdf",
        mime="application/pdf"
    )
