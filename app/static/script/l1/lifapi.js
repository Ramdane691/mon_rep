//la syntaxe


// les variables et les types




// permiers pas 

// fonction et procedure

//boucle if / else

// boucle for

// boucle while

// tableau

function verifierCarre() {
    const reponse = document.getElementById("code-carre").value.replace(/\s+/g, '');
    const attendu = "floataireCarre(floatcote){returncote*cote;}";

    const result = document.getElementById("result-carre");

    if (reponse === attendu) {
        result.textContent = "✅ Juste !";
        result.style.color = "green";
    } else {
        result.textContent = "❌ Faux. Vérifie ta syntaxe.";
        result.style.color = "red";
    }
}

// URL du backend Flask (Render ou local)
const BACKEND_URL =
    window.location.hostname === "localhost"
        ? "http://127.0.0.1:5000"
        : "https://lil1.onrender.com"; // 🔁 remplace par ton URL Render finale

function testerCode(id, expected) {
    const textarea = document.getElementById("code-" + id);
    const output = document.getElementById("resultat-" + id);

    const formData = new FormData();
    formData.append("code", textarea.value);

    console.log("➡️ Envoi du code :", textarea.value);

    fetch("https://lil1-backend.onrender.com/compile/", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        console.log("✅ Réponse reçue :", data);
        if (data.output !== undefined) {
            if (data.output.trim() === expected) {
                output.textContent = "✅ Correct !";
                output.style.color = "green";
            } else {
                output.textContent = "❌ Faux. Sortie obtenue : " + data.output;
                output.style.color = "red";
            }
        } else {
            output.textContent = "❌ Erreur : " + (data.error || "inconnue");
            output.style.color = "red";
        }
    })
    .catch(err => {
        console.error("❌ Erreur fetch :", err);
        output.textContent = "❌ Erreur de requête.";
        output.style.color = "red";
    });
}
