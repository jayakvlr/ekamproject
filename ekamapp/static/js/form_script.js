document.addEventListener('DOMContentLoaded', (event) => {
    const forms = ['Desktop', 'Mobile'];
    forms.forEach(formType => {
        console.log("formtype",formType)
        const form = document.getElementById(`registrationForm${formType}`);
        if (!form) return;

        const nameField = form.querySelector('#name');
        const whatsappField = form.querySelector('#whatsapp');
        const ageField = form.querySelector('#age');
        const countryField = form.querySelector('#country');
        const stateDiv = form.querySelector('#state').parentNode;
        const placeField = form.querySelector('#place');
        const genderField = form.querySelector('#gender');

        const nameError = form.querySelector('#nameError');
        const whatsappError = form.querySelector('#whatsappError');
        const ageError = form.querySelector('#ageError');
        const countryError = form.querySelector('#countryError');
        const stateError = form.querySelector('#stateError');
        const placeError = form.querySelector('#placeError');
        const genderError = form.querySelector('#genderError');

        const indiaStates = [
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
            "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
            "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
            "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
            "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
            "Uttar Pradesh", "Uttarakhand", "West Bengal"
        ];

        function updateStateField() {
            if (countryField.value === 'India') {
                stateDiv.innerHTML = `
  
                    <select id="state" name="state" class="form-control form-control-lg">
                        ${indiaStates.map(state => `<option value="${state}" ${state === 'Kerala' ? 'selected' : ''}>${state}</option>`).join('')}
                    </select>`;
            } else {
                stateDiv.innerHTML = `
                    <input type="text" id="state" name="state" class="form-control form-control-lg" placeholder="Enter state">`;
            }
        }

        function validateName() {
            const nameRegex = /^[A-Za-z ]+$/;
            if (!nameField.value.match(nameRegex)) {
                nameError.textContent = "Name must contain only letters and single spaces.";
                return false;
            }
            nameError.textContent = "";
            return true;
        }

        function validateWhatsapp() {
            const whatsappRegex = /^[0-9]{10}$/;
            if (!whatsappField.value.match(whatsappRegex)) {
                whatsappError.textContent = "Whatsapp number must contain only 10 digits.";
                return false;
            }
            whatsappError.textContent = "";
            return true;
        }

        function validateAge() {
            const ageRegex = /^[0-9]+$/;
            if (!ageField.value.match(ageRegex) || ageField.value.length > 2) {
                ageError.textContent = "Age must be a number between 1 and 99.";
                return false;
            }
            ageError.textContent = "";
            return true;
        }

        function validateForm(event) {
            let valid = true;
            if (!validateName()) valid = false;
            if (!validateWhatsapp()) valid = false;
            if (!validateAge()) valid = false;
            if (!validateGender()) valid = false;
            if (!validatePlace()) valid = false;
            if (!validateState()) valid = false;
            if (!validateCountry()) valid = false;
            if (!valid) event.preventDefault();
        }

        function validateGender() {
            if (genderField.value === "") {
                genderError.textContent = "Gender is required.";
                return false;
            }
            genderError.textContent = "";
            return true;
        }

        function validatePlace() {
            if (placeField.value === "") {
                placeError.textContent = "Place is required.";
                return false;
            }
            placeError.textContent = "";
            return true;
        }

        function validateState() {
            const stateField = stateDiv.querySelector('#state');
            if (stateField.value === "") {
                stateError.textContent = "State is required.";
                return false;
            }
            stateError.textContent = "";
            return true;
        }

        function validateCountry() {
            if (countryField.value === "") {
                countryError.textContent = "Country is required.";
                return false;
            }
            countryError.textContent = "";
            return true;
        }

        nameField.addEventListener('input', validateName);
        whatsappField.addEventListener('input', validateWhatsapp);
        ageField.addEventListener('input', validateAge);
        form.addEventListener('submit', validateForm);

        countryField.addEventListener('change', updateStateField);

        updateStateField(); // Initialize the state field on page load
    });
});