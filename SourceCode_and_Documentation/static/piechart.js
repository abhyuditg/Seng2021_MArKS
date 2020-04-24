$(document).ready(function () {
	var ctx = $("#pie-expenditure");

  	var data1 = {
  		labels : ["Housing", "Food", "Phone", "Entertainment", "Transport", "Car", "Other", "Health"],
  		datasets : [
  			{
  				data : data_transac,
  				backgroundColor : [
                      "#ebb7d5",
                      "#a5e6e3",
                      "#d0a7e8",
                      "#fcbc8d",
                      "#e6a5b7",
                      "#b3e092",
                      "#a3e7f7",
                      "#99e0a4"
                  ],
									borderAlign : "inner"

  			}
  		]
  	};


  	var options = {
  		title : {
  			display : true,
  			position : "top",
  			text : "Expenditure",
  			fontSize : 30,
  			fontColor : "#111",
				padding: 50
  		},
  		legend : {
				align: "center",
				padding: 50,
  			display : true,
  			position : "right"
  		}
  	};


  	var chart1 = new Chart( ctx, {
  		type : "pie",
  		data : data1,
  		options : options
  	});


    var canvas = document.getElementById("pie-expenditure");    
    canvas.onclick = function(evt) {
      var activePoints = chart1.getElementsAtEvent(evt);
      if (activePoints[0]) {
        var chartData = activePoints[0]['_chart'].config.data;
        var idx = activePoints[0]['_index'];

        var label = chartData.labels[idx];
        var value = chartData.datasets[0].data[idx];
        data_category

        alert(label);
      }
    };

  });
