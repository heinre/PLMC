var sec1='<div class="row"><div class="row" style="margin-right: -300px;">\n' +
    '       <div class="col-lg-1"></div><div class="col-lg-3" style="margin-right: -120px; left:100px;"><label style="margin-right: -10px; margin-left: 10px">תהליכים:</label><input type="text" name="process';
var sec2='"><span style="padding:0 10px 0 10px; ">+</span><select onchange="addProcess(this,this.value)">\n' +
    '       <option style="display: none;" selected>תהליך</option>';
var sec3='</select> \n' +
    '</div> \n' +
    '<div class="col-lg-2" style="left: 200px;"> \n' +
    '   <div class="input-group"> \n' +
    '       <span class="rtlform" style="margin-right: -25px;"><label style="width: 120px;">כמות:</label></span>\n' +
    '       <input type="text" name="pamount';
var sec4='"></div></div> \n'+
    '<div class="col-lg-2" style="left: 200px;"> \n' +
    '   <div class="input-group"> \n' +
    '       <span class="rtlform"  style="margin-right: -21px;"><label style="margin-left: -30px;">שם:</label></span>\n' +
    '       <input type="text" name="pname';


var sec5='"></div></div> \n' +
    '<div class="col-lg-1" style="left: 150px;"><h4 style="display: inline; margin-right: 27px;"> ';
var sec6='.</h4></div><div class="col-lg-1"></div></div><div class="row" style="margin-right: 00px;"><div class="col-lg-1"></div><div class="col-lg-1" style="left: 200px;">' +
    '<input type="checkbox" name="coc';
var sec7='" checked><label style="margin-right: 10px;">C.O.C </label></div>' +
    '<div class="col-lg-3" style="left: 225px; width: 310px"><div class="input-group"><span class="rtlform""><label>מספר שרטוט:</label></span><input type="text" name="schema';
var sec8='"></div></div><div class="col-lg-3" style="left: 115px;"><div class="input-group"><span class="rtlform">' +
    '<label>מהדורה/גרסה:</label></span><input type="text" name="version';
var sec9='"></div></div><div class="col-lg-2" style="left: 110px;"><div class="input-group"><span class="rtlform">' +
    '<label style="width: 100px;">מק"ט:</label></span><input type="text" name="CN';
var sec10='"></div></div></div>' +
    '<div class="row"><div class="col-lg-9"></div><div class="col-lg-1"><h4>פרמטרי ריתוך</h4></div></div>' +
    '<div class="row"><div class="col-lg-2"></div><div class="col-lg-3" style="left: 199px; width: 310px">' +
    '<div class="input-group"><span class="rtlform""><label style="width: 120px;" dir="ltr">:V(volt)</label>' +
    '</span><input type="text" name="volt';
var sec11='"></div></div>' +
    '<div class="col-lg-2" style="left: 200px;"><div class="input-group"><span class="rtlform"">' +
    '<label style="width: 100px; "dir="ltr">:Ms</label></span><input type="text" name="Ms';
var sec12='"></div></div>' +
    '<div class="col-lg-2" style="left: 242px;"><div class="input-group"><span class="rtlform">' +
    '<label style="width: 100px;" dir="ltr">:Hz</label></span><input type="text" name="Hz';
var sec13='"></div></div></div>' +
    '<div class="row"><div class="col-lg-2"></div><div class="col-lg-3" style="left: 199px; width: 310px">' +
    '<div class="input-group"><span class="rtlform" style="margin: 0px; width: 80px;">' +
    '<label style="width: 120px;" dir="ltr">:Diameter</label></span><input type="text" name="diameter';
var sec14='"></div></div>' +
    '<div class="col-lg-2" style="left: 215px;"><div class="input-group">' +
    '<span class="rtlform" style="margin: 0px; width:75px;"><label style="width: 100px; "dir="ltr">:Rotating</label>' +
    '</span><input type="text" name="rotating';
var sec15='"></div></div>' +
    '<div class="col-lg-3" style="left: 151px;"><div class="input-group"><span class="rtlform" style="margin: 0px;">' +
    '<label style="width: 100px;" dir="ltr">:Micro Weld</label></span><input type="text" name="microWeld';
var sec16='"></div></div></div>' +
    '<div class="row"><div class="col-lg-9"></div><div class="col-lg-1"><h4>פרמטרי סימון</h4></div></div>' +
    '<div class="row"><div class="col-lg-2"></div><div class="col-lg-3" style="left: 199px; width: 310px">' +
    '<div class="input-group"><span class="rtlform""><label style="width: 120px;" dir="ltr">:Power</label></span>' +
    '<input type="text" name="power';
var sec17='"></div></div>' +
    '<div class="col-lg-2" style="left: 200px;"><div class="input-group"><span class="rtlform">' +
    '<label style="width: 100px; "dir="ltr">:Freq.</label></span><input type="text" name="freq';
var sec18='"></div></div>' +
    '<div class="col-lg-3" style="left: 112px;"><div class="input-group">' +
    '<span class="rtlform" style="margin: 0px; width: 70px;"><label style="width: 100px;" dir="ltr">:Speed</label>' +
    '</span><input type="text" name="speed';
var sec19='"></div></div></div>' +
    '<div class="row"><div class="col-lg-2"></div><div class="col-lg-3" style="left: 199px; width: 310px">' +
    '<div class="input-group"><span class="rtlform" style="margin: 0px; width: 80px;">' +
    '<label style="width: 120px;" dir="ltr">:Others</label></span><input type="text" name="others';
var sec20='"></div></div>' +
    '<div class="col-lg-2" style="left: 190px;"><div class="input-group">' +
    '<span class="rtlform" style="margin: 0px; width:50px;"><label style="width: 100px; "dir="ltr">:F.s</label>' +
    '</span><input type="text" name="Fs';
var sec21='"></div></div>' +
    '<div class="col-lg-3" style="left: 128px;"><div class="input-group"><span class="rtlform" style="margin: 0px;">' +
    '<label style="width: 75px;" dir="ltr">:Density</label></span><input type="text" name="density';
var sec22='"></div></div></div>' +
    '<div class="row"><div class="col-lg-8"></div><div class="col-lg-2"><h4>פרמטרים כלליים</h4></div></div>' +
    '<div class="row" style="margin-bottom:50px; margin-right: -270px;"><div class="col-lg-1"></div>' +
    '<div class="col-lg-2"><input type="checkbox" name="packed" onclick="updateParameters(this,4)"><label style="margin-right: 10px;">ארוז </label></div>' +
    '<div class="col-lg-1" style="width: 100px;"><input type="checkbox" name="oilled" onclick="updateParameters(this,3)"><label style="margin-right: 10px;">משומן</label></div>' +
    '<div class="col-lg-1" ><label style="margin-left: 10px;">קושי עבודה:</label><select onchange="updateParameters(this,2)">' +
    '<option>1</option><option>2</option><option>3</option><option>4</option><option>5</option></select>' +
    '</div>' +
    '<div class="col-lg-2" style="left:60px;"><label style="margin-left: 10px;">שטח ריתוך/סימון (סמ"ר):</label><input type="text" style="width: 120px;" onkeyup="updateParameters(this,1)"></div>' +
    '<div class="col-lg-2" style="width: 190px; left:120px;"><label style="margin-left: 10px; margin-right: 20px;"">חומר:</label><select onchange="updateParameters(this,0)">' +
    '<option value="0">PVC</option><option value="1">Aluminum</option><option value="3">Copper</option></select></div>' +
    '<input style="display: none;" type="text" name="parameters';
var sec23='" value="0,0,1,0,0"></div><div id="perror';
var sec24='" class="row login-error" align="center" style="display:none; margin-bottom: 40px;"> \n' +
    '<span>אנא וודא שנתת למוצר שם, כמות גדולה מ-0 ורשימת תהליכים חוקית.</span></div></div>';

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
        final+=sec3+Pindex+sec4+Pindex+sec5+(Ecounter+Pindex+1)+sec6+Pindex+sec7+Pindex+sec8+Pindex+sec9+Pindex+sec10
            +Pindex+sec11+Pindex+sec12+Pindex+sec13+Pindex+sec14+Pindex+sec15+Pindex+sec16+Pindex+sec17+Pindex+sec18
            +Pindex+sec19+Pindex+sec20+Pindex+sec21+Pindex+sec22+Pindex+sec23+Pindex+sec24;
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

