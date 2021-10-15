username = input("type your name: ")
print("hello " + username)

print("Je woont in Afghanistan, er breekt een oorlog uit en het is niet langer veilig waar je woont.")
print("A = vlucht zonder je familie naar het buurland Iran om in veiligheid te komen. [2] ")
print("B = Je probeert een veilige plek in Afghanistan te zoeken. [7] ")
answer = input("type A or B: ")

if answer == "A" or answer == "a":
    print("Je bent in Iran aangekomen, je komt erachter dat het in Iran ook niet veilig is.")
    print("Je besluit door te vluchten naar Turkije, om een inburgering aan te vragen.")
    print("Je wordt niet toegelaten in Turkije en moet weg uit Turkije gaan. ")
    print("A = Je vlucht met een gammel bootje naar Griekenland. [3] ")
    print("B = Je probeert te voet door Turkije te reizen tot je in Bulgarije aan komt. [8] ")
    antwoord = input("type A or B ")

    if antwoord == "A" or antwoord == "a":
        print("Het is je gelukt om een boot ticket te krijgen om naar Griekenland te vluchten.")
        print("Je bent net aan in Griekenland beland en ziet dat de politie er aan komt in de verte. ")
        print("A = je wacht tot de politie komt, hopen dat je geholpen wordt. [4] ")
        print("B = je probeert te vluchten omdat je de politie niet vertrouwd. [4]  ")
        tekst = input("type A or B: ")

        if tekst == "A" or tekst == "a":
            print("Je wordt door de politie aangehouden vanwege illegale immigratie.")
            print("Je wordt in een gevangenis gestopt en word na een tijdje weer vrijgelaten,")
            print("maar je moet wel naar een ander land toe omdat Griekenland al te veel vluchtelingen heeft. ")
            print("A = je gaat naar Frankrijk omdat je naar Engeland of Amerika wilt omdat je Engels kan. [14] ")
            print("B = je besluit om naar Nederland te gaan omdat je hebt gehoord dat je daar toegelaten wordt. [5] ")
            keuze = input("type A or B")

            if keuze == "A" or keuze =="a":
                print("Je bent na een lange reis in Frankrijk aangekomen je probeert eerst in Frankrijk te blijven,")
                print("maar word weer doorgestuurd naar een ander land.")
                print("Je koopt een boot ticket naar Amerika en zodra je daar aan komt,")
                print("zie je dat de politie controleert op illegale immigranten.")
                print("A = je loopt door in de hoop dat je geholpen wordt [11] ")
                print("B = je probeert de politie te ontwijken [11] ")
                verhaal = input("type A or B: ")

                if verhaal == "A" or verhaal == "a":
                    print("Je wordt opgepakt door de politie en in de gevangenis gestopt. ")
                
                elif verhaal == "B" or verhaal == "b":
                    print("Je wordt opgepakt door de politie en in de gevangenis gestopt. ")
            
            elif keuze == "B" or keuze == "b":
                print("Je komt na een hele lange reis via smokkelaars terecht in Nederland.")
                print("Je gaat naar de overheid om een inburgering aan te vragen.")
                print("Je wordt in een kamp met andere vluchtelingen gezet en ondervraagt over je verhaal.")
                print("“Waarom ben je gevlucht? Hoe ben je in Nederland gekomen?” ")
                print("A = je besluit om de waarheid te spreken [6] ")
                print("B = je besluit om een verhaal op te maken waarmee je denkt dat je meer kans hebt om te mogen blijven [15] ")
                choice = input("type A or B: ")

                if choice == "A" or choice == "a":
                    print("Na een paar maanden krijg je te horen dat je bent toegelaten en je wordt geholpen om je aan te passen zoals,")
                    print("de taal leren in een speciale klas met meer vluchtelingen en er wordt geholpen om je aan een baan te krijgen.")
                    print("Er word ook geholpen om je familie te halen. ")

                elif choice == "B" or choice == "b":
                    print("Je wordt door iemand gewaarschuwd dat de overheid erachter is gekomen dat je verhaal niet waar is.") 
                    print("A = je probeert te vluchten omdat je verwacht dat je wordt teruggestuurd of in de gevangenis wordt gestopt. [16]")
                    print("B = je blijft rustig en probeert je verhaal alsnog te vertellen maar dan de waarheid dit keer [16] ")
                    option = input("type A or B: ")

                    if option == "A" or option == "a":
                        print("Je wordt teruggestuurd naar je eigen land ")

                    elif option == "B" or option == "b":
                        print("Je wordt teruggestuurd naar je eigen land ")

    elif antwoord == "B" or antwoord == "b":
        print("Je wordt door de politie aangehouden vanwege illegale immigratie.")
        print("Je wordt in een gevangenis gestopt en word na een tijdje weer vrijgelaten,")
        print("maar je moet wel naar een ander land toe omdat Griekenland al te veel vluchtelingen heeft.") 
        print("A = je gaat naar Frankrijk omdat je naar Engeland of Amerika wilt omdat je Engels kan. [14]") 
        print("B = je besluit om naar Nederland te gaan omdat je hebt gehoord dat je daar toegelaten wordt. [5] ")
        multiple = input("type A or B")

        if multiple == "A" or multiple == "a":
            print("Je bent na een lange reis in Frankrijk aangekomen je probeert eerst in Frankrijk te blijven,")
            print("maar word weer doorgestuurd naar een ander land.")
            print("Je koopt een boot ticket naar Amerika en zodra je daar aan komt zie je dat de politie controleert op illegale immigranten.")
            print("A = je loopt door in de hoop dat je geholpen wordt [11] ")
            print("B = je probeert de politie te ontwijken [11] ")
            keuzen = input("type A or B: ")

            if keuzen == "A" or keuzen == "a":
                print("Je wordt opgepakt door de politie en in de gevangenis gestopt. ")

            elif keuzen == "B" or keuzen == "b":
                print("Je wordt opgepakt door de politie en in de gevangenis gestopt. ")

        elif multiple == "B" or multiple == "b":
            print("Je komt na een hele lange reis via smokkelaars terecht in Nederland.")
            print("Je gaat naar de overheid om een inburgering aan te vragen.")
            print("Je wordt in een kamp met andere vluchtelingen gezet en ondervraagt over je verhaal.")
            print("“Waarom ben je gevlucht? Hoe ben je in Nederland gekomen?” ")
            print("A = je besluit om de waarheid te spreken [6]") 
            print("B = je besluit om een verhaal op te maken waarmee je denkt dat je meer kans hebt om te mogen blijven [15] ")
            choices = input("type A or B: ")

            if choices == "A" or choices == "a":
                print("Na een paar maanden krijg je te horen dat je bent toegelaten en je wordt geholpen om je aan te passen zoals,")
                print("de taal leren in een speciale klas met meer vluchtelingen en er wordt geholpen om je aan een baan te krijgen.")
                print("Er word ook geholpen om je familie te halen. ")

            elif choices == "B" or choices == "b":
                print("Je wordt door iemand gewaarschuwd dat de overheid erachter is gekomen dat je verhaal niet waar is.") 
                print("A = je probeert te vluchten omdat je verwacht dat je wordt teruggestuurd of in de gevangenis wordt gestopt. [16]") 
                print("B = je blijft rustig en probeert je verhaal alsnog te vertellen maar dan de waarheid dit keer [16] ")
                hulp = input("type A or B")

                if hulp == "A" or hulp == "a":
                    print("Je wordt teruggestuurd naar je eigen land ")

                elif hulp == "B" or hulp == "b":
                    print("Je wordt teruggestuurd naar je eigen land ")

elif answer == "B" or answer == "b":
    print("Je hebt een veilige plek gevonden en kan daar blijven.")
    print("Na een half jaar is de oorlog erger geworden en moet je alsnog naar een ander land vluchten. [2] ")
    print("A = vlucht alsnog naar een ander land.")
    oke = input("type A: ")

    if oke == "A" or oke == "a":
        print("Je bent in Iran aangekomen, je komt erachter dat het in Iran ook niet veilig is.")
        print("Je besluit door te vluchten naar Turkije, om een inburgering aan te vragen.")
        print("Je wordt niet toegelaten in Turkije en moet weg uit Turkije gaan. ")
        print("A = Je vlucht met een gammel bootje naar Griekenland. [3] ")
        print("B = Je probeert te voet door Turkije te reizen tot je in Bulgarije aan komt. [8] ")
        vluchten = input("type A or B: ")

        if vluchten == "A" or vluchten == "a":
            print("Het is je gelukt om een boot ticket te krijgen om naar Griekenland te vluchten.")
            print("Je bent net aan in Griekenland beland en ziet dat de politie er aan komt in de verte. ")
            print("A = je wacht tot de politie komt, hopen dat je geholpen wordt. [4] ")
            print("B = je probeert te vluchten omdat je de politie niet vertrouwd. [4] ")
            optie = input("type A or B: ")

            if optie == "A" or optie == "a":
                print("Je wordt door de politie aangehouden vanwege illegale immigratie.")
                print("Je wordt in een gevangenis gestopt en word na een tijdje weer vrijgelaten,")
                print("maar je moet wel naar een ander land toe omdat Griekenland al te veel vluchtelingen heeft.") 
                print("A = je gaat naar Frankrijk omdat je naar Engeland of Amerika wilt omdat je Engels kan. [14]")
                print("B = je besluit om naar Nederland te gaan omdat je hebt gehoord dat je daar toegelaten wordt. [5] ")
                onderweg = input("type A or B")

                if onderweg == "A" or onderweg == "a":
                    print("Je bent na een lange reis in Frankrijk aangekomen je probeert eerst in Frankrijk te blijven,")
                    print("maar word weer doorgestuurd naar een ander land.")
                    print("Je koopt een boot ticket naar Amerika en zodra je daar aan komt zie je dat de politie controleert op illegale immigranten.") 
                    print("A = je loopt door in de hoop dat je geholpen wordt [11]") 
                    print("B = je probeert de politie te ontwijken [11] ")
                    underway = input("type A or B")

                    if underway == "A" or underway == "a":
                        print("Je wordt opgepakt door de politie en in de gevangenis gestopt. ")

                    elif underway == "B" or underway == "b":
                        print("Je wordt opgepakt door de politie en in de gevangenis gestopt. ")

                elif onderweg == "B" or onderweg == "b":
                    print("Je komt na een hele lange reis via smokkelaars terecht in Nederland.")
                    print("Je gaat naar de overheid om een inburgering aan te vragen.")
                    print("Je wordt in een kamp met andere vluchtelingen gezet en ondervraagt over je verhaal.")
                    print("“Waarom ben je gevlucht? Hoe ben je in Nederland gekomen?”") 
                    print("A = je besluit om de waarheid te spreken [6] ")
                    print("B = je besluit om een verhaal op te maken waarmee je denkt dat je meer kans hebt om te mogen blijven [15] ")
                    vluchteling = input("type A or B: ")

                    if vluchteling == "A" or vluchteling == "a":
                        print("Na een paar maanden krijg je te horen dat je bent toegelaten en je wordt geholpen om je aan te passen zoals,")
                        print("de taal leren in een speciale klas met meer vluchtelingen en er wordt geholpen om je aan een baan te krijgen.")
                        print("Er word ook geholpen om je familie te halen. ")

                    elif vluchteling == "B" or vluchteling == "b":
                        print("Je wordt door iemand gewaarschuwd dat de overheid erachter is gekomen dat je verhaal niet waar is.") 
                        print("A = je probeert te vluchten omdat je verwacht dat je wordt teruggestuurd of in de gevangenis wordt gestopt. [16] ")
                        print("B = je blijft rustig en probeert je verhaal alsnog te vertellen maar dan de waarheid dit keer [16] ")
                        please = input("type A or B: ")

                        if please == "A" or please == "a":
                            print("Je wordt teruggestuurd naar je eigen land ")

                        elif please == "B" or please == "b":
                            print("Je wordt teruggestuurd naar je eigen land ")

            elif optie == "B" or optie == "b":
                print("Je wordt door de politie aangehouden vanwege illegale immigratie.")
                print("Je wordt in een gevangenis gestopt en word na een tijdje weer vrijgelaten,")
                print("maar je moet wel naar een ander land toe omdat Griekenland al te veel vluchtelingen heeft.")
                print("A = je gaat naar Frankrijk omdat je naar Engeland of Amerika wilt omdat je Engels kan. [14]") 
                print("B = je besluit om naar Nederland te gaan omdat je hebt gehoord dat je daar toegelaten wordt. [5] ")
                stop = input("type A or B: ")

                if stop == "A" or stop == "a":
                    print("Je bent na een lange reis in Frankrijk aangekomen je probeert eerst in Frankrijk te blijven,")
                    print("maar word weer doorgestuurd naar een ander land.")
                    print("Je koopt een boot ticket naar Amerika en zodra je daar aan komt zie je dat de politie controleert op illegale immigranten. ")
                    print("A = je loopt door in de hoop dat je geholpen wordt [11]") 
                    print("B = je probeert de politie te ontwijken [11] ")
                    madness = input("type A or B: ")

                    if madness == "A" or madness == "a":
                        print("Je wordt opgepakt door de politie en in de gevangenis gestopt. ")

                    elif madness == "B" or madness == "b":
                        print("Je wordt opgepakt door de politie en in de gevangenis gestopt. ")

                elif stop == "B" or stop == "b":
                    print("Je komt na een hele lange reis via smokkelaars terecht in Nederland.")
                    print("Je gaat naar de overheid om een inburgering aan te vragen.")
                    print("Je wordt in een kamp met andere vluchtelingen gezet en ondervraagt over je verhaal.")
                    print("“Waarom ben je gevlucht? Hoe ben je in Nederland gekomen?” ")
                    print("A = je besluit om de waarheid te spreken [6] ")
                    print("B = je besluit om een verhaal op te maken waarmee je denkt dat je meer kans hebt om te mogen blijven [15] ")
                    gekkenwerk = input("type A or B: ")

                    if gekkenwerk == "A" or gekkenwerk == "a":
                        print("Na een paar maanden krijg je te horen dat je bent toegelaten en je wordt geholpen om je aan te passen zoals,")
                        print("de taal leren in een speciale klas met meer vluchtelingen en er wordt geholpen om je aan een baan te krijgen.")
                        print("Er word ook geholpen om je familie te halen. ")

                    elif gekkenwerk == "B" or gekkenwerk == "b":
                        print("Je wordt door iemand gewaarschuwd dat de overheid erachter is gekomen dat je verhaal niet waar is.") 
                        print("A = je probeert te vluchten omdat je verwacht dat je wordt teruggestuurd of in de gevangenis wordt gestopt. [16] ")
                        print("B = je blijft rustig en probeert je verhaal alsnog te vertellen maar dan de waarheid dit keer [16] ")
                        crazy = input("type A or B: ")

                        if crazy == "A" or crazy == "a":
                            print("Je wordt teruggestuurd naar je eigen land ")

                        elif crazy == "B" or "b":
                            print("Je wordt teruggestuurd naar je eigen land ")

        elif vluchten == "B" or vluchten == "b":
            print("Je bent aangekomen in Bulgarije en daar krijg je te horen dat je niet kan blijven en dat je weer verder moet vluchten. ")
            print("A = je vlucht verder naar Romania. [17] ")
            print("B = je blijft illegaal in Bulgarije omdat je niet meer door kan vluchten. [9] ")