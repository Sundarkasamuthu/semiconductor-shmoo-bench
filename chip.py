# PRODUTION CODE

def chip_logic (voltage, frequency):
    if frequency >= ((voltage * 400)-100): #if voltage is too low for a given frequency
        return "fail"
    else: 
        return "pass"
    
#Initialisation & Testing
#this line ensures test runs only upon execution of the file- acts as a safety lock

if __name__ == "__main__":
    print("manual test logic running")

    sample_voltage = 0.8
    sample_frequency = 100

    result = chip_logic (sample_voltage, sample_frequency)
    print(f"Result for {sample_voltage}V at {sample_frequency}MHz: {result}")