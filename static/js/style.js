



/*=============================================================
    Authour URI: www.binarytheme.com
    License: Commons Attribution 3.0
    http://creativecommons.org/licenses/by/3.0/
    100% To use For Personal And Commercial Use.
    IN EXCHANGE JUST GIVE US CREDITS AND TELL YOUR FRIENDS ABOUT US

    ========================================================  */


(function ($) {
    "use strict";
    var mainApp = {

        main_fun: function () {

            /*====================================
              LOAD APPROPRIATE MENU BAR
           ======================================*/
            $(window).bind("load resize", function () {
                if ($(this).width() < 768) {
                    $('div.sidebar-collapse').addClass('collapse')
                } else {
                    $('div.sidebar-collapse').removeClass('collapse')
                }
            });



        },

        initialization: function () {
            mainApp.main_fun();

        }

    }
    // Initializing ///

    $(document).ready(function () {
        mainApp.main_fun();
    });

}(jQuery));
        $(".clickable-client-row").dblclick(function() {
            window.location="/clients/"+$(this).children('td')[0].innerHTML;
        });
        $(".clickable-potential-row").dblclick(function() {
            window.location="/clients/potential/"+$(this).children('td')[0].innerHTML;
        });
        $(".clickable-order-row").dblclick(function() {
            window.location="/orders/"+$(this).children('td')[0].innerHTML;
        });
        $(".clickable-product-row").dblclick(function() {
            var features = "innerHeight=320,location=no";
            var strWindowFeatures = "menubar=no,location=no,resizable=no,scrollbars=no,status=yes";
           // window.open("/orders/product/parameters/" +$(this).children('td')[0].innerHTML, "parameters",features);
            window.open("/orders/product/parameters/" +$(this).children('td')[0].innerHTML, "parameters",
                "toolbar=0,location=0,status=0,menubar=0,scrollbars=0,resizable=0,width=540,height=320");
        });
        $(".clickable-coc-row").dblclick(function() {
            window.open("/reports/coc/" +$(this).children('td')[0].innerHTML);
        });
        $(".clickable-worker-row").dblclick(function() {
            window.location="/workers/"+$(this).children('td')[0].innerHTML;
        });
        $(".clickable-shift-row").dblclick(function() {
            str=$(this).children('td')[0].innerHTML;
            window.location="/workers/"+str.substr(0,str.indexOf('-')-1);
        });
        $(".clickable-schedule-row").dblclick(function() {
            name=$(this).children('td')[0].innerHTML;
            amount=$(this).children('td')[2].innerHTML;
            p_time=$(this).children('td')[5].innerHTML;
            id=$(this).children('td')[6].innerHTML;
            process=$(this).children('td')[7].innerHTML;
            $.get("/productionFloor/wip", {'id': id, 'process': process, 'name': name, 'amount': amount,
                                             'p_time': p_time}, function (data) {
                $("#page-inner").html(data);
            });
        });

        $(document).on("click", "#end", function () {
            $("#endModal").modal();
        });

        $("#delete").click(function() {
            $("#deleteModal").modal();
        });


        function deleteClient(id){
            $("#deleteModal").modal("hide");
            $.post("/clients/delete/", {'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(), 'id': id},
                function(data){
                if (data['status'] == 'success'){
                    window.location.href = './';
                }
                else{
                    window.location.href = './delete';

                }
            });
        }

        function deletePotential(id){
            $("#deleteModal").modal("hide");
            $.post("/clients/potential/delete/", {'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(), 'id': id},
                function(data){
                if (data['status'] == 'success'){
                    window.location.href = './';
                }
                else{
                    window.location.href = './delete';

                }
            });
        }

        function deleteOrder(id){
            $("#deleteModal").modal("hide");
            $.post("/orders/delete/", {'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(), 'id': id},
                function(data){
                if (data['status'] == 'success'){
                    window.location.href = './'
                }
                else{
                    window.location.href = './delete'
                }
            });
        }

        function deleteProduct(id, orderId){
            $("#deleteModal").modal("hide");
            $.post("/orders/product/delete/", {'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(), 'id': id},
                function(data){
                if (data['status'] == 'success'){
                    window.location.href = './../../'+orderId;
                }
                else{
                    window.location.href = './0';

                }
            });
        }

        function deleteStation(id){
            $("#deleteModal").modal("hide");
            $.post("/productionFloor/stations/delete/", {'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(), 'id': id},
                function(data){
                if (data['status'] == 'success'){
                    window.location.href = '../../'
                }
                else{
                    window.location.href = '../delete'
                }
            });
        }

        function deleteWorker(id){
            $("#deleteModal").modal("hide");
            $.post("/workers/delete/", {'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(), 'id': id},
                function(data){
                if (data['status'] == 'success'){
                    window.location.href = './'
                }
                else{
                    window.location.href = './delete'
                }
            });
        }
        function transformPotential(id){
            $.post("/clients/potential/transform/", {'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(), 'id': id},
                function(data){
                if (data['status'] == 'success'){
                    window.location.href = '../'+data['id'];
                }
                else{
                    window.location.href = './delete';
                }
            });
        }
        function deleteForm(id,form){
            if (form == 'coc'){
                $("#dButton").attr("onclick",'deleteCOC('+id+')');
            }
            else{
                $("#dButton").attr("onclick",'deleteRouting('+id+')');
            }
            $("#deleteModal").modal();
        }
        function deleteCOC(id){
            $.post("../../reports/coc/delete/", {'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
                    'id': id},
                function(data){
                if (data['status'] == 'success'){
                    window.location.href = '../'+data['order'];
                }
                else{
                    window.location.href = '../../reports/coc/delete/';
                }
            });
        }
        function deleteRouting(id){
            $.post("../../reports/routing/delete/", {'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
                    'id': id},
                function(data){
                if (data['status'] == 'success'){
                    window.location.href = '../'+data['order'];
                }
                else{
                    window.location.href = '../../reports/routing/delete/';
                }
            });
        }
        function setCharAt(str,index,chr) {
            if(index > str.length-1) return str;
            return str.substr(0,index) + chr + str.substr(index+1);
        }
        function updateAvailability(shift){
            if ($("#shift"+shift).is(':checked')){
                $("#id_availability").val(setCharAt($("#id_availability").val(),shift,'o'))
            }
            else{
                $("#id_availability").val(setCharAt($("#id_availability").val(),shift,'x'))
            }
        }

        function sortTable(n,t) {
          var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
          table = document.getElementsByTagName("table")[t];
          switching = true;
          // Set the sorting direction to ascending:
          dir = "asc";
          /* Make a loop that will continue until
          no switching has been done: */
          while (switching) {
            // Start by saying: no switching is done:
            switching = false;
            rows = table.getElementsByTagName("tr");
            /* Loop through all table rows (except the
            first, which contains table headers): */
            for (i = 1; i < (rows.length - 1); i++) {
              // Start by saying there should be no switching:
              shouldSwitch = false;
              /* Get the two elements you want to compare,
              one from current row and one from the next: */
              x = rows[i].getElementsByTagName("TD")[n];
              y = rows[i + 1].getElementsByTagName("TD")[n];
              /* Check if the two rows should switch place,
              based on the direction, asc or desc: */
              if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                  // If so, mark as a switch and break the loop:
                  shouldSwitch= true;
                  break;
                }
              } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                  // If so, mark as a switch and break the loop:
                  shouldSwitch= true;
                  break;
                }
              }
            }
            if (shouldSwitch) {
              /* If a switch has been marked, make the switch
              and mark that a switch has been done: */
              rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
              switching = true;
              // Each time a switch is done, increase this count by 1:
              switchcount ++;
            } else {
              /* If no switching has been done AND the direction is "asc",
              set the direction to "desc" and run the while loop again. */
              if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
              }
            }
          }
        }