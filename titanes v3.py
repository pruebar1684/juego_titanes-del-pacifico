import random

class Personaje:
    def __init__(self, nombre, vida, velocidad_ataque, habilidades, partes_cuerpo):
        self.nombre = nombre
        self.vida = vida
        self.velocidad_ataque = velocidad_ataque
        self.partes_cuerpo = partes_cuerpo
        self.habilidades = habilidades
        self.dano_reducido = 0
        self.probabilidad_perder_turno = 0

    def recibir_dano(self, parte, dano):
        self.partes_cuerpo[parte] -= dano
        if self.partes_cuerpo[parte] < 0:
            self.partes_cuerpo[parte] = 0
        print(f"{self.nombre} recibió {dano} de daño en {parte}. Vida restante en {parte}: {self.partes_cuerpo[parte]}")
        self.aplicar_efectos_por_parte_danada(parte)
        self.vida -= dano

    def aplicar_efectos_por_parte_danada(self, parte):
        if self.partes_cuerpo[parte] == 0:
            print(f"{self.nombre} ha perdido la parte {parte}.")
            if parte == 'cabeza':
                self.probabilidad_perder_turno += 0.15
            elif parte in ['brazo_izquierdo', 'brazo_derecho']:
                self.dano_reducido += 6
                if self.partes_cuerpo['brazo_izquierdo'] == 0 and self.partes_cuerpo['brazo_derecho'] == 0:
                    self.dano_reducido = 12
            elif parte in ['pierna_izquierda', 'pierna_derecha']:
                self.probabilidad_perder_turno += 0.05
                if self.partes_cuerpo['pierna_izquierda'] == 0 and self.partes_cuerpo['pierna_derecha'] == 0:
                    self.probabilidad_perder_turno += 0.10

    def verificar_turno_perdido(self):
        if random.random() < self.probabilidad_perder_turno:
            print(f"{self.nombre} pierde su turno debido a daño crítico.")
            return True
        return False

    def ejecutar_ataque(self, dano):
        return dano * (1 - self.dano_reducido / 100)

class Jaeger(Personaje):
    def __init__(self, nombre, vida, velocidad_ataque, habilidades, partes_cuerpo):
        super().__init__(nombre, vida, velocidad_ataque, habilidades, partes_cuerpo)

class Kaiju(Personaje):
    def __init__(self, nombre, vida, velocidad_ataque, habilidades, partes_cuerpo):
        super().__init__(nombre, vida, velocidad_ataque, habilidades, partes_cuerpo)

class Juego:
    def __init__(self):
        self.jugadores = []
        self.dados_automaticos = False

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def elegir_modo_dados(self):
        while True:
            opcion = input("¿Quieres que los dados sean automáticos? (s/n): ").lower()
            if opcion in ['s', 'n']:
                self.dados_automaticos = (opcion == 's')
                break
            else:
                print("Opción inválida. Por favor, elige 's' o 'n'.")

    def lanzar_dados(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        print(f"Resultados de los dados: {dado1} y {dado2}")
        return dado1 + dado2

    def ingresar_dados(self):
        while True:
            try:
                dado1 = int(input("Introduce el resultado del primer dado (1-6): "))
                dado2 = int(input("Introduce el resultado del segundo dado (1-6): "))
                if 1 <= dado1 <= 6 and 1 <= dado2 <= 6:
                    return dado1 + dado2
                else:
                    print("Los valores de los dados deben estar entre 1 y 6. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Asegúrate de introducir números enteros. Intenta de nuevo.")
                

                #HABILIDADES 1

                #HABILIDADES DE LOS JAEGERS
                
    def determinar_ataque(self, resultado_dados, atacante):
        habilidades = atacante.habilidades
        if resultado_dados == 12:
            if "Cañón de Plasma" in habilidades:
                return "Cañón de Plasma", habilidades["Cañón de Plasma"]#Gipsy Danger
            if "Cañón de Iones" in habilidades:
                return "Cañón de Iones", habilidades["Cañón de Iones"]#Striker Eureka
            if "Tormenta de Golpes" in habilidades:
                return "Tormenta de Golpes", habilidades["Tormenta de Golpes"]#Crimson Typhoon
            if "Punzón Nuclear" in habilidades:
                return "Punzón Nuclear", habilidades["Punzón Nuclear"]#Cherno Alpha
            if "Carga Titánica" in habilidades:
                return "Carga Titánica", habilidades["Carga Titánica"]#Guardian Bravo
            if "Espada Veloz" in habilidades:
                return "Espada Veloz", habilidades["Espada Veloz"]#Saber Athena
            if "Golpe de Martillo" in habilidades:
                return "Golpe de Martillo", habilidades["Golpe de Martillo"]#Horizon Brave
            if "Slap de Titanio" in habilidades:
                return "Slap de Titanio", habilidades["Slap de Titanio"]#Bracer Phoenix
            if "Espada Encadenada" in habilidades:
                return "Espada Encadenada", habilidades["Espada Encadenada"]#Gipsy Avenger
            if "Tacleo Titánico" in habilidades:
                return "Tacleo Titánico", habilidades["Tacleo Titánico"]#Gypxer strike
            if "Rayo Destructor" in habilidades:
                return "Rayo Destructor", habilidades["Rayo Destructor"]#Valor Omega
            if "Golpe Ronin" in habilidades:
                return "Golpe Ronin", habilidades["Golpe Ronin"]#Tacit Ronin
            if "Carga Imparable" in habilidades:
                return "Carga Imparable", habilidades["Carga Imparable"]#Apex Titan
            if "Cañón Destructor" in habilidades:
                return "Cañón Destructor", habilidades["Cañón Destructor"]#Vanguard Prime
            if "Barrida Relámpago" in habilidades:
                return "Barrida Relámpago", habilidades["Barrida Relámpago"]#Blitzkrieg Blitz
            if "Golpe de Tempestad" in habilidades:
                return "Golpe de Tempestad", habilidades["Golpe de Tempestad"]#Tempest Fury
            if "Rayo Ascendente" in habilidades:
                return "Rayo Ascendente", habilidades["Rayo Ascendente"]#Avalon Ascendant
            if "Torbellino Destructor" in habilidades:
                return "Torbellino Destructor", habilidades["Torbellino Destructor"]#Vortex Voyager
            if "Martillo Redentor" in habilidades:
                return "Martillo Redentor", habilidades["Martillo Redentor"]#Titan Redeemer
            if "Explosión Nova" in habilidades:
                return "Explosión Nova", habilidades["Explosión Nova"]#Nova Titan
            #HABILIDADES DE LOS KAIJUS
            if "Escupitajo Tóxico" in habilidades:
                return "Escupitajo Tóxico", habilidades["Escupitajo Tóxico"]#Knifehead
            if "Mordida del Abismo" in habilidades:
                return "Mordida del Abismo", habilidades["Mordida del Abismo"]#Abyssal Leviathan
            if "Rayo de Tormenta" in habilidades:
                return "Rayo de Tormenta", habilidades["Rayo de Tormenta"]#Thunder Wyrm 
            if "Mordida Ácida" in habilidades:
                return "Mordida Ácida", habilidades["Mordida Ácida"]#Acid Fang
            if "Rugido Trueno" in habilidades:
                return "Rugido Trueno", habilidades["Rugido Trueno"]#Thunderclap
            if "Garras de Terror" in habilidades:
                return "Garras de Terror", habilidades["Garras de Terror"]#Terrorsaur
            if "Mordida Venenosa" in habilidades:
                return "Mordida Venenosa", habilidades["Mordida Venenosa"]#Basilisk
            if "Fuego de Dragón" in habilidades:
                return "Fuego de Dragón", habilidades["Fuego de Dragón"]#Hydra
            if "Torrente Ácido" in habilidades:
                return "Torrente Ácido", habilidades["Torrente Ácido"]#Leviatán
            if "Mordisco Devastador" in habilidades:
                return "Mordisco Devastador", habilidades["Mordisco Devastador"]#Kraken
            if "Estampida Terrestre" in habilidades:
                return "Estampida Terrestre", habilidades["Estampida Terrestre"]#Behemoth
            if "Zarpazo Aplastante" in habilidades:
                return "Zarpazo Aplastante", habilidades["Zarpazo Aplastante"]#Goliath
            if "Golpe Colosal" in habilidades:
                return "Golpe Colosal", habilidades["Golpe Colosal"]#Coloso
            if "Emboscada Nocturna" in habilidades:
                return "Emboscada Nocturna", habilidades["Emboscada Nocturna"]#Némesis
            if "Resplandor Celestial" in habilidades:
                return "Resplandor Celestial", habilidades["Resplandor Celestial"]#Aurora
            if "Llamarada Aviadora" in habilidades:
                return "Llamarada Aviadora", habilidades["Llamarada Aviadora"]#Fénix
            if "Mordida Víbora" in habilidades:
                return "Mordida Víbora", habilidades["Mordida Víbora"]#Serpentaria
            if "Tormenta Devastadora" in habilidades:
                return "Tormenta Devastadora", habilidades["Tormenta Devastadora"]#Tifón
            if "Golpe Profundo" in habilidades:
                return "Golpe Profundo", habilidades["Golpe Profundo"]#Abismo Oscuro
            if "Aullido Nocturno" in habilidades:
                return "Aullido Nocturno", habilidades["Aullido Nocturno"]#Colmillo Nocturno
            
            #HABILIDADES 2

            #HABILIDADES DE LOS JAEGERS
            
        elif resultado_dados in [11, 3]:
            if "Golpe nuclear" in habilidades:
                return "Golpe nuclear", habilidades["Golpe nuclear"]#Gipsy Danger
            if "Puño Torpedo" in habilidades:
                return "Puño Torpedo", habilidades["Puño Torpedo"]#Striker Eureka
            if "Viento Cortante" in habilidades:
                return "Viento Cortante", habilidades["Viento Cortante"]#Crimson Typhoon
            if "Martillo de Fuego" in habilidades:
                return "Martillo de Fuego", habilidades["Martillo de Fuego"]#Cherno Alpha
            if "Pulso de Energía" in habilidades:
                return "Pulso de Energía", habilidades["Pulso de Energía"]#Guardian Bravo
            if "Defensa Energética" in habilidades:
                return "Defensa Energética", habilidades["Defensa Energética"]#Saber Athena
            if "Latigazo Energético" in habilidades:
                return "Latigazo Energético", habilidades["Latigazo Energético"]#Horizon Brave
            if "Matriz Defensiva" in habilidades:
                return "Matriz Defensiva", habilidades["Matriz Defensiva"]#Bracer Phoenix
            if "Lanzador de Plasma" in habilidades:
                return "Lanzador de Plasma", habilidades["Lanzador de Plasma"]#Gipsy Avenger
            if "Látigo de Luz" in habilidades:
                return "Látigo de Luz", habilidades["Látigo de Luz"]#Gypxer strike
            if "Escudo Omega" in habilidades:
                return "Escudo Omega", habilidades["Escudo Omega"]#Valor Omega
            if "Choque Eléctrico" in habilidades:
                return "Choque Eléctrico", habilidades["Choque Eléctrico"]#Tacit Ronin
            if "Golpe Colosal" in habilidades:
                return "Golpe Colosal", habilidades["Golpe Colosal"]#Apex Titan
            if "Escudo Primordial" in habilidades:
                return "Escudo Primordial", habilidades["Escudo Primordial"]#Vanguard Prime
            if "Explosión de Rayo" in habilidades:
                return "Explosión de Rayo", habilidades["Explosión de Rayo"]#Blitzkrieg Blitz
            if "Tormenta Letal" in habilidades:
                return "Tormenta Letal", habilidades["Tormenta Letal"]#Tempest Fury
            if "Barrera de Aegis" in habilidades:
                return "Barrera de Aegis", habilidades["Barrera de Aegis"]#Avalon Ascendant
            if "Cañón Vortex" in habilidades:
                return "Cañón Vortex", habilidades["Cañón Vortex"]#Vortex Voyager
            if "Escudo Redentor" in habilidades:
                return "Escudo Redentor", habilidades["Escudo Redentor"]#Titan Redeemer
            if "Escudo Nova" in habilidades:
                return "Escudo Nova", habilidades["Escudo Nova"]#Nova Titan
            
            #HABILIDADES DE LOS KAIJUS
            
            if "Garras Afiladas" in habilidades:
                return "Garras Afiladas", habilidades["Garras Afiladas"]#Knifehead
            if "Tormenta de Tentáculos" in habilidades:
                return "Tormenta de Tentáculos", habilidades["Tormenta de Tentáculos"]#Abyssal Leviathan
            if "Golpe de Trueno" in habilidades:
                return "Golpe de Trueno", habilidades["Golpe de Trueno"]#Thunder Wyrm 
            if "Escupitajo Corrosivo" in habilidades:
                return "Escupitajo Corrosivo", habilidades["Escupitajo Corrosivo"]#Acid Fang
            if "Golpe Relámpago" in habilidades:
                return "Golpe Relámpago", habilidades["Golpe Relámpago"]#Thunderclap
            if "Aliento Ardiente" in habilidades:
                return "Aliento Ardiente", habilidades["Aliento Ardiente"]#Terrorsaur
            if "Golpe de Cola" in habilidades:
                return "Golpe de Cola", habilidades["Golpe de Cola"]#Basilisk
            if "Garras Venenosas" in habilidades:
                return "Garras Venenosas", habilidades["Garras Venenosas"]#Hydra
            if "Cañón de Plasma" in habilidades:
                return "Cañón de Plasma", habilidades["Embiste Oceánico"]#Leviatán
            if "Torbellino Marítimo" in habilidades:
                return "Torbellino Marítimo", habilidades["Torbellino Marítimo"]#Kraken
            if "Golpe Telúrico" in habilidades:
                return "Golpe Telúrico", habilidades["Golpe Telúrico"]#Behemoth
            if "Furia de Roca" in habilidades:
                return "Furia de Roca", habilidades["Furia de Roca"]#Goliath
            if "Estampida Salvaje" in habilidades:
                return "Estampida Salvaje", habilidades["Estampida Salvaje"]#Coloso
            if "Asalto Oscuro" in habilidades:
                return "Asalto Oscuro", habilidades["Asalto Oscuro"]#Némesis
            if "Luz Estelar" in habilidades:
                return "Luz Estelar", habilidades["Luz Estelar"]#Aurora
            if "Vuelo Infernal" in habilidades:
                return "Vuelo Infernal", habilidades["Vuelo Infernal"]#Fénix
            if "Enroscarse Mortal" in habilidades:
                return "Enroscarse Mortal", habilidades["Enroscarse Mortal"]#Serpentaria
            if "Ráfaga Ciclónica" in habilidades:
                return "Ráfaga Ciclónica", habilidades["Ráfaga Ciclónica"]#Tifón
            if "Marea Negra" in habilidades:
                return "Marea Negra", habilidades["Marea Negra"]#Abismo Oscuro
            if "Garra Sombría" in habilidades:
                return "Garra Sombría", habilidades["Garra Sombría"]#Colmillo Nocturno
            
            #HABILIDADES 3

            #HABILIDADES DE LOS JAEGERS
            
        elif resultado_dados in [2, 10]:
            if "Puño Cohete" in habilidades:
                return "Puño Cohete", habilidades["Puño Cohete"]#Gipsy Danger
            if "Carga Explosiva" in habilidades:
                return "Carga Explosiva", habilidades["Carga Explosiva"]#Striker Eureka
            if "Puño Ciclónico" in habilidades:
                return "Puño Ciclónico", habilidades["Puño Ciclónico"]#Crimson Typhoon
            if "Puño de Hierro" in habilidades:
                return "Puño de Hierro", habilidades["Puño de Hierro"]#Cherno Alpha
            if "Martillo Eléctrico" in habilidades:
                return "Martillo Eléctrico", habilidades["Martillo Eléctrico"]#Guardian Bravo
            if "Carga Afilada" in habilidades:
                return "Carga Afilada", habilidades["Carga Afilada"]#Saber Athena
            if "Choque Sónico" in habilidades:
                return "Choque Sónico", habilidades["Choque Sónico"]#Horizon Brave
            if "Explosión de Choques" in habilidades:
                return "Explosión de Choques", habilidades["Explosión de Choques"]#Bracer Phoenix
            if "Embestida Letal" in habilidades:
                return "Embestida Letal", habilidades["Embestida Letal"]#Gipsy Avenger
            if "Martillo Estelar" in habilidades:
                return "Martillo Estelar", habilidades["Martillo Estelar"]#Gypxer strike
            if "Explosión Fotónica" in habilidades:
                return "Explosión Fotónica", habilidades["Explosión Fotónica"]#Valor Omega
            if "Emboscada Letal" in habilidades:
                return "Emboscada Letal", habilidades["Emboscada Letal"]#Tacit Ronin
            if "Impacto Sísmico" in habilidades:
                return "Impacto Sísmico", habilidades["Impacto Sísmico"]#Apex Titan
            if "Explosión Potente" in habilidades:
                return "Explosión Potente", habilidades["Explosión Potente"]#Vanguard Prime
            if "Golpe de Tormenta" in habilidades:
                return "Golpe de Tormenta", habilidades["Golpe de Tormenta"]#Blitzkrieg Blitz
            if "Corte de Viento" in habilidades:
                return "Corte de Viento", habilidades["Corte de Viento"]#Tempest Fury
            if "Explosión de Ascenso" in habilidades:
                return "Explosión de Ascenso", habilidades["Explosión de Ascenso"]#Avalon Ascendant
            if "Sobrecarga Vortex" in habilidades:
                return "Sobrecarga Vortex", habilidades["Sobrecarga Vortex"]#Vortex Voyager
            if "Aplastamiento Atómico" in habilidades:
                return "Aplastamiento Atómico", habilidades["Aplastamiento Atómico"]#Titan Redeemer
            if "Rayo Titan" in habilidades:
                return "Rayo Titan", habilidades["Rayo Titan"]#Nova Titan

            #HABILIDADES DE LOS KAIJUS
            
            if "Pisotón" in habilidades:
                return "Pisotón", habilidades["Pisotón"]#Knifehead
            if "Explosión Abisal" in habilidades:
                return "Explosión Abisal", habilidades["Explosión Abisal"]#Abyssal Leviathan
            if "Aullido Eléctrico" in habilidades:
                return "Aullido Eléctrico", habilidades["Aullido Eléctrico"]#Thunder Wyrm 
            if "Garra Tóxica" in habilidades:
                return "Garra Tóxica", habilidades["Garra Tóxica"]#Acid Fang
            if "Carga Eléctrica" in habilidades:
                return "Carga Eléctrica", habilidades["Carga Eléctrica"]#Thunderclap
            if "Aplastar" in habilidades:
                return "Aplastar", habilidades["Aplastar"]#Terrorsaur
            if "Rugido Petrificante" in habilidades:
                return "Rugido Petrificante", habilidades["Rugido Petrificante"]#Basilisk
            if "Golpe de Cola" in habilidades:
                return "Golpe de Cola", habilidades["Golpe de Cola"]#Hydra
            if "Carga de Agua" in habilidades:
                return "Carga de Agua", habilidades["Carga de Agua"]#Leviatán
            if "Golpe de Oleaje" in habilidades:
                return "Golpe de Oleaje", habilidades["Golpe de Oleaje"]#Kraken
            if "Aplastamiento" in habilidades:
                return "Aplastamiento", habilidades["Aplastamiento"]#Behemoth
            if "Martillazo" in habilidades:
                return "Martillazo", habilidades["Martillazo"]#Goliath
            if "Zarpazo Feroz" in habilidades:
                return "Zarpazo Feroz", habilidades["Zarpazo Feroz"]#Coloso
            if "Golpe Umbrío" in habilidades:
                return "Golpe Umbrío", habilidades["Golpe Umbrío"]#Némesis
            if "Rayo Solar" in habilidades:
                return "Rayo Solar", habilidades["Rayo Solar"]#Aurora
            if "Golpe Ardiente" in habilidades:
                return "Golpe Ardiente", habilidades["Golpe Ardiente"]#Fénix
            if "Golpe de Serpiente" in habilidades:
                return "Golpe de Serpiente", habilidades["Golpe de Serpiente"]#Serpentaria
            if "Golpe de Vendaval" in habilidades:
                return "Golpe de Vendaval", habilidades["Golpe de Vendaval"]#Tifón
            if "Carga Abismal" in habilidades:
                return "Carga Abismal", habilidades["Carga Abismal"]#Abismo Oscuro  
            if "Carga Nocturna" in habilidades:
                return "Carga Nocturna", habilidades["Carga Nocturna"]#Colmillo Nocturno
            
            #HABILIDADES 4

            #HABILIDADES DE LOS JAEGERS
            
        elif resultado_dados in [9, 4]:
            if "Corte de Espada" in habilidades:
                return "Corte de Espada", habilidades["Corte de Espada"]#Gipsy Danger
            if "Cuchillas de Hombro" in habilidades:
                return "Cuchillas de Hombro", habilidades["Cuchillas de Hombro"]#Striker Eureka
            if "Golpe Huracanado" in habilidades:
                return "Golpe Huracanado", habilidades["Golpe Huracanado"]#Crimson Typhoon
            if "Patada Atómica" in habilidades:
                return "Patada Atómica", habilidades["Patada Atómica"]#Cherno Alpha
            if "Puñetazo Sónico" in habilidades:
                return "Puñetazo Sónico", habilidades["Puñetazo Sónico"]#Guardian Bravo
            if "Corte de Rayo" in habilidades:
                return "Corte de Rayo", habilidades["Corte de Rayo"]#Saber Athena
            if "Martillo de Trueno" in habilidades:
                return "Martillo de Trueno", habilidades["Martillo de Trueno"]#Horizon Brave
            if "Lluvia de Fuego" in habilidades:
                return "Lluvia de Fuego", habilidades["Lluvia de Fuego"]#Bracer Phoenix
            if "Cohetes Asesinos" in habilidades:
                return "Cohetes Asesinos", habilidades["Cohetes Asesinos"]#Gipsy Avenger
            if "Escudo Cósmico" in habilidades:
                return "Escudo Cósmico", habilidades["Escudo Cósmico"]#Gypxer strike
            if "Golpe Devastador" in habilidades:
                return "Golpe Devastador", habilidades["Golpe Devastador"]#Valor Omega
            if "Contraataque Sorpresa" in habilidades:
                return "Contraataque Sorpresa", habilidades["Contraataque Sorpresa"]#Tacit Ronin
            if "Golpe Destructor" in habilidades:
                return "Golpe Destructor", habilidades["Golpe Destructor"]#Apex Titan
            if "Embestida de Fuerza" in habilidades:
                return "Embestida de Fuerza", habilidades["Embestida de Fuerza"]#Vanguard Prime
            if "Impacto Sónico" in habilidades:
                return "Impacto Sónico", habilidades["Impacto Sónico"]#Blitzkrieg Blitz
            if "Impacto Eléctrico" in habilidades:
                return "Impacto Eléctrico", habilidades["Impacto Eléctrico"]#Tempest Fury
            if "Golpe de Defensa" in habilidades:
                return "Golpe de Defensa", habilidades["Golpe de Defensa"]#Avalon Ascendant
            if "Onda Vortex" in habilidades:
                return "Onda Vortex", habilidades["Onda Vortex"]#Vortex Voyager
            if "Golpe de Redención" in habilidades:
                return "Golpe de Redención", habilidades["Golpe de Redención"]#Titan Redeemer
            if "Onda Nova" in habilidades:
                return "Onda Nova", habilidades["Onda Nova"]#Nova Titan

            #HABILIDADES DE LOS KAIJUS
            
            if "Golpe de Cola" in habilidades:
                return "Golpe de Cola", habilidades["Golpe de Cola"]#Knifehead
            if "Carga Abismal" in habilidades:
                return "Carga Abismal", habilidades["Carga Abismal"]#Abyssal Leviathan
            if "Carga Relámpago" in habilidades:
                return "Carga Relámpago", habilidades["Carga Relámpago"]#Thunder Wyrm 
            if "Ráfaga Venenosa" in habilidades:
                return "Ráfaga Venenosa", habilidades["Ráfaga Venenosa"]#Acid Fang
            if "Impacto Electrostático" in habilidades:
                return "Impacto Electrostático", habilidades["Impacto Electrostático"]#Thunderclap
            if "Cola Afilada" in habilidades:
                return "Cola Afilada", habilidades["Cola Afilada"]#Terrorsaur
            if "Zarpazo Mortal" in habilidades:
                return "Zarpazo Mortal", habilidades["Zarpazo Mortal"]#Basilisk
            if "Rugido Paralizante" in habilidades:
                return "Rugido Paralizante", habilidades["Rugido Paralizante"]#Hydra
            if "Mordida Tóxica" in habilidades:
                return "Mordida Tóxica", habilidades["Mordida Tóxica"]#Leviatán
            if "Zarpazo Acuático" in habilidades:
                return "Zarpazo Acuático", habilidades["Zarpazo Acuático"]#Kraken
            if "Embiste Colosal" in habilidades:
                return "Embiste Colosal", habilidades["Embiste Colosal"]#Behemoth
            if "Golpe de Titanio" in habilidades:
                return "Golpe de Titanio", habilidades["Golpe de Titanio"]#Goliath
            if "Embestida Despiadada" in habilidades:
                return "Embestida Despiadada", habilidades["Embestida Despiadada"]#Coloso
            if "Aullido Tenebroso" in habilidades:
                return "Aullido Tenebroso", habilidades["Aullido Tenebroso"]#Némesis
            if "Fuego Estelar" in habilidades:
                return "Fuego Estelar", habilidades["Fuego Estelar"]#Aurora
            if "Explosión de Fuego" in habilidades:
                return "Explosión de Fuego", habilidades["Explosión de Fuego"]#Fénix
            if "Veneno Paralizante" in habilidades:
                return "Veneno Paralizante", habilidades["Veneno Paralizante"]#Serpentaria
            if "Viento Despiadado" in habilidades:
                return "Viento Despiadado", habilidades["Viento Despiadado"]#Tifón
            if "Tormenta Tenebrosa" in habilidades:
                return "Tormenta Tenebrosa", habilidades["Tormenta Tenebrosa"]#Abismo Oscuro
            if "Mordida Oscura" in habilidades:
                return "Mordida Oscura", habilidades["Mordida Oscura"]#Colmillo Nocturno
            
            #HABILIDADES 5

            #HABILIDADES DE LOS JAEGERS
            
        elif resultado_dados in [8, 7]:
            if "Embestida" in habilidades:
                return "Embestida", habilidades["Embestida"]#Gipsy Danger
            if "Golpe de honda" in habilidades:
                return "Golpe de honda", habilidades["Golpe de honda"]#Striker Eureka
            if "Barrido de Energía" in habilidades:
                return "Barrido de Energía", habilidades["Barrido de Energía"]#Crimson Typhoon
            if "Embestida Térmica" in habilidades:
                return "Embestida Térmica", habilidades["Embestida Térmica"]#Cherno Alpha
            if "Corte Angular" in habilidades:
                return "Corte Angular", habilidades["Corte Angular"]#Guardian Bravo
            if "Danza Letal" in habilidades:
                return "Danza Letales", habilidades["Danza Letal"]#Saber Athena
            if "Golpe Colosales" in habilidades:
                return "Golpe Colosales", habilidades["Golpe Colosales"]#Horizon Brave
            if "Golpe de Escudo" in habilidades:
                return "Golpe de Escudo", habilidades["Golpe de Escudo"]#Bracer Phoenix
            if "Golpe Gravitacional" in habilidades:
                return "Golpe Gravitacional", habilidades["Golpe Gravitacional"]#Gipsy Avenger
            if "Golpe Relámpago" in habilidades:
                return "Golpe Relámpago", habilidades["Golpe Relámpago"]#Gypxer strike
            if "Onda Impactante" in habilidades:
                return "Onda Impactante", habilidades["Onda Impactante"]#Valor Omega
            if "Danza Mortal" in habilidades:
                return "Danza Mortal", habilidades["Danza Mortal"]#Tacit Ronin
            if "Embestida Eléctrica" in habilidades:
                return "Embestida Eléctrica", habilidades["Embestida Eléctrica"]#Apex Titan
            if "Rompe Defensas" in habilidades:
                return "Rompe Defensas", habilidades["Rompe Defensas"]#Vanguard Prime
            if "Descarga Eléctrica" in habilidades:
                return "Descarga Eléctrica", habilidades["Descarga Eléctrica"]#Blitzkrieg Blitz
            if "Embestida de Huracán" in habilidades:
                return "Embestida de Huracán", habilidades["Embestida de Huracán"]#Tempest Fury
            if "Impacto Energético" in habilidades:
                return "Impacto Energético", habilidades["Impacto Energético"]#Avalon Ascendant
            if "Golpe Gravitacional" in habilidades:
                return "Golpe Gravitacional", habilidades["Golpe Gravitacional"]#Vortex Voyager
            if "Embestida Poderosa" in habilidades:
                return "Embestida Poderosa", habilidades["Embestida Poderosa"]#Titan Redeemer
            if "Impacto Nova" in habilidades:
                return "Impacto Nova", habilidades["Impacto Nova"]#Nova Titan

            #HABILIDADES DE LOS KAIJUS
            
            if "Empujon" in habilidades:
                return "Empujon", habilidades["Empujon"]#Knifehead
            if "Rugido Sombrío" in habilidades:
                return "Rugido Sombrío", habilidades["Rugido Sombrío"]#Abyssal Leviathan
            if "Mordida Eléctrica" in habilidades:
                return "Mordida Eléctrica", habilidades["Mordida Eléctrica"]#Thunder Wyrm 
            if "Golpe de Fuego Químico" in habilidades:
                return "Golpe de Fuego Químico", habilidades["Golpe de Fuego Químico"]#Acid Fang
            if "Descarga de Tormenta" in habilidades:
                return "Descarga de Tormenta", habilidades["Descarga de Tormenta"]#Thunderclap
            if "Golpe Bestial" in habilidades:
                return "Golpe Bestial", habilidades["Golpe Bestial"]#Terrorsaur
            if "Embestida Sorpresa" in habilidades:
                return "Embestida Sorpresa", habilidades["Embestida Sorpresa"]#Basilisk
            if "Barrera de Escamas" in habilidades:
                return "Barrera de Escamas", habilidades["Barrera de Escamas"]#Hydra
            if "Golpe Tsunami" in habilidades:
                return "Golpe Tsunami", habilidades["Golpe Tsunami"]#Leviatán
            if "Furia Submarina" in habilidades:
                return "Furia Submarina", habilidades["Furia Submarina"]#Kraken
            if "Furia Sísmica" in habilidades:
                return "Furia Sísmica", habilidades["Furia Sísmica"]#Behemoth
            if "Rugido Sónico" in habilidades:
                return "Rugido Sónico", habilidades["Rugido Sónico"]#Goliath
            if "Furia Brutal" in habilidades:
                return "Furia Brutal", habilidades["Furia Brutal"]#Coloso
            if "Espinas Sombrías" in habilidades:
                return "Espinas Sombrías", habilidades["Espinas Sombrías"]#Némesis
            if "Centella Radiante" in habilidades:
                return "Centella Radiante", habilidades["Centella Radiante"]#Aurora
            if "Plumas Abrasadoras" in habilidades:
                return "Plumas Abrasadoras", habilidades["Plumas Abrasadoras"]#Fénix
            if "Coil Venenoso" in habilidades:
                return "Coil Venenoso", habilidades["Coil Venenoso"]#Serpentaria
            if "Ciclón Destructor" in habilidades:
                return "Ciclón Destructor", habilidades["Ciclón Destructor"]#Tifón
            if "Aliento de Oscuridad" in habilidades:
                return "Aliento de Oscuridad", habilidades["Aliento de Oscuridad"]#Abismo Oscuro
            if "Niebla de Pesadilla" in habilidades:
                return "Niebla de Pesadilla", habilidades["Niebla de Pesadilla"]#Colmillo Nocturno
            
            
            #HABILIDADES 6

            #HABILIDADES DE LOS JAEGERS
            
        elif resultado_dados in [6, 5]:
            if "Patada trueno" in habilidades:
                return "Patada trueno", habilidades["Patada trueno"]#Gipsy Danger
            if "Carga relampago" in habilidades:
                return "Carga relampago", habilidades["Carga relampago"]#Striker Eureka
            if "Furia de Acero" in habilidades:
                return "Furia de Acero", habilidades["Furia de Acero"]#Crimson Typhoon
            if "Tormenta Radiactiva" in habilidades:
                return "Tormenta Radiactiva", habilidades["Tormenta Radiactiva"]#Cherno Alpha
            if "Embiste Relámpago" in habilidades:
                return "Embiste Relámpago", habilidades["Embiste Relámpago"]#Guardian Bravo
            if "Impacto Rápido" in habilidades:
                return "Impacto Rápido", habilidades["Impacto Rápido"]#Saber Athena
            if "Impacto Defensivo" in habilidades:
                return "Impacto Defensivo", habilidades["Impacto Defensivo"]#Horizon Brave
            if "Martillo de Plasma" in habilidades:
                return "Martillo de Plasma", habilidades["Martillo de Plasma"]#Bracer Phoenix
            if "Carga Energética" in habilidades:
                return "Carga Energética", habilidades["Carga Energética"]#Gipsy Avenger
            if "Descarga de Poder" in habilidades:
                return "Descarga de Poder", habilidades["Descarga de Poder"]#Gypxer strike
            if "Rompe Barreras" in habilidades:
                return "Rompe Barreras", habilidades["Rompe Barreras"]#Valor Omega
            if "Descargas Eléctricas" in habilidades:
                return "Descargas Eléctricas", habilidades["Descargas Eléctricas"]#Tacit Ronin
            if "Impacto Preciso" in habilidades:
                return "Impacto Preciso", habilidades["Impacto Preciso"]#Apex Titan
            if "Contraataque Primario" in habilidades:
                return "Contraataque Primario", habilidades["Contraataque Primario"]#Vanguard Prime
            if "Golpe Rápido" in habilidades:
                return "Golpe Rápido", habilidades["Golpe Rápido"]#Blitzkrieg Blitz
            if "Sobrecarga Tempestuosa" in habilidades:
                return "Sobrecarga Tempestuosa", habilidades["Sobrecarga Tempestuosa"]#Tempest Fury
            if "Ataque de Cima" in habilidades:
                return "Ataque de Cima", habilidades["Ataque de Cima"]#Avalon Ascendant
            if "Impacto de Vórtice" in habilidades:
                return "Impacto de Vórtice", habilidades["Impacto de Vórtice"]#Vortex Voyager
            if "Ataque de Redención" in habilidades:
                return "Ataque de Redención", habilidades["Ataque de Redención"]#Titan Redeemer
            if "Rompe Titanes" in habilidades:
                return "Rompe Titanes", habilidades["Rompe Titanes"]#Nova Titan
           

            #HABILIDADES DE LOS KAIJUS
            
            if "Rugido" in habilidades:
                return "Rugido", habilidades["Rugido"]#Knifehead
            if "Golpe de Marea" in habilidades:
                return "Golpe de Marea", habilidades["Golpe de Marea"]#Abyssal Leviathan
            if "Explosión de Chispa" in habilidades:
                return "Explosión de Chispa", habilidades["Explosión de Chispa"]#Thunder Wyrm 
            if "Nube de Ácido" in habilidades:
                return "Nube de Ácido", habilidades["Nube de Ácido"]#Acid Fang
            if "Torbellino Eléctrico" in habilidades:
                return "Torbellino Eléctrico", habilidades["Torbellino Eléctrico"]#Thunderclap
            if "Rugido Ensordecedor" in habilidades:
                return "Rugido Ensordecedor", habilidades["Rugido Ensordecedor"]#Terrorsaur
            if "Aplastamiento" in habilidades:
                return "Aplastamiento", habilidades["Aplastamiento"]#Basilisk
            if "Mordida Múltiple" in habilidades:
                return "Mordida Múltiple", habilidades["Mordida Múltiple"]#Hydra
            if "Tormenta Submarina" in habilidades:
                return "Tormenta Submarina", habilidades["Tormenta Submarina"]#Leviatán
            if "Aliento de Neblina" in habilidades:
                return "Aliento de Neblina", habilidades["Aliento de Neblina"]#Kraken
            if "Fragor Terremoto" in habilidades:
                return "Fragor Terremoto", habilidades["Fragor Terremoto"]#Behemoth
            if "Lanzamiento Roca" in habilidades:
                return "Cañón de Plasma", habilidades["Lanzamiento Roca"]#Goliath
            if "Rugido Infernal" in habilidades:
                return "Rugido Infernal", habilidades["Rugido Infernal"]#Coloso
            if "Tormenta de Sombra" in habilidades:
                return "Tormenta de Sombra", habilidades["Tormenta de Sombra"]#Némesis
            if "Brillo Cósmico" in habilidades:
                return "Brillo Cósmico", habilidades["Brillo Cósmico"]#Aurora
            if "Ala Incendiaria" in habilidades:
                return "Ala Incendiaria", habilidades["Ala Incendiaria"]#Fénix
            if "Danse Mortífera" in habilidades:
                return "Danse Mortífera", habilidades["Danse Mortífera"]#Serpentaria
            if "Furia Tornádica" in habilidades:
                return "Furia Tornádica", habilidades["Furia Tornádica"]#Tifón
            if "Ciclón Umbrío" in habilidades:
                return "Ciclón Umbrío", habilidades["Ciclón Umbrío"]#Abismo Oscuro
            if "Rugido Lunar" in habilidades:
                return "Rugido Lunar", habilidades["Rugido Lunar"]#Colmillo Nocturno
            

        print("No se encontró un ataque válido para este resultado de dados y habilidades del personaje atacante.")
        return "ataque_fallido", 0

    def seleccionar_parte_objetivo(self, defensor):
        partes_disponibles = [parte for parte, vida in defensor.partes_cuerpo.items() if vida > 0]
        print("Partes del cuerpo disponibles para atacar:")
        for i, parte in enumerate(partes_disponibles, 1):
            print(f"{i}. {parte}")
        while True:
            opcion = input("Selecciona el número de la parte del cuerpo a atacar: ")
            if opcion.isdigit() and 1 <= int(opcion) <= len(partes_disponibles):
                return partes_disponibles[int(opcion) - 1]
            else:
                print("Opción inválida. Selecciona un número válido.")

    def mostrar_especificaciones(self, personaje):
        print(f"Nombre: {personaje.nombre}")
        print(f"Vida: {personaje.vida}")
        print(f"Velocidad de Ataque: {personaje.velocidad_ataque}")
        print("Habilidades:")
        for habilidad, dano in personaje.habilidades.items():
            print(f"  {habilidad}: {dano} de daño")
        print("Partes del cuerpo y vida:")
        for parte, vida in personaje.partes_cuerpo.items():
            print(f"  {parte}: {vida} de vida")
        print()

    def seleccionar_personaje(self):
        jaegers = [
            Jaeger("Gipsy Danger", 1000, 10, {"Cañón de Plasma": 1, "Golpe nuclear": 2, "Puño Cohete": 3, "Corte de Espada": 4, "Embestida": 5, "Patada trueno": 6}, #Gipsy Danger
                   {"cabeza": 1000, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
            Jaeger("Striker Eureka", 550, 12, {"Cañón de Iones": 1, "Puño Torpedo": 2, "Carga Explosiva": 3, "Cuchillas de Hombro": 4, "Golpe de honda": 5, "Carga relampago": 6}, #Striker Eureka
                   {"cabeza": 1100, "torso": 160, "brazo_izquierdo": 85, "brazo_derecho": 85, "pierna_izquierda": 100, "pierna_derecha": 100}),
            Jaeger("Crimson Typhoon", 550, 12, {"Tormenta de Golpes": 1, "Viento Cortante": 2, "Puño Ciclónico": 3, "Golpe Huracanado": 4, "Barrido de Energía": 5, "Furia de Acero": 6}, #Crimson Typhoon
                   {"cabeza": 105, "torso": 155, "brazo_izquierdo": 82, "brazo_derecho": 82, "pierna_izquierda": 95, "pierna_derecha": 95}),
            Jaeger("Cherno Alpha", 140, 20, {"Punzón Nuclear": 1, "Martillo de Fuego": 2, "Puño de Hierro": 3, "Patada Atómica": 4, "Embestida Térmica": 5, "Tormenta Radiactiva": 6}, #Cherno Alpha
                    {"cabeza": 110, "torso": 140, "brazo_izquierdo": 120, "brazo_derecho": 120, "pierna_izquierda": 130, "pierna_derecha": 130}),
            Jaeger("Guardian Bravo", 130, 18, {"Carga Titánica": 1, "Latigazo Energético": 2, "Martillo Eléctrico": 3, "Puñetazo Sónico": 4, "Corte Angular": 5, "Embiste Relámpago": 6}, #Guardian Bravo
                    {"cabeza": 105, "torso": 130, "brazo_izquierdo": 115, "brazo_derecho": 115, "pierna_izquierda": 125, "pierna_derecha": 125}),
            Jaeger("Saber Athena", 120, 15, {"Espada Veloz": 1, "Pulso de Energía": 2, "Carga Afilada": 3, "Corte de Rayo": 4, "Danza Letal": 5, "Impacto Rápido": 6}, #Saber Athena
                  {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
             Jaeger("Horizon Brave", 110, 12, {"Golpe de Martillo": 1, "Defensa Energética": 2, "Choque Sónico": 3, "Martillo de Trueno": 4, "Golpe Colosales": 5, "Impacto Defensivo": 6}, #Horizon Brave
                  {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
             Jaeger("Bracer Phoenix", 105, 11, {"Slap de Titanio": 1, "Matriz Defensiva": 2, "Explosión de Choques": 3, "Lluvia de Fuego": 4, "Golpe de Escudo": 5, "Martillo de Plasma": 6}, #Bracer Phoenix
                  {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
            Jaeger("Gipsy Avenger", 110, 12, {"Espada Encadenada": 1, "Lanzador de Plasma": 2, "Embestida Letal": 3, "Cohetes Asesinos": 4, "Golpe Gravitacional": 5, "Carga Energética": 6}, #Gipsy Avenger
                  {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
            Jaeger("Gypxer strike", 105, 11, {"Tacleo Titánico": 1, "Látigo de Luz": 2, "Martillo Estelar": 3, "Escudo Cósmico": 4, "Golpe Relámpago": 5, "Descarga de Poder": 6}, #Gypxer strike
                  {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
             Jaeger("Valor Omega", 115, 12, {"Rayo Destructor": 1, "Escudo Omega": 2, "Explosión Fotónica": 3, "Golpe Devastador": 4, "Onda Impactante": 5, "Rompe Barreras": 6}, #Valor Omega
                  {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
            Jaeger("Tacit Ronin", 120, 14, {"Golpe Ronin": 1, "Choque Eléctrico": 2, "Emboscada Letal": 3, "Contraataque Sorpresa": 4, "Danza Mortal": 5, "Descargas Eléctricas": 6}, #Tacit Ronin
                  {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
            Jaeger("Apex Titan", 130, 15, {"Carga Imparable": 1, "Golpe Colosal": 2, "Impacto Sísmico": 3, "Golpe Destructor": 4, "Embestida Eléctrica": 5, "Impacto Preciso": 6}, #Apex Titan
                   {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
             Jaeger("Vanguard Prime", 130, 15, {"Cañón Destructor": 1, "Escudo Primordial": 2, "Explosión Potente": 3, "Embestida de Fuerza": 4, "Rompe Defensas": 5, "Contraataque Primario": 6}, #Vanguard Prime                   
                   {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
            Jaeger("Blitzkrieg Blitz", 110, 14, {"Barrida Relámpago": 1, "Explosión de Rayo": 2, "Golpe de Tormenta": 3, "Impacto Sónico": 4, "Descarga Eléctrica": 5, "Golpe Rápido": 6}, #Blitzkrieg Blitz
                   {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
            Jaeger("Tempest Fury", 130, 16, {"Golpe de Tempestad": 1, "Tormenta Letal": 2, "Corte de Viento": 3, "Impacto Eléctrico": 4, "Embestida de Huracán": 5, "Sobrecarga Tempestuosa": 6}, #Tempest Fury
                   {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
            Jaeger("Avalon Ascendant", 140, 20, {"Rayo Ascendente": 1, "Barrera de Aegis": 2, "Explosión de Ascenso": 3, "Golpe de Defensa": 4, "Impacto Energético": 5, "Ataque de Cima": 6}, #Avalon Ascendant
                   {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
            Jaeger("Vortex Voyager", 145, 22, {"Torbellino Destructor": 1, "Cañón Vortex": 2, "Sobrecarga Vortex": 3, "Onda Vortex": 4, "Golpe Gravitacional": 5, "Impacto de Vórtice": 6}, #Vortex Voyager
                   {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
             Jaeger("Titan Redeemer", 170, 28, {"Martillo Redentor": 1, "Escudo Redentor": 2, "Aplastamiento Atómico": 3, "Golpe de Redención": 4, "Embestida Poderosa": 5, "Ataque de Redención": 6}, #Titan Redeemer
                   {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100}),
             Jaeger("Nova Titan", 180, 30, {"Explosión Nova": 1, "Escudo Nova": 2, "Rayo Titan": 3, "Onda Nova": 4, "Impacto Nova": 5, "Rompe Titanes": 6},  #Nova Titan
                   {"cabeza": 100, "torso": 100, "brazo_izquierdo": 100, "brazo_derecho": 100, "pierna_izquierda": 100, "pierna_derecha": 100})
        ]
        kaijus = [
            Kaiju("Knifehead", 60000, 8, {"Escupitajo Tóxico": 70, "Garras Afiladas": 52, "Pisotón": 39, "Golpe de Cola": 27, "Empujon": 24, "Rugido": 15}, #Knifehead
                  {"cabeza": 120000, "torso": 170, "brazo_izquierdo": 90, "brazo_derecho": 90, "pierna_izquierda": 95, "pierna_derecha": 95}),
            Kaiju("Abyssal Leviathan", 120, 12, {"Mordida del Abismo": 1000, "Tormenta de Tentáculos": 70, "Explosión Abisal": 60, "Carga Abismal": 50, "Rugido Sombrío": 40, "Golpe de Marea": 30},#Abyssal Leviathan
                 {"cabeza": 120, "torso": 120, "brazo_izquierdo": 120, "brazo_derecho": 120, "pierna_izquierda": 120, "pierna_derecha": 120}),
            Kaiju("Thunder Wyrm", 115, 11, {"Rayo de Tormenta": 75, "Golpe de Trueno": 65, "Aullido Eléctrico": 55, "Carga Relámpago": 45, "Mordida Eléctrica": 35, "Explosión de Chispa": 25},#Thunder Wyrm 
                 {"cabeza": 115, "torso": 115, "brazo_izquierdo": 115, "brazo_derecho": 115, "pierna_izquierda": 115, "pierna_derecha": 115}),
            Kaiju("Acid Fang", 110, 12, {"Mordida Ácida": 80, "Escupitajo Corrosivo": 70, "Garra Tóxica": 60, "Ráfaga Venenosa": 50, "Golpe de Fuego Químico": 40, "Nube de Ácido": 30},#Acid Fang
                 {"cabeza": 110, "torso": 110, "brazo_izquierdo": 110, "brazo_derecho": 110, "pierna_izquierda": 110, "pierna_derecha": 110}),
            Kaiju("Thunderclap", 130, 15, {"Rugido Trueno": 90, "Golpe Relámpago": 80, "Carga Eléctrica": 70, "Impacto Electrostático": 60, "Descarga de Tormenta": 50, "Torbellino Eléctrico": 40},#Thunderclap
                  {"cabeza": 130, "torso": 130, "brazo_izquierdo": 130, "brazo_derecho": 130, "pierna_izquierda": 130, "pierna_derecha": 130}),
            Kaiju("Terrorsaur", 125, 14, {"Garras de Terror": 85, "Aliento Ardiente": 75, "Aplastar": 65, "Cola Afilada": 55, "Golpe Bestial": 45, "Rugido Ensordecedor": 35},#Terrorsaur
                 {"cabeza": 125, "torso": 125, "brazo_izquierdo": 125, "brazo_derecho": 125, "pierna_izquierda": 125, "pierna_derecha": 125}),
            Kaiju("Basilisk", 110, 12, {"Mordida Venenosa": 70, "Golpe de Cola": 60, "Rugido Petrificante": 55, "Zarpazo Mortal": 50, "Embestida Sorpresa": 45, "Aplastamiento": 40},#Basilisk 
                 {"cabeza": 110, "torso": 110, "brazo_izquierdo": 110, "brazo_derecho": 110, "pierna_izquierda": 110, "pierna_derecha": 110}),
            Kaiju("Hydra", 130, 15, {"Fuego de Dragón": 75, "Garras Venenosas": 65, "Golpe de Cola": 60, "Rugido Paralizante": 55, "Barrera de Escamas": 50, "Mordida Múltiple": 45},#Hydra
                 {"cabeza": 130, "torso": 130, "brazo_izquierdo": 130, "brazo_derecho": 130, "pierna_izquierda": 130, "pierna_derecha": 130}),
            Kaiju("Leviatán", 140, 20, {"Torrente Ácido": 80, "Embiste Oceánico": 70, "Carga de Agua": 65, "Mordida Tóxica": 60, "Golpe Tsunami": 55, "Tormenta Submarina": 50}, #Leviatán
                 {"cabeza": 140, "torso": 140, "brazo_izquierdo": 140, "brazo_derecho": 140, "pierna_izquierda": 140, "pierna_derecha": 140}),
            Kaiju("Kraken", 180, 30, {"Mordisco Devastador": 100, "Torbellino Marítimo": 95, "Golpe de Oleaje": 90, "Zarpazo Acuático": 85, "Furia Submarina": 80, "Aliento de Neblina": 75},#Kraken
                 {"cabeza": 180, "torso": 180, "brazo_izquierdo": 180, "brazo_derecho": 180, "pierna_izquierda": 180, "pierna_derecha": 180}),
            Kaiju("Behemoth", 180, 30, {"Estampida Terrestre": 100, "Golpe Telúrico": 95, "Aplastamiento": 90, "Embiste Colosal": 85, "Furia Sísmica": 80, "Fragor Terremoto": 75},#Behemoth
                 {"cabeza": 180, "torso": 180, "brazo_izquierdo": 180, "brazo_derecho": 180, "pierna_izquierda": 180, "pierna_derecha": 180}),
            Kaiju("Goliath", 180, 30, {"Zarpazo Aplastante": 100, "Furia de Roca": 95, "Martillazo": 90, "Golpe de Titanio": 85, "Rugido Sónico": 80, "Lanzamiento Roca": 75},#Goliath
                 {"cabeza": 180, "torso": 180, "brazo_izquierdo": 180, "brazo_derecho": 180, "pierna_izquierda": 180, "pierna_derecha": 180}),
            Kaiju("Coloso", 180, 30, {"Golpe Colosal": 100, "Estampida Salvaje": 95, "Zarpazo Feroz": 90, "Embestida Despiadada": 85, "Furia Brutal": 80, "Rugido Infernal": 75},#Coloso
                 {"cabeza": 180, "torso": 180, "brazo_izquierdo": 180, "brazo_derecho": 180, "pierna_izquierda": 180, "pierna_derecha": 180}),
             Kaiju("Némesis", 160, 25, {"Asalto Oscuro": 95, "Emboscada Nocturna": 90, "Golpe Umbrío": 85, "Aullido Tenebroso": 80, "Espinas Sombrías": 75, "Tormenta de Sombra": 70},#Némesis
                {"cabeza": 160, "torso": 160, "brazo_izquierdo": 160, "brazo_derecho": 160, "pierna_izquierda": 160, "pierna_derecha": 160}),
            Kaiju("Aurora", 140, 22, {"Resplandor Celestial": 90, "Luz Estelar": 85, "Rayo Solar": 80, "Fuego Estelar": 75, "Centella Radiante": 70, "Brillo Cósmico": 65},#Aurora
                {"cabeza": 140, "torso": 140, "brazo_izquierdo": 140, "brazo_derecho": 140, "pierna_izquierda": 140, "pierna_derecha": 140}),
            Kaiju("Fénix", 150, 28, {"Llamarada Aviadora": 95, "Vuelo Infernal": 90, "Golpe Ardiente": 85, "Explosión de Fuego": 80, "Plumas Abrasadoras": 75, "Ala Incendiaria": 70},#Fénix
                {"cabeza": 150, "torso": 150, "brazo_izquierdo": 150, "brazo_derecho": 150, "pierna_izquierda": 150, "pierna_derecha": 150}),
             Kaiju("Serpentaria", 130, 20, {"Mordida Víbora": 85, "Enroscarse Mortal": 80, "Golpe de Serpiente": 75, "Veneno Paralizante": 70, "Coil Venenoso": 65, "Danse Mortífera": 60},#Serpentaria 
                {"cabeza": 130, "torso": 130, "brazo_izquierdo": 130, "brazo_derecho": 130, "pierna_izquierda": 130, "pierna_derecha": 130}),
             Kaiju("Tifón", 170, 30, {"Tormenta Devastadora": 100, "Ráfaga Ciclónica": 95, "Golpe de Vendaval": 90, "Viento Despiadado": 85, "Ciclón Destructor": 80, "Furia Tornádica": 75},#Tifón
                {"cabeza": 170, "torso": 170, "brazo_izquierdo": 170, "brazo_derecho": 170, "pierna_izquierda": 170, "pierna_derecha": 170}),
            Kaiju("Abismo Oscuro", 180, 35, {"Golpe Profundo": 110, "Marea Negra": 105, "Carga Abismal": 100, "Tormenta Tenebrosa": 95, "Aliento de Oscuridad": 90, "Ciclón Umbrío": 85},#Abismo Oscuro
                {"cabeza": 180, "torso": 180, "brazo_izquierdo": 180, "brazo_derecho": 180, "pierna_izquierda": 180, "pierna_derecha": 180}),
             Kaiju("Colmillo Nocturno", 160, 30, {"Aullido Nocturno": 95, "Garra Sombría": 90, "Carga Nocturna": 85, "Mordida Oscura": 80, "Niebla de Pesadilla": 75, "Rugido Lunar": 70},#Colmillo Nocturno
                {"cabeza": 160, "torso": 160, "brazo_izquierdo": 160, "brazo_derecho": 160, "pierna_izquierda": 160, "pierna_derecha": 160})
            
        ]

        print("Jugador 1, elige tu bando:")
        print("1. Jaeger")
        print("2. Kaiju")
        while True:
            opcion1 = input("Ingresa el número de tu elección: ")
            if opcion1 in ['1', '2']:
                break
            else:
                print("Opción inválida. Selecciona '1' o '2'.")

        if opcion1 == '1':
            print("Jugador 1 ha elegido ser Jaeger. Aquí están los personajes disponibles:")
            for i, jaeger in enumerate(jaegers, 1):
                print(f"{i}. {jaeger.nombre}")
                self.mostrar_especificaciones(jaeger)
            while True:
                seleccion = input("Ingresa el número correspondiente al Jaeger: ")
                if seleccion.isdigit() and 1 <= int(seleccion) <= len(jaegers):
                    jugador1 = jaegers[int(seleccion) - 1]
                    break
                else:
                    print("Opción inválida. Selecciona un número válido.")
        else:
            print("Jugador 1 ha elegido ser Kaiju. Aquí están los personajes disponibles:")
            for i, kaiju in enumerate(kaijus, 1):
                print(f"{i}. {kaiju.nombre}")
                self.mostrar_especificaciones(kaiju)
            while True:
                seleccion = input("Ingresa el número correspondiente al Kaiju: ")
                if seleccion.isdigit() and 1 <= int(seleccion) <= len(kaijus):
                    jugador1 = kaijus[int(seleccion) - 1]
                    break
                else:
                    print("Opción inválida. Selecciona un número válido.")

        print("Jugador 2, elige tu bando:")
        print("1. Jaeger")
        print("2. Kaiju")
        while True:
            opcion2 = input("Ingresa el número de tu elección: ")
            if opcion2 in ['1', '2']:
                break
            else:
                print("Opción inválida. Selecciona '1' o '2'.")

        if opcion2 == '1':
            print("Jugador 2 ha elegido ser Jaeger. Aquí están los personajes disponibles:")
            for i, jaeger in enumerate(jaegers, 1):
                print(f"{i}. {jaeger.nombre}")
                self.mostrar_especificaciones(jaeger)
            while True:
                seleccion = input("Ingresa el número correspondiente al Jaeger: ")
                if seleccion.isdigit() and 1 <= int(seleccion) <= len(jaegers):
                    jugador2 = jaegers[int(seleccion) - 1]
                    break
                else:
                    print("Opción inválida. Selecciona un número válido.")
        else:
            print("Jugador 2 ha elegido ser Kaiju. Aquí están los personajes disponibles:")
            for i, kaiju in enumerate(kaijus, 1):
                print(f"{i}. {kaiju.nombre}")
                self.mostrar_especificaciones(kaiju)
            while True:
                seleccion = input("Ingresa el número correspondiente al Kaiju: ")
                if seleccion.isdigit() and 1 <= int(seleccion) <= len(kaijus):
                    jugador2 = kaijus[int(seleccion) - 1]
                    break
                else:
                    print("Opción inválida. Selecciona un número válido.")

        self.agregar_jugador(jugador1)
        self.agregar_jugador(jugador2)

    def ejecutar_turno(self, atacante, defensor):
        print(f"Turno de {atacante.nombre}")
        if atacante.verificar_turno_perdido():
            print(f"{atacante.nombre} pierde su turno debido a daño crítico.")
            return
        if self.dados_automaticos:
            resultado_dados = self.lanzar_dados()
        else:
            resultado_dados = self.ingresar_dados()
        tipo_ataque, dano = self.determinar_ataque(resultado_dados, atacante)
        if tipo_ataque == "ataque_fallido":
            print(f"{atacante.nombre} no logró realizar un ataque efectivo.")
            return
        parte_objetivo = self.seleccionar_parte_objetivo(defensor)
        dano_real = atacante.ejecutar_ataque(dano)
        print(f"{atacante.nombre} realizo {tipo_ataque} a {defensor.nombre} en la parte {parte_objetivo} causando {dano_real} de daño.")
        defensor.recibir_dano(parte_objetivo, dano_real)

    def iniciar_juego(self):
        self.elegir_modo_dados()
        self.seleccionar_personaje()
        while all(jugador.vida > 0 for jugador in self.jugadores):
            for i, atacante in enumerate(self.jugadores):
                defensor = self.jugadores[1 - i]
                self.ejecutar_turno(atacante, defensor)
                if defensor.vida <= 0:
                    print(f"{defensor.nombre} ha sido derrotado. {atacante.nombre} gana el juego!")
                    return

# Ejemplo de uso
juego = Juego()
juego.iniciar_juego()


