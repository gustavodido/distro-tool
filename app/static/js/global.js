$(function() {
	var handleResult = function(data, message) {
	    if (data.result = 202) {
	        alert(message);
	    } else {
            alert("Error: " + data.result);
        }
	};

    $("#refreshDistroName").click(function() {
        var ccNumber = $("#ccNumber").val();
        $.get("/api/refresh-distro-name?ccNumber=" + ccNumber)
            .then(function(data) {
            	handleResult(data, "Distro name successfully refreshed!");
            });
    });

    $("#refreshDistroStores").click(function() {
        var ccNumber = $("#ccNumber").val();
        $.get("/api/refresh-distro-stores?ccNumber=" + ccNumber)
            .then(function(data) {
            	handleResult(data, "Distro stores refresh requested!");
            })
    })

    $("#refreshDcMapping").click(function() {
        var ccNumber = $("#ccNumber").val();
        $.get("/api/refresh-dc-mapping?ccNumber=" + ccNumber)
            .then(function(data) {
            	handleResult(data, "DC mapping successfully refreshed!");
            })
    })

})
