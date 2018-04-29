var sec1='<div class="row">\n' +
    '       <div class="col-lg-1"><h4>'
var sec1a ='.</h4></div>\n' +
    '       <div class="col-lg-3">\n' +
    '           <div class="input-group">\n' +
    '               <label>Name:</label>\n' +
    '               <input type="text" name="pname';
var sec2='"></div>\n' +
    '     </div>\n' +
    '     <div class="col-lg-3">\n' +
    '       <div class="input-group">\n' +
    '           <label>Amount:</label>\n' +
    '           <input type="text" name="pamount';
var sec3 ='"></div>\n' +
    '       </div>\n' +
    '       <label>Processes:</label>\n' +
    '       <input type="text" name="process';
var sec4='"><span style="padding:0 10px 0 10px; ">+</span><select onchange="addProcess(this,this.value)">\n' +
    '       <option style="display: none;" selected>Process</option>';
var sec5='</select></div>';

var Pindex = 0;
var Ecounter = 0;
var stations = [];
$(document).ready(function () {
    if ($("#Ecounter").val()){
        Ecounter = Number($("#Ecounter").val());
    }
    else{
        Ecounter = 0;
    }
    $.ajax({
        url: "/api/stations/",
        success: function(data){
           stations = JSON.parse(data);
    }});
    $("#addProduct").click(function () {
        addProduct();
        //RefreshListener();
    });
    $("#removeProduct").click(function () {
        removeProduct();
    });
    //RefreshListener();
});

function RefreshListener() {
    // Remove handler from existing elements
    $(".form-control").off();

    // Re-add event handler for all matching elements
    $(".form-control").on("change", handler)
}
function addProduct() {
     var final=sec1+(Ecounter+Pindex+1)+sec1a+Pindex+sec2+Pindex+sec3+Pindex+sec4;
	    for (var i in stations){
	        final+='<option>'+stations[i]+'</option>';
        }
        final+=sec5;
    $(".fields").append(final);
    Pindex++;
    document.getElementById('Pcounter').value = Pindex;
}

function removeProduct() {
    if(Pindex  == 0){
        return;
    }
    $(".fields > .row:last").remove();
    Pindex--;
    document.getElementById('Pcounter').value = Pindex;
}

function addProcess(obj,station){
    $(obj).siblings()[4].value += station +',';
    $(obj).prop('selectedIndex', 0);
}

function validateProduct(){
    for(var i=0; i < Pindex; i++){
        /*if ($("input[name='pname"+i+"']").val().length < 1 && $("input[name='pamount"+i+"']").val() <= 0
        && $("input[name='process"+i+"']").val().length < 1){
            return false;
        }*/
        alert($("input[name='pamount"+i+"']").val() < 1) && $("input[name='pamount"+i+"']").val().length < 1 && $.isNumeric($("input[name='pamount0']").val());
    }
    return true;
}

function isProcessList(){

}