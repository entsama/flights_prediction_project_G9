function displayResult(data) {
    const resultDiv = document.getElementById('result');
    if (data.error) {
        resultDiv.innerHTML = `Error: ${data.error}`;
        resultDiv.style.backgroundColor = '#f8d7da';
        resultDiv.style.color = '#721c24';
    } else {
        resultDiv.innerHTML = `Predicted Salary: $${data.predicted_salary.toFixed(2)}`;
    }
    resultDiv.style.display = 'block';
}

function submitForm() {
    const formData = {
        work_year: document.getElementById('work_year').value,
        experience_level: document.getElementById('experience_level').value,
        employment_type: document.getElementById('employment_type').value,
        job_title: document.getElementById('job_title').value,
        employee_residence: document.getElementById('employee_residence').value,
        remote_ratio: document.getElementById('remote_ratio').value,
        company_location: document.getElementById('company_location').value,
        company_size: document.getElementById('company_size').value
    };

    fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        displayResult(data);
    })
    .catch(error => {
        console.error('Error:', error);
        displayResult({ error: "Failed to fetch prediction"});
    });
}
