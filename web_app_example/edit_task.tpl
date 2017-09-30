<p>Edit an existing task in the ToDo list:</p>
<form action="/edit/{{id}}" method="POST">
  <input type="text" size="100" maxlength="100" name="task">{{text}}</input>
  <input type="submit" name="SAVE" value="SAVE">
  <input type="button" value="BACK" name="BACK" onclick="window.open('../tasks', '_self')">
</form>