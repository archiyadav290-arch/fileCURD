from pathlib import Path
import os
import streamlit as st

st.set_page_config(page_title="File Manager", layout="centered")

st.title("📁 File & Folder Manager")


# ---------------- HELPER FUNCTION ---------------- #

def get_all_items():
    p = Path(".")
    return list(p.rglob("*"))


# ---------------- SIDEBAR ---------------- #

option = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder",
    ]
)

st.sidebar.subheader("Current Files & Folders")

items = get_all_items()

for item in items:
    st.sidebar.write(item)


# ---------------- CREATE FILE ---------------- #

if option == "Create File":

    st.header("Create File")

    file_name = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create File"):

        p = Path(file_name)

        if p.exists():
            st.error("File already exists!")

        else:
            with open(file_name, "w") as file:
                file.write(content)

            st.success("File created successfully!")


# ---------------- READ FILE ---------------- #

elif option == "Read File":

    st.header("Read File")

    file_name = st.text_input("Enter file name")

    if st.button("Read File"):

        p = Path(file_name)

        if p.exists():

            with open(file_name, "r") as file:
                st.text(file.read())

        else:
            st.error("File not found!")


# ---------------- UPDATE FILE ---------------- #

elif option == "Update File":

    st.header("Update File")

    file_name = st.text_input("Enter file name")

    update_option = st.radio(
        "Choose update type",
        ["Overwrite", "Append"]
    )

    content = st.text_area("Enter new content")

    if st.button("Update File"):

        p = Path(file_name)

        if p.exists():

            if update_option == "Overwrite":

                with open(file_name, "w") as file:
                    file.write(content)

            else:

                with open(file_name, "a") as file:
                    file.write(content)

            st.success("File updated successfully!")

        else:
            st.error("File does not exist!")


# ---------------- DELETE FILE ---------------- #

elif option == "Delete File":

    st.header("Delete File")

    file_name = st.text_input("Enter file name")

    if st.button("Delete File"):

        p = Path(file_name)

        if p.exists():

            os.remove(p)

            st.success("File deleted!")

        else:
            st.error("File does not exist!")


# ---------------- RENAME FILE ---------------- #

elif option == "Rename File":

    st.header("Rename File")

    old_name = st.text_input("Enter current file name")

    new_name = st.text_input("Enter new file name")

    if st.button("Rename File"):

        p = Path(old_name)

        if p.exists():

            p.rename(new_name)

            st.success("File renamed successfully!")

        else:
            st.error("File not found!")


# ---------------- CREATE FOLDER ---------------- #

elif option == "Create Folder":

    st.header("Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        p = Path(folder_name)

        if p.exists():
            st.error("Folder already exists!")

        else:
            p.mkdir()

            st.success("Folder created successfully!")


# ---------------- DELETE FOLDER ---------------- #

elif option == "Delete Folder":

    st.header("Delete Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists():

            p.rmdir()

            st.success("Folder deleted!")

        else:
            st.error("Folder not found!")
            