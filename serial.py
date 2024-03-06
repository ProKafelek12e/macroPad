import serial
# Define the serial port and baud rate
serial_port = 'COM4'  # Change this to match your Arduino's serial port
baud_rate = 9600

# Create a serial object
ser = serial.Serial(serial_port, baud_rate)

try:
    # Loop indefinitely to continuously read data
    while True:
        # Read a line from the serial port
        line = ser.readline().decode().strip()
        
        # Print the line received from Arduino
        print("Received:", line)
        if line.startswith("P:"):
            try:
                # Extract the percent value from the received line
                percent = int(line.replace("P:", ""))
                
            except ValueError:
                print("Invalid data format received from Arduino:", line)
except KeyboardInterrupt:
    # Close the serial port when the program is interrupted
    ser.close()
    print("Serial port closed.")
