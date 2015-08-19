% rebase('base.tpl')
<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
    <h1 class="page-header">Schecule List</h1>    
    <div class="table-responsive">
        <table class="table table-striped">
            <thead>
            <tr>
                <th>Schedule Name</th>
                <th>AutoScaling Group</th>
                <th>Setting Time (UTC)</th>
                <th>Time</th>
                <th></th>
            </tr>
            </thead>
            <tbody>

            % for schedule in aschedule:
            <tr>
                <td>{{schedule["ScheduledActionName"]}}</td>
                <td>{{schedule["AutoScalingGroupName"]}}</td>
                <td>{{schedule["StartTime"]}}</td>                
                <td></td>
                <td>
                  <div class="input-group clockpicker-with-callbacks">
                    <input type="text" class="form-control" value={{schedule["StartTime"]}}>
                    <span class="input-group-addon">
                      <span class="glyphicon glyphicon-time"></span>
                    </span>
                    </div>
                  <script type="text/javascript">
                    var input = $('.clockpicker-with-callbacks').clockpicker({
                    donetext: 'Done',
                    init: function() {
                    console.log("colorpicker initiated");
                    },
                    beforeShow: function() {
                    console.log("before show");
                    },
                    afterShow: function() {
                    console.log("after show");
                    },
                    beforeHide: function() {
                    console.log("before hide");
                    },
                    afterHide: function() {
                    console.log("after hide");
                    },
                    beforeHourSelect: function() {
                    console.log("before hour selected");
                    },
                    afterHourSelect: function() {
                    console.log("after hour selected");
                    },
                    beforeDone: function() {
                    console.log("before done");
                    },
                    afterDone: function() {
                    times();
                    console.log("after done");
                    }
                    });

                    // Manually toggle to the minutes view
                    $('#check-minutes').click(function(e){
                    // Have to stop propagation here
                    e.stopPropagation();
                    input.clockpicker('show')
                    .clockpicker('toggleView', 'minutes');
                    });
                                    </script>
                </td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
</div>


