from pyscript import document


clubs = {
    "Math Club": {
        "name": "Math Club",
        "description": "A club for math  enthusiasts of all skill levels.",
        "meeting_time": "Every Monday 2:30-5:00 PM",
        "location": "Room 705",
        "moderator": "Mr. Ferma",
        "members": 20,
        "category": "Academic"
    },
    "Science Club": {
        "name": "Science Club",
        "description": "Experiments, discoveries, and exciting science activities.",
        "meeting_time": "Mondays & Thursdays 4:00-5:30 PM",
        "location": "Laboratory 1",
        "moderator": "Mr. Alanano",
        "members": 10,
        "category": "Academic"
    },
    "Art Club": {
        "name": "Art Club",
        "description": "A creative space for drawing, painting, and crafts.",
        "meeting_time": "Fridays 3:00-5:00 PM",
        "location": "Art Room (403)",
        "moderator": "Ms. Suarez",
        "members": 25,
        "category": "Arts"
    },
    "Social Science Club": {
        "name": "Social Science Club",
        "description": "turn curiosity into action and spark change in their community. Explore history, politics, culture, and current issues while developing skills that shape both thought and action beyond the classroom!",
        "meeting_time": "Every Tuesday 2:00-4:00 PM",
        "location": "Room 708",
        "moderator": "Mrs. Libramonte",
        "members": 18,
        "category": "Debating"
    }
}

club_select = document.getElementById("club-select")

for club_name in clubs:
    option = document.createElement("option")
    option.textContent = club_name
    option.value = club_name
    club_select.appendChild(option)

def show_club_information(event=None):
    selected = club_select.value
    club = clubs[selected]

    display_box = document.getElementById("club-info-display")
    display_box.style.display = "block"  # Show the box
    

    info_text = (
        f"{club['name']}\n"
        f"Description: {club['description']}\n"
        f"Meeting Time: {club['meeting_time']}\n"
        f"Location: {club['location']}\n"
        f"Advisor: {club['moderator']}\n"
        f"Number of Members: {club['members']}\n"
        f"Category: {club['category']}\n"
    )

    display_box.textContent = info_text
