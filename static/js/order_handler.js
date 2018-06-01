var sec1='<div class="row"><div class="row" style="margin-right: -2px;"">\n' +
    '       <div class="col-lg-1"></div><div class="col-lg-3"><label style="margin-right: -10px; margin-left: 10px">תהליכים:</label><input type="text" name="process';
var sec2='"><span style="padding:0 10px 0 10px; ">+</span><select onchange="addProcess(this,this.value)">\n' +
    '       <option style="display: none;" selected>תהליך</option>';
var sec3='</select> \n' +
    '</div> \n' +
    '<div class="col-lg-3"> \n' +
    '   <div class="input-group"> \n' +
    '       <span class="rtlform" style="margin-right: -25px;"><label style="margin-left: -30px;">כמות:</label></span>\n' +
    '       <input type="text" name="pamount';
var sec4='"></div></div> \n'+
    '<div class="col-lg-3"> \n' +
    '   <div class="input-group"> \n' +
    '       <span class="rtlform"  style="margin-right: -21px;"><label style="margin-left: -30px;">שם:</label></span>\n' +
    '       <input type="text" name="pname';
var sec5='"></div></div> \n' +
    '<div class="col-lg-1"><h4 style="display: inline; margin-right: 27px;"> ';
var sec6='.</h4></div><div class="col-lg-1"></div></div><div class="row" style="margin-bottom:50px; margin-right: -270px;"><div class="col-lg-1"></div>' +
    '<div class="col-lg-1" ><input type="checkbox" name="packed" onclick="updateParameters(this,4)"><label style="margin-right: 10px;">ארוז </label></div>' +
    '<div class="col-lg-1" ><input type="checkbox" name="oilled" onclick="updateParameters(this,3)"><label style="margin-right: 10px;">משומן</label></div>' +
    '<div class="col-lg-2" style="margin-right: -70px;"><label style="margin-left: 10px;">קושי עבודה:</label><select onchange="updateParameters(this,2)">' +
    '<option>1</option><option>2</option><option>3</option><option>4</option><option>5</option></select>' +
    '</div>' +
    '<div class="col-lg-3"><label style="margin-left: 10px;">שטח ריתוך/סימון (סמ"ר):</label><input type="text" style="width: 120px;" onkeyup="updateParameters(this,1)"></div>' +
    '<div class="col-lg-2"><label style="margin-left: 10px; margin-right: 20px;"">חומר:</label><select onchange="updateParameters(this,0)">' +
    '<option value="0">PVC</option><option value="1">Aluminum</option><option value="3">Copper</option></select></div>' +
    '<input style="display: none;" type="text" name="parameters';
var sec7='" value="0,0,1,0,0"></div><div id="perror';
var sec8='" class="row login-error" align="center" style="display:none; margin-bottom: 40px;"> \n' +
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
        final+=sec3+Pindex+sec4+Pindex+sec5+(Ecounter+Pindex+1)+sec6+Pindex+sec7+Pindex+sec8;
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
    list = list.split(',');
    if (list[list.length-1]==''){
        list.pop();
    }
    for (var i=0; i<list.length; i++){
        if (!stations.includes(list[i])) {
            return false;
        }
    }
    return true;
}

function updateParameters(obj,index){
    $element = $(obj)
    var params = $element.closest(".row").find("input[name*='parameters']");
    var parametersField = params.val().split(',');
    switch (index){
        case 4:
        case 3:
            if ($element.is(':checked')){
                parametersField[index] = 1;
            }
            else{
             parametersField[index] = 0;
            }
            break;
        default:

            parametersField[index] = obj.value ? obj.value : 0;
    }
    a = parametersField.join(',');
    params.val(a);
    console.log(a);
}

