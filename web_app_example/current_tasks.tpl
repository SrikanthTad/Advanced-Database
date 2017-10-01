%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>Welcome to the Todo list Application!</p>
<p>Here is task list(View Tasks)</p>
<p>The open items are as follows:</p>

<a href="tasks" target="_self">View Tasks</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="new" target="_self">Add Tasks</a>

<table border="1">
    %for row in rows:
      <tr>
      %for col in row:
        <td>{{col}}</td>
      %end
        <td><input type="button" value="EDIT" name="EDIT" onclick="window.open('edit/{{row[0]}}', '_self')"></td>
        <td><input type="button" value="DELETE" name="DELETE" onclick="window.open('delete/{{row[0]}}', '_self')"></td>
        <td><input type="button" value="COMPLETE" name="COMPLETE" onclick="window.open('complete/{{row[0]}}', '_self')"></td>
      </tr>
    %end
</table>
