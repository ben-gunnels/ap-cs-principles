import time

MINIMUM_TEMPERATURE = 65
MAXIMUM_TEMPERATURE = 77

def heater(temperature):
    # Heat the room up by 5% for every call
    # Set the minimum increase to 2 degrees
    temperature += max(abs(0.05 * temperature), 2)

    return temperature

def air_conditioner(temperature):
    # Cool the room down by 5% for every call
    # Set the minimum decrease to 2 degrees
    temperature -= max(abs(0.05 * temperature), 2)

    return temperature

def temp_sensor(temperature):
    if temperature < MINIMUM_TEMPERATURE:
        return "too cold"

    elif temperature > MAXIMUM_TEMPERATURE:
        return "too hot"
    
    else:
        return "just right"
    
def thermostat(signal, temperature):
    if signal == "too cold":
        temperature = heater(temperature)

    elif signal == "too hot":
        temperature = air_conditioner(temperature)

    return temperature

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

        # no more work to do
        if signal == "just right":
            break

        # Adjust the temperature to try to make it right
        temperature = thermostat(signal, temperature)

        if signal == "too cold":
            print("Warming up...\n")

        elif signal == "too hot":
            print("Cooling down...\n")

        time.sleep(2)

    print(f"The room is now comfortable!\n")

if __name__ == "__main__":
    main()


    


