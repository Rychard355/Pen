<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../styles/login.css">
    <title>Login - Pen</title>
</head>
<body>
    <main class="content-form">
        <form class="form-login" action="toCheck.php" method="post">
            <h2 class="login-title">Login</h2>

            <label class="content-entry-data" for="id-username">
                <span class="label-entry-data">Usuário:</span>
                <input class="entry-data" type="text" name="id-username" id="id-username" autocomplete="off" placeholder="username@gmail.com">
            </label>

            <label class="content-entry-data" for="password">
                <span class="label-entry-data">Senha:</span>
                <input class="entry-data" type="password" name="password" id="password" autocomplete="off" placeholder="***********">
            </label>

            <label class="content-checkbox" for="remember">
                <input class="remember" type="checkbox" name="remember" id="remember">
                <span class="label-checkbox">Lembre-se de min</span>
            </label>

            <input class="submit" type="submit" value="Entrar">
        </form>
        
        <span class="link"><a href="#">Esqueceu sua senha?</a> | <a href="register.php">Cadastrar-se</a></span>
    </main>
</body>
</html>