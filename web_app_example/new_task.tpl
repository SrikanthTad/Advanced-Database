<p>Welcome to the Todo list Application!</p>
<p>Add a new task to the ToDo list:</p>
<p>The open items are as follows:</p>

<a href="tasks" target="_self">View Tasks</a>&nbsp;&nbsp;&nbsp;&nbsp;


<form action="/new" method="POST">
  <input type="text" size="100" maxlength="100" name="task">
  <input type="submit" name="ADD" value="ADD">
  <input type="button" value="BACK" onclick="window.open('tasks', '_self')">
</form>