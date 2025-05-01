//la syntaxe


// les variables et les types

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.toggle').forEach(title => {
        title.addEventListener('click', () => {
            const content = title.nextElementSibling;
            if (content) {
                content.classList.toggle('hidden');
            }
        });
    });
});


// permiers pas 

// fonction et procedure

//boucle if / else

// boucle for

// boucle while

// tableau