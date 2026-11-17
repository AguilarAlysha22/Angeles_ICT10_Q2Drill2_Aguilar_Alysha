from pyscript import document

grade7 = {
    "Isabella Hizon",
    "Ji Hyun Kim",
    "Caela Regulacion",
    "Pearl Sumbillo"
}

grade8 = {
    "Dezzarae Almirol",
    "Gabriel Ferrer",
    "Ji Won Son",
    "Miko Alvis"
}

grade9 = {
    "Kean Lardizabal",
    "Aubrey Cabrera",
    "Marteena David",
    "Princess Arucan"
}

grade10 = {
    "Alysha Aguilar",
    "Megan Tan",
    "Raji Santos",
    "Lucas Tanglao"
}

new_members = set()

def add_member(event):
    first = document.getElementById("first_name").value.strip().title()
    last = document.getElementById("last_name").value.strip().title()

    full_name = first + " " + last

    new_members.add(full_name)

    all_members = grade7 | grade8 | grade9 | grade10 | new_members

    member_list = "<br>".join(sorted(all_members))
    total = len(all_members)

    document.getElementById("output").innerHTML = f"""
        All members: <br>
        {member_list}
        <br><br>
        Total members: {total}
    """
        
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""