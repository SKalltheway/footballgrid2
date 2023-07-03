
function loadCSV() {
    // Path to your CSV file
    const csvFilePath = 'immaculategridiron/footballgrid2/all_NFL_players_ever.csv';

    // Create a new XMLHttpRequest object
    const xhr = new XMLHttpRequest();
    
    // Setup the request
    xhr.open('GET', csvFilePath, true);
    
    // Set the response type to 'text'
    xhr.responseType = 'text';
    
    // Handle the request load event
    xhr.onload = function() {
        if (xhr.status === 200) {
            const csvData = xhr.responseText;
            const rows = csvData.split('\n');
            
            // Assume the first row contains column headers
            const headers = rows[0].split(',');
            const columnToExtract = 'Player'; // Specify the column you want to extract
            
            // Find the index of the specified column
            const columnIndex = headers.indexOf(columnToExtract);
            
            // Create an array to store the values in the column
            const columnValues = [];
            
            // Iterate through the remaining rows and extract the values in the specified column
            for (let i = 1; i < rows.length; i++) {
                const row = rows[i].split(',');
                if (row[columnIndex]) {
                    columnValues.push(row[columnIndex]);
                }
            }
            
            // Create a list of the extracted column values
            const list = document.getElementById('list');
            columnValues.forEach(value => {
                const listItem = document.createElement('li');
                listItem.textContent = value;
                list.appendChild(listItem);
            });
        } else {
            console.error('Failed to load CSV file.');
        }
    };
    
    // Send the request
    xhr.send();
}
