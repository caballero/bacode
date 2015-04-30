%#template for the form for a new job
<h2>Agregar un nuevo trabajo disponible:</h2>
<form action="/new" method="GET">
<p>Nombre:</p>
<input type="text" size="60" maxlength="100" name="name">
<p>Descripción:</p>
<input type="text" size="60" maxlength="100" name="description">
<p>Responsable:</p>
<input type="text" size="60" maxlength="100" name="teacher">
<p>Habiliades requeridas:</p>
<input type="text" size="60" maxlength="100" name="skills">
<input type="submit" name="save" value="save">
</form>
