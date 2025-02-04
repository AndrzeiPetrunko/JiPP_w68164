open System
//ZADANIE 1
printfn"Zadanie 1"
printf "Wprowadź wagę (kg): "
let waga = Console.ReadLine() |> float
printf "Wprowadź wzrost (cm): "
let wzrost = (Console.ReadLine() |> float)/100.00
let bmi = waga/(wzrost*wzrost)
let bmiwynik bmi =
    if bmi < 18.5 then
        printfn "Waga niedostateczna %F" bmi
    elif bmi > 29.9 then
        printfn "Waga zbytnia %F" bmi
    else 
        printfn"Waga normalna %F" bmi
bmiwynik bmi
printfn " "

//ZADANIE 2
printfn"Zadanie 2"
let kursyWymiany =
    Map [
        ("USD", "EUR"), 0.85
        ("USD", "GBP"), 0.75
        ("EUR", "USD"), 1.18
        ("EUR", "GBP"), 0.88
        ("GBP", "USD"), 1.33
        ("GBP", "EUR"), 1.14
    ]

let przeliczWalute kwota walutaZ walutaDo =
    match Map.tryFind (walutaZ, walutaDo) kursyWymiany with
    | Some kurs -> Some (kwota * kurs)
    | None -> None

let wykonajKonwersje () =
    printf "Podaj kwotę do przeliczenia: "
    let kwota = Console.ReadLine() |> float
    printf "Podaj walutę źródłową (np. USD, EUR, GBP): "
    let walutaZ = Console.ReadLine().ToUpper()
    printf "Podaj walutę docelową: "
    let walutaDo = Console.ReadLine().ToUpper()
    
    match przeliczWalute kwota walutaZ walutaDo with
    | Some przeliczonaKwota -> printfn "Przeliczona kwota: %.2f %s" przeliczonaKwota walutaDo
    | None -> printfn "Nieobsługiwana para walut."
wykonajKonwersje()
printfn " "

//ZADANIE 3
printfn"Zadanie 3"
let liczSlowa (tekst: string) =
    tekst.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries)
    |> Array.length

let liczZnakiBezSpacji (tekst: string) =
    tekst.Replace(" ", "").Length

let najczestszeSlowo (tekst: string) =
    let slowa = tekst.ToLower().Split([|' '; '\t'; '\n'; '\r'; '.'; ','; '!'|], StringSplitOptions.RemoveEmptyEntries)
    let licznik =
        slowa
        |> Array.groupBy id
        |> Array.map (fun (slowo, wystapienia) -> (slowo, wystapienia.Length))
        |> Array.sortByDescending snd
    if licznik.Length > 0 then Some (fst licznik.[0]) else None

let analizujTekst () =
    printf "Wpisz tekst do analizy: "
    let tekst = Console.ReadLine()
    printfn "Liczba słów: %d" (liczSlowa tekst)
    printfn "Liczba znaków (bez spacji): %d" (liczZnakiBezSpacji tekst)
    match najczestszeSlowo tekst with
    | Some slowo -> printfn "Najczęściej występujące słowo: %s" slowo
    | None -> printfn "Brak słów w tekście."

analizujTekst()
printfn " "

//ZADANIE 4
printfn"Zadanie 4"
type Konto = { Numer: string; Saldo: decimal }

let mutable konta = Map.empty<string, Konto>

let stworzKonto numer =
    if Map.containsKey numer konta then
        printfn "Konto o numerze %s już istnieje." numer
    else
        konta <- konta.Add(numer, { Numer = numer; Saldo = 0m })
        printfn "Konto o numerze %s zostało utworzone." numer

let depozyt numer kwota =
    match konta.TryFind numer with
    | Some konto ->
        let noweKonto = { konto with Saldo = konto.Saldo + kwota }
        konta <- konta.Add(numer, noweKonto)
        printfn "Wpłacono %.2f. Nowe saldo: %.2f" kwota noweKonto.Saldo
    | None -> 
        printfn "Konto o numerze %s nie istnieje." numer

let wyplata numer kwota =
    match konta.TryFind numer with
    | Some konto when konto.Saldo >= kwota ->
        let noweKonto = { konto with Saldo = konto.Saldo - kwota }
        konta <- konta.Add(numer, noweKonto)
        printfn "Wypłacono %.2f. Nowe saldo: %.2f" kwota noweKonto.Saldo
    | Some _ -> 
        printfn "Brak wystarczających środków na koncie."
    | None -> 
        printfn "Konto o numerze %s nie istnieje." numer

let pokazSaldo numer =
    match konta.TryFind numer with
    | Some konto -> 
        printfn "Saldo konta %s: %.2f" numer konto.Saldo
    | None -> 
        printfn "Konto o numerze %s nie istnieje." numer

let menu () =
    let rec loop () =
        printfn "\n1. Stwórz konto"
        printfn "2. Wpłać środki"
        printfn "3. Wypłać środki"
        printfn "4. Sprawdź saldo"
        printfn "5. Wyjście"
        printf "Wybierz opcję: "
        match Console.ReadLine() with
        | "1" -> 
            printf "Podaj numer konta: " 
            let numer = Console.ReadLine()
            stworzKonto numer
            loop()
        | "2" -> 
            printf "Podaj numer konta: " 
            let numer = Console.ReadLine()
            printf "Podaj kwotę: " 
            try 
                let kwota = Decimal.Parse(Console.ReadLine())
                depozyt numer kwota
            with 
            | :? FormatException -> printfn "Niepoprawny format kwoty."
            loop()
        | "3" -> 
            printf "Podaj numer konta: " 
            let numer = Console.ReadLine()
            printf "Podaj kwotę: " 
            try 
                let kwota = Decimal.Parse(Console.ReadLine())
                wyplata numer kwota
            with 
            | :? FormatException -> printfn "Niepoprawny format kwoty."
            loop()
        | "4" -> 
            printf "Podaj numer konta: " 
            let numer = Console.ReadLine()
            pokazSaldo numer
            loop()
        | "5" -> 
            printfn "Koniec programu."
        | _ -> 
            printfn "Niepoprawna opcja."
            loop()
    loop()
menu()
printfn " "
//ZADANIE 5
printfn"Zadanie 5"
open System

type Symbol = X | O | Empty

let stworzPlansze () : Symbol[] = Array.create 9 Empty

let wyswietlPlansze (plansza: Symbol[]) =
    let symbolDoTekstu = function
        | X -> "X"
        | O -> "O"
        | Empty -> " "
    for i in 0 .. 8 do
        if i % 3 = 0 && i > 0 then printfn ""
        printf " %s " (symbolDoTekstu plansza.[i])
        if i % 3 <> 2 then printf "|"
    printfn "\n"

let sprawdzWygrana (plansza: Symbol[]) =
    let wygrywajaceKombinacje = [
        [0; 1; 2]; [3; 4; 5]; [6; 7; 8]  // wiersze
        [0; 3; 6]; [1; 4; 7]; [2; 5; 8]  // kolumny
        [0; 4; 8]; [2; 4; 6]             // przekątne
    ]
    let sprawdzKombinacje kombinacja =
        let symbole = kombinacja |> List.map (fun i -> plansza.[i])
        match symbole with
        | [X; X; X] -> Some X
        | [O; O; O] -> Some O
        | _ -> None
    wygrywajaceKombinacje |> List.tryPick sprawdzKombinacje

let sprawdzRemis (plansza: Symbol[]) =
    plansza |> Array.forall (fun pole -> pole <> Empty)

let wykonajRuch (plansza: Symbol[]) pozycja symbol =
    if plansza.[pozycja] = Empty then
        plansza.[pozycja] <- symbol
        true
    else
        false

let ruchKomputera (plansza: Symbol[]) =
    let pustePola = [for i in 0 .. 8 do if plansza.[i] = Empty then yield i]
    let losowaPozycja = pustePola.[Random().Next(pustePola.Length)]
    plansza.[losowaPozycja] <- O

let rec gra (plansza: Symbol[]) =
    wyswietlPlansze plansza
    match sprawdzWygrana plansza with
    | Some X -> printfn "Gracz wygrywa!"
    | Some O -> printfn "Komputer wygrywa!"
    | None when sprawdzRemis plansza -> printfn "Remis!"
    | None ->
        printf "Wybierz pozycję (0-8): "
        match Int32.TryParse(Console.ReadLine()) with
        | (true, pozycja) when pozycja >= 0 && pozycja < 9 ->
            if wykonajRuch plansza pozycja X then
                if sprawdzWygrana plansza = None && not (sprawdzRemis plansza) then
                    ruchKomputera plansza
                gra plansza
            else
                printfn "To pole jest już zajęte."
                gra plansza
        | _ ->
            printfn "Niepoprawna pozycja. Spróbuj ponownie."
let plansza = stworzPlansze()
gra plansza