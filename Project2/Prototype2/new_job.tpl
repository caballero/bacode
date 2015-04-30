%#template for the form for a new job
<h2>Agregar un nuevo trabajo disponible</h2>
<form action="/new" method="GET">
<p>Nombre: <input type="text" size="60" maxlength="100" name="name"> </p>
<p>Descripción: <input type="text" size="60" maxlength="100" name="description"></p>
<p>Responsable: <input type="text" size="60" maxlength="100" name="teacher"></p>
<p>Habilidades requeridas: <input type="text" size="60" maxlength="100" name="skills"></p>
<br>
<input type="submit" name="save" value="save">
</form>
