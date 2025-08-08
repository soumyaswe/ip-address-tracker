import streamlit as st
import requests

def get_geolocation(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        data = response.json()
        
        if data.get("status") != "success":
            return {"error": "Invalid IP address or unable to fetch geolocation"}
        
        geolocation = {
            "IP": data.get("query"),
            "City": data.get("city"),
            "State": data.get("regionName"),
            "Country": data.get("country"),
            "Latitude": data.get("lat"),
            "Longitude": data.get("lon"),
            "ISP": data.get("org")
        }
        return geolocation
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}

def get_current_ip():
    try:
        # Using a service like ipify to get the current public IP of the user
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip_data = response.json()
        return ip_data['ip']
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to get current IP: {e}"}

# Streamlit app layout
st.markdown("""
    <style>
        .main-title {
            color: #2a5ef4;
            font-size: 40px;
            font-weight: bold;
        }
        .sub-title {
            color: #32cd32;
            font-size: 30px;
            font-weight: bold;
        }
        .card {
            background-color: #f0f8ff;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .info-title {
            color: #ff1493;
            font-size: 22px;
            font-weight: bold;
        }
        .team-title {
            color: #000000;
            font-size: 25px;
            font-weight: bold;
        }
        .team-member {
            font-size: 18px;
            margin-top: 10px;
            color: #000000;
            font-weight: bold;
        }
        
        .sidebar .sidebar-content .team-member {
            color:#000000;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Current IP
st.markdown("<div class='main-title'>🌍 IP Geolocation Finder 🌎</div>", unsafe_allow_html=True)

# Get the current IP address
current_ip = get_current_ip()
if isinstance(current_ip, str):
    st.markdown(f"### 📡 Your current public IP: {current_ip}")
else:
    st.error(f"Error getting current IP: {current_ip.get('error')}")

st.write("Enter any IP address to find its geolocation 📍:")

# Input widget for custom IP address
ip = st.text_input("IP Address", current_ip)  # Defaulting to the user's IP address

# When the user submits the IP address
if ip:
    location = get_geolocation(ip)
    
    if "error" in location:
        st.error(location["error"])
    else:
        # Creating a colorful two-column layout for geolocation info
        st.markdown(f"<div class='sub-title'>📍 Geolocation for IP: {ip}</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        # Column 1: Location details
        with col1:
            st.markdown(f"<div class='info-title'>🌆 City:</div> {location['City']}", unsafe_allow_html=True)
            st.markdown(f"<div class='info-title'>🏙️ State:</div> {location['State']}", unsafe_allow_html=True)
            st.markdown(f"<div class='info-title'>🌍 Country:</div> {location['Country']}", unsafe_allow_html=True)

        # Column 2: Geographical details
        with col2:
            st.markdown(f"<div class='info-title'>🌐 Latitude:</div> {location['Latitude']}", unsafe_allow_html=True)
            st.markdown(f"<div class='info-title'>🌐 Longitude:</div> {location['Longitude']}", unsafe_allow_html=True)
            st.markdown(f"<div class='info-title'>💻 ISP:</div> {location['ISP']}", unsafe_allow_html=True)

        

# Sidebar for Team Information
with st.sidebar:
    st.markdown("<div class='team-title'>👨‍💻 Project Team 👩‍💻</div>", unsafe_allow_html=True)

    # Team Members with their details
    team_members = [
        {"name": "Smaranika Porel", "college_roll": "CSE2023111", "university_roll": "11700123185"},
        {"name": "Soumya Das", "college_roll": "CSE2023078", "university_roll": "11700123194"},
        {"name": "Soham Kumar Dey", "college_roll": "CSE2023075", "university_roll": "11700123188"},
        {"name": "Sayandeep Banik", "college_roll": "CSE2023077", "university_roll": "11700123173"}
    ]

    # Displaying team members' details in the sidebar
    for member in team_members:
        st.markdown(f"<div class='team-member'>👤 {member['name']}</div> College Roll: {member['college_roll']} | University Roll: {member['university_roll']}", unsafe_allow_html=True)
