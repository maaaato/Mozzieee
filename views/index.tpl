% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
    <h1 class="page-header">Schecule List</h1>

    <div class="table-responsive">
        <table class="table table-striped">
            <thead>
            <tr>
                <th>id</th>
                <th>タイトル</th>
                <th>価格</th>
                <th>メモ</th>
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
                <div class="input-group clockpicker">
                    <input type="text" class="form-control" value="09:30">
                            <span class="input-group-addon">
                                            <span class="glyphicon glyphicon-time"></span>
                            </span>
                </div>
                    <script type="text/javascript">
                    $('.clockpicker').clockpicker();
                    </script>
                </td>
            </tr>
            % end
            </tbody>
        </table>
    </div>
</div>