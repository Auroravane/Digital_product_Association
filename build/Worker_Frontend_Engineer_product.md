html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI-Generated Legal Contract Template Tool</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>AI-Generated Legal Contract Template Tool</h1>
    </header>
    <main>
        <section id="template-selector">
            <h2>Template Selector</h2>
            <select id="template-options" aria-label="Select a template">
                <option value="">Select a template</option>
                <option value="employment-contract">Employment Contract</option>
                <option value="non-disclosure-agreement">Non-Disclosure Agreement</option>
                <option value="lease-agreement">Lease Agreement</option>
            </select>
        </section>
        <section id="customization-form">
            <h2>Customization Form</h2>
            <form id="customization-form-fields">
                <label for="contract-title">Contract Title:</label>
                <input type="text" id="contract-title" name="contract-title" required>
                <label for="party-names">Party Names:</label>
                <input type="text" id="party-names" name="party-names" required>
                <label for="contract-duration">Contract Duration:</label>
                <input type="number" id="contract-duration" name="contract-duration" required>
                <button type="submit" id="generate-contract">Generate Contract</button>
            </form>
        </section>
    </main>
    <script src="script.js" defer></script>
</body>
</html>