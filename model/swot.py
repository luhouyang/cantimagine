
import streamlit as st


def extract_swot(text):
    import re
    # Define the possible headers for each SWOT category
    categories = ['Strengths', 'Weaknesses', 'Opportunities', 'Threats']
    # Use regular expressions to find these categories
    pattern = '|'.join([f'({cat}):' for cat in categories])
    # Find all matches and their indices
    matches = list(re.finditer(pattern, text))

    # Extract sections based on found indices
    swot_data = {}
    for i, match in enumerate(matches):
        start = match.end()
        # Determine end by the next match or end of text
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        # The current category without the colon
        current_category = match.group()[:-1]
        # Extract and clean the content
        content = text[start:end].strip()
        items = [line.strip() for line in content.split('\n') if line.strip()]
        swot_data[current_category] = items

    return swot_data


def create_swot_chart(swot_data):
    # Create two columns for Strengths/Weaknesses and Opportunities/Threats
    col1, col2 = st.columns(2)

    with col1:
        container1 = st.container(height=200, border=True)
        with container1:
            st.subheader("Strengths")
            # Check if category exists in data to avoid key errors
            if "Strengths" in swot_data:
                for item in swot_data["Strengths"]:
                    st.text(f"- {item}")

        container2 = st.container(height=200, border=True)
        with container2:
            st.subheader("Weaknesses")
            if "Weaknesses" in swot_data:
                for item in swot_data["Weaknesses"]:
                    st.text(f"- {item}")

    with col2:
        container3 = st.container(height=200, border=True)
        with container3:
            st.subheader("Opportunities")
            if "Opportunities" in swot_data:
                for item in swot_data["Opportunities"]:
                    st.text(f"- {item}")

        container4 = st.container(height=200, border=True)
        with container4:

            st.subheader("Threats")
            if "Threats" in swot_data:
                for item in swot_data["Threats"]:
                    st.text(f"- {item}")
