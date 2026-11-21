function runEjemplo1() {
    const patron = /^ab*$/;

    const palabras = ["a", "ab", "abbb", "abab", "b", ""];

    for (const palabra of palabras) {
        console.log(`${palabra} => ${patron.test(palabra)}`);
    }
}

function runEjemplo2() {
    const regex = /^[TO][0-9]{3}$/;

    const lista = ["T001", "O120", "T01", "X001", "T0001"];

    for (const elemento of lista) {
        console.log(`${elemento} => ${regex.test(elemento)}`);
    }
}

function runEjemplo3() {
    const texto =
        "Sensores: T001 reporta 23.5 C ; O001 reporta 12 PERSONAS; T002 reporta -2 C.";

    const patron = /T[0-9]{3}/g;

    let coincidencia;

    while ((coincidencia = patron.exec(texto)) !== null) {
        console.log(
            `Encontrado: ${coincidencia[0]}, posición: ${coincidencia.index}`
        );
    }
}

function main() {
    runEjemplo1();
    runEjemplo2();
    runEjemplo3();
}

main();
