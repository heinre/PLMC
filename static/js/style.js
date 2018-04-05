


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
        $(".clickable-order-row").dblclick(function() {
            window.location="/orders/"+$(this).children('td')[0].innerHTML;
        });
        $("#delete").click(function() {
            $("#deleteModal").modal();
        });

        function deleteClient(id){
            $("#deleteModal").modal("hide");
            $.post("/clients/delete/", {'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(), 'id': id},
                function(data){
                if (data['status'] == 'success'){
                    window.location.href = './'
                }
                else{
                    window.location.href = './delete'
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
