var sec1='<div class="row"><div class="col-lg-2"><select class="form-control" name="';
var sec2='"><option style="display: none;" selected>';
var sec2a ='</option>';
var sec3='</select></div><div class="col-lg-10"><input name="';
var sec4='" type="text" class="form-control" placeholder="';
var sec4a = '"><br></div></div>';
var Pindex = 0;
$(document).ready(function () {
    addProduct();
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
    console.log(Pindex++);
}

function removeProduct() {
    if(Pindex  == 1){
        return;
    }
    /*$(".fields > .row:last").remove();
    Pindex--;
    document.getElementById('Pcounter').value = Pindex;*/
    console.log(--Pindex);
}