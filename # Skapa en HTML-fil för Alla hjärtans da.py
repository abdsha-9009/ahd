# Skapa en HTML-fil för Alla hjärtans dag
html_content = """
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alla hjärtans dag</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #ffe6f2;
            text-align: center;
            padding: 50px;
            overflow: hidden;
            position: relative;
        }
        h1 {
            color: #ff4d4d;
            font-size: 3rem;
            margin-bottom: 20px;
        }
        p {
            color: #333;
            font-size: 1.5rem;
            margin: 10px 0;
        }
        .hearts, .flowers, .teddies {
            font-size: 2rem;
            margin: 20px 0;
        }
        .hearts {
            color: #ff4d4d;
        }
        .flowers {
            color: #4dff4d;
        }
        .teddies {
            color: #996633;
        }
        .button {
            background-color: #ff4d4d;
            color: white;
            padding: 15px 30px;
            font-size: 1.5rem;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 20px;
        }
        .button:hover {
            background-color: #e60000;
        }
        .heart {
            position: absolute;
            color: #ff4d4d;
            font-size: 2rem;
            animation: float 5s infinite ease-in-out;
        }
        @keyframes float {
            0% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0); }
        }
    </style>
</head>
<body>
    <h1>❤️ Vill du bli min Valentine? ❤️</h1>
    <p>Käraste [Hennes namn],</p>
    <p>Jag har något mycket viktigt att fråga dig...</p>
    <p>Vill du bli min Valentine och dela alla framtida Alla hjärtans dagar med mig? ❤️</p>
    <div class="hearts">
        ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
    </div>
    <div class="flowers">
        🌸🌼🌺🌻🌷🌹💐🌸🌼🌺🌻🌷🌹💐
    </div>
    <div class="teddies">
        🧸🧸🧸🧸🧸🧸🧸🧸🧸🧸🧸🧸🧸🧸
    </div>
    <button class="button" onclick="alert('Jag älskar dig! ❤️')">Ja, jag vill!</button>

    <!-- Animationer av hjärtan -->
    <div class="heart" style="left: 10%; top: 20%;">❤️</div>
    <div class="heart" style="left: 20%; top: 50%;">❤️</div>
    <div class="heart" style="left: 30%; top: 80%;">❤️</div>
    <div class="heart" style="left: 40%; top: 30%;">❤️</div>
    <div class="heart" style="left: 50%; top: 60%;">❤️</div>
    <div class="heart" style="left: 60%; top: 10%;">❤️</div>
    <div class="heart" style="left: 70%; top: 40%;">❤️</div>
    <div class="heart" style="left: 80%; top: 70%;">❤️</div>
    <div class="heart" style="left: 90%; top: 20%;">❤️</div>
</body>
</html>
"""

# Ersätt [Hennes namn] och [Ditt namn] med riktiga namn
html_content = html_content.replace("[Hennes namn]", "Emma")  # Byt ut "Emma" till hennes namn
html_content = html_content.replace("[Ditt namn]", "Alex")    # Byt ut "Alex" till ditt namn

# Spara HTML-innehållet till en fil
with open("alla_hjartans_dag.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Filen 'alla_hjartans_dag.html' har skapats! Skicka den till din flickvän. ❤️")
