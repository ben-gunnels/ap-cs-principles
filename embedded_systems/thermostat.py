import time
import threading

MINIMUM_TEMPERATURE = 65
MAXIMUM_TEMPERATURE = 77

def heater(temperature):
    # Heat the room up by 5% for every call
    temperature *= 1.05 

    return temperature

def air_conditioner(temperature):
    # Cool the room down by 5% for every call
    temperature *= 0.95

    return temperature

def temp_sensor(temperature):
    if temperature < MAXIMUM_TEMPERATURE:
        return "too cold"

    elif temperature > MINIMUM_TEMPERATURE:
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
        print(f"The room temperature is {signal}\n")

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


    


