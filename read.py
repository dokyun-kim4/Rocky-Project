# Python script for saving Serial output to a csv file
import serial
import csv

# Open serial port
ser = serial.Serial("COM5", 9600)  # Replace 'COM3' with your Arduino's port

# Open CSV file for writing
csv_file = open("data.csv", "w", newline="")
csv_writer = csv.writer(csv_file)

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode().strip()

        # Split the line into values
        values = line.split(",")

        # Write values to CSV file
        csv_writer.writerow(values)

        # Print values to console
        print(values)
except KeyboardInterrupt:
    print("Keyboard Interrupt detected. Closing...")
    ser.close()
    csv_file.close()
