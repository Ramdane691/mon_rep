function verifierCommande1() {
    const input = document.getElementById("reponse1").value.trim();
    const resultat = document.getElementById("resultat1");

    // Réponse(s) acceptée(s)
    const bonnesReponses = ["ls", "ls ."];

    if (bonnesReponses.includes(input)) {
        resultat.textContent = "✅ Correct !";
        resultat.style.color = "green";
    } else {
        resultat.textContent = "❌ Faux. Essaie encore.";
        resultat.style.color = "red";
    }
}