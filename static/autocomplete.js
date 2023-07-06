// Load CSV data
function loadCSV(callback) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        var csvData = xhr.responseText;
        callback(csvData);
      }
    };
    xhr.open("GET", "all_NFL_players_ever.csv", true);
    xhr.send();
  }
  
  // Parse CSV data
  function parseCSV(csvData) {
    var lines = csvData.split("\n"); 
    var data = [];
    for (var i = 0; i < lines.length; i++) {
      var cells = lines[i].split(",");
      data.push(cells[0].trim());
    }
    return data;
  }
  

  // Filter suggestions based on input 
  function filterSuggestions(inputValue, data) {
    var filteredData = [];
    for (var i = 0; i < data.length; i++) {
      var item = data[i];
      if (item.toLowerCase().indexOf(inputValue.toLowerCase()) !== -1) {
        filteredData.push(item);
      }
    }
    return filteredData;
  }
  
  // Update autocomplete list
  function updateAutocompleteList(inputValue, suggestions) {
    var autocompleteList = document.getElementById("autocompleteList");
    autocompleteList.innerHTML = "";
  
    for (var i = 0; i < suggestions.length; i++) {
      var suggestion = suggestions[i];
      var li = document.createElement("li");
      li.textContent = suggestion;
      autocompleteList.appendChild(li);
    }
  
    if (suggestions.length === 0) {
      autocompleteList.style.display = "none";
    } else {
      autocompleteList.style.display = "block";
    }
  }
  
  // Initialize autocomplete
  function initAutocomplete() {
    var searchInput = document.getElementById("searchInput");
    var autocompleteList = document.getElementById("autocompleteList");
  
    searchInput.addEventListener("input", function() {
      var inputValue = this.value;
      loadCSV(function(csvData) {
        var data = parseCSV(csvData);
        var suggestions = filterSuggestions(inputValue, data);
        updateAutocompleteList(inputValue, suggestions);
      });
    });
  
    autocompleteList.addEventListener("click", function(event) {
      if (event.target.tagName === "LI") {
        searchInput.value = event.target.textContent;
        autocompleteList.style.display = "none";
      }
    });
  
    document.addEventListener("click", function(event) {
      if (event.target !== searchInput && event.target !== autocompleteList) {
        autocompleteList.style.display = "none";
      }
    });
  }
  
  // Initialize autocomplete when the page is loaded
  window.addEventListener("load", function() {
    initAutocomplete();
  });
  