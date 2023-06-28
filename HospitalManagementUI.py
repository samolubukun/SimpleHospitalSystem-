from tkinter import *
from tkinter import messagebox

class HospitalManagementUI:
    def __init__(self):
        self.patientRecords = []

    def drawLoginUI(self):
        def login():
            username = usernameTextField.get()
            password = passwordField.get()

            if username == "admin" and password == "adminpass":
                loginFrame.destroy()
                self.drawMainMenuUI()
            else:
                messagebox.showerror("Error", "Invalid username or password. Please try again.")
                passwordField.delete(0, END)

        loginFrame = Tk()
        loginFrame.title("Hospital Management System")

        usernameLabel = Label(loginFrame, text="Username:")
        usernameLabel.grid(row=0, column=0, sticky=W)
        usernameTextField = Entry(loginFrame)
        usernameTextField.grid(row=0, column=1)

        passwordLabel = Label(loginFrame, text="Password:")
        passwordLabel.grid(row=1, column=0, sticky=W)
        passwordField = Entry(loginFrame, show="*")
        passwordField.grid(row=1, column=1)

        loginBtn = Button(loginFrame, text="Login", command=login)
        loginBtn.grid(row=2, columnspan=2)

        loginFrame.mainloop()

    def drawMainMenuUI(self):
        def addPatient():
            self.drawAddPatientUI()

        def viewRecords():
            self.drawViewRecordsUI()

        def searchPatient():
            self.drawSearchPatientUI()

        def editRecords():
            self.drawEditRecordsUI()

        def deleteRecord():
            self.drawDeleteRecordUI()

        mainMenuFrame = Tk()
        mainMenuFrame.title("Hospital Management System")

        addPatientBtn = Button(mainMenuFrame, text="Add Patient Records", command=addPatient)
        addPatientBtn.pack()

        viewRecordsBtn = Button(mainMenuFrame, text="View Available Records", command=viewRecords)
        viewRecordsBtn.pack()

        searchPatientBtn = Button(mainMenuFrame, text="Search Patient", command=searchPatient)
        searchPatientBtn.pack()

        editRecordsBtn = Button(mainMenuFrame, text="Edit Records", command=editRecords)
        editRecordsBtn.pack()

        deleteRecordBtn = Button(mainMenuFrame, text="Delete Patient's Record", command=deleteRecord)
        deleteRecordBtn.pack()

        mainMenuFrame.mainloop()

    def drawAddPatientUI(self):
        def savePatient():
            name = nameTextField.get().strip()
            disease = diseaseTextField.get()

            if not name.isalpha():
                messagebox.showerror("Error", "Invalid name. Please enter a valid name.")
                return

            try:
                age = int(ageTextField.get())
                cabinNumber = int(cabinNumberTextField.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid input for age or cabin number. Please enter valid numbers.")
                return

            patient = Patient(name, disease, age, cabinNumber)
            self.patientRecords.append(patient)
            messagebox.showinfo("Success", "Patient record saved successfully.")

            nameTextField.delete(0, END)
            diseaseTextField.delete(0, END)
            ageTextField.delete(0, END)
            cabinNumberTextField.delete(0, END)

        addPatientFrame = Tk()
        addPatientFrame.title("Add Patient Records")

        nameLabel = Label(addPatientFrame, text="Name:")
        nameLabel.grid(row=0, column=0, sticky=W)
        nameTextField = Entry(addPatientFrame)
        nameTextField.grid(row=0, column=1)

        diseaseLabel = Label(addPatientFrame, text="Disease:")
        diseaseLabel.grid(row=1, column=0, sticky=W)
        diseaseTextField = Entry(addPatientFrame)
        diseaseTextField.grid(row=1, column=1)

        ageLabel = Label(addPatientFrame, text="Age:")
        ageLabel.grid(row=2, column=0, sticky=W)
        ageTextField = Entry(addPatientFrame)
        ageTextField.grid(row=2, column=1)

        cabinNumberLabel = Label(addPatientFrame, text="Cabin Number:")
        cabinNumberLabel.grid(row=3, column=0, sticky=W)
        cabinNumberTextField = Entry(addPatientFrame)
        cabinNumberTextField.grid(row=3, column=1)

        savePatientBtn = Button(addPatientFrame, text="Save", command=savePatient)
        savePatientBtn.grid(row=4, columnspan=2)

        addPatientFrame.mainloop()

    def drawViewRecordsUI(self):
        viewRecordsFrame = Tk()
        viewRecordsFrame.title("View Available Records")

        recordsTextArea = Text(viewRecordsFrame)
        recordsTextArea.pack()

        records = ""
        for patient in self.patientRecords:
            records += patient.toString() + "\n"
        recordsTextArea.insert(END, records)

        viewRecordsFrame.mainloop()

    def drawSearchPatientUI(self):
        def search():
            searchName = searchNameTextField.get()
            searchResults = ""

            for patient in self.patientRecords:
                if (patient.getName().lower() == searchName.lower()
                        or patient.getDisease().lower() == searchName.lower()
                        or str(patient.getAge()) == searchName
                        or str(patient.getCabinNumber()) == searchName):
                    searchResults += patient.toString() + "\n"

            if searchResults:
                searchResultsTextArea.config(state=NORMAL)
                searchResultsTextArea.delete(1.0, END)
                searchResultsTextArea.insert(END, searchResults)
                searchResultsTextArea.config(state=DISABLED)
            else:
                searchResultsTextArea.config(state=NORMAL)
                searchResultsTextArea.delete(1.0, END)
                searchResultsTextArea.insert(END, "No matching records found.")
                searchResultsTextArea.config(state=DISABLED)

        searchPatientFrame = Tk()
        searchPatientFrame.title("Search Patient")

        searchNameLabel = Label(searchPatientFrame, text="Name:")
        searchNameLabel.grid(row=0, column=0, sticky=W)
        searchNameTextField = Entry(searchPatientFrame)
        searchNameTextField.grid(row=0, column=1)

        searchBtn = Button(searchPatientFrame, text="Search", command=search)
        searchBtn.grid(row=1, columnspan=2)

        searchResultsTextArea = Text(searchPatientFrame, state=DISABLED)
        searchResultsTextArea.grid(row=2, columnspan=2)

        searchPatientFrame.mainloop()

    def drawEditRecordsUI(self):
        def edit():
            editName = editNameTextField.get()
            messagebox.showerror("Error", "Insufficient Access Level For Editing patient record: " + editName)

        editRecordsFrame = Tk()
        editRecordsFrame.title("Edit Records")

        editNameLabel = Label(editRecordsFrame, text="Name:")
        editNameLabel.grid(row=0, column=0, sticky=W)
        editNameTextField = Entry(editRecordsFrame)
        editNameTextField.grid(row=0, column=1)

        editBtn = Button(editRecordsFrame, text="Edit", command=edit)
        editBtn.grid(row=1, columnspan=2)

        editRecordsFrame.mainloop()

    def drawDeleteRecordUI(self):
        def delete():
            deleteName = deleteNameTextField.get()
            for patient in self.patientRecords:
                if patient.getName().lower() == deleteName.lower():
                    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the patient record?")
                    if confirmation:
                        self.patientRecords.remove(patient)
                        messagebox.showinfo("Success", "Patient record deleted successfully.")
                    deleteRecordFrame.destroy()
                    return

            messagebox.showerror("Error", "Patient not found.")

        deleteRecordFrame = Tk()
        deleteRecordFrame.title("Delete Patient's Record")

        deleteNameLabel = Label(deleteRecordFrame, text="Name:")
        deleteNameLabel.grid(row=0, column=0, sticky=W)
        deleteNameTextField = Entry(deleteRecordFrame)
        deleteNameTextField.grid(row=0, column=1)

        deleteBtn = Button(deleteRecordFrame, text="Delete", command=delete)
        deleteBtn.grid(row=1, columnspan=2)

        deleteRecordFrame.mainloop()


class Patient:
    def __init__(self, name, disease, age, cabinNumber):
        self.name = name
        self.disease = disease
        self.age = age
        self.cabinNumber = cabinNumber

    def getName(self):
        return self.name

    def getDisease(self):
        return self.disease

    def getAge(self):
        return self.age

    def getCabinNumber(self):
        return self.cabinNumber

    def toString(self):
        return "Name: " + self.name + ", Disease: " + self.disease + ", Age: " + str(self.age) + ", Cabin Number: " + str(self.cabinNumber)


if __name__ == "__main__":
    hospitalUI = HospitalManagementUI()
    hospitalUI.drawLoginUI()
