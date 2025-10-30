function verifScheme() {
    const input = document.getElementById("rep-scheme").value.trim();
    const solution = "(define (somme lst) (if (null? lst) 0 (+ (car lst) (somme (cdr lst)))))";
    const result = document.getElementById("rep-scheme-resultat");

    if (input.replace(/\s+/g, '') === solution.replace(/\s+/g, '')) {
        result.textContent = "✅ Correct !";
        result.style.color = "green";
    } else {
        result.textContent = "❌ Pas encore. Vérifie la syntaxe.";
        result.style.color = "red";
    }
}