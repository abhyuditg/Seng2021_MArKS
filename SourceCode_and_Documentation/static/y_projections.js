$(document).ready(function() {

	var ctx = $("#yearly-projections");

	var data = {
		labels : ["2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
		datasets : [
			{
				label : "Projected Savings",
				data : [3191.19, 8237.19, 12812.18, 15269.19, 19827.10, 23812.91, 29180.19, 35179.29, 43129.19, 50289.19, 57269.19],
        backgroundColor : "orange",
				borderColor : "#edbd64",
				fill : false,
				lineTension : 0,
				pointRadius : 5
			},
			{
				label : "Projected Expenditure",
				data : [4823.19, 10951.38, 16780.57, 23909.76, 32219.86, 38139.96, 45268.06, 52105.16, 58388.26, 65670.17, 70908.36],
				backgroundColor : "#79fa00",
				borderColor : "#bfed64",
				fill : false,
				lineTension : 0,
				pointRadius : 5
			}
		]
	};

	var options = {
		legend : {
			display : true,
			position : "bottom"
		}
	};

	var chart = new Chart( ctx, {
		type : "line",
		data : data,
		options : options
	} );

});
