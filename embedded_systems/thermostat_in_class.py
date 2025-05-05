import time

def heater(temperature):
    pass

def air_conditioner(temperature):
    pass

def temp_sensor(temperature):
    pass

def thermostat(signal, temperature):
    pass

def main():
    temperature = int(input(f"Enter a temperature to start: "))
    while (1):
        print(f"The room is {temperature:.2f} degrees Fahrenheit\n")

        # Get the reading of the room temperature
        signal = temp_sensor(temperature)

        time.sleep(2)

        # Tell the viewer if the temperature is too hot, cold or just right
        if signal == "too hot":
            emoji = "🔥"

        elif signal == "too cold":
            emoji = "❄️"
        
        else:
            emoji = "😎"

        print(f"The room temperature is {signal} {emoji}\n")

        # No more work to do
        if signal == "just right":
            break

        # Adjust the temperature to try to make it right via the thermostat
        temperature = thermostat(signal, temperature)

        if signal == "too cold":
            print("Warming up...\n")

        elif signal == "too hot":
            print("Cooling down...\n")

        time.sleep(2)

    print(f"The room is now comfortable!\n")

if __name__ == "__main__":
    main()