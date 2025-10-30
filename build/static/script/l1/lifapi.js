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


function testerCode(id, expected) {
    const textarea = document.getElementById("code-" + id);
    const output = document.getElementById("resultat-" + id);

    const formData = new FormData();
    formData.append("code", textarea.value);

    fetch("/compile", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.result !== undefined) {
            if (data.result.trim() === expected) {
                output.textContent = "✅ Correct !";
                output.style.color = "green";
            } else {
                output.textContent = "❌ Faux. Sortie obtenue : " + data.result;
                output.style.color = "red";
            }
        } else {
            output.textContent = "❌ Erreur : " + (data.error || "inconnue");
            output.style.color = "red";
        }
    })
    .catch(err => {
        output.textContent = "❌ Erreur de requête.";
        output.style.color = "red";
    });
}




