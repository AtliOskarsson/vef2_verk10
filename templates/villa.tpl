<!DOCTYPE html>
<html>
<head>
	<title>log-in</title>
	<link rel="stylesheet" type="text/css" href="css/styles.css">
</head>
<body>
	<form action="/login" method="post">
		{{ villa }}
		<h1>Login</h1>
		<label>Notendanafn</label><br>
			<input type="text" name="notendanafn"><br>
		<label>Lykilorð</label><br>
			<input type="password" name="lykilord"><br>
		<input type="submit" name="submit" value="Login" class="input"><br>
		<input type="submit" name="submit" value="Sign-up" class="input">

	</form>

</body>
</html>