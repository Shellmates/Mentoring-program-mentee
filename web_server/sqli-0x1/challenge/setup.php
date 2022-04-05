<?php
    $username = "admin";
    $salt = bin2hex(random_bytes(4));
    $password_hash = hash("sha256", random_bytes(16));
    $db = new SQLite3("/var/db.sqlite");
    $db->exec("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)");
    $db->exec("INSERT INTO users VALUES ('$username', '$password_hash\$$salt')");
    $db->close();
?>
