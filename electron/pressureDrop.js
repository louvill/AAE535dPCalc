let fs = require('fs');
let path = require('path');
let {PythonShell} = require('python-shell');

$(document).ready(function() {
  // Load component information from componentTypes JSON file
  var libDir = path.join(__dirname, '..', 'lib');
  var rawJSON = fs.readFileSync(path.join(libDir, 'componentTypes.json'), 'utf8'); 
  var txtJSON = String(rawJSON);
  componentList = JSON.parse(txtJSON);
  
  // Load unit information from units.json
  var rawUnitJSON = fs.readFileSync(path.join(libDir, 'units.json'), 'utf8')
  var txtUnitJSON = String(rawUnitJSON);
  unitObj = JSON.parse(txtUnitJSON);
  
  var components = Object.keys(componentList);
  addRow(components);
  
  $("#calculateButton").click(calculateResults);
  $("#resultsButton").click(clickedResultsButton);
  $("#loadSaveFileButton").click(loadSaveFile);
});

function addComponentElement(value, index, array) {
  var componentName = componentList[value].displayName;
  $(this).parent().append('<div class="dropDownContent" index="'+index+'">'+componentName+'</div>');
}

function addRowElement(componentName, paramType, value, index, array) {
  var componentObj = componentList[componentName];
  var componentObj = componentObj[paramType];
  var paramObj = componentObj[value];
  
  var displayName = paramObj.displayName;
  var rowStringHTML = '<div class="parameterButton">'+displayName;
  
  if (!(paramObj.tooltip === null)) {
    rowStringHTML = rowStringHTML.concat(
      ' <span class="tooltip">?<span class="tooltiptext">'+paramObj.tooltip+'</span></span>'
    );
  }
  
  rowStringHTML = rowStringHTML.concat('<br>');
  
  if (paramObj.unit == "boolean") {
      var inputType ="boolean";
      rowStringHTML = rowStringHTML.concat(
          '<select name="value"><option>True</option><option>False</option></select></div>');
  } else if (paramObj.unit === null) {
      var inputType = null;
      rowStringHTML = rowStringHTML.concat(
        '<input type="text" size="3"></input></div>');
  } else {
      var inputType = "normal";
      var unitType = paramObj.unit;
      var unitsArray = Object.keys(unitObj[unitType]);

      rowStringHTML = rowStringHTML.concat(
          '<input type="text" size="3"></input> '+
          '<select name="unit">');
      unitsArray.forEach( function(value) {
        rowStringHTML = rowStringHTML.concat('<option>'+value+'</option>');
      });
      rowStringHTML = rowStringHTML.concat("</select></div>");
  }
  $(this).append(rowStringHTML);
  $(this).children(":last").prop("key", value);
  $(this).children(":last").prop("displayName", displayName);
    $(this).children(":last").prop("inputType", inputType);
}

function addRow(components) {
  $('#main').append(
  '<div class="row">'+
    '<div class="dropDown">'+
      '<div class="button addComponent">Add Component</div>'+
    '</div>'+
    '<div class="parameterContainer collapsable uncollapsed hidden">'+
      '<div class="button collapsableButton"><span>Parameters</span></div>'+
      '<div class="buttonContainer"></div>'+
    '</div>'+
    '<div class="fluidContainer collapsable collapsed hidden">'+
      '<div class="button collapsableButton"><span>Fluid Properties</span></div>'+
      '<div class="buttonContainer"></div>'+
    '</div>'+
  '</div>'); 
  
  // Add each component type to the drop down menu
  components.forEach(addComponentElement.bind($(".addComponent:last")));
  
  // Define function to show dropdown when add component is clicked
  /*
  $(".addComponent:last").click( function() {
    $(this).siblings('.dropDownContent').show();
  });
  */
 
  // Define function to add component when component type is clicked
  $(".addComponent:last ~ .dropDownContent").click( function() {  
    var rowElement = $(this).parents(".row");
    
    // Remove any existing parameter buttons
    rowElement.find('.parameterButton').remove();
    
    // Set up collapsable menus
    rowElement.children('.collapsable').children(".collapsableButton").off("click");
    rowElement.children('.collapsable').children(".collapsableButton").click(function() {
      var collapsableElement = $(this).parent();
      if (collapsableElement.hasClass("collapsed")) {
        collapsableElement.removeClass("collapsed");
        collapsableElement.addClass("uncollapsed");
      } else {
        collapsableElement.removeClass("uncollapsed");
        collapsableElement.addClass("collapsed");
      }
    });
   
    // Define parameter array based on componentIndex
    var componentIndex = $(this).attr("index");
    var componentName = components[componentIndex];
    var componentParams = Object.keys(componentList[componentName].component);
    var fluidParams = Object.keys(componentList[componentName].fluid);
    
    rowElement.prop("key", componentName);
    
    // Add component parameter buttons
    componentParams.forEach(addRowElement.bind(rowElement.children(".parameterContainer").children(
      ".buttonContainer"), componentName, 'component'));
    
    //Add fluid parameter buttons     
    fluidParams.forEach(addRowElement.bind(rowElement.children(".fluidContainer").children(
      ".buttonContainer"), componentName, 'fluid'));
    
    //Show component parameters and fluid property buttons
    rowElement.children(".hidden").removeClass("hidden");
    
    // Change 'Add Component' -> 'Change Component'
    $(this).siblings('.addComponent').text(componentList[componentName].displayName);
    if ($(this).siblings().last().text() != "Clear Component") {
      // Add row
      addRow(components);
      
      $(this).parent().append('<div class="dropDownContent"">Clear Component</div>');
      $(this).siblings().last().off("click");
      
      $(this).siblings().last().click(function () { 
        $(this).parents(".row").last().remove();
      });
    }
  });
}


function extractInputFile() {
  var components = [];
  var rows = $(".row:not(:last)");
  var numRows = rows.length
  
  rows.each(function( index ) {
    var componentType = $(this).prop("key");
    var currObject = {};
    currObject.IIN = "00"+(index+1);
    currObject.CID = componentList[componentType].CID;
    currObject.displayName = componentList[componentType].displayName;
    currObject.parent = (index!=0)?("00"+(index)):("null");
    currObject.child = (index!=numRows-1)?("00"+(index+2)):("null");
    currObject.values = {};
    currObject.values.component = {};
    currObject.values.fluid = {};
    
    $(this).children('.parameterContainer').find('.parameterButton').each(function() {
      var paramType = $(this).prop("key");
      var inputType = $(this).prop("inputType");
      var paramObj = {};
      paramObj.displayName = $(this).prop("displayName");
      if (inputType == "boolean") {
        paramObj.value = $(this).children("select").val()
        paramObj.unit = "boolean";
      } else if (inputType == null) {
        paramObj.value = $(this).children("input").val();
        paramObj.unit = null;
      } else {
        paramObj.value = $(this).children("input").val();
        paramObj.unit = $(this).children("select").val();
      }
      currObject.values.component[paramType] = paramObj;
    });
    
    $(this).children('.fluidContainer').find('.parameterButton').each(function() {
      var paramType = $(this).prop("key");
      var paramObj = {};
      paramObj.value = $(this).children("input").val();
      paramObj.displayName = $(this).prop("displayName");
      paramObj.unit = $(this).children("select").val();
      currObject.values.fluid[paramType] = paramObj;
    });
    
    components[index] = currObject;
  });
  inputObject = {
    "fileDisplayName" : "Test Save",
    "softwareVer" : "0.1.0",
    "componentList" : []
  }
  
  inputObject.componentList = components;
  inputFile = JSON.stringify(inputObject);
  return(inputFile);
}

function runPython() {
  var python = require('child_process').spawn('python', ['./main.py']);
  var outputFileExists = false;
  var savePath = path.join(__dirname, '..', 'saves', 'testOutput.json');
  fs.unlinkSync(savePath);
  while (!(outputFileExists)) {
    outputFileExists = fs.existsSync(savePath);
  }
}

function calculateResults() {
  var inputFile = extractInputFile();
  fs.writeFileSync('saves/testSave.json', inputFile);
  runPython();
  displayResults();
  $("#resultsButton").removeClass("hidden");
  $("#resultsButton").text("Hide Results");
  $("#results").removeClass("hidden");
}

function displayResults() {
  $("#resultsContainer").text("");
  
  var saveDir = path.join(__dirname, '..', 'saves');
  var results = fs.readFileSync(path.join(saveDir, 'testOutput.json'), 'utf8');
  results = String(results);
  results = JSON.parse(results);
  
  componentResults = results.components;
  componentResults.forEach(function(value) {
    var curr = value.pressureDrop;
    var currValue = Math.round(curr.value*1000)/1000;
    $("#resultsContainer").append(curr.displayName+": "+currValue+" "+curr.unit+"<br>");
  });
  
  dp_total = Math.round(results.pressureDropSum.value*1000)/1000;;
  dp_total_unit = results.pressureDropSum.unit;
  $("#resultsContainer").append("<br>Total Pressure Drop: "+dp_total+" "+dp_total_unit+"<br><br>");

}

function clickedResultsButton() {
  if ($("#results").hasClass("hidden")) {
    $("#resultsButton").text("Hide Results");
    $("#results").removeClass("hidden");
  } else {
    $("#resultsButton").text("Show Results");
    $("#results").addClass("hidden");
  }
}

function loadSaveFile() {
  var fName = $("#loadSaveFileButton").siblings("input").val();
  var saveDir = path.join(__dirname, '..', 'saves');
  var input = fs.readFileSync(path.join(saveDir, fName), 'utf8');
  input = String(input);
  input = JSON.parse(input);
  
  var componentsInput = input.componentList;
  componentsInput.forEach(function(value) {
/*    var components = Object.keys(componentList);
    addRow(components)*/
    window.alert(value.CID);
  });
}