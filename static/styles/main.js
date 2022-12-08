
      var button = document.getElementById("okay");
      button.innerText = "Ok";
  

      function killOk() {
        var killSwitchButton = document.getElementById("action");
        killSwitchButton.setAttribute('value','Kill Switch Pressed');
    
      }

      function autoModalWriter() {
        var ON = document.getElementById("status");
        ON.setAttribute('value','')
        if (document.getElementById("toggle-event").checked === true) {
          document.getElementById("autoModal").innerHTML =
            "You are about to turn autonomous mode " +
            document.getElementById("toggle-event").getAttribute("data-off");
          document.getElementById("taskNumber").classList.add("d-none")
        } else if (document.getElementById("toggle-event").checked === false) {
          document.getElementById("autoModal").innerHTML =
            "You are about to turn autonomous mode " +
            document.getElementById("toggle-event").getAttribute("data-on");
          document.getElementById("taskNumber").classList.remove("d-none")
          
          
        }
      }

    
   
      
      function onclickShifter() {
        
        if (document.getElementById("toggle-event").checked === true) {
          var ON = document.getElementById("status");
          var TASK = document.getElementById("task");
          // $("#toggle-event").attr("checked");
          ON.setAttribute('value','ON');
          TASK.setAttribute('value',$('select option:selected').val());

          // if(TASK.getAttribute("value") == 1){
          //   document.getElementById("tab2").classList.remove("d-none")
          //   var taskInitial = document.getElementById("taskZero");
          //   var currentTask = document.getElementById("taskOne");

          //   taskInitial.removeAttribute("selected");
          //   currentTask.setAttribute("selected","");
           
          // }
          // $("#modal-event").modal("hide");


          
          $("#toggle-event").bootstrapToggle("on", true);
          
          

        } else if (document.getElementById("toggle-event").checked === false) {
          var OFF = document.getElementById("status");
          var TASK = document.getElementById("task");

          OFF.setAttribute('value','OFF');
          TASK.setAttribute('value',$('select option:selected').val());
          
      
        }

       


        
      }
      function yesButton() {
        $("#modal-event").modal("hide");
      }
      function closeButton() {
        if (!$("#toggle-event").bootstrapToggle("off")) {
          $("#toggle-event").bootstrapToggle("on", true);
        }
        if ($(!"#toggle-event").bootstrapToggle("on")) {
          $("#toggle-event").bootstrapToggle("off", true);
        }
        $("#modal-event").modal("hide");
      }
      function togglerOntoOff() {
        $("#toggle-event").prop("disabled", false);
        $("#toggle-event").bootstrapToggle("off", true);
        $("#toggle-event").prop("disabled", true);
      }
      function togglerOfftoOn() {
        $("#toggle-event").prop("disabled", false);
        $("#toggle-event").bootstrapToggle("on", true);
        $("#toggle-event").prop("disabled", true);
      }
    