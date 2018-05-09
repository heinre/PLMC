var sec1='<div class="row">\n' +
    '       <div class="col-lg-1"></div><div class="col-lg-3"><label>תהליכים:</label><input type="text" name="process';
var sec2='"><span style="padding:0 10px 0 10px; ">+</span><select onchange="addProcess(this,this.value)">\n' +
    '       <option style="display: none;" selected>תהליך</option>';
var sec3='</select> \n' +
    '</div> \n' +
    '<div class="col-lg-3"> \n' +
    '   <div class="input-group"> \n' +
    '       <span class="rtlform"><label>כמות:</label></span>\n' +
    '       <input type="text" name="pamount';
var sec4='"></div></div> \n'+
    '<div class="col-lg-3"> \n' +
    '   <div class="input-group"> \n' +
    '       <span class="rtlform"><label>שם:</label></span>\n' +
    '       <input type="text" name="pname';
var sec5='"></div></div> \n' +
    '<div class="col-lg-1"><h4>';
var sec6='.</h4></div><div class="row"></div><div id="perror';
var sec7='" class="row login-error" align="center" style="display:none; margin-bottom: 40px;"> \n' +
    '<span>אנא וודא שנתת למוצר שם, כמות גדולה מ-0 ורשימת תהליכים חוקית.</span></div></div>';
/*
var sec1='<div class="row">\n' +
    '       <div class="col-lg-1"></div><div class="col-lg-3"><label>תהליכים:</label><input type="text" name="process';
var sec2='"><span style="padding:0 10px 0 10px; ">+</span><select onchange="addProcess(this,this.value)">\n' +
    '       <option style="display: none;" selected>תהליך</option>';
var sec3='</select><br><div class="row"></div><div id="perror';
var sec4='" class="row login-error" align="center" style="display:none; margin-bottom: 40px;"><span>Make sure you have named the product, \n' +
    '      entered an amount bigger than 0 and using a valid processes list.</span></div></div> \n' +
    '<div class="col-lg-3"> \n' +
    '   <div class="input-group"> \n' +
    '       <label>כמות:</label>\n' +
    '       <input type="text" name="pamount';
var sec5='"></div></div> \n'+
    '<div class="col-lg-3"> \n' +
    '   <div class="input-group"> \n' +
    '       <label>שם:</label>\n' +
    '       <input type="text" name="pname';
var sec6='"></div></div> \n' +
    '<div class="col-lg-1"><h4>';
var sec7='.</h4></div></div>';
*/
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
    /*
     var final=sec1+(Ecounter+Pindex+1)+sec1a+Pindex+sec2+Pindex+sec3+Pindex+sec4;
	    for (var i in stations){
	        final+='<option>'+stations[i]+'</option>';
        }
        final+=sec5+Pindex+sec6;
        */
    var final=sec1+Pindex+sec2;
        for (var i in stations){
	        final+='<option>'+stations[i]+'</option>';
        }
        final+=sec3+Pindex+sec4+Pindex+sec5+(Ecounter+Pindex+1)+sec6+Pindex+sec7;
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
    console.log(station);
    $(obj).siblings()[1].value += station +',';
    $(obj).prop('selectedIndex', 0);
}

function validateAndSubmit(){
    $("#cerror").hide()
    var client = true;
    if ($("#id_clientID").val() == ""){
        $("#cerror").show()
        client = false;
    }
    if (validateProduct() && client){
        $("#form").submit();
    }
}

function validateProduct(){
    for(var i=0; i < Pindex; i++){
        $("#perror"+i).hide()
        if ($("input[name='pname"+i+"']").val().length < 1 || $("input[name='pamount"+i+"']").val() < 1 || $("input[name='pamount"+i+"']").val().length < 1 || !$.isNumeric($("input[name='pamount0']").val()) || !isProcessList(i)){
            $("#perror"+i).show()
            return false;
        }
    }
    return true;
}

function isProcessList(index){
    var list = $("input[name='process"+index+"']").val();
    if (list.length < 1){
        return false;
    }
    for (var i=0; i<list.length; i++){
        if (!(i%2)) {
            if (!stations.includes(list[i])) {
                return false;
            }
        }
        else{
            if (list[i] != ','){
                return false;
            }
        }
    }
    return true;
}


