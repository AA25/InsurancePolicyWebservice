const policySearchForm = document.getElementById('policySearchForm');
const searchInput = document.getElementById('policySearchInput');
const policyTableBody = document.getElementById('policyTableBody');

policySearchForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission - inorder to prevent the page from reloading
    const policyNumber = searchInput.value.trim();
    fetchPolicyByNumber(policyNumber);
});

async function fetchPolicyByNumber(policyNumber = 100123) {
    if (!policyNumber) {
        console.log("No policy number")
        return;
    }

    let apiUrl = `http://localhost:8000/api/v1/policies/${encodeURIComponent(policyNumber)}`;

    try {
        const response = await fetch(apiUrl);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        policyTableBody.innerHTML = '';

        const policy = await response.json();

        const row = `
            <tr>
                <th scope="row">${policy.policy_number}</th>
                <td>${policy.status}</td>
                <td>${policy.policy_type}</td>
                <td>${policy.premium_amount}</td>
                <td>${policy.policy_start_date}</td>
                <td>${policy.policy_end_date}</td>
            </tr>
        `;
        policyTableBody.insertAdjacentHTML('beforeend', row);

    } catch (error) {
        console.error('Error fetching policy:', error);
    }
}

async function fetchAllPolicies() {
    let apiUrl = `http://localhost:8000/api/v1/policies`;

    try {
        // Clear existing table rows before fetching new ones
        policyTableBody.innerHTML = '';

        // Optional: Show a loading indicator for all policies fetch
        policyTableBody.innerHTML = `
            <tr>
                <td colspan="6" class="text-center py-4 text-muted">
                    <div class="spinner-border text-primary" role="status">
                        <span class="visually-hidden">Loading policies...</span>
                    </div>
                    Loading all policies...
                </td>
            </tr>
        `;

        const response = await fetch(apiUrl);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const policies = await response.json();

        policyTableBody.innerHTML = '';
        policies.forEach(policy => {
            const row = `
                <tr>
                    <th scope="row">${policy.policy_number}</th>
                    <td>${policy.status}</td>
                    <td>${policy.policy_type}</td>
                    <td>${policy.premium_amount}</td>
                    <td>${policy.policy_start_date}</td>
                    <td>${policy.policy_end_date}</td>
                </tr>
            `;
            policyTableBody.insertAdjacentHTML('beforeend', row);
        });

    } catch (error) {
        console.error('Error fetching policy:', error);
    }
}

// Trigger retrieval of all policies when page is ready
document.addEventListener('DOMContentLoaded', () => {
    fetchAllPolicies()
})