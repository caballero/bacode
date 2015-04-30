%#template for the form for a new teacher
<h2>Agregar un profesor nuevo</h2>
<form action="/new" method="GET">
<p>Nombre:</p>
<input type="text" size="60" maxlength="100" name="name">
<p>Correo:</p>
<input type="text" size="60" maxlength="100" name="email">
<p>Afiliación:</p>
<input type="text" size="60" maxlength="100" name="affiliation">
<p>Teléfono:</p>
<input type="text" size="60" maxlength="100" name="phone">
<p>Intereses de investigación:</p>
<input type="text" size="60" maxlength="100" name="interest">
<input type="submit" name="save" value="save">
</form>
